# DB2ADMIN.SCDA_WKC_PRIORITY

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `WP_IDENTIFIER`, `WP_WKCNTER`, `WP_WKCT_PROC`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184313

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WP_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `WP_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `WP_WKCT_PROC` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `WP_SEQ_DEPEND` | CHAR(1) |  |  |  |  |
| 4 | `WP_SEQALPHA` | VARCHAR(3) |  |  |  |  |
| 5 | `WP_PRIORITY_RALATION` | CHAR(1) |  |  |  |  |
| 6 | `WP_MACH_SETUP_CODE_LEVEL` | CHAR(1) |  |  |  |  |
| 7 | `WP_USR_NAMECR` | VARCHAR(10) |  |  |  |  |
| 8 | `WP_USR_TIMECR` | TIMESTAMP |  |  |  |  |
| 9 | `WP_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 10 | `WP_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.WP_IDENTIFIER,
       t.WP_WKCNTER,
       t.WP_WKCT_PROC,
       t.WP_SEQ_DEPEND,
       t.WP_SEQALPHA,
       t.WP_PRIORITY_RALATION,
       t.WP_MACH_SETUP_CODE_LEVEL,
       t.WP_USR_NAMECR,
       t.WP_USR_TIMECR,
       t.WP_USR_NAMECG,
       t.WP_USR_TIMECG
FROM   DB2ADMIN.SCDA_WKC_PRIORITY t
FETCH FIRST 100 ROWS ONLY;
```
