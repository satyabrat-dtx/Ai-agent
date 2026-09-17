# DB2ADMIN.ACCOUNTTRANSACTIONHEADERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 75
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 87090

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `STATUS` | CHAR(2) |  |  |  |  |
| 2 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 3 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 4 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 5 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 6 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 7 | `LINETYPE` | CHAR(1) |  |  |  |  |
| 8 | `TRANSACTIONORIGIN` | CHAR(15) |  |  |  |  |
| 9 | `ENTRYDATE` | DATE |  |  |  |  |
| 10 | `TRANSACTIONDATE` | DATE |  |  |  |  |
| 11 | `TRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 12 | `DOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 13 | `DOCUMENTDATE` | DATE |  |  |  |  |
| 14 | `ORIGINDOCUMENTCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 15 | `ORIGINDOCUMENTNUMBER` | CHAR(50) |  |  |  |  |
| 16 | `REGISTERTAXCODE` | CHAR(3) |  |  |  |  |
| 17 | `TAXREFERENCECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 18 | `TAXDOCUMENTNUMBER` | CHAR(50) |  |  |  |  |
| 19 | `GENERATEDENTRYNUMBER` | DECIMAL(7,0) |  |  |  |  |
| 20 | `GENERATEDENTRYLINENUMBER` | DECIMAL(7,0) |  |  |  |  |
| 21 | `ACCOUNTTEMPLATECODE` | CHAR(6) |  |  |  |  |
| 22 | `ACCOUNTCODE` | CHAR(20) |  |  |  |  |
| 23 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 24 | `AGENTFIRSTCODE` | CHAR(3) |  |  |  |  |
| 25 | `AGENTSECONDCODE` | CHAR(3) |  |  |  |  |
| 26 | `AGENTTHIRDCODE` | CHAR(3) |  |  |  |  |
| 27 | `AGENTFOURTHCODE` | CHAR(3) |  |  |  |  |
| 28 | `AGENTFIFTHCODE` | CHAR(3) |  |  |  |  |
| 29 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 30 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 31 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 32 | `EXTERNALBANKCODE` | CHAR(15) |  |  |  |  |
| 33 | `COMPANYBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 34 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 35 | `CONTROLDEBITCREDIT` | CHAR(1) |  |  |  |  |
| 36 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 37 | `PRIMARYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 38 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 39 | `PRIMARYCURRENCYAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 40 | `FOREIGNCURRENCYAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 41 | `PRIMARYCURRENCYTAXABLEAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 42 | `FOREIGNCURRENCYTAXABLEAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 43 | `PRIMARYCURRENCYTAXAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 44 | `FOREIGNCURRENCYTAXAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 45 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 46 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 47 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 48 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 49 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 50 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 51 | `HIERARCHICQUERY` | SMALLINT | NOT NULL |  |  |  |
| 52 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 53 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 54 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 55 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 56 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 57 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 58 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 59 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 60 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 61 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 62 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 63 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 64 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 65 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 66 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 67 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 68 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 69 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 70 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 71 | `ADVANCEINVOICEISSUED` | SMALLINT | NOT NULL |  |  |  |
| 72 | `PURADVANCEINVOICEREFERENCE` | CHAR(20) |  |  |  |  |
| 73 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 74 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **ACCOUNTTRANSACTION**.`ABSUNIQUEID` (medium confidence — name = 'ACCOUNTTRANSACTION' + recurring fragment 'HEADER' (seen in 72 tables))
  - JOIN predicate: `ACCOUNTTRANSACTIONHEADERBEAN.FATHERID = ACCOUNTTRANSACTION.ABSUNIQUEID`

## Indexes

- `ACCTRANSACTIONHEADERBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.STATUS,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.ORDERTYPE,
       t.LINETYPE,
       t.TRANSACTIONORIGIN,
       t.ENTRYDATE,
       t.TRANSACTIONDATE,
       t.TRANSACTIONNUMBER
FROM   DB2ADMIN.ACCOUNTTRANSACTIONHEADERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
