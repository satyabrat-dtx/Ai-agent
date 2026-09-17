# DB2ADMIN.USADUMMYENTITY

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 2
- **Primary key**: `DUMMYCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 88383

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DUMMYCODE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 1 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `USADUMMYENTITYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DUMMYCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.USADUMMYENTITY t
FETCH FIRST 100 ROWS ONLY;
```
