# DB2ADMIN.WRKDEMANDRESERVATION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 126
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 214084

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 2 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 3 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 4 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 5 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 6 | `EXISTENTRESERVATION` | SMALLINT | NOT NULL |  |  |  |
| 7 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 8 | `USEDBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 9 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 12 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 13 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 14 | `USEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 15 | `USEDBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 16 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 17 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 18 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 19 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 20 | `USEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `ORIGINTYPE` | CHAR(2) |  |  |  |  |
| 23 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `ORDERCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 25 | `ORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 26 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 28 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 30 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 32 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `RESERVATIONLINE` | DECIMAL(7,0) |  |  |  |  |
| 34 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 39 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 40 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 41 | `RESERVATIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 42 | `RESERVATIONGROUPCOMPONENTTYPE` | CHAR(2) |  |  |  |  |
| 43 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 44 | `EXTISSUERESSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 45 | `EXTENTRYRESSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 46 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 47 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 48 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 49 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 50 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 51 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 52 | `CUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 53 | `CUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 54 | `SUBCONTRACTORSUPPLYTYPE` | CHAR(2) |  |  |  |  |
| 55 | `SBCWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 56 | `SUBCONTRACTORWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 57 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 58 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 59 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 60 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 61 | `ISSUEDATE` | DATE |  |  |  |  |
| 62 | `PLANSCHEDULEDISSUEDATE` | DATE |  |  |  |  |
| 63 | `SCHEDULEDISSUEDATE` | DATE |  |  |  |  |
| 64 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 65 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 66 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 67 | `RESERVATIONNATURE` | CHAR(1) |  |  |  |  |
| 68 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 69 | `VARIANTCODE` | CHAR(20) |  |  |  |  |
| 70 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 71 | `REFERENCEITEM` | CHAR(2) |  |  |  |  |
| 72 | `RCPGROUPPATREFERENCE` | CHAR(3) |  |  |  |  |
| 73 | `RCPGROUPNOPATLEVEL` | DECIMAL(5,0) |  |  |  |  |
| 74 | `OBSOLETEDISCARDEDITEM` | INTEGER | NOT NULL |  |  |  |
| 75 | `PICKUPQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 76 | `DYELOTWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 77 | `DYELOTWEIGHTUMCODE` | CHAR(3) |  |  |  |  |
| 78 | `PACKAGINGQTYFROMSTEP` | SMALLINT | NOT NULL |  |  |  |
| 79 | `CURRENTSTATUS` | CHAR(2) |  |  |  |  |
| 80 | `RUNMANUALREOPEN` | SMALLINT | NOT NULL |  |  |  |
| 81 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 82 | `QUANTITYPER` | DECIMAL(15,5) |  |  |  |  |
| 83 | `COMPONENTUOMCODE` | CHAR(3) |  |  |  |  |
| 84 | `CALCULATEQTYCODE` | CHAR(20) |  |  |  |  |
| 85 | `ASSEMBLYUOMCODE` | CHAR(3) |  |  |  |  |
| 86 | `WASTETYPE1` | CHAR(2) |  |  |  |  |
| 87 | `WASTE1` | DECIMAL(11,2) |  |  |  |  |
| 88 | `WASTETYPE2` | CHAR(2) |  |  |  |  |
| 89 | `WASTE2` | DECIMAL(11,2) |  |  |  |  |
| 90 | `ASSEMBLYFIXLEADTIMEADJ` | DECIMAL(10,5) |  |  |  |  |
| 91 | `BOMCOMPBILLOFMATERIALNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 92 | `BOMCOMPSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 93 | `BOMCOMPSUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 94 | `RELATEDCMPBILLOFMATITEMTYPECOD` | CHAR(3) |  |  |  |  |
| 95 | `RELATEDCMPBILLOFMATSUBCODE01` | CHAR(20) |  |  |  |  |
| 96 | `RELATEDCMPBILLOFMATSUBCODE02` | CHAR(10) |  |  |  |  |
| 97 | `RELATEDCMPBILLOFMATSUBCODE03` | CHAR(10) |  |  |  |  |
| 98 | `RELATEDCMPBILLOFMATSUBCODE04` | CHAR(10) |  |  |  |  |
| 99 | `RELATEDCMPBILLOFMATSUBCODE05` | CHAR(10) |  |  |  |  |
| 100 | `RELATEDCMPBILLOFMATSUBCODE06` | CHAR(10) |  |  |  |  |
| 101 | `RELATEDCMPBILLOFMATSUBCODE07` | CHAR(10) |  |  |  |  |
| 102 | `RELATEDCMPBILLOFMATSUBCODE08` | CHAR(10) |  |  |  |  |
| 103 | `RELATEDCMPBILLOFMATSUBCODE09` | CHAR(10) |  |  |  |  |
| 104 | `RELATEDCMPBILLOFMATSUBCODE10` | CHAR(10) |  |  |  |  |
| 105 | `RELATEDCMPBILLOFMATSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 106 | `RELATEDCOMPONENTSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 107 | `RELATEDGROUPLINE` | INTEGER | NOT NULL |  |  |  |
| 108 | `RELATEDRESERVATIONLINE` | DECIMAL(7,0) |  |  |  |  |
| 109 | `POLICYCHANGENATURE` | CHAR(2) |  |  |  |  |
| 110 | `REFERENCEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 111 | `ROUNDED` | CHAR(1) |  |  |  |  |
| 112 | `CALCULATIONSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 113 | `BOMUOMTYPE` | CHAR(2) |  |  |  |  |
| 114 | `BOMUOMCODE` | CHAR(3) |  |  |  |  |
| 115 | `BOMQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 116 | `PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 117 | `MANUALRESERVATION` | SMALLINT | NOT NULL |  |  |  |
| 118 | `MANUALMODIFIEDQUANTITY` | SMALLINT | NOT NULL |  |  |  |
| 119 | `MANUALMODIFIEDRESERVATION` | SMALLINT | NOT NULL |  |  |  |
| 120 | `NOTEDITABLERESERVATION` | SMALLINT | NOT NULL |  |  |  |
| 121 | `GROUPLINE` | INTEGER | NOT NULL |  |  |  |
| 122 | `GROUPSTEPNUMBER` | INTEGER | NOT NULL |  |  |  |
| 123 | `RESERVATIONINGROUPORDER` | SMALLINT | NOT NULL |  |  |  |
| 124 | `HEADERLINELINK` | CHAR(140) |  |  |  |  |
| 125 | `SUBRECIPERESERVATION` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CHOOSE,
       t.USERPRIMARYUOMCODE,
       t.USERPRIMARYQUANTITY,
       t.USEDUSERPRIMARYQUANTITY,
       t.BASEPRIMARYUOMCODE,
       t.EXISTENTRESERVATION,
       t.BASEPRIMARYQUANTITY,
       t.USEDBASEPRIMARYQUANTITY,
       t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE
FROM   DB2ADMIN.WRKDEMANDRESERVATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
