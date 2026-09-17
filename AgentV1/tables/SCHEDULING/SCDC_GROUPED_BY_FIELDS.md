# DB2ADMIN.SCDC_GROUPED_BY_FIELDS

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `GB_IDENTIFIER`, `GB_WKST_CODE`, `GB_GROUPEDBY_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189581

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `GB_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `GB_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `GB_GROUPEDBY_CODE` | VARCHAR(20) | NOT NULL | PK | primary_key |  |
| 3 | `GB_PROD_REQ` | CHAR(1) |  |  |  |  |
| 4 | `GB_PROD_FAMILY` | CHAR(1) |  |  |  |  |
| 5 | `GB_PROP_CODE1` | VARCHAR(5) |  |  |  |  |
| 6 | `GB_PROP_CODE2` | VARCHAR(5) |  |  |  |  |
| 7 | `GB_PROP_CODE3` | VARCHAR(5) |  |  |  |  |
| 8 | `GB_PROP_CODE4` | VARCHAR(5) |  |  |  |  |
| 9 | `GB_PROP_CODE5` | VARCHAR(5) |  |  |  |  |
| 10 | `GB_PROP_CODE6` | VARCHAR(5) |  |  |  |  |
| 11 | `GB_PROP_CODE7` | VARCHAR(5) |  |  |  |  |
| 12 | `GB_PROP_CODE8` | VARCHAR(5) |  |  |  |  |
| 13 | `GB_PROP_CODE9` | VARCHAR(5) |  |  |  |  |
| 14 | `GB_PROP_CODE10` | VARCHAR(5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.GB_IDENTIFIER,
       t.GB_WKST_CODE,
       t.GB_GROUPEDBY_CODE,
       t.GB_PROD_REQ,
       t.GB_PROD_FAMILY,
       t.GB_PROP_CODE1,
       t.GB_PROP_CODE2,
       t.GB_PROP_CODE3,
       t.GB_PROP_CODE4,
       t.GB_PROP_CODE5,
       t.GB_PROP_CODE6,
       t.GB_PROP_CODE7
FROM   DB2ADMIN.SCDC_GROUPED_BY_FIELDS t
FETCH FIRST 100 ROWS ONLY;
```
