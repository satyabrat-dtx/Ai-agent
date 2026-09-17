# DB2ADMIN.ALLOCATIONIMPORTERROR

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `ERRORTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 202

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ERRORTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `IMPORTLINECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 2 | `IMPORTLINECODE` | CHAR(15) |  |  |  |  |
| 3 | `IMPORTLINELINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 4 | `IMPORTLINECOMPONENTLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ALLOCATIONIMPORTERRORUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ERRORTIMESTAMP,
       t.IMPORTLINECOMPANYCODE,
       t.IMPORTLINECODE,
       t.IMPORTLINELINENUMBER,
       t.IMPORTLINECOMPONENTLINENUMBER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ALLOCATIONIMPORTERROR t
FETCH FIRST 100 ROWS ONLY;
```
