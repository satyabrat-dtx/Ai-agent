# DB2ADMIN.SCDA_ITEMTYPETEMPLATE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `IDENTIFIER`, `ITEMTYPECODE`, `PRODUCTIONDEMANDTEMPLATECODE`, `WORKCENTERFORSPLIT`, `OPERATIONFORSPLIT`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185307

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `ITEMTYPECODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `PRODUCTIONDEMANDTEMPLATECODE` | VARCHAR(40) | NOT NULL | PK | primary_key |  |
| 3 | `HOSTSPLITCONFIRMLEVEL` | CHAR(1) |  |  |  |  |
| 4 | `WORKCENTERFORSPLIT` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `OPERATIONFORSPLIT` | VARCHAR(8) | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.ITEMTYPECODE,
       t.PRODUCTIONDEMANDTEMPLATECODE,
       t.HOSTSPLITCONFIRMLEVEL,
       t.WORKCENTERFORSPLIT,
       t.OPERATIONFORSPLIT
FROM   DB2ADMIN.SCDA_ITEMTYPETEMPLATE t
FETCH FIRST 100 ROWS ONLY;
```
