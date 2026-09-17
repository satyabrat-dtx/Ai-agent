# DB2ADMIN.EXTOPDOCUMENTCOMMENT

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOP')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `EXTOPDOCLINEEXTOPDOCCMYCODE`, `EXTOPDOCLINEEXTOPDOCPROVCNTCOD`, `EXTOPDOCLINEEXTOPDOCPRVCODE`, `EXTOPDOCUMENTLINEORDERLINE`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 30026

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EXTOPDOCLINEEXTOPDOCCMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EXTOPDOCLINEEXTOPDOCPROVCNTCOD` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EXTOPDOCLINEEXTOPDOCPRVCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `EXTOPDOCUMENTLINEORDERLINE` | DECIMAL(7,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 5 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 7 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 8 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 12 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 13 | `LOGREASONCODE` | CHAR(2) |  | FK | foreign_key |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EXTOPDOCUMENTLINE_COMMENT` | `EXTOPDOCLINEEXTOPDOCCMYCODE`, `EXTOPDOCLINEEXTOPDOCPROVCNTCOD`, `EXTOPDOCLINEEXTOPDOCPRVCODE`, `EXTOPDOCUMENTLINEORDERLINE` | [`EXTOPDOCUMENTLINE`](../SUBCONTRACTING/EXTOPDOCUMENTLINE.md) | `EXTOPDOCUMENTCOMPANYCODE`, `EXTOPDOCUMENTPROVCOUNTERCODE`, `EXTOPDOCUMENTPROVISIONALCODE`, `ORDERLINE` | RESTRICT | `EXTOPDOCUMENTCOMMENT.EXTOPDOCLINEEXTOPDOCCMYCODE = EXTOPDOCUMENTLINE.EXTOPDOCUMENTCOMPANYCODE AND EXTOPDOCUMENTCOMMENT.EXTOPDOCLINEEXTOPDOCPROVCNTCOD = EXTOPDOCUMENTLINE.EXTOPDOCUMENTPROVCOUNTERCODE AND EXTOPDOCUMENTCOMMENT.EXTOPDOCLINEEXTOPDOCPRVCODE = EXTOPDOCUMENTLINE.EXTOPDOCUMENTPROVISIONALCODE AND EXTOPDOCUMENTCOMMENT.EXTOPDOCUMENTLINEORDERLINE = EXTOPDOCUMENTLINE.ORDERLINE` |
| `LOGREASON_LOGREASON` | `EXTOPDOCLINEEXTOPDOCCMYCODE`, `LOGREASONCODE` | [`LOGREASON`](../LOGISTICS/LOGREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EXTOPDOCUMENTCOMMENT.EXTOPDOCLINEEXTOPDOCCMYCODE = LOGREASON.COMPANYCODE AND EXTOPDOCUMENTCOMMENT.LOGREASONCODE = LOGREASON.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EXTOPDOCUMENTCOMMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EXTOPDOCLINEEXTOPDOCCMYCODE,
       t.EXTOPDOCLINEEXTOPDOCPROVCNTCOD,
       t.EXTOPDOCLINEEXTOPDOCPRVCODE,
       t.EXTOPDOCUMENTLINEORDERLINE,
       t.REPORTTYPE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED,
       t.ABSUNIQUEID,
       t.TERMSOFLOGORDERTYPE
FROM   DB2ADMIN.EXTOPDOCUMENTCOMMENT t
FETCH FIRST 100 ROWS ONLY;
```
