# DB2ADMIN.WRKINTDOCUMENTGROUPCOMMENTS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `CREATIONTIMESTAMP`, `INTERNALDOCUMENTCOMPANYCODE`, `INTDOCPROVISIONALCOUNTERCODE`, `INTDOCUMENTPROVISIONALCODE`, `LINEGROUP`, `ORIGIN`, `CODE`, `COUNTERCODE`, `PROVENIENCECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 2543

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `INTERNALDOCUMENTCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `INTDOCPROVISIONALCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `INTDOCUMENTPROVISIONALCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `LINEGROUP` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 7 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 8 | `PROVENIENCECODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 9 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 10 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.INTERNALDOCUMENTCOMPANYCODE,
       t.INTDOCPROVISIONALCOUNTERCODE,
       t.INTDOCUMENTPROVISIONALCODE,
       t.LINEGROUP,
       t.ORIGIN,
       t.CODE,
       t.COUNTERCODE,
       t.PROVENIENCECODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE
FROM   DB2ADMIN.WRKINTDOCUMENTGROUPCOMMENTS t
FETCH FIRST 100 ROWS ONLY;
```
