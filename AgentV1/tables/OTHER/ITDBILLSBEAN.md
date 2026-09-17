# DB2ADMIN.ITDBILLSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 29
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 173174

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `SERIALNO` | BIGINT | NOT NULL |  |  |  |
| 3 | `REFERENCENO` | CHAR(15) |  |  |  |  |
| 4 | `AMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 5 | `AUTHORIZEDFLAG` | INTEGER | NOT NULL |  |  |  |
| 6 | `SUMMARY` | CHAR(50) |  |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 14 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 17 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 18 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 19 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 20 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 21 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 22 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 23 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 24 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 25 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 26 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 27 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 28 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `ITDBILLSBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `ITDBILLSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.SERIALNO,
       t.REFERENCENO,
       t.AMOUNT,
       t.AUTHORIZEDFLAG,
       t.SUMMARY,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.USECREATIONUSER
FROM   DB2ADMIN.ITDBILLSBEAN t
FETCH FIRST 100 ROWS ONLY;
```
