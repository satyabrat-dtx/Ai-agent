# DB2ADMIN.WRKBOMCOMPONENT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 97
- **Primary key**: `WRKBILLOFMATERIALCOMPANYCODE`, `WRKBIOFMATCREATIONTIMESTAMP`, `WRKBILLOFMATERIALPRODUCTITCODE`, `WRKBILLOFMATERIALSUBCODE01`, `WRKBILLOFMATERIALSUBCODE02`, `WRKBILLOFMATERIALSUBCODE03`, `WRKBILLOFMATERIALSUBCODE04`, `WRKBILLOFMATERIALSUBCODE05`, `WRKBILLOFMATERIALSUBCODE06`, `WRKBILLOFMATERIALSUBCODE07`, `WRKBILLOFMATERIALSUBCODE08`, `WRKBILLOFMATERIALSUBCODE09`, `WRKBILLOFMATERIALSUBCODE10`, `LINENO`, `COMPITEMTYPECODE`, `ITEMTYPEAFICODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 127586

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WRKBILLOFMATERIALCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `WRKBIOFMATCREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `WRKBILLOFMATERIALPRODUCTITCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `WRKBILLOFMATERIALSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `WRKBILLOFMATERIALSUBCODE02` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 5 | `WRKBILLOFMATERIALSUBCODE03` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 6 | `WRKBILLOFMATERIALSUBCODE04` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 7 | `WRKBILLOFMATERIALSUBCODE05` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 8 | `WRKBILLOFMATERIALSUBCODE06` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 9 | `WRKBILLOFMATERIALSUBCODE07` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 10 | `WRKBILLOFMATERIALSUBCODE08` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 11 | `WRKBILLOFMATERIALSUBCODE09` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 12 | `WRKBILLOFMATERIALSUBCODE10` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 13 | `BOMNATURE` | CHAR(10) |  |  |  |  |
| 14 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 15 | `COPYFLAG` | SMALLINT | NOT NULL |  |  |  |
| 16 | `COMPITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 17 | `COMPITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 18 | `COMPONENTCODE` | CHAR(10) |  |  |  |  |
| 19 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 20 | `ITEMTYPEAFICODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 21 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 22 | `SUBCODE02` | CHAR(20) |  |  | generic_classification_code |  |
| 23 | `SUBCODE03` | CHAR(20) |  |  | generic_classification_code |  |
| 24 | `SUBCODE04` | CHAR(20) |  |  | generic_classification_code |  |
| 25 | `SUBCODE05` | CHAR(20) |  |  | generic_classification_code |  |
| 26 | `SUBCODE06` | CHAR(20) |  |  | generic_classification_code |  |
| 27 | `SUBCODE07` | CHAR(20) |  |  | generic_classification_code |  |
| 28 | `SUBCODE08` | CHAR(20) |  |  | generic_classification_code |  |
| 29 | `SUBCODE09` | CHAR(20) |  |  | generic_classification_code |  |
| 30 | `SUBCODE10` | CHAR(20) |  |  | generic_classification_code |  |
| 31 | `SUBCODE1DESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 32 | `SUBCODE2DESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 33 | `SUBCODE3DESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 34 | `SUBCODE4DESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 35 | `SUBCODE5DESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 36 | `SUBCODE6DESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 37 | `SUBCODE7DESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 38 | `SUBCODE8DESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 39 | `SUBCODE9DESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 40 | `SUBCODE10DESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 41 | `DEPONGRMCOLOR` | SMALLINT | NOT NULL |  |  |  |
| 42 | `DEPONGRMSIZE` | SMALLINT | NOT NULL |  |  |  |
| 43 | `COLORSKIPBOM` | SMALLINT | NOT NULL |  |  |  |
| 44 | `COMPUGGROUPTYPECODE` | CHAR(10) |  |  |  |  |
| 45 | `COLORCODE` | CHAR(10) |  |  |  |  |
| 46 | `SIZESKIPBOM` | SMALLINT | NOT NULL |  |  |  |
| 47 | `USERGENERICGROUPTYPECODE` | CHAR(10) |  |  |  |  |
| 48 | `SIZEUGGROUPTYPECODE` | CHAR(10) |  |  |  |  |
| 49 | `DESTSKIPSELECTED` | SMALLINT | NOT NULL |  |  |  |
| 50 | `DESTSKIPALL` | SMALLINT | NOT NULL |  |  |  |
| 51 | `DESTSKIPUNSELECTED` | SMALLINT | NOT NULL |  |  |  |
| 52 | `DUSERGENGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 53 | `DUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 54 | `DESTINATIONCODE` | CHAR(10) |  |  |  |  |
| 55 | `LOTHANDLED` | SMALLINT | NOT NULL |  |  |  |
| 56 | `POHANDLED` | SMALLINT | NOT NULL |  |  |  |
| 57 | `QUANTITYPERUOM` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 58 | `WASTAGE` | DECIMAL(11,2) |  |  |  |  |
| 59 | `REFERENCEQUANTITY` | DECIMAL(11,0) |  |  |  |  |
| 60 | `RESERVATIONWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 61 | `RESERVATIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 62 | `CALSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 63 | `PRODUCTIONRESERVATIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 64 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 65 | `CONSUMPTION` | DECIMAL(9,5) |  |  |  |  |
| 66 | `TOTALCONSUMPTION` | DECIMAL(9,5) |  |  |  |  |
| 67 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 68 | `PRODUCED` | SMALLINT | NOT NULL |  |  |  |
| 69 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 70 | `ITEMSPECIFICATIONS` | CHAR(50) |  |  |  |  |
| 71 | `ITEMPLACEMENT` | CHAR(50) |  |  |  |  |
| 72 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 73 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 74 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 75 | `SUPPLIERPRICE` | DECIMAL(18,5) |  |  |  |  |
| 76 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 77 | `CONVERSIONRATE` | DECIMAL(18,5) |  |  |  |  |
| 78 | `LOCALRATE` | DECIMAL(18,5) |  |  |  |  |
| 79 | `COSTPERPC` | DECIMAL(18,5) |  |  |  |  |
| 80 | `COSTPERGMNT` | DECIMAL(18,5) |  |  |  |  |
| 81 | `STATUSMODE` | SMALLINT | NOT NULL |  |  |  |
| 82 | `APPROVED` | SMALLINT | NOT NULL |  |  |  |
| 83 | `INITIALDATE` | DATE |  |  |  |  |
| 84 | `FINALDATE` | DATE |  |  |  |  |
| 85 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 86 | `PLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 87 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 88 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 89 | `COLORSIZESKIPBOM` | SMALLINT | NOT NULL |  |  |  |
| 90 | `CALCULATEQTYCODE` | CHAR(20) |  |  |  |  |
| 91 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 92 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 93 | `RULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 94 | `STATUS` | CHAR(1) | NOT NULL |  |  |  |
| 95 | `COSTPLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 96 | `COSTPLANTCODE` | CHAR(8) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKBOMCOMPONENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.WRKBILLOFMATERIALCOMPANYCODE,
       t.WRKBIOFMATCREATIONTIMESTAMP,
       t.WRKBILLOFMATERIALPRODUCTITCODE,
       t.WRKBILLOFMATERIALSUBCODE01,
       t.WRKBILLOFMATERIALSUBCODE02,
       t.WRKBILLOFMATERIALSUBCODE03,
       t.WRKBILLOFMATERIALSUBCODE04,
       t.WRKBILLOFMATERIALSUBCODE05,
       t.WRKBILLOFMATERIALSUBCODE06,
       t.WRKBILLOFMATERIALSUBCODE07,
       t.WRKBILLOFMATERIALSUBCODE08,
       t.WRKBILLOFMATERIALSUBCODE09
FROM   DB2ADMIN.WRKBOMCOMPONENT t
FETCH FIRST 100 ROWS ONLY;
```
