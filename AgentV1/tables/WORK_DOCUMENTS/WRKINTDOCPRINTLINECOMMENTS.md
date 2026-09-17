# DB2ADMIN.WRKINTDOCPRINTLINECOMMENTS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `WRKINTDOCPRTCREATIONTIMESTAMP`, `WRKINTDOCPRTLINWRKDOCPRTLINE`, `WRKINTDOCPRINTLINESUBLINE`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 61425

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WRKINTDOCPRTCREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `WRKINTDOCPRTLINWRKDOCPRTLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `WRKINTDOCPRINTLINESUBLINE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 3 | `INTERNALDOCUMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `INTDOCPROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 5 | `INTDOCUMENTPROVISIONALCODE` | CHAR(15) |  |  |  |  |
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
SELECT t.WRKINTDOCPRTCREATIONTIMESTAMP,
       t.WRKINTDOCPRTLINWRKDOCPRTLINE,
       t.WRKINTDOCPRINTLINESUBLINE,
       t.INTERNALDOCUMENTCOMPANYCODE,
       t.INTDOCPROVISIONALCOUNTERCODE,
       t.INTDOCUMENTPROVISIONALCODE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE
FROM   DB2ADMIN.WRKINTDOCPRINTLINECOMMENTS t
FETCH FIRST 100 ROWS ONLY;
```
