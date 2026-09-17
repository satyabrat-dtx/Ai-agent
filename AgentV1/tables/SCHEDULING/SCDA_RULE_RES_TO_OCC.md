# DB2ADMIN.SCDA_RULE_RES_TO_OCC

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `RO_IDENTIFIER`, `RO_WKCNTER`, `RO_RSC_CODE`, `RO_RES_CATEGORY`, `RO_WC_PROCESS`, `RO_PROPERTY`, `RO_TYPE_PROD`, `RO_LINE_NUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184165

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RO_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `RO_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `RO_RSC_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `RO_RES_CATEGORY` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `RO_WC_PROCESS` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `RO_PROPERTY` | VARCHAR(5) | NOT NULL | PK | primary_key |  |
| 6 | `RO_TYPE_PROD` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 7 | `RO_LINE_NUMBER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 8 | `RO_SEQUENCE` | SMALLINT |  |  |  |  |
| 9 | `RO_OPERAND` | VARCHAR(2) |  |  |  |  |
| 10 | `RO_DEP_ON_CURR` | CHAR(1) |  |  |  |  |
| 11 | `RO_DEP_VALUE` | VARCHAR(90) |  |  |  |  |
| 12 | `RO_CASE` | VARCHAR(2) |  |  |  |  |
| 13 | `RO_USR_NAMECR` | VARCHAR(10) |  |  |  |  |
| 14 | `RO_USR_TIMECR` | TIMESTAMP |  |  |  |  |
| 15 | `RO_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 16 | `RO_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.RO_IDENTIFIER,
       t.RO_WKCNTER,
       t.RO_RSC_CODE,
       t.RO_RES_CATEGORY,
       t.RO_WC_PROCESS,
       t.RO_PROPERTY,
       t.RO_TYPE_PROD,
       t.RO_LINE_NUMBER,
       t.RO_SEQUENCE,
       t.RO_OPERAND,
       t.RO_DEP_ON_CURR,
       t.RO_DEP_VALUE
FROM   DB2ADMIN.SCDA_RULE_RES_TO_OCC t
FETCH FIRST 100 ROWS ONLY;
```
