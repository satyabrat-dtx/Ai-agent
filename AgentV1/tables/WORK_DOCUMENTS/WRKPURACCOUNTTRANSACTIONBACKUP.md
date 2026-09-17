# DB2ADMIN.WRKPURACCOUNTTRANSACTIONBACKUP

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 166
- **Primary key**: `COMPANYCODE`, `WRKIDENTIFIER`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 98883

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CHOOSER` | SMALLINT | NOT NULL |  |  |  |
| 1 | `TYPE` | CHAR(1) |  |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `TRANSACTIONSTATUS` | CHAR(2) |  |  |  |  |
| 4 | `APPLYCHARGETOTRANSACTIONCOST` | SMALLINT | NOT NULL |  |  |  |
| 5 | `CHARGETOAPPLY` | CHAR(20) |  |  |  |  |
| 6 | `CHARGEIDENTIFIER` | CHAR(2) |  |  |  |  |
| 7 | `WRKIDENTIFIER` | BIGINT | NOT NULL | PK | primary_key |  |
| 8 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 9 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 10 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 11 | `BASECOSTUOMCODE` | CHAR(3) |  |  |  |  |
| 12 | `BASECOSTQTY` | DECIMAL(15,5) |  |  |  |  |
| 13 | `UNITPRICE` | DECIMAL(18,5) |  |  |  |  |
| 14 | `ORIGINALUNITPRICE` | DECIMAL(18,5) |  |  |  |  |
| 15 | `TOTALPRICE` | DECIMAL(18,5) |  |  |  |  |
| 16 | `ORIGINALTOTALPRICE` | DECIMAL(18,5) |  |  |  |  |
| 17 | `TAXABLEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 18 | `ORIGINALTAXABLEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 19 | `HEADERAMOUNTDISCOUNT` | DECIMAL(18,5) |  |  |  |  |
| 20 | `LINEAMOUNTDISCOUNT` | DECIMAL(18,5) |  |  |  |  |
| 21 | `TRANSACTIONDATE` | DATE |  |  |  |  |
| 22 | `TRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 23 | `ACCOUNTCODE` | CHAR(20) |  |  |  |  |
| 24 | `ACCOUNTTEMPLATECODE` | CHAR(6) |  |  |  |  |
| 25 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 26 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 27 | `TRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 28 | `DETAILTYPE` | CHAR(2) |  |  |  |  |
| 29 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 30 | `STOCKTRANSACTIONTYPE` | CHAR(2) |  |  |  |  |
| 31 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 32 | `DECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 33 | `DECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 34 | `DECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 35 | `DECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 36 | `DECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 37 | `DECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 38 | `DECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 39 | `DECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 40 | `DECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 41 | `DECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 42 | `ITEMDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 43 | `EXTERNALOPERATIONMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 44 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 45 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 46 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 47 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 48 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 49 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 50 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 51 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 52 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 53 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 54 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 55 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 56 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 57 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 58 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 59 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 60 | `DERIVATIONCODE` | CHAR(15) |  |  |  |  |
| 61 | `DERIVATIONLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 62 | `DERIVATIONCOMPONENTLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 63 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 64 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 65 | `WHSLOCATIONWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 66 | `WAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 67 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 68 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 69 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 70 | `LOTCODE` | CHAR(10) |  |  |  |  |
| 71 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 72 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 73 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 74 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 75 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 76 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 77 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 78 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 79 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 80 | `BILLDATE` | DATE |  |  |  |  |
| 81 | `BILLTYPE` | SMALLINT | NOT NULL |  |  |  |
| 82 | `BILLCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 83 | `BILLCODE` | CHAR(50) |  |  |  |  |
| 84 | `INTERNALDOCUMENTDATE` | DATE |  |  |  |  |
| 85 | `INTERNALDOCUMENTNUMBER` | INTEGER | NOT NULL |  |  |  |
| 86 | `ORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 87 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 88 | `ORDERLINE` | DECIMAL(5,0) |  |  |  |  |
| 89 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 90 | `ORDERCOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 91 | `ORDERDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 92 | `INVOICEDATE` | DATE |  |  |  |  |
| 93 | `INVOICECODE` | CHAR(50) |  |  |  |  |
| 94 | `ACCOUNTTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 95 | `ENTRYDOCUMENTTOGENERATE` | CHAR(2) |  |  |  |  |
| 96 | `LOTCOSTUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 97 | `RETURNTRANSACTION` | SMALLINT | NOT NULL |  |  |  |
| 98 | `PORTFOLIOCONTROL` | SMALLINT | NOT NULL |  |  |  |
| 99 | `ONHANDUPDATE` | CHAR(2) |  |  |  |  |
| 100 | `LOTRECEIVEDQUANTITYUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 101 | `WAREHOUSEACCOUNTINGGROUPCODE` | CHAR(3) |  |  |  |  |
| 102 | `TMPGROUPSTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 103 | `TEMPLATEGROUPCODE` | CHAR(3) |  |  |  |  |
| 104 | `POSTEDTRANSACTION` | SMALLINT | NOT NULL |  |  |  |
| 105 | `DYNAMICAVERAGECOSTUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 106 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 107 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 108 | `PERCENTAGEFORQUANTITYORVALUE` | DECIMAL(5,2) |  |  |  |  |
| 109 | `DAILYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 110 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 111 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 112 | `COSTINBASECURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 113 | `BASECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 114 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 115 | `BASECOSTUNITCODE` | CHAR(3) |  |  |  |  |
| 116 | `BASECOSTUNITQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 117 | `PROVISIONALBASECOST` | DECIMAL(18,5) |  |  |  |  |
| 118 | `PROVISIONALCOSTSTATUS` | CHAR(2) |  |  |  |  |
| 119 | `CLOSINGBASECOST` | DECIMAL(18,5) |  |  |  |  |
| 120 | `CLOSINGCOSTSTATUS` | CHAR(2) |  |  |  |  |
| 121 | `VALUATIONPRIORITY` | DECIMAL(2,0) |  |  |  |  |
| 122 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 123 | `TOTALCHARGEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 124 | `ITEMCODE` | CHAR(140) |  |  |  |  |
| 125 | `PRODUCTITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 126 | `PRODUCTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 127 | `PRODUCTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 128 | `PRODUCTSUBCODE01` | CHAR(20) |  |  |  |  |
| 129 | `PRODUCTSUBCODE02` | CHAR(10) |  |  |  |  |
| 130 | `PRODUCTSUBCODE03` | CHAR(10) |  |  |  |  |
| 131 | `PRODUCTSUBCODE04` | CHAR(10) |  |  |  |  |
| 132 | `PRODUCTSUBCODE05` | CHAR(10) |  |  |  |  |
| 133 | `PRODUCTSUBCODE06` | CHAR(10) |  |  |  |  |
| 134 | `PRODUCTSUBCODE07` | CHAR(10) |  |  |  |  |
| 135 | `PRODUCTSUBCODE08` | CHAR(10) |  |  |  |  |
| 136 | `PRODUCTSUBCODE09` | CHAR(10) |  |  |  |  |
| 137 | `PRODUCTSUBCODE10` | CHAR(10) |  |  |  |  |
| 138 | `PRODUCTDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 139 | `PRODUCTITEMCODE` | CHAR(140) |  |  |  |  |
| 140 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 141 | `FLAGROWRELOAD` | SMALLINT | NOT NULL |  |  |  |
| 142 | `FLAGROWORDERBY` | SMALLINT | NOT NULL |  |  |  |
| 143 | `CREATIONDATETIMEVIEW` | TIMESTAMP |  |  |  |  |
| 144 | `CREATIONUSERVIEW` | CHAR(25) |  |  |  |  |
| 145 | `ACCOUNTINGTYPE` | CHAR(2) |  |  |  |  |
| 146 | `HRACCOUNTCODE` | CHAR(20) |  |  |  |  |
| 147 | `HRACCOUNTTEMPLATECODE` | CHAR(6) |  |  |  |  |
| 148 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 149 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 150 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 151 | `EXTERNALBANKCODE` | CHAR(15) |  |  |  |  |
| 152 | `COMPANYBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 153 | `ORDPRNBANKORDPRNCSMSUPTYPE` | CHAR(1) |  |  |  |  |
| 154 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 155 | `SUPPLIERFATTYPE` | CHAR(1) |  |  |  |  |
| 156 | `SUPPLIERFATCODE` | CHAR(8) |  |  |  |  |
| 157 | `COSTELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 158 | `COSTELEMENTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 159 | `COSTELEMENTSUBCODE01` | CHAR(20) |  |  |  |  |
| 160 | `DEMANDSTEPPRODEMANDCNTCODE` | CHAR(8) |  |  |  |  |
| 161 | `DEMANDSTEPPRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 162 | `DEMANDSTEPSTEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 163 | `DIVISIONFATCODE` | CHAR(3) |  |  |  |  |
| 164 | `HRCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 165 | `HREXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CHOOSER,
       t.TYPE,
       t.COMPANYCODE,
       t.TRANSACTIONSTATUS,
       t.APPLYCHARGETOTRANSACTIONCOST,
       t.CHARGETOAPPLY,
       t.CHARGEIDENTIFIER,
       t.WRKIDENTIFIER,
       t.CREATIONUSER,
       t.LINE,
       t.ALLOWEDDIVISIONS,
       t.BASECOSTUOMCODE
FROM   DB2ADMIN.WRKPURACCOUNTTRANSACTIONBACKUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
