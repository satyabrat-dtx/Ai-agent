# DB2ADMIN.SCDC_CUSTOM_DATE_COLUMN

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `CD_IDENTIFIER`, `CD_WKST_CODE`, `CD_BIN_COL_FIELD`, `CD_PROPCODE`, `CD_TYP_OPRATION`, `CD_TIME_TYPE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189429

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CD_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CD_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `CD_BIN_COL_FIELD` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `CD_PROPCODE` | VARCHAR(5) | NOT NULL | PK | primary_key |  |
| 4 | `CD_TYP_OPRATION` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 5 | `CD_TIME_TYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CD_IDENTIFIER,
       t.CD_WKST_CODE,
       t.CD_BIN_COL_FIELD,
       t.CD_PROPCODE,
       t.CD_TYP_OPRATION,
       t.CD_TIME_TYPE
FROM   DB2ADMIN.SCDC_CUSTOM_DATE_COLUMN t
FETCH FIRST 100 ROWS ONLY;
```
