# DB2ADMIN.SCDM_EXT_INFO_HDR

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `EH_IDENTIFIER`, `EH_CONNE_KEY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186079

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EH_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `EH_CONNE_KEY` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `EH_CONNE_TYPE` | CHAR(1) |  |  |  |  |
| 3 | `EH_DUE_DATE` | TIMESTAMP |  |  |  |  |
| 4 | `EH_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 5 | `EH_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.EH_IDENTIFIER,
       t.EH_CONNE_KEY,
       t.EH_CONNE_TYPE,
       t.EH_DUE_DATE,
       t.EH_USR_NAMECG,
       t.EH_USR_TIMECG
FROM   DB2ADMIN.SCDM_EXT_INFO_HDR t
FETCH FIRST 100 ROWS ONLY;
```
