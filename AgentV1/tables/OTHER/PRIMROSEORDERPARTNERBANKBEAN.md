# DB2ADMIN.PRIMROSEORDERPARTNERBANKBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 40
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 43495

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `IDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 3 | `FOBABCAB` | CHAR(1) | NOT NULL |  |  |  |
| 4 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 5 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 6 | `EXTERNALBANKCODE` | CHAR(15) |  |  |  |  |
| 7 | `CINCODE` | CHAR(2) |  |  |  |  |
| 8 | `CURRENTACCOUNTID` | CHAR(30) |  |  |  |  |
| 9 | `BBAN` | CHAR(30) |  |  |  |  |
| 10 | `BIC` | CHAR(11) |  |  |  |  |
| 11 | `IBAN` | CHAR(34) |  |  |  |  |
| 12 | `PRIORITY` | DECIMAL(3,0) |  |  |  |  |
| 13 | `T40CD` | CHAR(5) |  |  |  |  |
| 14 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 15 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 16 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 17 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 18 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 19 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 20 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 22 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 23 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 24 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 25 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 26 | `ACCOUNTOWNER` | CHAR(100) |  |  |  |  |
| 27 | `DIRECTDEBIT` | SMALLINT | NOT NULL |  |  |  |
| 28 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 29 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 30 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 31 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 32 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 33 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 34 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 35 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 36 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 37 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 38 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 39 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `PRIMROSEORDERPARTNERBANKBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `PRIMROSEORDPRNBANKBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.IDENTIFIER,
       t.FOBABCAB,
       t.BANKCODE,
       t.BANKBRANCHCODE,
       t.EXTERNALBANKCODE,
       t.CINCODE,
       t.CURRENTACCOUNTID,
       t.BBAN,
       t.BIC,
       t.IBAN
FROM   DB2ADMIN.PRIMROSEORDERPARTNERBANKBEAN t
FETCH FIRST 100 ROWS ONLY;
```
