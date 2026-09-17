# DB2ADMIN.PRIMROSECONTACTBOOKKEY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `NUMBERID`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 5593

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `NUMBERID` | DECIMAL(8,0) | NOT NULL | PK | primary_key |  |
| 1 | `CODE` | CHAR(8) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `ANRCD` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRIMROSECONTACTBOOKKEYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.NUMBERID,
       t.CODE,
       t.ANRCD,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PRIMROSECONTACTBOOKKEY t
FETCH FIRST 100 ROWS ONLY;
```
