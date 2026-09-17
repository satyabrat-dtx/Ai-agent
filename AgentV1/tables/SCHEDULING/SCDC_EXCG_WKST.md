# DB2ADMIN.SCDC_EXCG_WKST

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `CEW_IDENTIFIER`, `CEW_WKST_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188759

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CEW_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CEW_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `CEW_CONNECT` | TIMESTAMP |  |  |  |  |
| 3 | `CEW_LAST_UPD` | SMALLINT |  |  |  |  |
| 4 | `CEW_OP` | CHAR(1) |  |  |  |  |
| 5 | `CEW_POLL` | CHAR(1) |  |  |  |  |
| 6 | `CEW_COUNTER` | INTEGER |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CEW_IDENTIFIER,
       t.CEW_WKST_CODE,
       t.CEW_CONNECT,
       t.CEW_LAST_UPD,
       t.CEW_OP,
       t.CEW_POLL,
       t.CEW_COUNTER
FROM   DB2ADMIN.SCDC_EXCG_WKST t
FETCH FIRST 100 ROWS ONLY;
```
