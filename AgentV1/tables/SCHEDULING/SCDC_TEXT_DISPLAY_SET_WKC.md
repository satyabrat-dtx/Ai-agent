# DB2ADMIN.SCDC_TEXT_DISPLAY_SET_WKC

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `TDW_IDENTIFIER`, `TDW_WORKSTATION`, `TDW_SET_NAME`, `TDW_SET_TYPE`, `TDW_WKCNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189526

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TDW_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `TDW_WORKSTATION` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 2 | `TDW_SET_NAME` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `TDW_SET_TYPE` | VARCHAR(14) | NOT NULL | PK | primary_key |  |
| 4 | `TDW_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.TDW_IDENTIFIER,
       t.TDW_WORKSTATION,
       t.TDW_SET_NAME,
       t.TDW_SET_TYPE,
       t.TDW_WKCNTER
FROM   DB2ADMIN.SCDC_TEXT_DISPLAY_SET_WKC t
FETCH FIRST 100 ROWS ONLY;
```
