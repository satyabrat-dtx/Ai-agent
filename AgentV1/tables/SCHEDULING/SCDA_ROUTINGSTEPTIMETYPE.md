# DB2ADMIN.SCDA_ROUTINGSTEPTIMETYPE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `IDENTIFIER`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184631

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CODE` | VARCHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 3 | `TYPE` | VARCHAR(2) |  |  |  |  |
| 4 | `APPLY` | VARCHAR(2) |  |  |  |  |
| 5 | `APPLYTYPECODE` | VARCHAR(20) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.CODE,
       t.SHORTDESCRIPTION,
       t.TYPE,
       t.APPLY,
       t.APPLYTYPECODE
FROM   DB2ADMIN.SCDA_ROUTINGSTEPTIMETYPE t
FETCH FIRST 100 ROWS ONLY;
```
