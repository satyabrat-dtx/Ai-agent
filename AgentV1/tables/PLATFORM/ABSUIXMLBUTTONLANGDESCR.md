# DB2ADMIN.ABSUIXMLBUTTONLANGDESCR

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `ABSUIXMLBUTTONABSUIXMLPATH`, `ABSUIXMLBUTTONABSUIXMLNAME`, `ABSUIXMLBUTTONNAME`, `ABSUIXMLBUTTONFORM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 32305

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUIXMLBUTTONABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `ABSUIXMLBUTTONABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `ABSUIXMLBUTTONNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `ABSUIXMLBUTTONFORM` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `LABEL` | VARCHAR(150) |  |  |  |  |
| 5 | `ALTTEXT` | VARCHAR(150) |  |  |  |  |
| 6 | `TITLE` | VARCHAR(150) |  |  |  |  |
| 7 | `BREADCRUMB` | CHAR(20) |  |  |  |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSUIXMLBUTTONLANGDESCRUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSUIXMLBUTTONABSUIXMLPATH,
       t.ABSUIXMLBUTTONABSUIXMLNAME,
       t.ABSUIXMLBUTTONNAME,
       t.ABSUIXMLBUTTONFORM,
       t.LABEL,
       t.ALTTEXT,
       t.TITLE,
       t.BREADCRUMB,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSUIXMLBUTTONLANGDESCR t
FETCH FIRST 100 ROWS ONLY;
```
