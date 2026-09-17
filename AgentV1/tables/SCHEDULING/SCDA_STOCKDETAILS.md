# DB2ADMIN.SCDA_STOCKDETAILS

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `SD_IDENTIFIER`, `SD_BALANCEID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185468

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SD_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `SD_BALANCEID` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `SD_TYPE_PROD` | VARCHAR(3) |  |  |  |  |
| 3 | `SD_PRODUCT_CODE` | VARCHAR(120) |  |  |  |  |
| 4 | `SD_NET_GROUP_CODE` | VARCHAR(16) |  |  |  |  |
| 5 | `SD_DETAILS` | VARCHAR(120) |  |  |  |  |
| 6 | `SD_USED` | CHAR(1) |  |  |  |  |
| 7 | `SD_PREQ_NO` | VARCHAR(30) |  |  |  |  |
| 8 | `SD_PSTEP_ID` | SMALLINT |  |  |  |  |
| 9 | `SD_PSUBST_ID` | SMALLINT |  |  |  |  |
| 10 | `SD_REPROC_NO` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.SD_IDENTIFIER,
       t.SD_BALANCEID,
       t.SD_TYPE_PROD,
       t.SD_PRODUCT_CODE,
       t.SD_NET_GROUP_CODE,
       t.SD_DETAILS,
       t.SD_USED,
       t.SD_PREQ_NO,
       t.SD_PSTEP_ID,
       t.SD_PSUBST_ID,
       t.SD_REPROC_NO
FROM   DB2ADMIN.SCDA_STOCKDETAILS t
FETCH FIRST 100 ROWS ONLY;
```
