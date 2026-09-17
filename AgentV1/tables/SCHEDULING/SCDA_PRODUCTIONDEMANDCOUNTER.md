# DB2ADMIN.SCDA_PRODUCTIONDEMANDCOUNTER

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `IDENTIFIER`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185140

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CODE` | VARCHAR(8) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `S_DESCR` | VARCHAR(60) |  |  |  |  |
| 3 | `FAMILYCODEENDPOSITION` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.CODE,
       t.S_DESCR,
       t.FAMILYCODEENDPOSITION
FROM   DB2ADMIN.SCDA_PRODUCTIONDEMANDCOUNTER t
FETCH FIRST 100 ROWS ONLY;
```
