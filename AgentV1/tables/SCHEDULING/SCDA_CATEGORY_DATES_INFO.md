# DB2ADMIN.SCDA_CATEGORY_DATES_INFO

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `CD_IDENTIFIER`, `CD_WKCNTER`, `CD_CATEGORY`, `CD_DATE_BEGIN`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184906

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CD_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CD_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `CD_CATEGORY` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `CD_DATE_BEGIN` | TIMESTAMP | NOT NULL | PK | primary_key |  |
| 4 | `CD_NUM_OF_MACHINES` | SMALLINT |  |  |  |  |
| 5 | `CD_FINITECAPACITY` | SMALLINT |  |  |  |  |
| 6 | `CD_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 7 | `CD_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CD_IDENTIFIER,
       t.CD_WKCNTER,
       t.CD_CATEGORY,
       t.CD_DATE_BEGIN,
       t.CD_NUM_OF_MACHINES,
       t.CD_FINITECAPACITY,
       t.CD_USR_NAMECG,
       t.CD_USR_TIMECG
FROM   DB2ADMIN.SCDA_CATEGORY_DATES_INFO t
FETCH FIRST 100 ROWS ONLY;
```
