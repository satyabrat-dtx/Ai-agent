# Naming conventions in the DB2ADMIN schema

Decoded from 3,762 table names and 25,869 distinct
column names. The DDL carries no comments, so these conventions are the only
available source of meaning — and they are **inferences**, not declarations.

## Table name structure

`[MODULE PREFIX] + [ENTITY] + [ROLE SUFFIX]`

### Role suffixes

| Suffix | Meaning | Relationship to the base table |
|---|---|---|
| `…HEADER` | document header | parent of `…LINE` |
| `…LINE`, `…LINES` | document line item | child, usually via composite FK |
| `…DETAIL` | sub-line detail | child of a line |
| `…BLOCKS` | processing blocks/holds on a document | child via `FATHERID` |
| `…COMMENT`, `…COMMENTS` | free-text notes | child via `FATHERID` |
| `…TYPE` | classification/reference table | parent of the base table |
| `…TEMPLATE` | reusable pattern for creating documents | independent |
| `…DEFINITION` | configuration of a behaviour | independent |
| `…MASTER` | master-data root | parent |
| `…GROUP` | grouping/classification | parent |
| `…MAPPING` | association between two entities | join table |
| `…EXP` | export/extract variant | derived |
| `…LOG` | change history | child, time-series |
| `…BEAN` | **integration staging mirror — do not query** | shadows the base table |

### Module prefixes

See [`AGENT_GUIDE.md` §6](AGENT_GUIDE.md) and `catalog/modules.json`. Notable
cases where the prefix is **not** what it looks like:

- `LOGICALWAREHOUSE*` is *logical warehouse*, not the `LOG` (logistics) prefix.
- `LOGINTERNALORDER`, `LOGORDERPARTNER`, `LOGINVOICETYPE` **are** `LOG` + entity.
- `INTERNAL*` (internal orders) and `INTRASTAT*` are unrelated despite both
  starting `INT`.
- `PRODUCT*` (item master) and `PRODUCTION*` (production orders) are different
  domains.

## Column conventions

| Pattern | Meaning |
|---|---|
| `COMPANYCODE` | company / legal entity — the tenant key, on 1934 tables |
| `DIVISIONCODE` | division inside a company |
| `CODE` | the table's own business key, usually the last PK column |
| `<ENTITY>CODE` | reference to `<ENTITY>`'s business key — check the FK for the real target |
| `<ROLE><ENTITY>CODE` | role-qualified reference, e.g. `DISCOUNTCURRENCYCODE` → `CURRENCY.CODE` |
| `ABSUNIQUEID` | framework surrogate id; never a PK, never an FK target |
| `FATHERID` | implicit parent pointer → parent's `ABSUNIQUEID` (no FK declared) |
| `SHORT/LONG/SEARCHDESCRIPTION` | the standard label triplet; `SEARCH…` is normalised for lookup |
| `SUBCODE01`…`SUBCODE10` | generic user-defined classification slots |
| `CREATION*` / `LASTUPDATE*` | audit columns; `*UTC` variants are timezone-safe |
| `LOGTIMESTAMP/LOGOPERATION/LOGUSER` | marks a row-level change-log table |
| `IMPORTAUTOCOUNTER/IMPORTSTATUS/WSOPERATION/NEXTRETRY/RETRYNR` | marks a staging mirror |
| `MARK…` | boolean-ish flag (`SMALLINT`, 0/1) |
| `…SIGNED` | the same amount carried with its sign applied |
| `…CURRENCY1` | the amount restated in the company's local currency |

### Role-qualified foreign key columns

A child column is rarely named the same as the parent column it points at. The
FK constraint name usually reads `<PARENT>_<ROLE>`:

```sql
-- PURCHASEDISCOUNTHEADER, constraint CURRENCY_DISCOUNTCURRENCY
DISCOUNTCURRENCYCODE  ->  CURRENCY.CODE
```

**Always take the column pairing from the FK definition** in the table card or
`catalog/foreign_keys.json`. Matching by column name will be wrong.

## Physical layout

All 3,762 tables are row-organised (`ORGANIZE BY ROW`) in a single
tablespace, `NOWRUNRGTS`. There is no partitioning or column-organisation to
exploit, so index coverage is the only physical consideration — see each card's
*Indexes* section.
