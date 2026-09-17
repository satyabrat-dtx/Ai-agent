# DB2ADMIN.WRKRECEIPT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 157
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 77580

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `HEADERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `HEADERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 5 | `HEADERCODE` | CHAR(15) |  |  |  |  |
| 6 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 7 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 8 | `COMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 9 | `DELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 10 | `SUBLINE` | INTEGER | NOT NULL |  |  |  |
| 11 | `ORDERDATE` | DATE |  |  |  |  |
| 12 | `RECEIPTORDERTYPE` | CHAR(2) |  |  |  |  |
| 13 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 14 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 15 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 16 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 17 | `ALLOCATIONCODE` | CHAR(15) |  |  |  |  |
| 18 | `ALLOCATIONLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 19 | `ALLOCATIONCOMPONENTLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 20 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 21 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 22 | `DESTINATIONTYPE` | CHAR(1) |  |  |  |  |
| 23 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 24 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 25 | `ORDERRELEASETYPE` | CHAR(2) |  |  |  |  |
| 26 | `CURRENTSTATUS` | CHAR(2) |  |  |  |  |
| 27 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 28 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 29 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 30 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 31 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 32 | `BUYERCODE` | CHAR(50) |  |  |  |  |
| 33 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 34 | `ORDERLINERELEASETYPE` | CHAR(2) |  |  |  |  |
| 35 | `LINESOURCE` | CHAR(2) |  |  |  |  |
| 36 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 37 | `TERMOFSHIPPINGANDRECEIVINGTYPE` | CHAR(2) |  |  |  |  |
| 38 | `ORDERLINESTATUS` | CHAR(2) |  |  |  |  |
| 39 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 40 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 41 | `DELIVERYDATE` | DATE |  |  |  |  |
| 42 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 43 | `CREATIONTYPE` | CHAR(1) |  |  |  |  |
| 44 | `WAREHOUSEWIPCODE` | CHAR(8) |  |  |  |  |
| 45 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 46 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 47 | `RESERVATIONDATE` | DATE |  |  |  |  |
| 48 | `CONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 49 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 50 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 51 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 52 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 53 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 54 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 55 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 56 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 57 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 58 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 59 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 60 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 61 | `ITEMDESCRIPTION` | CHAR(200) |  |  |  |  |
| 62 | `DESTINATIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 63 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 64 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 65 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 66 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 67 | `ORDERDELIVERYRELEASETYPE` | CHAR(2) |  |  |  |  |
| 68 | `CONFIRMATION` | CHAR(15) |  |  |  |  |
| 69 | `REMINDERCOMMENTCODE` | CHAR(12) |  |  |  |  |
| 70 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 71 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 72 | `STOCKTRANSACTIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 73 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 74 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 75 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 76 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 77 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 78 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 79 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 80 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 81 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 82 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 83 | `EXTERNALDOCUMENTCHECK` | SMALLINT | NOT NULL |  |  |  |
| 84 | `EXTERNALDOCUMENTCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 85 | `EXTERNALDOCUMENTCODE` | CHAR(50) |  |  |  |  |
| 86 | `EXTERNALDOCUMENTDATE` | DATE |  |  |  |  |
| 87 | `HASPRODUCEDALLOCATION` | SMALLINT | NOT NULL |  |  |  |
| 88 | `MAINTAINALLOCATION` | SMALLINT | NOT NULL |  |  |  |
| 89 | `LOTCHECK` | CHAR(2) |  |  |  |  |
| 90 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 91 | `SUPPLIERLOTCHECK` | SMALLINT | NOT NULL |  |  |  |
| 92 | `SUPPLIERLOTCODE` | CHAR(35) |  |  |  |  |
| 93 | `FIRSTQUALITYCONTROLCHECK` | SMALLINT | NOT NULL |  |  |  |
| 94 | `QUALITYREASONCODE` | CHAR(3) |  |  |  |  |
| 95 | `FIRSTQUALITYCONTROLDATE` | DATE |  |  |  |  |
| 96 | `FIRSTQUALITYCONTROLCOUNTER` | CHAR(8) |  |  |  |  |
| 97 | `FIRSTQUALITYCONTROLNUMBER` | CHAR(15) |  |  |  |  |
| 98 | `ITEMELEMENTCHECK` | CHAR(2) |  |  |  |  |
| 99 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 100 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 101 | `ENTRYITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 102 | `ENTRYITEMCODE` | VARCHAR(120) |  |  |  |  |
| 103 | `ENTRYITEMDESCRIPTION` | CHAR(200) |  |  |  |  |
| 104 | `ENTRYITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 105 | `ENTRYITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 106 | `WAREHOUSELOCATIONCHECK` | SMALLINT | NOT NULL |  |  |  |
| 107 | `WHSLOCWHSZONEPHYWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 108 | `WHSLOCATIONWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 109 | `WAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 110 | `CONTAINERCHECK` | CHAR(2) |  |  |  |  |
| 111 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 112 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 113 | `CONTAINERELEMENTCHECK` | SMALLINT | NOT NULL |  |  |  |
| 114 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 115 | `WEIGHT` | SMALLINT | NOT NULL |  |  |  |
| 116 | `WEIGHTCHECK` | CHAR(2) | NOT NULL |  |  |  |
| 117 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 118 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 119 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 120 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 121 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 122 | `DSTCOST` | DECIMAL(18,5) |  |  |  |  |
| 123 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 124 | `CHOOSED` | SMALLINT | NOT NULL |  |  |  |
| 125 | `CLOSE` | SMALLINT | NOT NULL |  |  |  |
| 126 | `TRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 127 | `BALANCECUSTOMERCHECK` | SMALLINT | NOT NULL |  |  |  |
| 128 | `BALANCECUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 129 | `BALANCECUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 130 | `BALANCESUPPLIERCHECK` | SMALLINT | NOT NULL |  |  |  |
| 131 | `BALANCESUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 132 | `BALANCESUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 133 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 134 | `HEADERCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 135 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 136 | `PLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 137 | `BUYERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 138 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 139 | `WAREHOUSEWIPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 140 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 141 | `DESTINATIONWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 142 | `QUALITYITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 143 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 144 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 145 | `REMINDERCOMMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 146 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 147 | `STOCKTRNTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 148 | `LOTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 149 | `QUALITYREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 150 | `ITEMELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 151 | `ENTRYITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 152 | `ENTRYITEMELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 153 | `WHSLOCWHSZONEPHYWHSCMYCODE` | CHAR(3) |  |  |  |  |
| 154 | `CONTAINERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 155 | `CONTAINERELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 156 | `ISENTRYCOMPONENT` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.HEADERCOMPANYCODE,
       t.HEADERCOUNTERCODE,
       t.HEADERCODE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.COMPONENTORDERLINE,
       t.DELIVERYLINE,
       t.SUBLINE,
       t.ORDERDATE
FROM   DB2ADMIN.WRKRECEIPT t
FETCH FIRST 100 ROWS ONLY;
```
