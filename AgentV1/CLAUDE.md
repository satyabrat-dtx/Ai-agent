# CLAUDE.md — DB2ADMIN query knowledge base

Read [`AGENT_GUIDE.md`](AGENT_GUIDE.md) first. It is the contract for this KB: retrieval
protocol, what is authoritative, the SQL generation rules, and the traps (`*BEAN` staging
mirrors, `ACT_*` engine internals, `FATHERID` implicit links, hub tables, role-qualified
FKs, `ABSUNIQUEID`). Do not restate those rules here — follow them.

This file records only what the guide does not: the views-first rule, verified join paths,
and tooling gotchas.

---

## 1. Check views before base tables — always

`catalog/views.json` holds **424 views**. Search it before hand-writing any join.
The DDL has **zero `COMMENT ON` statements** and many real relationships are **not declared
as foreign keys**, so a join reconstructed from the FK graph can be subtly wrong in ways the
schema cannot warn you about. The shipped views encode the application's actual semantics —
including effective-dating, substitution chains, status filters and destination-type
discriminators that no FK expresses.

Search all three ways. Missing any one of them has already caused a wrong answer:

```bash
cd D:/DB2ADMIN_DDL/kb && python -c "
import json
v=json.load(open('catalog/views.json',encoding='utf-8'))
q='ALLOC'                                     # <- your topic
print([x['name'] for x in v if q in x['name'].upper()])                    # by NAME
print([x['name'] for x in v if 'SALESORDER' in x['depends_on_tables']])    # by DEPENDENCY
print([x['name'] for x in v if 'LEGALNAME' in x['sql'].upper()])           # by SQL TEXT
"
```

Then check **which other views reference the candidate view by name**. That reveals the
canonical join predicate and any literal filters the application relies on — e.g.
`VIEWSTDELIVERY` joins `VIEWORDERPARTNER` with `CUSTOMERSUPPLIERTYPE = '1'`.

Before using a view, establish its **grain**. The `VIEWST*` family is delivery-line grained
and will fan out order headers.

View names in the DDL source appear in mixed case (`ViewTaxTemplateHeader`,
`ViewMRNRegister`). Reference them unquoted in uppercase.

---

## 2. Verified join paths

Established against the DDL and the shipped views. Prefer these over re-deriving.

### Sales order header
Key is `COMPANYCODE, COUNTERCODE, CODE`. `CODE` alone is **not** unique.
`ORDERTYPE` doubles as the partner type in partner joins (`'1'` = sales/customer).

### Customer name — use `VIEWORDERPARTNER`
```sql
LEFT JOIN DB2ADMIN.VIEWORDERPARTNER vop
       ON  so.COMPANYCODE                = vop.CUSTOMERSUPPLIERCOMPANYCODE
       AND so.ORDERTYPE                  = vop.CUSTOMERSUPPLIERTYPE
       AND so.ORDPRNCUSTOMERSUPPLIERCODE = vop.CUSTOMERSUPPLIERCODE
```
Name is `LEGALNAME1` / `LEGALNAME2` / `SHORTNAME`. The view is
`ORDERPARTNER ⟕ CUSTOMERSUPPLIERDATA ⟕ BUSINESSPARTNER`, resolved via
`ORDERPARTNER.ORDERBUSINESSPARTNERNUMBERID` and walking `SUBSTITUTEBPNUMBERID`
recursively so merged partners return the surviving name.

**Do not** hand-build this. `SALESORDER` has no FK to the customer master (only carrier
roles), `CUSTOMERSUPPLIERDATA` holds no name, and the `BUSINESSPARTNER.NUMBERID` hop is
undeclared — `CUSTOMERSUPPLIERDATA.BUSINESSPARTNERNUMBERID` looks equally plausible but is
the wrong column, and a hand-built join silently loses the substitution walk.

Partner roles on `SALESORDER`: `ORDPRNCUSTOMERSUPPLIERCODE` (sold-to),
`FNCORDPRNCUSTOMERSUPPLIERCODE` (bill-to), `RFORDPRNCUSTOMERSUPPLIERCODE` (reference),
`PAYMENTCUSTOMERCODE`. Ask which one the question means; do not default silently.

### Allocation vs production reservation — use `VIEWALLOCATIONANDRESERVATION`
Three-branch UNION with a `TYPE` discriminator:

| `TYPE` | Meaning |
|---|---|
| `ALL` | reservation has allocation; allocation detail populated (code, warehouse, lot, location, `SIGNED*QUANTITY`) |
| `PARTIAL` | residual remains; `PRIMARYQTY`/`SECONDARYQTY`/`PACKAGINGQTY` = reserved − used − allocated |
| `FREE` | no allocation; quantities 0 |

One reservation can yield several `ALL` rows **plus** a `PARTIAL` row. It bakes in
`PROGRESSSTATUS <> '2'` (closed reservations excluded) and `ALLOCATION.DESTINATIONTYPE = '4'`
(destination is a production reservation). Reservation side is `VIEWDEMANDORDERRESERVATION`,
which unions `PRODUCTIONRESERVATION` (`RESERVATIONINGROUPORDER = 0`) and
`PRODUCTIONORDERRESERVATION`, distinguished by `RECORDTYPE` — both are live tables.

### `ALLOCATION` is not `LINKEDSTOCK`
Two different concepts; confusing them produces a query that runs and answers the wrong
question.

- **`ALLOCATION`** (CORE_MASTER, 105 cols) — the allocation module. `DESTINATIONTYPE = '4'`
  means the destination is a production reservation; `DETAILTYPE = '1'` for detail rows.
  Joins to a reservation on `COMPANYCODE, COUNTERCODE, ORDERCODE, ORDERLINE`, where
  `ORDERLINE` matches the reservation's `RESERVATIONLINE`.
- **`LINKEDSTOCK`** (OTHER, 61 cols) — demand↔supply **planning peg**. `DESTINATIONORDER = '1'`
  means the destination is a sales order delivery (`DLV*` columns);
  `RESERVATIONORDERCOUNTERCODE`/`RESERVATIONORDERCODE`/`RESERVATIONRESERVATIONLINE` identify
  the source reservation. Used by `VIEWORDERPLANNINGDASHBOARD`, which sums
  `BASEPRIMARYQUANTITYUNIT` per delivery line.

### Localization extension tables (`*IE`)
`SALESORDERIE` is 1:1 with `SALESORDER` — **identical PK**, but no FK declares the link, so
join on matching primary keys. It carries `TAXTEMPLATETEMPLATETYPE` + `TAXTEMPLATECODE`,
supply state, advance licence. May be empty if that localization is not in use, so
`LEFT JOIN`. Same pattern for `SALESORDERLINEIE`, `SALESDOCUMENTIE`, `PURCHASEORDERIE`.

A tax template is identified by **both** `TAXTEMPLATETEMPLATETYPE` and `TAXTEMPLATECODE`.

### Effective-dated master data
`TAXTEMPLATEHEADER` PK includes `EFFECTIVEFROMDATE`, so a direct join duplicates each row
per version. `ViewTaxTemplateHeader` collapses to one row per company/type/code but uses
`MAX(LONGDESCRIPTION)` — the **lexically greatest** description, not the version in force.
For the description that actually applied, join the base table with an explicit date range
against the document date.

---

## 3. Tooling

Run the CLI from the **parent** directory; its paths are `kb/`-relative:

```bash
cd D:/DB2ADMIN_DDL && python kb/tools/kb.py search "sales order delivery"
```

`search`, `find-column`, `join-path` work. **`describe <TABLE>` crashes on Windows** with
`UnicodeEncodeError` (cp1252 cannot encode `→` in the join predicates) — read the card
directly instead:

```
kb/tables/<MODULE>/<TABLE>.md
```

`catalog/foreign_keys.json` is a flat list of 11,001 objects with keys
`constraint`, `child`, `child_columns`, `parent`, `parent_columns`, `on_clause` — use
`on_clause` verbatim. `column_index.json` maps column name → tables. `kb.sqlite` carries the
same content plus `tables_fts` / `columns_fts`.

---

## 4. Output expectations

- Schema-qualify everything as `DB2ADMIN.X`, constrain `COMPANYCODE`, use `FETCH FIRST n ROWS ONLY`.
- State which joins are **declared FKs** and which are **inferred**, so the reader knows what
  the schema guarantees.
- Flag grain and fan-out whenever a join can multiply rows.
- Never `SUM` a quantity across differing unit-of-measure columns without grouping by the
  UoM code or saying why it is safe.
- `SELECT` only — this KB describes a read model.
