# DB2ADMIN.ORDERPARTNERTDSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 38
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 182278

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `CSMSUPCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 4 | `CSMSUPCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 5 | `TDSTEUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 6 | `TDSTYPECODE` | CHAR(10) |  |  |  |  |
| 7 | `TDSCODE` | CHAR(6) |  |  |  |  |
| 8 | `TDSITAXCODE` | CHAR(3) |  |  |  |  |
| 9 | `EXEMPTIONNUMBER` | CHAR(15) |  |  |  |  |
| 10 | `EXEMPTIONTAXPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 11 | `EXEMPTIONMAXAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 12 | `EXEMPTIONFROMDATE` | DATE |  |  |  |  |
| 13 | `EXEMPTIONTODATE` | DATE |  |  |  |  |
| 14 | `DEFAULTLINE` | SMALLINT | NOT NULL |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 22 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 24 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 25 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 26 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 27 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 28 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 29 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 30 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 31 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 32 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 33 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 34 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 35 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 36 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 37 | `TILLDATEAMTCR` | DECIMAL(15,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `ORDERPARTNERTDSBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `ORDERPARTNERTDSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.CSMSUPCUSTOMERSUPPLIERTYPE,
       t.CSMSUPCUSTOMERSUPPLIERCODE,
       t.TDSTEUSERGENERICGROUPTYPECODE,
       t.TDSTYPECODE,
       t.TDSCODE,
       t.TDSITAXCODE,
       t.EXEMPTIONNUMBER,
       t.EXEMPTIONTAXPERCENTAGE,
       t.EXEMPTIONMAXAMOUNT
FROM   DB2ADMIN.ORDERPARTNERTDSBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
