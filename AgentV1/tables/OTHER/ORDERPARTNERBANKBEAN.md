# DB2ADMIN.ORDERPARTNERBANKBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 39
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 43276

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `IDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 3 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 4 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 5 | `EXTERNALBANKCODE` | CHAR(15) |  |  |  |  |
| 6 | `CINCODE` | CHAR(2) |  |  |  |  |
| 7 | `CURRENTACCOUNTID` | CHAR(30) |  |  |  |  |
| 8 | `BBAN` | CHAR(30) |  |  |  |  |
| 9 | `BIC` | CHAR(11) |  |  |  |  |
| 10 | `IBAN` | CHAR(34) |  |  |  |  |
| 11 | `PRIORITY` | DECIMAL(3,0) |  |  |  |  |
| 12 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 13 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 14 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 15 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 16 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 17 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 18 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 19 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 20 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 21 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 22 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 23 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 24 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 25 | `ACCOUNTOWNER` | CHAR(100) |  |  |  |  |
| 26 | `DIRECTDEBIT` | SMALLINT | NOT NULL |  |  |  |
| 27 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 28 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 29 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 30 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 31 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 32 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 33 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 34 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 35 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 36 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 37 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 38 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **ORDERPARTNER**.`ABSUNIQUEID` (medium confidence — name = 'ORDERPARTNER' + recurring fragment 'BANK' (seen in 5 tables))
  - JOIN predicate: `ORDERPARTNERBANKBEAN.FATHERID = ORDERPARTNER.ABSUNIQUEID`

## Indexes

- `ORDERPARTNERBANKBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.IDENTIFIER,
       t.BANKCODE,
       t.BANKBRANCHCODE,
       t.EXTERNALBANKCODE,
       t.CINCODE,
       t.CURRENTACCOUNTID,
       t.BBAN,
       t.BIC,
       t.IBAN,
       t.PRIORITY
FROM   DB2ADMIN.ORDERPARTNERBANKBEAN t
FETCH FIRST 100 ROWS ONLY;
```
