# DB2ADMIN.SCDM_FILTERS

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `ID`, `IDENTIFIER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189753

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID` | INTEGER | NOT NULL | PK | primary_key |  |
| 1 | `CTABLE` | VARCHAR(30) |  |  |  |  |
| 2 | `BACTIVE` | SMALLINT |  |  |  |  |
| 3 | `CSQL` | VARCHAR(1024) |  |  |  |  |
| 4 | `CLOCK` | SMALLINT |  |  |  |  |
| 5 | `CCAPTION` | VARCHAR(100) |  |  |  |  |
| 6 | `IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ID,
       t.CTABLE,
       t.BACTIVE,
       t.CSQL,
       t.CLOCK,
       t.CCAPTION,
       t.IDENTIFIER
FROM   DB2ADMIN.SCDM_FILTERS t
FETCH FIRST 100 ROWS ONLY;
```
