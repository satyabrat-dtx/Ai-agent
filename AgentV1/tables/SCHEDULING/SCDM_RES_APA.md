# DB2ADMIN.SCDM_RES_APA

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `RD_IDENTIFIER`, `RD_RSC_CODE`, `RD_SUB_RSC`, `RD_DATE_BEGIN`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186877

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RD_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `RD_RSC_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `RD_SUB_RSC` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `RD_DATE_BEGIN` | TIMESTAMP | NOT NULL | PK | primary_key |  |
| 4 | `RD_DATE_END` | TIMESTAMP |  |  |  |  |
| 5 | `RD_NUM_RSC_COMP` | DECIMAL(5,0) |  |  |  |  |
| 6 | `RD_USR_NAMECR` | VARCHAR(10) |  |  |  |  |
| 7 | `RD_USR_TIMECR` | TIMESTAMP |  |  |  |  |
| 8 | `RD_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 9 | `RD_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.RD_IDENTIFIER,
       t.RD_RSC_CODE,
       t.RD_SUB_RSC,
       t.RD_DATE_BEGIN,
       t.RD_DATE_END,
       t.RD_NUM_RSC_COMP,
       t.RD_USR_NAMECR,
       t.RD_USR_TIMECR,
       t.RD_USR_NAMECG,
       t.RD_USR_TIMECG
FROM   DB2ADMIN.SCDM_RES_APA t
FETCH FIRST 100 ROWS ONLY;
```
