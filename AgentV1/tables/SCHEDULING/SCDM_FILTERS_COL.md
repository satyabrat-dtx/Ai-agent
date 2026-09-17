# DB2ADMIN.SCDM_FILTERS_COL

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `ID_TABLE`, `CCOLUMN`, `IDENTIFIER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189780

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_TABLE` | INTEGER | NOT NULL | PK | primary_key |  |
| 1 | `CCOLUMN` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 2 | `CCAPTION` | VARCHAR(100) |  |  |  |  |
| 3 | `CCOND` | VARCHAR(12) |  |  |  |  |
| 4 | `CVALUES` | VARCHAR(50) |  |  |  |  |
| 5 | `BVISIBLE` | SMALLINT |  |  |  |  |
| 6 | `IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ID_TABLE,
       t.CCOLUMN,
       t.CCAPTION,
       t.CCOND,
       t.CVALUES,
       t.BVISIBLE,
       t.IDENTIFIER
FROM   DB2ADMIN.SCDM_FILTERS_COL t
FETCH FIRST 100 ROWS ONLY;
```
