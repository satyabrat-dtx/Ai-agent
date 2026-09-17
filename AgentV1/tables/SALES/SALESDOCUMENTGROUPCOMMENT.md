# DB2ADMIN.SALESDOCUMENTGROUPCOMMENT

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `SALESDOCUMENTCOMPANYCODE`, `SALDOCPROVISIONALCOUNTERCODE`, `SALESDOCUMENTPROVISIONALCODE`, `LINEGROUP`, `ORIGIN`, `CODE`, `COUNTERCODE`, `PROVENIENCECODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 3403

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESDOCUMENTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SALDOCPROVISIONALCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SALESDOCUMENTPROVISIONALCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 4 | `LINEGROUP` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 7 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 8 | `PROVENIENCECODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 9 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 10 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `SALESDOCUMENT_GROUPCOMMENT` | `SALESDOCUMENTCOMPANYCODE`, `SALDOCPROVISIONALCOUNTERCODE`, `SALESDOCUMENTPROVISIONALCODE` | [`SALESDOCUMENT`](../SALES/SALESDOCUMENT.md) | `COMPANYCODE`, `PROVISIONALCOUNTERCODE`, `PROVISIONALCODE` | RESTRICT | `SALESDOCUMENTGROUPCOMMENT.SALESDOCUMENTCOMPANYCODE = SALESDOCUMENT.COMPANYCODE AND SALESDOCUMENTGROUPCOMMENT.SALDOCPROVISIONALCOUNTERCODE = SALESDOCUMENT.PROVISIONALCOUNTERCODE AND SALESDOCUMENTGROUPCOMMENT.SALESDOCUMENTPROVISIONALCODE = SALESDOCUMENT.PROVISIONALCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESDOCUMENTGROUPCOMMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SALESDOCUMENTCOMPANYCODE,
       t.SALDOCPROVISIONALCOUNTERCODE,
       t.SALESDOCUMENTPROVISIONALCODE,
       t.REPORTTYPE,
       t.LINEGROUP,
       t.ORIGIN,
       t.CODE,
       t.COUNTERCODE,
       t.PROVENIENCECODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED
FROM   DB2ADMIN.SALESDOCUMENTGROUPCOMMENT t
FETCH FIRST 100 ROWS ONLY;
```
