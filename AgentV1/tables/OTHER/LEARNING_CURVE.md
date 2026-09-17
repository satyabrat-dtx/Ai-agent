# DB2ADMIN.LEARNING_CURVE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `LC_LEARNING_CURVE_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 108253

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LC_LEARNING_CURVE_CODE` | VARCHAR(6) | NOT NULL | PK | primary_key |  |
| 1 | `LC_LEARNING_CURVE_DESC` | VARCHAR(30) |  |  |  |  |
| 2 | `LC_CURVE_FIRST_HOURS` | DECIMAL(4,1) |  |  |  |  |
| 3 | `LC_CURVE_FIRST_EFFIC` | SMALLINT |  |  |  |  |
| 4 | `LC_CURVE_SECOND_HOURS` | DECIMAL(4,1) |  |  |  |  |
| 5 | `LC_CURVE_SECOND_EFFIC` | SMALLINT |  |  |  |  |
| 6 | `LC_CURVE_THIRD_HOURS` | DECIMAL(4,1) |  |  |  |  |
| 7 | `LC_CURVE_THIRD_EFFIC` | SMALLINT |  |  |  |  |
| 8 | `LC_CURVE_FORTH_HOURS` | DECIMAL(4,1) |  |  |  |  |
| 9 | `LC_CURVE_FORTH_EFFIC` | SMALLINT |  |  |  |  |
| 10 | `LC_CURVE_FIFTH_HOURS` | DECIMAL(4,1) |  |  |  |  |
| 11 | `LC_CURVE_FIFTH_EFFIC` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.LC_LEARNING_CURVE_CODE,
       t.LC_LEARNING_CURVE_DESC,
       t.LC_CURVE_FIRST_HOURS,
       t.LC_CURVE_FIRST_EFFIC,
       t.LC_CURVE_SECOND_HOURS,
       t.LC_CURVE_SECOND_EFFIC,
       t.LC_CURVE_THIRD_HOURS,
       t.LC_CURVE_THIRD_EFFIC,
       t.LC_CURVE_FORTH_HOURS,
       t.LC_CURVE_FORTH_EFFIC,
       t.LC_CURVE_FIFTH_HOURS,
       t.LC_CURVE_FIFTH_EFFIC
FROM   DB2ADMIN.LEARNING_CURVE t
FETCH FIRST 100 ROWS ONLY;
```
