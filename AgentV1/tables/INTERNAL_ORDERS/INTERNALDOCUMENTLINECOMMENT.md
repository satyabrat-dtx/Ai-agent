# DB2ADMIN.INTERNALDOCUMENTLINECOMMENT

- **Module**: `INTERNAL_ORDERS` (high confidence — table name starts with 'INTERNAL')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `INTDOCLINEINTDOCCOMPANYCODE`, `INTDOCLINEINTDOCPRVCNTCODE`, `INTDOCLINEINTDOCPRVCODE`, `INTERNALDOCUMENTLINEORDERLINE`, `INTDOCUMENTLINEORDERSUBLINE`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 5364

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INTDOCLINEINTDOCCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `INTDOCLINEINTDOCPRVCNTCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `INTDOCLINEINTDOCPRVCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `INTERNALDOCUMENTLINEORDERLINE` | DECIMAL(7,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `INTDOCUMENTLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 6 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 8 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 9 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `INTERNALDOCUMENTLINE_COMMENT` | `INTDOCLINEINTDOCCOMPANYCODE`, `INTDOCLINEINTDOCPRVCNTCODE`, `INTDOCLINEINTDOCPRVCODE`, `INTERNALDOCUMENTLINEORDERLINE`, `INTDOCUMENTLINEORDERSUBLINE` | [`INTERNALDOCUMENTLINE`](../INTERNAL_ORDERS/INTERNALDOCUMENTLINE.md) | `INTERNALDOCUMENTCOMPANYCODE`, `INTDOCPROVISIONALCOUNTERCODE`, `INTDOCUMENTPROVISIONALCODE`, `ORDERLINE`, `ORDERSUBLINE` | RESTRICT | `INTERNALDOCUMENTLINECOMMENT.INTDOCLINEINTDOCCOMPANYCODE = INTERNALDOCUMENTLINE.INTERNALDOCUMENTCOMPANYCODE AND INTERNALDOCUMENTLINECOMMENT.INTDOCLINEINTDOCPRVCNTCODE = INTERNALDOCUMENTLINE.INTDOCPROVISIONALCOUNTERCODE AND INTERNALDOCUMENTLINECOMMENT.INTDOCLINEINTDOCPRVCODE = INTERNALDOCUMENTLINE.INTDOCUMENTPROVISIONALCODE AND INTERNALDOCUMENTLINECOMMENT.INTERNALDOCUMENTLINEORDERLINE = INTERNALDOCUMENTLINE.ORDERLINE AND INTERNALDOCUMENTLINECOMMENT.INTDOCUMENTLINEORDERSUBLINE = INTERNALDOCUMENTLINE.ORDERSUBLINE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INTDOCUMENTLINECOMMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.INTDOCLINEINTDOCCOMPANYCODE,
       t.INTDOCLINEINTDOCPRVCNTCODE,
       t.INTDOCLINEINTDOCPRVCODE,
       t.INTERNALDOCUMENTLINEORDERLINE,
       t.INTDOCUMENTLINEORDERSUBLINE,
       t.REPORTTYPE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED,
       t.ABSUNIQUEID
FROM   DB2ADMIN.INTERNALDOCUMENTLINECOMMENT t
FETCH FIRST 100 ROWS ONLY;
```
