# DB2ADMIN.ADSTORAGEIMPORTERROR

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `ERRORTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 194421

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ERRORTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `IMPORTLINEOWNERENTITYNAME` | CHAR(50) |  |  |  |  |
| 2 | `IMPORTLINEOWNERADUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 3 | `IMPORTLINENAMEENTITYNAME` | CHAR(50) |  |  |  |  |
| 4 | `IMPORTLINENAMENAME` | CHAR(50) |  |  |  |  |
| 5 | `IMPORTLINEFIELDNAME` | VARCHAR(120) |  |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ADSTORAGEIMPORTERRORUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ERRORTIMESTAMP,
       t.IMPORTLINEOWNERENTITYNAME,
       t.IMPORTLINEOWNERADUNIQUEID,
       t.IMPORTLINENAMEENTITYNAME,
       t.IMPORTLINENAMENAME,
       t.IMPORTLINEFIELDNAME,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ADSTORAGEIMPORTERROR t
FETCH FIRST 100 ROWS ONLY;
```
