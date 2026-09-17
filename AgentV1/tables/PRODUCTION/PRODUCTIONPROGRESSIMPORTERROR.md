# DB2ADMIN.PRODUCTIONPROGRESSIMPORTERROR

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `ERRORTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 25709

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ERRORTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `IMPORTLINECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 2 | `IMPORTLINEPROGRESSNUMBER` | INTEGER | NOT NULL |  |  |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 4 | `IMPORTLINEPROGRESSNUMBERPREFIX` | CHAR(5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PROPROGRESSIMPORTERRORUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ERRORTIMESTAMP,
       t.IMPORTLINECOMPANYCODE,
       t.IMPORTLINEPROGRESSNUMBER,
       t.ABSUNIQUEID,
       t.IMPORTLINEPROGRESSNUMBERPREFIX
FROM   DB2ADMIN.PRODUCTIONPROGRESSIMPORTERROR t
FETCH FIRST 100 ROWS ONLY;
```
