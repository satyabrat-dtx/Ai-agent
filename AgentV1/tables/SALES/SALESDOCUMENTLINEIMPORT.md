# DB2ADMIN.SALESDOCUMENTLINEIMPORT

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `business_data`
- **Columns**: 118
- **Primary key**: `SALESDOCUMENTIMPORTCOMPANYCODE`, `SALDOCIMPIMPPROVISIONALCODE`, `ORDERLINE`, `ORDERSUBLINE`, `COMPONENTORDERLINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 48529

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESDOCUMENTIMPORTCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `SALDOCIMPIMPPROVISIONALCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `IMPORTOPERATION` | INTEGER | NOT NULL |  |  |  |
| 3 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 4 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 5 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 6 | `COMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 7 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 8 | `LINEGROUP` | CHAR(3) |  |  |  |  |
| 9 | `LINESOURCE` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `PREVIOUSLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 11 | `PREVIOUSDOCUMENTTYPEORDERTYPE` | CHAR(1) |  |  |  |  |
| 12 | `PREVIOUSDOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 13 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 14 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 15 | `PREVIOUSORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 16 | `PREVIOUSORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 17 | `PREVIOUSCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 18 | `PREVIOUSDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 19 | `PREVIOUSORIGINFROM` | CHAR(2) |  |  |  |  |
| 20 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 21 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 22 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 23 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 24 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 25 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 26 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `ITEMBARCODE` | VARCHAR(50) |  |  |  |  |
| 36 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 37 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 38 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 39 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 40 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 41 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 42 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 43 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 44 | `CREDITUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 45 | `CREDITUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 46 | `CREDITUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 48 | `CONSIGNMENTTYPE` | CHAR(2) |  |  |  |  |
| 49 | `CONSIGNMENTWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 50 | `LINESTATUS` | CHAR(2) |  |  |  |  |
| 51 | `INVOICEEVOLUTIONTYPE` | CHAR(2) |  |  |  |  |
| 52 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 53 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 54 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 55 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 56 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 57 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 58 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 59 | `DLVSALORDLINESALORDCNTCODE` | CHAR(8) |  |  |  |  |
| 60 | `DLVSALORDERLINESALESORDERCODE` | CHAR(15) |  |  |  |  |
| 61 | `DLVSALESORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 62 | `DLVSALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 63 | `DLVSALORDLINECMPORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 64 | `DELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 65 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 66 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 67 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 68 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 69 | `DISCOUNTCATEGORYORDERTYPE` | CHAR(1) |  |  |  |  |
| 70 | `DISCOUNTCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 71 | `LINEUSERVALUE` | CHAR(20) |  |  |  |  |
| 72 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 73 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 74 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 75 | `PRICESIGN` | CHAR(2) |  |  |  |  |
| 76 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 77 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 78 | `FREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 79 | `NETVALUEINCLUDINGTAX` | DECIMAL(18,5) |  |  |  |  |
| 80 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 81 | `COMMISSIONLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 82 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 83 | `COMMISSIONLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 84 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 85 | `COMMISSIONLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 86 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 87 | `COMMISSIONLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 88 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 89 | `COMMISSIONLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 90 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 91 | `ADUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 92 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 93 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 94 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 95 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 96 | `PREVIOUSCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 97 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 98 | `QUALITYITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 99 | `CONSIGNMENTWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 100 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 101 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 102 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 103 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 104 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 105 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 106 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 107 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 108 | `PAYMENTLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 109 | `INVOICELIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 110 | `PAYMENTLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 111 | `INVOICELIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 112 | `PAYMENTLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 113 | `INVOICELIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 114 | `PAYMENTLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 115 | `INVOICELIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 116 | `PAYMENTLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 117 | `INVOICELIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESDOCUMENTLINEIMPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SALESDOCUMENTIMPORTCOMPANYCODE,
       t.SALDOCIMPIMPPROVISIONALCODE,
       t.IMPORTOPERATION,
       t.ORDERTYPE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.COMPONENTORDERLINE,
       t.LINETEMPLATECODE,
       t.LINEGROUP,
       t.LINESOURCE,
       t.PREVIOUSLINETEMPLATECODE,
       t.PREVIOUSDOCUMENTTYPEORDERTYPE
FROM   DB2ADMIN.SALESDOCUMENTLINEIMPORT t
FETCH FIRST 100 ROWS ONLY;
```
