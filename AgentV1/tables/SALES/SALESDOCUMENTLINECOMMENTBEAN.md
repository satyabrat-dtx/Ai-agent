# DB2ADMIN.SALESDOCUMENTLINECOMMENTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 32
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 96343

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 1 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 2 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 3 | `ORIGIN` | INTEGER | NOT NULL |  |  |  |
| 4 | `CODE` | CHAR(12) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `COMMENTTEXT` | LONG VARCHAR |  |  |  |  |
| 6 | `COMMENTTYPE` | CHAR(2) |  |  |  |  |
| 7 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `SALESDOCUMENTLINEBEAN` | BLOB(1000000) |  |  |  |  |
| 9 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 10 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 11 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 12 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 13 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 14 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 15 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 16 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 17 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 18 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 19 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 20 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 21 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 22 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 23 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 24 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 25 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 26 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 27 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 28 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 29 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 30 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 31 | `ENTITYNAME` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **SALESDOCUMENTLINE**.`ABSUNIQUEID` (high confidence — name = 'SALESDOCUMENTLINE' + known child suffix 'COMMENT')
  - JOIN predicate: `SALESDOCUMENTLINECOMMENTBEAN.FATHERID = SALESDOCUMENTLINE.ABSUNIQUEID`

## Indexes

- `SALDOCLINECOMMENTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.REPORTTYPE,
       t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED,
       t.SALESDOCUMENTLINEBEAN,
       t.WSOPERATION,
       t.IMPORTSTATUS,
       t.IMPCREATIONDATETIME
FROM   DB2ADMIN.SALESDOCUMENTLINECOMMENTBEAN t
FETCH FIRST 100 ROWS ONLY;
```
