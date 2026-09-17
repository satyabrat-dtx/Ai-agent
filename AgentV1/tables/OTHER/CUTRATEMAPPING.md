# DB2ADMIN.CUTRATEMAPPING

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 130140

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 1 | `DIFFAPPREALIZATIONFROMDAYS` | INTEGER | NOT NULL |  |  |  |
| 2 | `DIFFAPPREALIZATIONTODAYS` | INTEGER | NOT NULL |  |  |  |
| 3 | `DIFFAPPLEOFROMDAYS` | INTEGER | NOT NULL |  |  |  |
| 4 | `DIFFAPPLEOTODAYS` | INTEGER | NOT NULL |  |  |  |
| 5 | `CUTPERC` | DECIMAL(5,2) |  |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CUTRATEMAPPINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.LINENO,
       t.DIFFAPPREALIZATIONFROMDAYS,
       t.DIFFAPPREALIZATIONTODAYS,
       t.DIFFAPPLEOFROMDAYS,
       t.DIFFAPPLEOTODAYS,
       t.CUTPERC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.CUTRATEMAPPING t
FETCH FIRST 100 ROWS ONLY;
```
