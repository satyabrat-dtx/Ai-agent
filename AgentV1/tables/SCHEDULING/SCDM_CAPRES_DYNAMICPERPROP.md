# DB2ADMIN.SCDM_CAPRES_DYNAMICPERPROP

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `CRP_IDENTIFIER`, `CRP_RSC_CODE`, `CRP_DATE_BEGIN`, `CRP_FROMTIME`, `CRP_SEQUENCE`, `CRP_PROPERTY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185924

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CRP_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CRP_RSC_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `CRP_DATE_BEGIN` | TIMESTAMP | NOT NULL | PK | primary_key |  |
| 3 | `CRP_FROMTIME` | SMALLINT | NOT NULL | PK | primary_key |  |
| 4 | `CRP_SEQUENCE` | SMALLINT | NOT NULL | PK | primary_key |  |
| 5 | `CRP_PROPERTY` | VARCHAR(5) | NOT NULL | PK | primary_key |  |
| 6 | `CRP_VALUE` | VARCHAR(90) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CRP_IDENTIFIER,
       t.CRP_RSC_CODE,
       t.CRP_DATE_BEGIN,
       t.CRP_FROMTIME,
       t.CRP_SEQUENCE,
       t.CRP_PROPERTY,
       t.CRP_VALUE
FROM   DB2ADMIN.SCDM_CAPRES_DYNAMICPERPROP t
FETCH FIRST 100 ROWS ONLY;
```
