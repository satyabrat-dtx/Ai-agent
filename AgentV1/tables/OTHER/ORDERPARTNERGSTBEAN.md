# DB2ADMIN.ORDERPARTNERGSTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 32
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 182214

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 3 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 4 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 5 | `CUSTOMERSUPPLIERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 7 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 8 | `CUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 9 | `CUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 10 | `GSTREGISTRATIONTYPE` | CHAR(1) |  |  |  |  |
| 11 | `ECOMMERCEOPERATOR` | SMALLINT | NOT NULL |  |  |  |
| 12 | `LATESTCOMPLIANCERATING` | CHAR(3) |  |  |  |  |
| 13 | `LATESTCOMPLIANCERATINGDATE` | DATE |  |  |  |  |
| 14 | `RCMAPPLICABLE` | CHAR(2) |  |  |  |  |
| 15 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 16 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 17 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 18 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 19 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 20 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 22 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 24 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 25 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 26 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 27 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 28 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 29 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 30 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 31 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `ORDERPARTNERGSTBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `ORDERPARTNERGSTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.CUSTOMERSUPPLIERCOMPANYCODE,
       t.LASTUPDATEUSER,
       t.USECREATIONUSER,
       t.CUSTOMERSUPPLIERTYPE,
       t.CUSTOMERSUPPLIERCODE,
       t.GSTREGISTRATIONTYPE,
       t.ECOMMERCEOPERATOR
FROM   DB2ADMIN.ORDERPARTNERGSTBEAN t
FETCH FIRST 100 ROWS ONLY;
```
