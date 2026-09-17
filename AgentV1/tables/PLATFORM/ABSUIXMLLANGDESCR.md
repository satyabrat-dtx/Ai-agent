# DB2ADMIN.ABSUIXMLLANGDESCR

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `ABSUIXMLPATH`, `ABSUIXMLNAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 32346

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `ABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `OBJTITLE` | VARCHAR(150) |  |  |  |  |
| 3 | `COLTITLE` | VARCHAR(150) |  |  |  |  |
| 4 | `LKPTITLE` | VARCHAR(150) |  |  |  |  |
| 5 | `COLBREADCRUMB` | CHAR(20) |  |  |  |  |
| 6 | `OBJBREADCRUMB` | CHAR(20) |  |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSUIXMLLANGDESCRUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSUIXMLPATH,
       t.ABSUIXMLNAME,
       t.OBJTITLE,
       t.COLTITLE,
       t.LKPTITLE,
       t.COLBREADCRUMB,
       t.OBJBREADCRUMB,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSUIXMLLANGDESCR t
FETCH FIRST 100 ROWS ONLY;
```
