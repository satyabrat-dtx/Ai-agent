# DB2ADMIN.SETUPORDCOMMON

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `ID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 13389

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 1 | `ACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 2 | `DOCUMENTTYPE` | SMALLINT | NOT NULL |  |  |  |
| 3 | `LIFECYCLECOMPLETE` | SMALLINT | NOT NULL |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SETUPORDCOMMONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ID,
       t.ACTIVE,
       t.DOCUMENTTYPE,
       t.LIFECYCLECOMPLETE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.SETUPORDCOMMON t
FETCH FIRST 100 ROWS ONLY;
```
