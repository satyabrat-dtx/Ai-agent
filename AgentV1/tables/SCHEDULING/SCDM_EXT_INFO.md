# DB2ADMIN.SCDM_EXT_INFO

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `EI_IDENTIFIER`, `EI_CONNE_KEY`, `EI_INFO_LINE_NUM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186052

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EI_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `EI_CONNE_KEY` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `EI_INFO_LINE_NUM` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `EI_INFO_AREA` | VARCHAR(120) |  |  |  |  |
| 4 | `EI_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 5 | `EI_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.EI_IDENTIFIER,
       t.EI_CONNE_KEY,
       t.EI_INFO_LINE_NUM,
       t.EI_INFO_AREA,
       t.EI_USR_NAMECG,
       t.EI_USR_TIMECG
FROM   DB2ADMIN.SCDM_EXT_INFO t
FETCH FIRST 100 ROWS ONLY;
```
