# DB2ADMIN.SCDC_CLR_CAP_RES

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `CRC_IDENTIFIER`, `CRC_WKST_CODE`, `CRC_VALUE_FROM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189367

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CRC_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CRC_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `CRC_VALUE_FROM` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `CRC_INT_COLOR` | INTEGER |  |  |  |  |
| 4 | `CRC_BDR_COLOR` | INTEGER |  |  |  |  |
| 5 | `CRC_TXT_COLOR` | INTEGER |  |  |  |  |
| 6 | `CRC_TXT_DESCRIPTION` | VARCHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CRC_IDENTIFIER,
       t.CRC_WKST_CODE,
       t.CRC_VALUE_FROM,
       t.CRC_INT_COLOR,
       t.CRC_BDR_COLOR,
       t.CRC_TXT_COLOR,
       t.CRC_TXT_DESCRIPTION
FROM   DB2ADMIN.SCDC_CLR_CAP_RES t
FETCH FIRST 100 ROWS ONLY;
```
