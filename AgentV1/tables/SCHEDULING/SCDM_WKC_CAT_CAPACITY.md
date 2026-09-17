# DB2ADMIN.SCDM_WKC_CAT_CAPACITY

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `WCC_IDENTIFIER`, `WCC_WKST_CODE`, `WCC_WKCNTER`, `WCC_CATEGORY`, `WCC_DATE_BEGIN`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187394

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WCC_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `WCC_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `WCC_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `WCC_CATEGORY` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `WCC_DATE_BEGIN` | TIMESTAMP | NOT NULL | PK | primary_key |  |
| 5 | `WCC_NUM_MACHINE_SUSPEND` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.WCC_IDENTIFIER,
       t.WCC_WKST_CODE,
       t.WCC_WKCNTER,
       t.WCC_CATEGORY,
       t.WCC_DATE_BEGIN,
       t.WCC_NUM_MACHINE_SUSPEND
FROM   DB2ADMIN.SCDM_WKC_CAT_CAPACITY t
FETCH FIRST 100 ROWS ONLY;
```
