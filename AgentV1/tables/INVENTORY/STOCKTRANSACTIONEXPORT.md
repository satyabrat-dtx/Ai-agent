# DB2ADMIN.STOCKTRANSACTIONEXPORT

- **Module**: `INVENTORY` (high confidence — table name starts with 'STOCK')
- **Roles**: `business_data`
- **Columns**: 103
- **Primary key**: `COMPANYCODE`, `TRANSACTIONNUMBER`, `TRANSACTIONDETAILNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 41796

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 1 | `EXPORTSTATUS` | INTEGER | NOT NULL |  |  |  |
| 2 | `TRANSACTIONSTATUS` | CHAR(2) |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `TRANSACTIONDATE` | DATE |  |  |  |  |
| 5 | `TRANSACTIONNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 6 | `TRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `DETAILTYPE` | CHAR(2) |  |  |  |  |
| 8 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 9 | `STOCKTRANSACTIONTYPE` | CHAR(2) |  |  |  |  |
| 10 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 11 | `DECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 12 | `DECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 13 | `DECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 14 | `DECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 15 | `DECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 16 | `DECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 17 | `DECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 18 | `DECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 19 | `DECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 20 | `DECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 21 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 22 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 23 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 24 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 25 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 27 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 28 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 29 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 31 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 32 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 33 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 34 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 35 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 36 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 37 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 38 | `DERIVATIONCODE` | CHAR(15) |  |  |  |  |
| 39 | `DERIVATIONLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 40 | `DERIVATIONCOMPONENTLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 41 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 42 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 43 | `WHSLOCATIONWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 44 | `WAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 45 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 46 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 47 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 48 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 49 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 50 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 51 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 52 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 53 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 54 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 55 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 56 | `COSTINBASECURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 57 | `BASECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 58 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 59 | `BASECOSTUNITCODE` | CHAR(3) |  |  |  |  |
| 60 | `BASECOSTUNITQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 61 | `PROVISIONALBASECOST` | DECIMAL(18,5) |  |  |  |  |
| 62 | `PROVISIONALCOSTSTATUS` | CHAR(2) |  |  |  |  |
| 63 | `CLOSINGBASECOST` | DECIMAL(18,5) |  |  |  |  |
| 64 | `CLOSINGCOSTSTATUS` | CHAR(2) |  |  |  |  |
| 65 | `VALUATIONPRIORITY` | DECIMAL(2,0) |  |  |  |  |
| 66 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 67 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 68 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 69 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 70 | `BILLDATE` | DATE |  |  |  |  |
| 71 | `BILLTYPE` | SMALLINT | NOT NULL |  |  |  |
| 72 | `BILLCOUNTER` | CHAR(8) |  |  |  |  |
| 73 | `BILLCODE` | CHAR(50) |  |  |  |  |
| 74 | `INTERNALDOCUMENTDATE` | DATE |  |  |  |  |
| 75 | `INTERNALDOCUMENTNUMBER` | INTEGER | NOT NULL |  |  |  |
| 76 | `ORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 77 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 78 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 79 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 80 | `ORDERCOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 81 | `ORDERDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 82 | `INVOICEDATE` | DATE |  |  |  |  |
| 83 | `INVOICECODE` | CHAR(50) |  |  |  |  |
| 84 | `LOTCOSTUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 85 | `RETURNTRANSACTION` | SMALLINT | NOT NULL |  |  |  |
| 86 | `PORTFOLIOCONTROL` | SMALLINT | NOT NULL |  |  |  |
| 87 | `ONHANDUPDATE` | CHAR(2) |  |  |  |  |
| 88 | `LOTRECEIVEDQUANTITYUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 89 | `WAREHOUSEACCOUNTINGGROUPCODE` | CHAR(3) |  |  |  |  |
| 90 | `TMPGROUPSTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 91 | `TEMPLATEGROUPCODE` | CHAR(3) |  |  |  |  |
| 92 | `POSTEDTRANSACTION` | SMALLINT | NOT NULL |  |  |  |
| 93 | `DYNAMICAVERAGECOSTUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 94 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 95 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 96 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 97 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 98 | `TOKENCODE` | CHAR(20) |  |  |  |  |
| 99 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 100 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 101 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 102 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `STOCKTRANSACTIONEXPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.OPERATIONTYPE,
       t.EXPORTSTATUS,
       t.TRANSACTIONSTATUS,
       t.COMPANYCODE,
       t.TRANSACTIONDATE,
       t.TRANSACTIONNUMBER,
       t.TRANSACTIONDETAILNUMBER,
       t.DETAILTYPE,
       t.TEMPLATECODE,
       t.STOCKTRANSACTIONTYPE,
       t.ITEMTYPECODE,
       t.DECOSUBCODE01
FROM   DB2ADMIN.STOCKTRANSACTIONEXPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
