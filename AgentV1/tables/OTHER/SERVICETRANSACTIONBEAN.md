# DB2ADMIN.SERVICETRANSACTIONBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 89
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 120783

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `TRANSACTIONDATE` | DATE |  |  |  |  |
| 5 | `TRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 6 | `TRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 7 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 8 | `EXTERNALOPERATIONMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 9 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 10 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 11 | `SUPPLIERDOCUMENTDATE` | DATE |  |  |  |  |
| 12 | `SUPPLIERDOCUMENTNUMBER` | CHAR(50) |  |  |  |  |
| 13 | `ORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 14 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 15 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 16 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 17 | `ORDERDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 18 | `PRODPROGRESSPROGRESSNUMBER` | CHAR(15) |  |  |  |  |
| 19 | `INTERNALDOCUMENTDATE` | DATE |  |  |  |  |
| 20 | `INTERNALDOCUMENTNUMBER` | INTEGER | NOT NULL |  |  |  |
| 21 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 22 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 23 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 24 | `TRANSACTIONTYPE` | CHAR(2) |  |  |  |  |
| 25 | `STATUS` | CHAR(2) |  |  |  |  |
| 26 | `REVOKETRANSACTION` | SMALLINT | NOT NULL |  |  |  |
| 27 | `PRODUCTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 28 | `PRODUCTSUBCODE01` | CHAR(20) |  |  |  |  |
| 29 | `PRODUCTSUBCODE02` | CHAR(10) |  |  |  |  |
| 30 | `PRODUCTSUBCODE03` | CHAR(10) |  |  |  |  |
| 31 | `PRODUCTSUBCODE04` | CHAR(10) |  |  |  |  |
| 32 | `PRODUCTSUBCODE05` | CHAR(10) |  |  |  |  |
| 33 | `PRODUCTSUBCODE06` | CHAR(10) |  |  |  |  |
| 34 | `PRODUCTSUBCODE07` | CHAR(10) |  |  |  |  |
| 35 | `PRODUCTSUBCODE08` | CHAR(10) |  |  |  |  |
| 36 | `PRODUCTSUBCODE09` | CHAR(10) |  |  |  |  |
| 37 | `PRODUCTSUBCODE10` | CHAR(10) |  |  |  |  |
| 38 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 39 | `COSTELEMENTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 40 | `COSTELEMENTSUBCODE01` | CHAR(20) |  |  |  |  |
| 41 | `DEMANDSTEPPRODEMANDCNTCODE` | CHAR(8) |  |  |  |  |
| 42 | `DEMANDSTEPPRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 43 | `DEMANDSTEPSTEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 44 | `SERVICEITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 45 | `SERVICESUBCODE01` | CHAR(20) |  |  |  |  |
| 46 | `SERVICEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 47 | `ELEMENTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 48 | `ELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 49 | `ELEMENTCODE` | CHAR(15) |  |  |  |  |
| 50 | `PERCENTAGEFORQUANTITYORVALUE` | DECIMAL(5,2) |  |  |  |  |
| 51 | `TRANSACTIONUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 52 | `TRANSACTIONQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 53 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 54 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 55 | `GROUPSTEPNUMBER` | INTEGER | NOT NULL |  |  |  |
| 56 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 57 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 58 | `BASECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 59 | `VALUEINBASECURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 60 | `PROVISIONALVALUE` | DECIMAL(18,5) |  |  |  |  |
| 61 | `POSTEDTRANSACTION` | SMALLINT | NOT NULL |  |  |  |
| 62 | `INVOICECODE` | CHAR(50) |  |  |  |  |
| 63 | `INVOICEDATE` | DATE |  |  |  |  |
| 64 | `ACCOUNTTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 65 | `DAILYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 66 | `CLOSINGVALUE` | DECIMAL(18,5) |  |  |  |  |
| 67 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 68 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 69 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 70 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 71 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 72 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 73 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 74 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 75 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 76 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 77 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 78 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 79 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 80 | `SKIPCONTROL` | CHAR(3) |  |  |  |  |
| 81 | `SKIPSUPWHSTRANSACTION` | SMALLINT | NOT NULL |  |  |  |
| 82 | `ORGSERVTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 83 | `ORGSERVTRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 84 | `PREVIOUSCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 85 | `PREVIOUSPROVISIONALVALUE` | DECIMAL(18,5) |  |  |  |  |
| 86 | `PREVIOUSDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 87 | `SERVTRENTRYTRLINK` | DECIMAL(11,0) |  |  |  |  |
| 88 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SERVICETRANSACTIONBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.TRANSACTIONDATE,
       t.TRANSACTIONNUMBER,
       t.TRANSACTIONDETAILNUMBER,
       t.TEMPLATECODE,
       t.EXTERNALOPERATIONMANAGEMENT,
       t.SUPPLIERTYPE,
       t.SUPPLIERCODE,
       t.SUPPLIERDOCUMENTDATE
FROM   DB2ADMIN.SERVICETRANSACTIONBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
