# DB2ADMIN.SCDC_CUSTOM_DATES_GAP_COLUMN

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `CDG_IDENTIFIER`, `CDG_WKST_CODE`, `CDG_COLUMN_NUM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189459

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CDG_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CDG_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `CDG_COLUMN_NUM` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `CDG_STARTING_DATE_COLUMN` | SMALLINT |  |  |  |  |
| 4 | `CDG_TYP_OPRATION` | CHAR(1) |  |  |  |  |
| 5 | `CDG_PROPERTY_DATE_COLUMN` | VARCHAR(5) |  |  |  |  |
| 6 | `CDG_BIN_DATE_COLUMN` | SMALLINT |  |  |  |  |
| 7 | `CDG_TIME_TYPE` | CHAR(1) |  |  |  |  |
| 8 | `CDG_ABSOLUTE_VALUE` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CDG_IDENTIFIER,
       t.CDG_WKST_CODE,
       t.CDG_COLUMN_NUM,
       t.CDG_STARTING_DATE_COLUMN,
       t.CDG_TYP_OPRATION,
       t.CDG_PROPERTY_DATE_COLUMN,
       t.CDG_BIN_DATE_COLUMN,
       t.CDG_TIME_TYPE,
       t.CDG_ABSOLUTE_VALUE
FROM   DB2ADMIN.SCDC_CUSTOM_DATES_GAP_COLUMN t
FETCH FIRST 100 ROWS ONLY;
```
