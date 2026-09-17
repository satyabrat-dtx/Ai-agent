# DB2ADMIN.SCDC_PLAN_TAB_DET

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `PVD_IDENTIFIER`, `PVD_WKST_CODE`, `PVD_TABCODE`, `PVD_RSC_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188671

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PVD_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PVD_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `PVD_TABCODE` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `PVD_RSC_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `PVD_TOPOS` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PVD_IDENTIFIER,
       t.PVD_WKST_CODE,
       t.PVD_TABCODE,
       t.PVD_RSC_CODE,
       t.PVD_TOPOS
FROM   DB2ADMIN.SCDC_PLAN_TAB_DET t
FETCH FIRST 100 ROWS ONLY;
```
