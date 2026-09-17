# DB2ADMIN.WRKEXTOPDOCPRINTLINECOMMENTS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `WRKEXTDOCPRTCREATIONTIMESTAMP`, `WRKEXTDOCPRTLINWRKDOCPRTLINE`, `WRKEXTOPDOCPRINTLINESUBLINE`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 30849

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WRKEXTDOCPRTCREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `WRKEXTDOCPRTLINWRKDOCPRTLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `WRKEXTOPDOCPRINTLINESUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 3 | `EXTOPDOCUMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `EXTOPDOCUMENTPROVCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 5 | `EXTOPDOCUMENTPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 6 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 8 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 9 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.WRKEXTDOCPRTCREATIONTIMESTAMP,
       t.WRKEXTDOCPRTLINWRKDOCPRTLINE,
       t.WRKEXTOPDOCPRINTLINESUBLINE,
       t.EXTOPDOCUMENTCOMPANYCODE,
       t.EXTOPDOCUMENTPROVCOUNTERCODE,
       t.EXTOPDOCUMENTPROVISIONALCODE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE
FROM   DB2ADMIN.WRKEXTOPDOCPRINTLINECOMMENTS t
FETCH FIRST 100 ROWS ONLY;
```
