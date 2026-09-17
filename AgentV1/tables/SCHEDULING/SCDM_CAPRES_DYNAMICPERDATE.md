# DB2ADMIN.SCDM_CAPRES_DYNAMICPERDATE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `CRD_IDENTIFIER`, `CRD_RSC_CODE`, `CRD_DATE_BEGIN`, `CRD_FROMTIME`, `CRD_SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185891

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CRD_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CRD_RSC_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `CRD_DATE_BEGIN` | TIMESTAMP | NOT NULL | PK | primary_key |  |
| 3 | `CRD_FROMTIME` | SMALLINT | NOT NULL | PK | primary_key |  |
| 4 | `CRD_SEQUENCE` | SMALLINT | NOT NULL | PK | primary_key |  |
| 5 | `CRD_NUMBEROFHOURS` | SMALLINT |  |  |  |  |
| 6 | `CRD_COLOR` | INTEGER |  |  |  |  |
| 7 | `CRD_DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 8 | `CRD_COMPCASENUM` | SMALLINT |  |  |  |  |
| 9 | `CRD_COMMENT` | VARCHAR(30) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CRD_IDENTIFIER,
       t.CRD_RSC_CODE,
       t.CRD_DATE_BEGIN,
       t.CRD_FROMTIME,
       t.CRD_SEQUENCE,
       t.CRD_NUMBEROFHOURS,
       t.CRD_COLOR,
       t.CRD_DESCRIPTION,
       t.CRD_COMPCASENUM,
       t.CRD_COMMENT
FROM   DB2ADMIN.SCDM_CAPRES_DYNAMICPERDATE t
FETCH FIRST 100 ROWS ONLY;
```
