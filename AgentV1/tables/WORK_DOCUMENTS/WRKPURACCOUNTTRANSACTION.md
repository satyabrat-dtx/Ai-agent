# DB2ADMIN.WRKPURACCOUNTTRANSACTION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 168
- **Primary key**: `COMPANYCODE`, `WRKIDENTIFIER`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 80501

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CHOOSER` | SMALLINT | NOT NULL |  |  |  |
| 1 | `TYPE` | CHAR(1) |  |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `TRANSACTIONSTATUS` | CHAR(2) |  |  |  |  |
| 4 | `CHARGETOAPPLY` | CHAR(20) |  |  |  |  |
| 5 | `CHARGEIDENTIFIER` | CHAR(2) |  |  |  |  |
| 6 | `WRKIDENTIFIER` | BIGINT | NOT NULL | PK | primary_key |  |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 9 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 10 | `ITEMCODE` | CHAR(140) |  |  |  |  |
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
| 42 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
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
| 70 | `LOTCODE` | CHAR(35) |  |  |  |  |
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
| 82 | `PRODUCTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 83 | `BILLCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 84 | `PRODUCTSUBCODE01` | CHAR(20) |  |  |  |  |
| 85 | `PRODUCTSUBCODE02` | CHAR(10) |  |  |  |  |
| 86 | `PRODUCTSUBCODE03` | CHAR(10) |  |  |  |  |
| 87 | `PRODUCTSUBCODE04` | CHAR(10) |  |  |  |  |
| 88 | `PRODUCTSUBCODE05` | CHAR(10) |  |  |  |  |
| 89 | `PRODUCTSUBCODE06` | CHAR(10) |  |  |  |  |
| 90 | `PRODUCTSUBCODE07` | CHAR(10) |  |  |  |  |
| 91 | `PRODUCTSUBCODE08` | CHAR(10) |  |  |  |  |
| 92 | `PRODUCTSUBCODE09` | CHAR(10) |  |  |  |  |
| 93 | `PRODUCTSUBCODE10` | CHAR(10) |  |  |  |  |
| 94 | `PRODUCTDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 95 | `PRODUCTITEMCODE` | CHAR(140) |  |  |  |  |
| 96 | `BILLCODE` | CHAR(50) |  |  |  |  |
| 97 | `INTERNALDOCUMENTDATE` | DATE |  |  |  |  |
| 98 | `INTERNALDOCUMENTNUMBER` | INTEGER | NOT NULL |  |  |  |
| 99 | `ORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 100 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 101 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 102 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 103 | `ORDERCOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 104 | `ORDERDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 105 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 106 | `INVOICEDATE` | DATE |  |  |  |  |
| 107 | `INVOICECODE` | CHAR(50) |  |  |  |  |
| 108 | `ACCOUNTTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 109 | `ENTRYDOCUMENTTOGENERATE` | CHAR(2) |  |  |  |  |
| 110 | `LOTCOSTUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 111 | `RETURNTRANSACTION` | SMALLINT | NOT NULL |  |  |  |
| 112 | `PORTFOLIOCONTROL` | SMALLINT | NOT NULL |  |  |  |
| 113 | `ONHANDUPDATE` | CHAR(2) |  |  |  |  |
| 114 | `LOTRECEIVEDQUANTITYUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 115 | `WAREHOUSEACCOUNTINGGROUPCODE` | CHAR(3) |  |  |  |  |
| 116 | `TMPGROUPSTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 117 | `TEMPLATEGROUPCODE` | CHAR(3) |  |  |  |  |
| 118 | `POSTEDTRANSACTION` | SMALLINT | NOT NULL |  |  |  |
| 119 | `DYNAMICAVERAGECOSTUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 120 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 121 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 122 | `PERCENTAGEFORQUANTITYORVALUE` | DECIMAL(5,2) |  |  |  |  |
| 123 | `DAILYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 124 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 125 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 126 | `COSTINBASECURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 127 | `BASECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 128 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 129 | `BASECOSTUNITCODE` | CHAR(3) |  |  |  |  |
| 130 | `BASECOSTUNITQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 131 | `PROVISIONALBASECOST` | DECIMAL(18,5) |  |  |  |  |
| 132 | `PROVISIONALCOSTSTATUS` | CHAR(2) |  |  |  |  |
| 133 | `CLOSINGBASECOST` | DECIMAL(18,5) |  |  |  |  |
| 134 | `CLOSINGCOSTSTATUS` | CHAR(2) |  |  |  |  |
| 135 | `VALUATIONPRIORITY` | DECIMAL(2,0) |  |  |  |  |
| 136 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 137 | `TOTALCHARGEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 138 | `PRODUCTITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 139 | `PRODUCTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 140 | `FLAGROWRELOAD` | SMALLINT | NOT NULL |  |  |  |
| 141 | `FLAGROWORDERBY` | SMALLINT | NOT NULL |  |  |  |
| 142 | `CREATIONDATETIMEVIEW` | TIMESTAMP |  |  |  |  |
| 143 | `CREATIONUSERVIEW` | CHAR(50) |  |  |  |  |
| 144 | `ACCOUNTINGTYPE` | CHAR(2) |  |  |  |  |
| 145 | `HRACCOUNTCODE` | CHAR(20) |  |  |  |  |
| 146 | `HRACCOUNTTEMPLATECODE` | CHAR(6) |  |  |  |  |
| 147 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 148 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 149 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 150 | `EXTERNALBANKCODE` | CHAR(15) |  |  |  |  |
| 151 | `COMPANYBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 152 | `ORDPRNBANKORDPRNCSMSUPTYPE` | CHAR(1) |  |  |  |  |
| 153 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 154 | `SUPPLIERFATTYPE` | CHAR(1) |  |  |  |  |
| 155 | `SUPPLIERFATCODE` | CHAR(8) |  |  |  |  |
| 156 | `COSTELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 157 | `COSTELEMENTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 158 | `COSTELEMENTSUBCODE01` | CHAR(20) |  |  |  |  |
| 159 | `DEMANDSTEPPRODEMANDCNTCODE` | CHAR(8) |  |  |  |  |
| 160 | `DEMANDSTEPPRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 161 | `DEMANDSTEPSTEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 162 | `DIVISIONFATCODE` | CHAR(3) |  |  |  |  |
| 163 | `HRCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 164 | `HREXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 165 | `EXCLUDE` | SMALLINT | NOT NULL |  |  |  |
| 166 | `CURRENCYPOOLNOTES` | VARCHAR(3000) |  |  |  |  |
| 167 | `PREPAYMENTAMOUNT` | DECIMAL(18,5) |  |  |  |  |

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
       t.CHARGETOAPPLY,
       t.CHARGEIDENTIFIER,
       t.WRKIDENTIFIER,
       t.CREATIONUSER,
       t.LINE,
       t.ALLOWEDDIVISIONS,
       t.ITEMCODE,
       t.BASECOSTUOMCODE
FROM   DB2ADMIN.WRKPURACCOUNTTRANSACTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
