# DB2ADMIN.SCDM_RES_SUB

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `DH_IDENTIFIER`, `DH_RSC_CODE`, `DH_SUB_RSC`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186191

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DH_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `DH_RSC_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `DH_SUB_RSC` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `DH_CAL` | VARCHAR(3) |  |  |  |  |
| 4 | `DH_PROD_LINE` | VARCHAR(4) |  |  |  |  |
| 5 | `DH_COMMENT` | VARCHAR(30) |  |  |  |  |
| 6 | `DH_NUM_RSC_COMPONENTS` | SMALLINT |  |  |  |  |
| 7 | `DH_USR_NAMECR` | VARCHAR(10) |  |  |  |  |
| 8 | `DH_USR_TIMECR` | TIMESTAMP |  |  |  |  |
| 9 | `DH_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 10 | `DH_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.DH_IDENTIFIER,
       t.DH_RSC_CODE,
       t.DH_SUB_RSC,
       t.DH_CAL,
       t.DH_PROD_LINE,
       t.DH_COMMENT,
       t.DH_NUM_RSC_COMPONENTS,
       t.DH_USR_NAMECR,
       t.DH_USR_TIMECR,
       t.DH_USR_NAMECG,
       t.DH_USR_TIMECG
FROM   DB2ADMIN.SCDM_RES_SUB t
FETCH FIRST 100 ROWS ONLY;
```
