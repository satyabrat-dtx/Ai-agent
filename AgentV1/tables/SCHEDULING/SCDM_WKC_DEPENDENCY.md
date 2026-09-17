# DB2ADMIN.SCDM_WKC_DEPENDENCY

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `WD_IDENTIFIER`, `WD_SCHED_WKC`, `WD_SCHED_WKC_PROC`, `WD_DEPEND_ON`, `WD_DEP_IS_SCHD_RSC_CAT`, `WD_DEP_IS_SCHD_WKC`, `WD_DEP_IS_SCHD_RSC`, `WD_NO_SCHED_RSC_CAT`, `WD_NO_SCHED_WKC`, `WD_NO_SCHED_RSC`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187587

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WD_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `WD_SCHED_WKC` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `WD_SCHED_WKC_PROC` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `WD_DEPEND_ON` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 4 | `WD_DEP_IS_SCHD_RSC_CAT` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `WD_DEP_IS_SCHD_WKC` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 6 | `WD_DEP_IS_SCHD_RSC` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 7 | `WD_NO_SCHED_RSC_CAT` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 8 | `WD_NO_SCHED_WKC` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 9 | `WD_NO_SCHED_RSC` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 10 | `WD_USR_NAMECR` | VARCHAR(10) |  |  |  |  |
| 11 | `WD_USR_TIMECR` | TIMESTAMP |  |  |  |  |
| 12 | `WD_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 13 | `WD_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.WD_IDENTIFIER,
       t.WD_SCHED_WKC,
       t.WD_SCHED_WKC_PROC,
       t.WD_DEPEND_ON,
       t.WD_DEP_IS_SCHD_RSC_CAT,
       t.WD_DEP_IS_SCHD_WKC,
       t.WD_DEP_IS_SCHD_RSC,
       t.WD_NO_SCHED_RSC_CAT,
       t.WD_NO_SCHED_WKC,
       t.WD_NO_SCHED_RSC,
       t.WD_USR_NAMECR,
       t.WD_USR_TIMECR
FROM   DB2ADMIN.SCDM_WKC_DEPENDENCY t
FETCH FIRST 100 ROWS ONLY;
```
