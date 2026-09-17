# DB2ADMIN.WRKISSUETOPO

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 102
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`, `COMPANYCODE`, `DECOSUBCODE01`, `DECOSUBCODE02`, `DECOSUBCODE03`, `DECOSUBCODE04`, `DECOSUBCODE05`, `DECOSUBCODE06`, `DECOSUBCODE07`, `DECOSUBCODE08`, `DECOSUBCODE09`, `DECOSUBCODE10`, `LOTCODE`, `CONTAINERITEMTYPECODE`, `CONTAINERSUBCODE01`, `CONTAINERELEMENTCODE`, `PHYSICALWAREHOUSECODE`, `WHSLOCATIONWAREHOUSEZONECODE`, `WAREHOUSELOCATIONCODE`, `ITEMTYPECODE`, `SUBCODEKEY`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 128315

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CHOOSER` | SMALLINT | NOT NULL |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 3 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 4 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 7 | `SUBCODEKEY` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 8 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 9 | `DECOSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 10 | `DECOSUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 11 | `DECOSUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 12 | `DECOSUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 13 | `DECOSUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 14 | `DECOSUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 15 | `DECOSUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 16 | `DECOSUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 17 | `DECOSUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 18 | `DECOSUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 19 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 21 | `PHYSICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 22 | `PHYSICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 23 | `WHSLOCWHSZONEPHYWHSCMYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 24 | `WHSLOCATIONWAREHOUSEZONECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 25 | `WAREHOUSELOCATIONCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 26 | `QUALITYLVLITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 27 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 28 | `ENTRYDATE` | DATE |  |  |  |  |
| 29 | `CONTAINERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 30 | `CONTAINERITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 31 | `CONTAINERSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 32 | `CONTAINERELEMENTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 33 | `CONTAINERELEMENTCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 34 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 35 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 36 | `LOTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 37 | `LOTCODE` | CHAR(35) | NOT NULL | PK | primary_key |  |
| 38 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 39 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 40 | `STATUSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 41 | `STATUSCODE` | CHAR(3) |  |  |  |  |
| 42 | `SUMMARIZEDDESCRIPTION` | CHAR(200) |  |  |  |  |
| 43 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 44 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 45 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 46 | `ELEMENTSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 47 | `ELEMENTSSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 48 | `ELEMENTSCODE` | CHAR(15) |  |  |  |  |
| 49 | `QUALITYREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 50 | `QUALITYREASONCODE` | CHAR(3) |  |  |  |  |
| 51 | `FIRSTQUALITYCONTROLCOUNTER` | CHAR(8) |  |  |  |  |
| 52 | `FIRSTQUALITYCONTROLNUMBER` | CHAR(15) |  |  |  |  |
| 53 | `FIRSTQUALITYCONTROLDATE` | DATE |  |  |  |  |
| 54 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 55 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 56 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 57 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 58 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 59 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 60 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 61 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 62 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 63 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 64 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 65 | `BASEPRIMARYUNITCODE` | CHAR(3) |  |  |  |  |
| 66 | `BASEPRIMARYQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 67 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 68 | `BASESECONDARYUNITCODE` | CHAR(3) |  |  |  |  |
| 69 | `BASESECONDARYQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 70 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 71 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 72 | `PACKAGINGCODE` | CHAR(3) |  |  |  |  |
| 73 | `PACKAGINGQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 74 | `BALANCECUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 75 | `BALANCECUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 76 | `BALANCESUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 77 | `BALANCESUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 78 | `CUTNO` | CHAR(10) |  |  |  |  |
| 79 | `LAYNO` | CHAR(10) |  |  |  |  |
| 80 | `MARKERCODE` | CHAR(15) |  |  |  |  |
| 81 | `LAYLENGTH` | DECIMAL(7,2) |  |  |  |  |
| 82 | `LAYERS` | INTEGER | NOT NULL |  |  |  |
| 83 | `SHRINKAGEGROUP` | CHAR(10) |  |  |  |  |
| 84 | `SHADEGROUP` | CHAR(10) |  |  |  |  |
| 85 | `ENDBITS` | DECIMAL(7,2) |  |  |  |  |
| 86 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 87 | `DYELOTNO` | CHAR(10) |  |  |  |  |
| 88 | `ELEMENTSID` | BIGINT | NOT NULL |  |  |  |
| 89 | `PLANNINGGROUP` | BIGINT | NOT NULL |  |  |  |
| 90 | `PRESERVATIONORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 91 | `PRODRESERVATIONORDERCODE` | CHAR(15) |  |  |  |  |
| 92 | `PRODRESERVATIONRESERVATIONLINE` | DECIMAL(5,0) |  |  |  |  |
| 93 | `EXTRAPERC` | DECIMAL(5,2) |  |  |  |  |
| 94 | `RESERVATIONQTY` | DECIMAL(15,5) |  |  |  |  |
| 95 | `REMAININGRESERVATIONQTY` | DECIMAL(15,5) |  |  |  |  |
| 96 | `ISSUEDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 97 | `POCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 98 | `POCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 99 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 100 | `ORDERLINE` | DECIMAL(5,0) |  |  |  |  |
| 101 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKISSUETOPOUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CHOOSER,
       t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODEKEY,
       t.CODE,
       t.DECOSUBCODE01,
       t.DECOSUBCODE02,
       t.DECOSUBCODE03
FROM   DB2ADMIN.WRKISSUETOPO t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
