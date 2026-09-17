# DB2ADMIN.SCDC_PROP_SHOW_COLOR

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `PC_IDENTIFIER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189313

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PC_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PC_WKST_CODE` | VARCHAR(10) |  |  |  |  |
| 2 | `PC_PROPERTY` | VARCHAR(5) |  |  |  |  |
| 3 | `PC_PROPVALFROM` | VARCHAR(90) |  |  |  |  |
| 4 | `PC_PROPVALTO` | VARCHAR(90) |  |  |  |  |
| 5 | `PC_JOB_PROP_COLOR` | INTEGER |  |  |  |  |
| 6 | `PC_DFT_COLOR` | INTEGER |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PC_IDENTIFIER,
       t.PC_WKST_CODE,
       t.PC_PROPERTY,
       t.PC_PROPVALFROM,
       t.PC_PROPVALTO,
       t.PC_JOB_PROP_COLOR,
       t.PC_DFT_COLOR
FROM   DB2ADMIN.SCDC_PROP_SHOW_COLOR t
FETCH FIRST 100 ROWS ONLY;
```
