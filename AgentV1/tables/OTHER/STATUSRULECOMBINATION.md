# DB2ADMIN.STATUSRULECOMBINATION

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`, `STATUSCODE`, `LINENR`, `SUBLINE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 190798

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `STATUSCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINENR` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SUBLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `KEY1VALUE` | CHAR(20) |  |  |  |  |
| 6 | `KEY2VALUE` | CHAR(10) |  |  |  |  |
| 7 | `KEY3VALUE` | CHAR(10) |  |  |  |  |
| 8 | `KEY4VALUE` | CHAR(10) |  |  |  |  |
| 9 | `KEY5VALUE` | CHAR(10) |  |  |  |  |
| 10 | `KEY6VALUE` | CHAR(10) |  |  |  |  |
| 11 | `KEY7VALUE` | CHAR(10) |  |  |  |  |
| 12 | `KEY8VALUE` | CHAR(10) |  |  |  |  |
| 13 | `KEY9VALUE` | CHAR(10) |  |  |  |  |
| 14 | `KEY10VALUE` | CHAR(10) |  |  |  |  |
| 15 | `CONTINUEWHENERROR` | SMALLINT | NOT NULL |  |  |  |
| 16 | `CONTINUEWHENOK` | SMALLINT | NOT NULL |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 24 | `SUFFIXCODEVALUE` | CHAR(20) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `STATUSRULE_STATUSRULECOMBINATIONLIST` | `COMPANYCODE`, `ITEMTYPECODE`, `STATUSCODE`, `LINENR` | [`STATUSRULE`](../OTHER/STATUSRULE.md) | `ARTICLESTATUSCOMPANYCODE`, `ARTICLESTATUSITEMTYPECODE`, `ARTICLESTATUSCODE`, `LINENR` | RESTRICT | `STATUSRULECOMBINATION.COMPANYCODE = STATUSRULE.ARTICLESTATUSCOMPANYCODE AND STATUSRULECOMBINATION.ITEMTYPECODE = STATUSRULE.ARTICLESTATUSITEMTYPECODE AND STATUSRULECOMBINATION.STATUSCODE = STATUSRULE.ARTICLESTATUSCODE AND STATUSRULECOMBINATION.LINENR = STATUSRULE.LINENR` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `STATUSRULECOMBINATION_STATUSRULEPOLICYLIST` | [`STATUSRULEPOLICY`](../OTHER/STATUSRULEPOLICY.md) | `COMPANYCODE`, `ITEMTYPECODE`, `STATUSCODE`, `LINENR`, `STATUSRULECOMBINATIONSUBLINE` | `STATUSRULEPOLICY.COMPANYCODE = STATUSRULECOMBINATION.COMPANYCODE AND STATUSRULEPOLICY.ITEMTYPECODE = STATUSRULECOMBINATION.ITEMTYPECODE AND STATUSRULEPOLICY.STATUSCODE = STATUSRULECOMBINATION.STATUSCODE AND STATUSRULEPOLICY.LINENR = STATUSRULECOMBINATION.LINENR AND STATUSRULEPOLICY.STATUSRULECOMBINATIONSUBLINE = STATUSRULECOMBINATION.SUBLINE` |

## Indexes

- `STATUSRULECOMBINATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.STATUSCODE,
       t.LINENR,
       t.SUBLINE,
       t.KEY1VALUE,
       t.KEY2VALUE,
       t.KEY3VALUE,
       t.KEY4VALUE,
       t.KEY5VALUE,
       t.KEY6VALUE,
       t.KEY7VALUE
FROM   DB2ADMIN.STATUSRULECOMBINATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
