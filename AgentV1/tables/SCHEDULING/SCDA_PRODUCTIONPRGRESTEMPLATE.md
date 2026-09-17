# DB2ADMIN.SCDA_PRODUCTIONPRGRESTEMPLATE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `IDENTIFIER`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185113

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CODE` | VARCHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `S_DESCR` | VARCHAR(80) |  |  |  |  |
| 3 | `L_DESCR` | VARCHAR(200) |  |  |  |  |
| 4 | `HANDLEDBYMQM` | CHAR(1) |  |  |  |  |
| 5 | `QUANTITYTYPE` | CHAR(1) |  |  |  |  |
| 6 | `FINALANDSPLIT` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.CODE,
       t.S_DESCR,
       t.L_DESCR,
       t.HANDLEDBYMQM,
       t.QUANTITYTYPE,
       t.FINALANDSPLIT
FROM   DB2ADMIN.SCDA_PRODUCTIONPRGRESTEMPLATE t
FETCH FIRST 100 ROWS ONLY;
```
