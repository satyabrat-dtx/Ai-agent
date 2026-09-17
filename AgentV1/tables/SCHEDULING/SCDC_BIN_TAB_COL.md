# DB2ADMIN.SCDC_BIN_TAB_COL

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `BC_IDENTIFIER`, `BC_WKST_CODE`, `BC_TABCODE`, `BC_BIN_COL_FIELD`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189395

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BC_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `BC_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `BC_TABCODE` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `BC_BIN_COL_FIELD` | SMALLINT | NOT NULL | PK | primary_key |  |
| 4 | `BC_BIN_COL_TITLE` | VARCHAR(50) |  |  |  |  |
| 5 | `BC_BIN_COL_POS` | SMALLINT |  |  |  |  |
| 6 | `BC_BIN_COL_WIDTH` | SMALLINT |  |  |  |  |
| 7 | `BC_BIN_COL_VIS` | SMALLINT |  |  |  |  |
| 8 | `BC_BIN_COL_ORD` | SMALLINT |  |  |  |  |
| 9 | `BC_BIN_COL_DESCENDING` | CHAR(1) |  |  |  |  |
| 10 | `BC_PROPCODE` | VARCHAR(5) |  |  |  |  |
| 11 | `BC_BIN_COL_NUM_COL_SORTED` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.BC_IDENTIFIER,
       t.BC_WKST_CODE,
       t.BC_TABCODE,
       t.BC_BIN_COL_FIELD,
       t.BC_BIN_COL_TITLE,
       t.BC_BIN_COL_POS,
       t.BC_BIN_COL_WIDTH,
       t.BC_BIN_COL_VIS,
       t.BC_BIN_COL_ORD,
       t.BC_BIN_COL_DESCENDING,
       t.BC_PROPCODE,
       t.BC_BIN_COL_NUM_COL_SORTED
FROM   DB2ADMIN.SCDC_BIN_TAB_COL t
FETCH FIRST 100 ROWS ONLY;
```
