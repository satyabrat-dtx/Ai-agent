# DB2ADMIN.SCDA_RESCAT

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `CT_IDENTIFIER`, `CT_RES_CATEGORY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184017

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CT_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CT_RES_CATEGORY` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `CT_DESC` | VARCHAR(14) |  |  |  |  |
| 3 | `CT_LONG_DESC` | VARCHAR(30) |  |  |  |  |
| 4 | `CT_ADDITIONAL_CAPACITY` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CT_IDENTIFIER,
       t.CT_RES_CATEGORY,
       t.CT_DESC,
       t.CT_LONG_DESC,
       t.CT_ADDITIONAL_CAPACITY
FROM   DB2ADMIN.SCDA_RESCAT t
FETCH FIRST 100 ROWS ONLY;
```
