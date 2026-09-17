# DB2ADMIN.SCDM_WKST

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `WK_IDENTIFIER`, `WK_WKST_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187303

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WK_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `WK_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `WK_WKDESCR` | VARCHAR(30) |  |  |  |  |
| 3 | `WK_WKPASSWD` | VARCHAR(10) |  |  |  |  |
| 4 | `WK_USR_NAMECR` | VARCHAR(10) |  |  |  |  |
| 5 | `WK_USR_TIMECR` | TIMESTAMP |  |  |  |  |
| 6 | `WK_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 7 | `WK_USR_TIMECG` | TIMESTAMP |  |  |  |  |
| 8 | `WK_WORKSTATIONTYPE` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.WK_IDENTIFIER,
       t.WK_WKST_CODE,
       t.WK_WKDESCR,
       t.WK_WKPASSWD,
       t.WK_USR_NAMECR,
       t.WK_USR_TIMECR,
       t.WK_USR_NAMECG,
       t.WK_USR_TIMECG,
       t.WK_WORKSTATIONTYPE
FROM   DB2ADMIN.SCDM_WKST t
FETCH FIRST 100 ROWS ONLY;
```
