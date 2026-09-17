# DB2ADMIN.SALPRICEDEFINITIONDETAILBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 37
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 81311

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `QUALITYLEVELITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 4 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 5 | `BREAKDOWNLIMIT` | DECIMAL(18,5) |  |  |  |  |
| 6 | `SOURCEPRICETYPE` | CHAR(2) |  |  |  |  |
| 7 | `NUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 8 | `COMPOUNDPRICETYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 10 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 11 | `PRICEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 12 | `PRICESIGN` | CHAR(2) |  |  |  |  |
| 13 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 14 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 20 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 21 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 22 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 23 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 24 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 25 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 26 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 27 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 28 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 29 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 30 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 31 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 32 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 33 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 34 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 35 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 36 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `SALPRICEDEFINITIONDETAILBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `SALPRCDEFDETAILBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.QUALITYLEVELITEMTYPECODE,
       t.QUALITYLEVELCODE,
       t.UNITOFMEASURECODE,
       t.BREAKDOWNLIMIT,
       t.SOURCEPRICETYPE,
       t.NUMBERLINEID,
       t.COMPOUNDPRICETYPECODE,
       t.PRICETYPE,
       t.PRICE,
       t.PRICEPERCENTAGE
FROM   DB2ADMIN.SALPRICEDEFINITIONDETAILBEAN t
FETCH FIRST 100 ROWS ONLY;
```
