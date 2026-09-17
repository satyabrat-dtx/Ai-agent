# DB2ADMIN.SCDA_WKC_PENALTIES

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `PN_IDENTIFIER`, `PN_PLAN_WKCT_CODE`, `PN_PLAN_WKCT_PROC`, `PN_COMPCASENUM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184936

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PN_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PN_PLAN_WKCT_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `PN_PLAN_WKCT_PROC` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `PN_COMPCASENUM` | VARCHAR(2) | NOT NULL | PK | primary_key |  |
| 4 | `PN_DAYSPANELTY` | SMALLINT |  |  |  |  |
| 5 | `PN_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 6 | `PN_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PN_IDENTIFIER,
       t.PN_PLAN_WKCT_CODE,
       t.PN_PLAN_WKCT_PROC,
       t.PN_COMPCASENUM,
       t.PN_DAYSPANELTY,
       t.PN_USR_NAMECG,
       t.PN_USR_TIMECG
FROM   DB2ADMIN.SCDA_WKC_PENALTIES t
FETCH FIRST 100 ROWS ONLY;
```
