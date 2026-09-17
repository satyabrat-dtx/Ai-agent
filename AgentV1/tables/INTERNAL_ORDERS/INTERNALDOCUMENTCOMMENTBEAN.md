# DB2ADMIN.INTERNALDOCUMENTCOMMENTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `INTERNAL_ORDERS` (high confidence — table name starts with 'INTERNAL')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 33
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 66919

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 1 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 2 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 3 | `ORIGIN` | INTEGER | NOT NULL |  |  |  |
| 4 | `CODE` | CHAR(12) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 6 | `PROVENIENCECODE` | CHAR(15) |  |  |  |  |
| 7 | `COMMENTTEXT` | LONG VARCHAR |  |  |  |  |
| 8 | `COMMENTTYPE` | CHAR(2) |  |  |  |  |
| 9 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 11 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 12 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 13 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 14 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 15 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 16 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 17 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 18 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 19 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 20 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 21 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 27 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 28 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 29 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 30 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 31 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 32 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **INTERNALDOCUMENT**.`ABSUNIQUEID` (high confidence — name = 'INTERNALDOCUMENT' + known child suffix 'COMMENT')
  - JOIN predicate: `INTERNALDOCUMENTCOMMENTBEAN.FATHERID = INTERNALDOCUMENT.ABSUNIQUEID`

## Indexes

- `INTDOCUMENTCOMMENTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.REPORTTYPE,
       t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.ORIGIN,
       t.CODE,
       t.COUNTERCODE,
       t.PROVENIENCECODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED,
       t.WSOPERATION,
       t.IMPORTSTATUS
FROM   DB2ADMIN.INTERNALDOCUMENTCOMMENTBEAN t
FETCH FIRST 100 ROWS ONLY;
```
