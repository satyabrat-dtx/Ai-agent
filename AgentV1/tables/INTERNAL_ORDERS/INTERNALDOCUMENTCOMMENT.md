# DB2ADMIN.INTERNALDOCUMENTCOMMENT

- **Module**: `INTERNAL_ORDERS` (high confidence — table name starts with 'INTERNAL')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `INTERNALDOCUMENTCOMPANYCODE`, `INTDOCPROVISIONALCOUNTERCODE`, `INTDOCUMENTPROVISIONALCODE`, `ORIGIN`, `CODE`, `COUNTERCODE`, `PROVENIENCECODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 24088

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INTERNALDOCUMENTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `INTDOCPROVISIONALCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `INTDOCUMENTPROVISIONALCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 4 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 7 | `PROVENIENCECODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 8 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 9 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
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
| `INTERNALDOCUMENT_COMMENT` | `INTERNALDOCUMENTCOMPANYCODE`, `INTDOCPROVISIONALCOUNTERCODE`, `INTDOCUMENTPROVISIONALCODE` | [`INTERNALDOCUMENT`](../INTERNAL_ORDERS/INTERNALDOCUMENT.md) | `COMPANYCODE`, `PROVISIONALCOUNTERCODE`, `PROVISIONALCODE` | RESTRICT | `INTERNALDOCUMENTCOMMENT.INTERNALDOCUMENTCOMPANYCODE = INTERNALDOCUMENT.COMPANYCODE AND INTERNALDOCUMENTCOMMENT.INTDOCPROVISIONALCOUNTERCODE = INTERNALDOCUMENT.PROVISIONALCOUNTERCODE AND INTERNALDOCUMENTCOMMENT.INTDOCUMENTPROVISIONALCODE = INTERNALDOCUMENT.PROVISIONALCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INTERNALDOCUMENTCOMMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.INTERNALDOCUMENTCOMPANYCODE,
       t.INTDOCPROVISIONALCOUNTERCODE,
       t.INTDOCUMENTPROVISIONALCODE,
       t.REPORTTYPE,
       t.ORIGIN,
       t.CODE,
       t.COUNTERCODE,
       t.PROVENIENCECODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED,
       t.COUNTERCOMPANYCODE
FROM   DB2ADMIN.INTERNALDOCUMENTCOMMENT t
FETCH FIRST 100 ROWS ONLY;
```
