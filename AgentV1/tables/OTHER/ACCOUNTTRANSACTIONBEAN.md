# DB2ADMIN.ACCOUNTTRANSACTIONBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 71
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 86987

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
| 12 | `TRANSACTIONLINENUMBER` | INTEGER | NOT NULL |  |  |  |
| 13 | `DOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 14 | `DOCUMENTDATE` | DATE |  |  |  |  |
| 15 | `ORIGINDOCUMENTCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 16 | `ORIGINDOCUMENTNUMBER` | CHAR(50) |  |  |  |  |
| 17 | `REGISTERTAXCODE` | CHAR(3) |  |  |  |  |
| 18 | `TAXREFERENCECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 19 | `TAXDOCUMENTNUMBER` | CHAR(50) |  |  |  |  |
| 20 | `GENERATEDENTRYNUMBER` | DECIMAL(7,0) |  |  |  |  |
| 21 | `GENERATEDENTRYLINENUMBER` | DECIMAL(7,0) |  |  |  |  |
| 22 | `ACCOUNTTEMPLATECODE` | CHAR(6) |  |  |  |  |
| 23 | `ACCOUNTCODE` | CHAR(20) |  |  |  |  |
| 24 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 25 | `AGENTFIRSTCODE` | CHAR(3) |  |  |  |  |
| 26 | `AGENTSECONDCODE` | CHAR(3) |  |  |  |  |
| 27 | `AGENTTHIRDCODE` | CHAR(3) |  |  |  |  |
| 28 | `AGENTFOURTHCODE` | CHAR(3) |  |  |  |  |
| 29 | `AGENTFIFTHCODE` | CHAR(3) |  |  |  |  |
| 30 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 31 | `CONTROLDEBITCREDIT` | CHAR(1) |  |  |  |  |
| 32 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 33 | `PRIMARYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 34 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 35 | `PRIMARYCURRENCYAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 36 | `FOREIGNCURRENCYAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 37 | `PRIMARYCURRENCYTAXABLEAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 38 | `FOREIGNCURRENCYTAXABLEAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 39 | `PRIMARYCURRENCYTAXAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 40 | `FOREIGNCURRENCYTAXAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 41 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 42 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 43 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 44 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 45 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 46 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 47 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 48 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 49 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 50 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 51 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 52 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 53 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 54 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 55 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 56 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 57 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 58 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 59 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 60 | `FINANCIALPROJECTCODE` | CHAR(40) |  |  |  |  |
| 61 | `FIXEDASSETCODE` | CHAR(40) |  |  |  |  |
| 62 | `PROFITCENTERCODE` | CHAR(40) |  |  |  |  |
| 63 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 64 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 65 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 66 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 67 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 68 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 69 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 70 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `ACCOUNTTRANSACTIONBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `ACCOUNTTRANSACTIONBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

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
FROM   DB2ADMIN.ACCOUNTTRANSACTIONBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
