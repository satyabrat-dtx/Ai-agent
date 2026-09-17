# DB2ADMIN.EXPORTENTITYCUSTOM

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `ENTITYNAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 106555

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENTITYNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `ITEMTYPESUPPORTED` | SMALLINT | NOT NULL |  |  |  |
| 2 | `TEMPLATEUIXMLNAME` | VARCHAR(100) |  |  |  |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EXPORTENTITYCUSTOMUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENTITYNAME,
       t.ITEMTYPESUPPORTED,
       t.TEMPLATEUIXMLNAME,
       t.ABSUNIQUEID
FROM   DB2ADMIN.EXPORTENTITYCUSTOM t
FETCH FIRST 100 ROWS ONLY;
```
