# DB2ADMIN.NETCUST

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'NET')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 122747

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(5) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `DESCRIPTION` | VARCHAR(1000) |  |  | description |  |
| 2 | `ACTIVE` | INTEGER | NOT NULL |  |  |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `NETCUSTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.DESCRIPTION,
       t.ACTIVE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.NETCUST t
FETCH FIRST 100 ROWS ONLY;
```
