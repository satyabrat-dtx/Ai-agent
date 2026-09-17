# DB2ADMIN.ELEMENTSINSPECTIONIMPORTERROR

- **Module**: `QUALITY` (low confidence — table name starts with 'ELEMENT')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `ERRORTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 1921

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ERRORTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `ELEMENTSINSPECTIONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 2 | `ELEMENTSINSPECTIONITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `ELEMENTSINSPECTIONEVENTSLINK` | CHAR(15) |  |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ELEMENTSINSIMPORTERRORUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ERRORTIMESTAMP,
       t.ELEMENTSINSPECTIONCOMPANYCODE,
       t.ELEMENTSINSPECTIONITEMTYPECODE,
       t.ELEMENTSINSPECTIONEVENTSLINK,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ELEMENTSINSPECTIONIMPORTERROR t
FETCH FIRST 100 ROWS ONLY;
```
