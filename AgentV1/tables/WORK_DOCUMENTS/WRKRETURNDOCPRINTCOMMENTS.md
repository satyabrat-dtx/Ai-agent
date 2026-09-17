# DB2ADMIN.WRKRETURNDOCPRINTCOMMENTS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `CREATIONTIMESTAMP`, `WRKRETURNDOCUMENTPRINTLINE`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 24231

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `WRKRETURNDOCUMENTPRINTLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 5 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.WRKRETURNDOCUMENTPRINTLINE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE
FROM   DB2ADMIN.WRKRETURNDOCPRINTCOMMENTS t
FETCH FIRST 100 ROWS ONLY;
```
