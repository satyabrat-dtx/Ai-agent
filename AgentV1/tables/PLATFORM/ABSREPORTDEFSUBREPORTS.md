# DB2ADMIN.ABSREPORTDEFSUBREPORTS

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `ABSREPORTDEFCODE`, `SUBREPORTNAME`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 70527

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSREPORTDEFCODE` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SUBREPORTNAME` | CHAR(60) | NOT NULL | PK | primary_key |  |
| 2 | `CONNECTIONNAME` | CHAR(100) |  |  |  |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSREPORTDEF_SUBREPORTS` | `ABSREPORTDEFCODE` | [`ABSREPORTDEF`](../PLATFORM/ABSREPORTDEF.md) | `CODE` | RESTRICT | `ABSREPORTDEFSUBREPORTS.ABSREPORTDEFCODE = ABSREPORTDEF.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSREPORTDEFSUBREPORTSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSREPORTDEFCODE,
       t.SUBREPORTNAME,
       t.CONNECTIONNAME,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSREPORTDEFSUBREPORTS t
FETCH FIRST 100 ROWS ONLY;
```
