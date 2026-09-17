# DB2ADMIN.SCDA_MACHINE_SETUP_CODE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `MS_IDENTIFIER`, `MS_RES_CAT_CODE`, `MS_WKCNTER`, `MS_WKCT_PROC`, `MS_RSC_CODE`, `MS_MACHINE_SETUP_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 183819

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MS_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `MS_RES_CAT_CODE` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `MS_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `MS_WKCT_PROC` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `MS_RSC_CODE` | VARCHAR(6) | NOT NULL | PK | primary_key |  |
| 5 | `MS_DESCRIPTION` | VARCHAR(70) |  |  |  |  |
| 6 | `MS_MACHINE_SETUP_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 7 | `MS_USR_NAMECR` | VARCHAR(10) |  |  |  |  |
| 8 | `MS_USR_TIMECR` | TIMESTAMP |  |  |  |  |
| 9 | `MS_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 10 | `MS_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.MS_IDENTIFIER,
       t.MS_RES_CAT_CODE,
       t.MS_WKCNTER,
       t.MS_WKCT_PROC,
       t.MS_RSC_CODE,
       t.MS_DESCRIPTION,
       t.MS_MACHINE_SETUP_CODE,
       t.MS_USR_NAMECR,
       t.MS_USR_TIMECR,
       t.MS_USR_NAMECG,
       t.MS_USR_TIMECG
FROM   DB2ADMIN.SCDA_MACHINE_SETUP_CODE t
FETCH FIRST 100 ROWS ONLY;
```
