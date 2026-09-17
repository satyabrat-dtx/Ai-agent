# DB2ADMIN.SCDM_CAPRES_DYNAMICPERRES

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `CRR_IDENTIFIER`, `CRR_RSC_CODE`, `CRR_DATE_BEGIN`, `CRR_FROMTIME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185864

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CRR_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CRR_RSC_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `CRR_DATE_BEGIN` | TIMESTAMP | NOT NULL | PK | primary_key |  |
| 3 | `CRR_FROMTIME` | SMALLINT | NOT NULL | PK | primary_key |  |
| 4 | `CRR_TODATELIMIT` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CRR_IDENTIFIER,
       t.CRR_RSC_CODE,
       t.CRR_DATE_BEGIN,
       t.CRR_FROMTIME,
       t.CRR_TODATELIMIT
FROM   DB2ADMIN.SCDM_CAPRES_DYNAMICPERRES t
FETCH FIRST 100 ROWS ONLY;
```
