# DB2ADMIN.SCDA_WKS_WKC

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `WW_IDENTIFIER`, `WW_WKST_CODE`, `WW_WKCNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184437

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WW_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `WW_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `WW_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `WW_TYPEUSED` | CHAR(1) |  |  |  |  |
| 4 | `WW_VISIBLE` | CHAR(1) |  |  |  |  |
| 5 | `WW_USR_NAMECR` | VARCHAR(10) |  |  |  |  |
| 6 | `WW_USR_TIMECR` | TIMESTAMP |  |  |  |  |
| 7 | `WW_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 8 | `WW_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.WW_IDENTIFIER,
       t.WW_WKST_CODE,
       t.WW_WKCNTER,
       t.WW_TYPEUSED,
       t.WW_VISIBLE,
       t.WW_USR_NAMECR,
       t.WW_USR_TIMECR,
       t.WW_USR_NAMECG,
       t.WW_USR_TIMECG
FROM   DB2ADMIN.SCDA_WKS_WKC t
FETCH FIRST 100 ROWS ONLY;
```
