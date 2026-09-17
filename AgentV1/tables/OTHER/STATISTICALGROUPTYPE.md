# DB2ADMIN.STATISTICALGROUPTYPE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `TYPE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 10241

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TYPE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `LONGDESCRIPTION` | CHAR(50) | NOT NULL |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | CHAR(20) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | CHAR(30) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.TYPE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ABSUNIQUEID
FROM   DB2ADMIN.STATISTICALGROUPTYPE t
FETCH FIRST 100 ROWS ONLY;
```
