# DB2ADMIN.ABSHELPCOPY

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `LANGUAGE`, `COUNTRY`, `ABSUIXMLPATH`, `ABSUIXMLNAME`, `NAME`, `HELPTYPE`, `RECORDTYPE`, `FORM`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 60905

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LANGUAGE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 1 | `COUNTRY` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 2 | `ABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `ABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 4 | `NAME` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 5 | `HELPTYPE` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `RECORDTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 7 | `FORM` | INTEGER | NOT NULL | PK | primary_key |  |
| 8 | `HELPTEXT` | CLOB(2000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.LANGUAGE,
       t.COUNTRY,
       t.ABSUIXMLPATH,
       t.ABSUIXMLNAME,
       t.NAME,
       t.HELPTYPE,
       t.RECORDTYPE,
       t.FORM,
       t.HELPTEXT
FROM   DB2ADMIN.ABSHELPCOPY t
FETCH FIRST 100 ROWS ONLY;
```
