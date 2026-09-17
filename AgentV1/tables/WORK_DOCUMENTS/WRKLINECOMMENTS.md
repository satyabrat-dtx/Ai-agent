# DB2ADMIN.WRKLINECOMMENTS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `CREATIONTIMESTAMP`, `SALORDLINESALORDERCOMPANYCODE`, `SALORDLINESALORDERCOUNTERCODE`, `SALESORDERLINESALESORDERCODE`, `SALESORDERLINEORDERLINE`, `SALESORDERLINEORDERSUBLINE`, `SALORDLINECOMPONENTORDERLINE`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 7032

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `SALORDLINESALORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `SALORDLINESALORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `SALESORDERLINESALESORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `SALESORDERLINEORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 5 | `SALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 6 | `SALORDLINECOMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 7 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 8 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 9 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 10 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.SALORDLINESALORDERCOMPANYCODE,
       t.SALORDLINESALORDERCOUNTERCODE,
       t.SALESORDERLINESALESORDERCODE,
       t.SALESORDERLINEORDERLINE,
       t.SALESORDERLINEORDERSUBLINE,
       t.SALORDLINECOMPONENTORDERLINE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE
FROM   DB2ADMIN.WRKLINECOMMENTS t
FETCH FIRST 100 ROWS ONLY;
```
