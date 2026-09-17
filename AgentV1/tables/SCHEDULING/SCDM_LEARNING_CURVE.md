# DB2ADMIN.SCDM_LEARNING_CURVE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `LC_IDENTIFIER`, `LC_LEARNING_CURVE_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187984

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LC_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `LC_LEARNING_CURVE_CODE` | VARCHAR(6) | NOT NULL | PK | primary_key |  |
| 2 | `LC_LEARNING_CURVE_DESC` | VARCHAR(30) |  |  |  |  |
| 3 | `LC_CURVE_FIRST_HOURS` | DECIMAL(4,1) |  |  |  |  |
| 4 | `LC_CURVE_FIRST_EFFIC` | SMALLINT |  |  |  |  |
| 5 | `LC_CURVE_SECOND_HOURS` | DECIMAL(4,1) |  |  |  |  |
| 6 | `LC_CURVE_SECOND_EFFIC` | SMALLINT |  |  |  |  |
| 7 | `LC_CURVE_THIRD_HOURS` | DECIMAL(4,1) |  |  |  |  |
| 8 | `LC_CURVE_THIRD_EFFIC` | SMALLINT |  |  |  |  |
| 9 | `LC_CURVE_FORTH_HOURS` | DECIMAL(4,1) |  |  |  |  |
| 10 | `LC_CURVE_FORTH_EFFIC` | SMALLINT |  |  |  |  |
| 11 | `LC_CURVE_FIFTH_HOURS` | DECIMAL(4,1) |  |  |  |  |
| 12 | `LC_CURVE_FIFTH_EFFIC` | SMALLINT |  |  |  |  |
| 13 | `LC_CURVE_SIXTH_HOURS` | DECIMAL(4,1) |  |  |  |  |
| 14 | `LC_CURVE_SIXTH_EFFIC` | SMALLINT |  |  |  |  |
| 15 | `LC_CURVE_SEVENTH_HOURS` | DECIMAL(4,1) |  |  |  |  |
| 16 | `LC_CURVE_SEVENTH_EFFIC` | SMALLINT |  |  |  |  |
| 17 | `LC_CURVE_EIGHTH_HOURS` | DECIMAL(4,1) |  |  |  |  |
| 18 | `LC_CURVE_EIGHTH_EFFIC` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.LC_IDENTIFIER,
       t.LC_LEARNING_CURVE_CODE,
       t.LC_LEARNING_CURVE_DESC,
       t.LC_CURVE_FIRST_HOURS,
       t.LC_CURVE_FIRST_EFFIC,
       t.LC_CURVE_SECOND_HOURS,
       t.LC_CURVE_SECOND_EFFIC,
       t.LC_CURVE_THIRD_HOURS,
       t.LC_CURVE_THIRD_EFFIC,
       t.LC_CURVE_FORTH_HOURS,
       t.LC_CURVE_FORTH_EFFIC,
       t.LC_CURVE_FIFTH_HOURS
FROM   DB2ADMIN.SCDM_LEARNING_CURVE t
FETCH FIRST 100 ROWS ONLY;
```
