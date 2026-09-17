# DB2ADMIN.WRKSCHEDULEDORDERDETAIL

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 126
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`, `DLVSALORDLINESALORDCMYCODE`, `DLVSALORDLINESALORDCNTCODE`, `DLVSALORDERLINESALESORDERCODE`, `DLVSALESORDERLINEORDERLINE`, `DLVSALESORDERLINEORDERSUBLINE`, `DLVSALORDLINECMPORDERLINE`, `DELIVERYDELIVERYLINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 34935

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `HEADERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `HEADERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 5 | `HEADERCODE` | CHAR(15) |  |  |  |  |
| 6 | `ORDERLINESALESORDERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 7 | `ORDERLINESALESORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 8 | `ORDERLINESALESORDERCODE` | CHAR(15) |  |  |  |  |
| 9 | `ORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 10 | `ORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 11 | `ORDERLINECOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 12 | `DLVSALORDLINESALORDCMYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 13 | `DLVSALORDLINESALORDCNTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 14 | `DLVSALORDERLINESALESORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 15 | `DLVSALESORDERLINEORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 16 | `DLVSALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 17 | `DLVSALORDLINECMPORDERLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 18 | `DELIVERYDELIVERYLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 19 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 20 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 21 | `HEADERSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 22 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 23 | `ORDERLINESTATUS` | CHAR(2) |  |  |  |  |
| 24 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 25 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 26 | `DELIVERYDATE` | DATE |  |  |  |  |
| 27 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 28 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 29 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 30 | `ORDERDATE` | DATE | NOT NULL |  |  |  |
| 31 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 32 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 33 | `ORDERPARTNERLEGALNAME1` | VARCHAR(200) |  |  |  |  |
| 34 | `ORDERPARTNERLEGALNAME2` | VARCHAR(200) |  |  |  |  |
| 35 | `ORDERPARTNERTOWN` | VARCHAR(200) |  |  |  |  |
| 36 | `FNCORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 37 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 38 | `EXTERNALREFERENCE` | CHAR(30) |  |  |  |  |
| 39 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 40 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 41 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 42 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 43 | `FNCACCGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 44 | `FINANCIALACCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 45 | `FNCACCOUNTGRPLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 46 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 47 | `ITEMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 48 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 49 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 50 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 51 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 52 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 53 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 54 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 55 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 56 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 57 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 58 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 59 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 60 | `ITEMLONGDESCRIPTION` | CHAR(200) |  |  |  |  |
| 61 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 62 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 63 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 64 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 65 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 66 | `RESERVATIONDATE` | DATE |  |  |  |  |
| 67 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 68 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 69 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 70 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 71 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 72 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 73 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 74 | `RELEASEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 75 | `SCHEDULEDDELIVERYDATE` | DATE |  |  |  |  |
| 76 | `CONFIRMEDDELIVERYDATE` | DATE |  |  |  |  |
| 77 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 78 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 79 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 80 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 81 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 82 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 83 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 84 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 85 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 86 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 87 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 88 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 89 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 90 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 91 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 92 | `RESIDUALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 93 | `RESIDUALBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 94 | `RESIDUALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 95 | `RESIDUALBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 96 | `RESIDUALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 97 | `CONSIGNMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 98 | `CONSIGNMENTWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 99 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 100 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 101 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 102 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 103 | `USEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 104 | `RESIDUALAMOUNT` | DECIMAL(15,5) |  |  |  |  |
| 105 | `RESIDUALVALUE` | DECIMAL(18,5) |  |  |  |  |
| 106 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 107 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 108 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 109 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 110 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 111 | `PAYMENTCUSTOMERUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 112 | `PAYMENTCUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 113 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 114 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 115 | `BANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 116 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 117 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 118 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 119 | `QUALITYITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 120 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 121 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 122 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 123 | `CONSIGNMENTWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 124 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 125 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |

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
       t.ORDERLINESALESORDERCOMPANYCODE,
       t.ORDERLINESALESORDERCOUNTERCODE,
       t.ORDERLINESALESORDERCODE,
       t.ORDERLINEORDERLINE,
       t.ORDERLINEORDERSUBLINE,
       t.ORDERLINECOMPONENTORDERLINE
FROM   DB2ADMIN.WRKSCHEDULEDORDERDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
