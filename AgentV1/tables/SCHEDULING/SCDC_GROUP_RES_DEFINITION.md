# DB2ADMIN.SCDC_GROUP_RES_DEFINITION

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `GR_IDENTIFIER`, `GR_WORKSTATION`, `GR_SET_NAME`, `GR_RSC_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189617

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `GR_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `GR_WORKSTATION` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 2 | `GR_SET_NAME` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `GR_RSC_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `GR_NUM_SCHED_COUNTER` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.GR_IDENTIFIER,
       t.GR_WORKSTATION,
       t.GR_SET_NAME,
       t.GR_RSC_CODE,
       t.GR_NUM_SCHED_COUNTER
FROM   DB2ADMIN.SCDC_GROUP_RES_DEFINITION t
FETCH FIRST 100 ROWS ONLY;
```
