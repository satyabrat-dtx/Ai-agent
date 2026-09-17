# DB2ADMIN.SALESDOCUMENTLINECOMMENT

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `SALDOCLINESALDOCCOMPANYCODE`, `SALDOCLINESALDOCPRVCNTCODE`, `SALDOCLINESALDOCPRVCODE`, `SALESDOCUMENTLINEORDERLINE`, `SALESDOCUMENTLINEORDERSUBLINE`, `SALDOCLINECOMPONENTORDERLINE`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 8321

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALDOCLINESALDOCCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SALDOCLINESALDOCPRVCNTCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SALDOCLINESALDOCPRVCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SALESDOCUMENTLINEORDERLINE` | DECIMAL(7,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SALESDOCUMENTLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `SALDOCLINECOMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 7 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 8 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 9 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 10 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `SALESDOCUMENTLINE_COMMENT` | `SALDOCLINESALDOCCOMPANYCODE`, `SALDOCLINESALDOCPRVCNTCODE`, `SALDOCLINESALDOCPRVCODE`, `SALESDOCUMENTLINEORDERLINE`, `SALESDOCUMENTLINEORDERSUBLINE`, `SALDOCLINECOMPONENTORDERLINE` | [`SALESDOCUMENTLINE`](../SALES/SALESDOCUMENTLINE.md) | `SALESDOCUMENTCOMPANYCODE`, `SALDOCPROVISIONALCOUNTERCODE`, `SALESDOCUMENTPROVISIONALCODE`, `ORDERLINE`, `ORDERSUBLINE`, `COMPONENTORDERLINE` | RESTRICT | `SALESDOCUMENTLINECOMMENT.SALDOCLINESALDOCCOMPANYCODE = SALESDOCUMENTLINE.SALESDOCUMENTCOMPANYCODE AND SALESDOCUMENTLINECOMMENT.SALDOCLINESALDOCPRVCNTCODE = SALESDOCUMENTLINE.SALDOCPROVISIONALCOUNTERCODE AND SALESDOCUMENTLINECOMMENT.SALDOCLINESALDOCPRVCODE = SALESDOCUMENTLINE.SALESDOCUMENTPROVISIONALCODE AND SALESDOCUMENTLINECOMMENT.SALESDOCUMENTLINEORDERLINE = SALESDOCUMENTLINE.ORDERLINE AND SALESDOCUMENTLINECOMMENT.SALESDOCUMENTLINEORDERSUBLINE = SALESDOCUMENTLINE.ORDERSUBLINE AND SALESDOCUMENTLINECOMMENT.SALDOCLINECOMPONENTORDERLINE = SALESDOCUMENTLINE.COMPONENTORDERLINE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESDOCUMENTLINECOMMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SALDOCLINESALDOCCOMPANYCODE,
       t.SALDOCLINESALDOCPRVCNTCODE,
       t.SALDOCLINESALDOCPRVCODE,
       t.SALESDOCUMENTLINEORDERLINE,
       t.SALESDOCUMENTLINEORDERSUBLINE,
       t.SALDOCLINECOMPONENTORDERLINE,
       t.REPORTTYPE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED
FROM   DB2ADMIN.SALESDOCUMENTLINECOMMENT t
FETCH FIRST 100 ROWS ONLY;
```
