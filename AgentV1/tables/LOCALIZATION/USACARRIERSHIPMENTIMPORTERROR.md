# DB2ADMIN.USACARRIERSHIPMENTIMPORTERROR

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `ERRORTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 107613

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ERRORTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `ERRCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 2 | `ERRIMPORTTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 3 | `ERRCARRIERREFERENCE` | VARCHAR(100) |  |  |  |  |
| 4 | `ERRREVERSALENTRY` | SMALLINT |  |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `USACSIERR01` (ERRCOMPANYCODE, ERRIMPORTTRANSACTIONNUMBER, ERRCARRIERREFERENCE, ERRREVERSALENTRY)
- `USACARRIERSHIPMENTIMPERRORUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ERRORTIMESTAMP,
       t.ERRCOMPANYCODE,
       t.ERRIMPORTTRANSACTIONNUMBER,
       t.ERRCARRIERREFERENCE,
       t.ERRREVERSALENTRY,
       t.ABSUNIQUEID
FROM   DB2ADMIN.USACARRIERSHIPMENTIMPORTERROR t
FETCH FIRST 100 ROWS ONLY;
```
