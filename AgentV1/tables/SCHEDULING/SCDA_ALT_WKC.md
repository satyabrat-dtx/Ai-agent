# DB2ADMIN.SCDA_ALT_WKC

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `AW_IDENTIFIER`, `AW_WKCNTER`, `AW_WKCT_PROC`, `AW_ALTERN_WC`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 183669

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `AW_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `AW_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `AW_WKCT_PROC` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `AW_ALTERN_WC` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `AW_ALTERN_WC_PROCES` | VARCHAR(8) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.AW_IDENTIFIER,
       t.AW_WKCNTER,
       t.AW_WKCT_PROC,
       t.AW_ALTERN_WC,
       t.AW_ALTERN_WC_PROCES
FROM   DB2ADMIN.SCDA_ALT_WKC t
FETCH FIRST 100 ROWS ONLY;
```
