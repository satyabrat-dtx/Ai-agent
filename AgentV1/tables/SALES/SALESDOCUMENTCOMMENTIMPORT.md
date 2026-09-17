# DB2ADMIN.SALESDOCUMENTCOMMENTIMPORT

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `SALESDOCUMENTIMPORTCOMPANYCODE`, `SALDOCIMPIMPPROVISIONALCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 13509

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESDOCUMENTIMPORTCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `SALDOCIMPIMPPROVISIONALCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `IMPORTOPERATION` | INTEGER | NOT NULL |  |  |  |
| 3 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 4 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `COMMENTTEXT` | LONG VARCHAR |  |  |  |  |
| 6 | `COMMENTTYPE` | CHAR(2) |  |  |  |  |
| 7 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SALESDOCUMENTCOMMENTIMPORT_COMMENTIMPORT` | [`MILSALORDIMPERR`](../SALES/MILSALORDIMPERR.md) | `HEADERIMPORTCC`, `HEADERIMPORTIC`, `COMMENTIMPORTCODE` | `MILSALORDIMPERR.HEADERIMPORTCC = SALESDOCUMENTCOMMENTIMPORT.SALESDOCUMENTIMPORTCOMPANYCODE AND MILSALORDIMPERR.HEADERIMPORTIC = SALESDOCUMENTCOMMENTIMPORT.SALDOCIMPIMPPROVISIONALCODE AND MILSALORDIMPERR.COMMENTIMPORTCODE = SALESDOCUMENTCOMMENTIMPORT.CODE` |

## Indexes

- `SALESDOCUMENTCOMMENTIMPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SALESDOCUMENTIMPORTCOMPANYCODE,
       t.SALDOCIMPIMPPROVISIONALCODE,
       t.IMPORTOPERATION,
       t.REPORTTYPE,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.SALESDOCUMENTCOMMENTIMPORT t
FETCH FIRST 100 ROWS ONLY;
```
