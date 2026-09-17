# DB2ADMIN.WRKDOCUMENTPRINTCOMMENTS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `CREATIONTIMESTAMP`, `WRKDOCUMENTPRINTLINE`, `ORIGIN`, `CODE`, `COUNTERCODE`, `PROVENIENCECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 8169

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `WRKDOCUMENTPRINTLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `PROVENIENCECODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 6 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 7 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.WRKDOCUMENTPRINTLINE,
       t.ORIGIN,
       t.CODE,
       t.COUNTERCODE,
       t.PROVENIENCECODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE
FROM   DB2ADMIN.WRKDOCUMENTPRINTCOMMENTS t
FETCH FIRST 100 ROWS ONLY;
```
