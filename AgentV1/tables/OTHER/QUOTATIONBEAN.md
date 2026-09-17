# DB2ADMIN.QUOTATIONBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 54
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 110340

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `RFQHEADERRFQHEADERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 3 | `RFQHEADERRFQHEADERCODE` | CHAR(15) |  |  |  |  |
| 4 | `RFQHEADERLINENO` | INTEGER | NOT NULL |  |  |  |
| 5 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 6 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 7 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 8 | `UOMDESCRIPTION` | CHAR(100) |  |  |  |  |
| 9 | `DELIVERYTERMDESC` | CHAR(100) |  |  |  |  |
| 10 | `PAYMENTMETHODDESC` | CHAR(100) |  |  |  |  |
| 11 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 12 | `SHIPMENTTERMDESC` | CHAR(100) |  |  |  |  |
| 13 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 14 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 15 | `PRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 16 | `DELIVERYDATE` | DATE |  |  |  |  |
| 17 | `NEWEXISTING` | CHAR(5) |  |  |  |  |
| 18 | `QUOTATIONNO` | CHAR(15) |  |  |  |  |
| 19 | `QUOTATIONDATE` | DATE |  |  |  |  |
| 20 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 21 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 22 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 24 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 26 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 27 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 28 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 29 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 30 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 31 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 32 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 33 | `VALIDDAYS` | INTEGER | NOT NULL |  |  |  |
| 34 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 35 | `ATTACHMENT` | BLOB(1000000000) |  |  |  |  |
| 36 | `ATTACHMENTNAME` | CHAR(20) |  |  |  |  |
| 37 | `QUOTELOCK` | SMALLINT | NOT NULL |  |  |  |
| 38 | `RFQCLOSED` | INTEGER | NOT NULL |  |  |  |
| 39 | `ATTACHMENTPATH` | CHAR(30) |  |  |  |  |
| 40 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 41 | `ADQUOTEEXPORT` | BLOB(1000000) |  |  |  |  |
| 42 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 43 | `ALREADYUSED` | SMALLINT | NOT NULL |  |  |  |
| 44 | `PRICEUOMDESCRIPTION` | CHAR(100) |  |  |  |  |
| 45 | `SECONDARYUOMDESCRIPTION` | CHAR(100) |  |  |  |  |
| 46 | `PACKAGINGUOMDESCRIPTION` | CHAR(100) |  |  |  |  |
| 47 | `SECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 48 | `PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `SECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 50 | `PACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 51 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 52 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 53 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `QUOTATIONBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.RFQHEADERRFQHEADERCOUNTERCODE,
       t.RFQHEADERRFQHEADERCODE,
       t.RFQHEADERLINENO,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.ITEMDESCRIPTION,
       t.UOMDESCRIPTION,
       t.DELIVERYTERMDESC,
       t.PAYMENTMETHODDESC,
       t.QUANTITY
FROM   DB2ADMIN.QUOTATIONBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
