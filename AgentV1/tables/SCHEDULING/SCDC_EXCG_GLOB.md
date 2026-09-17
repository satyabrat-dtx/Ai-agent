# DB2ADMIN.SCDC_EXCG_GLOB

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `CEG_IDENTIFIER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188736

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CEG_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CEG_LAST_UPD` | SMALLINT |  |  |  |  |
| 2 | `CEG_SL_OP` | CHAR(1) |  |  |  |  |
| 3 | `CEG_SL_ON` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CEG_IDENTIFIER,
       t.CEG_LAST_UPD,
       t.CEG_SL_OP,
       t.CEG_SL_ON
FROM   DB2ADMIN.SCDC_EXCG_GLOB t
FETCH FIRST 100 ROWS ONLY;
```
