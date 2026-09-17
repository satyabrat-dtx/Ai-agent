# DB2ADMIN.PRODUCTIONCOSTEXCHANGERATE

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `PRODUCTIONCOSTCOMPANYCODE`, `PRODUCTIONCOSTCOUNTERCODE`, `PRODUCTIONCOSTCODE`, `PRODUCTIONCOSTCOSTNUMBER`, `CURRENCYCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 42050

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PRODUCTIONCOSTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PRODUCTIONCOSTCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PRODUCTIONCOSTCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PRODUCTIONCOSTCOSTNUMBER` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CURRENCYCODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 5 | `EXCHANGERATETOSYSTEMCURRENCY` | DECIMAL(28,15) |  |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PRODUCTIONCOST_COSTEXCHANGERATE` | `PRODUCTIONCOSTCOMPANYCODE`, `PRODUCTIONCOSTCOUNTERCODE`, `PRODUCTIONCOSTCODE`, `PRODUCTIONCOSTCOSTNUMBER` | [`PRODUCTIONCOST`](../PRODUCTION/PRODUCTIONCOST.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE`, `COSTNUMBER` | RESTRICT | `PRODUCTIONCOSTEXCHANGERATE.PRODUCTIONCOSTCOMPANYCODE = PRODUCTIONCOST.COMPANYCODE AND PRODUCTIONCOSTEXCHANGERATE.PRODUCTIONCOSTCOUNTERCODE = PRODUCTIONCOST.COUNTERCODE AND PRODUCTIONCOSTEXCHANGERATE.PRODUCTIONCOSTCODE = PRODUCTIONCOST.CODE AND PRODUCTIONCOSTEXCHANGERATE.PRODUCTIONCOSTCOSTNUMBER = PRODUCTIONCOST.COSTNUMBER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRODUCTIONCOSTEXCHANGERATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PRODUCTIONCOSTCOMPANYCODE,
       t.PRODUCTIONCOSTCOUNTERCODE,
       t.PRODUCTIONCOSTCODE,
       t.PRODUCTIONCOSTCOSTNUMBER,
       t.CURRENCYCODE,
       t.EXCHANGERATETOSYSTEMCURRENCY,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PRODUCTIONCOSTEXCHANGERATE t
FETCH FIRST 100 ROWS ONLY;
```
