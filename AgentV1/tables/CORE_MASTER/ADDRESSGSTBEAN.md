# DB2ADMIN.ADDRESSGSTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `CORE_MASTER` (high confidence — table name starts with 'ADDRESS')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 30
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 182152

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 3 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 4 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 5 | `UNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 6 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 7 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 8 | `GSTINNUMBER` | CHAR(15) |  |  |  |  |
| 9 | `GSTDATE` | DATE |  |  |  |  |
| 10 | `STATECODE` | CHAR(3) |  |  |  |  |
| 11 | `PROVISIONALGSTINNUMBER` | CHAR(15) |  |  |  |  |
| 12 | `PROVISIONALGSTDATE` | DATE |  |  |  |  |
| 13 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 14 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 15 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 16 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 17 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 18 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 19 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 20 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 22 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 23 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 24 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 25 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 26 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 27 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 28 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 29 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `ADDRESSGSTBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `ADDRESSGSTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.UNIQUEID,
       t.LASTUPDATEUSER,
       t.USECREATIONUSER,
       t.GSTINNUMBER,
       t.GSTDATE,
       t.STATECODE,
       t.PROVISIONALGSTINNUMBER
FROM   DB2ADMIN.ADDRESSGSTBEAN t
FETCH FIRST 100 ROWS ONLY;
```
