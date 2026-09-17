# DB2ADMIN.SCDC_AUTO_SCHED_WC_CFG

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `ASW_IDENTIFIER`, `ASW_WKST_CODE`, `ASW_WKCNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188504

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ASW_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `ASW_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `ASW_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `ASW_CFGNAME` | VARCHAR(14) |  |  |  |  |
| 4 | `ASW_STANDARD_SLOT_DUR` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ASW_IDENTIFIER,
       t.ASW_WKST_CODE,
       t.ASW_WKCNTER,
       t.ASW_CFGNAME,
       t.ASW_STANDARD_SLOT_DUR
FROM   DB2ADMIN.SCDC_AUTO_SCHED_WC_CFG t
FETCH FIRST 100 ROWS ONLY;
```
