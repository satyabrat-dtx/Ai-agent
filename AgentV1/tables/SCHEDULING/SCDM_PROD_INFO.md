# DB2ADMIN.SCDM_PROD_INFO

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `PI_IDENTIFIER`, `PI_PREQ_NO`, `PI_INFO_TYPE`, `PI_PSTEP_ID`, `PI_INFO_LINE_NUM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186308

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PI_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PI_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `PI_INFO_TYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 3 | `PI_PSTEP_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 4 | `PI_INFO_LINE_NUM` | SMALLINT | NOT NULL | PK | primary_key |  |
| 5 | `PI_INFO_AREA` | VARCHAR(120) |  |  |  |  |
| 6 | `PI_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 7 | `PI_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PI_IDENTIFIER,
       t.PI_PREQ_NO,
       t.PI_INFO_TYPE,
       t.PI_PSTEP_ID,
       t.PI_INFO_LINE_NUM,
       t.PI_INFO_AREA,
       t.PI_USR_NAMECG,
       t.PI_USR_TIMECG
FROM   DB2ADMIN.SCDM_PROD_INFO t
FETCH FIRST 100 ROWS ONLY;
```
