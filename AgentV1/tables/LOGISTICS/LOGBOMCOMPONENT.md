# DB2ADMIN.LOGBOMCOMPONENT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 115
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 56603

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BILLOFMATERIALCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `BILLOFMATERIALNUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 2 | `BILLOFMATERIALITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `BILLOFMATERIALSUBCODE01` | CHAR(20) | NOT NULL |  |  |  |
| 4 | `BILLOFMATERIALSUBCODE02` | CHAR(10) |  |  |  |  |
| 5 | `BILLOFMATERIALSUBCODE03` | CHAR(10) |  |  |  |  |
| 6 | `BILLOFMATERIALSUBCODE04` | CHAR(10) |  |  |  |  |
| 7 | `BILLOFMATERIALSUBCODE05` | CHAR(10) |  |  |  |  |
| 8 | `BILLOFMATERIALSUBCODE06` | CHAR(10) |  |  |  |  |
| 9 | `BILLOFMATERIALSUBCODE07` | CHAR(10) |  |  |  |  |
| 10 | `BILLOFMATERIALSUBCODE08` | CHAR(10) |  |  |  |  |
| 11 | `BILLOFMATERIALSUBCODE09` | CHAR(10) |  |  |  |  |
| 12 | `BILLOFMATERIALSUBCODE10` | CHAR(10) |  |  |  |  |
| 13 | `BILLOFMATERIALSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 14 | `SEQUENCE` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 15 | `SUBSEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 16 | `COMPONENTINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 17 | `REFBOMSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 18 | `REFBOMSUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 19 | `REFBOMSTATUS` | CHAR(2) |  |  |  |  |
| 20 | `BOMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 21 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 22 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 23 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 33 | `VARIANTCODE` | CHAR(20) |  |  |  |  |
| 34 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 35 | `CALCULATEQTYCODE` | CHAR(20) |  |  |  |  |
| 36 | `QUANTITYPERTYPE` | CHAR(2) |  |  |  |  |
| 37 | `QUANTITYPER` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 38 | `COMPONENTUOMCODE` | CHAR(3) |  |  |  |  |
| 39 | `COSTPER` | DECIMAL(18,5) |  |  |  |  |
| 40 | `COSTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 41 | `ASSEMBLYUOMCODE` | CHAR(3) |  |  |  |  |
| 42 | `POLICYCHANGENATURE` | CHAR(2) |  |  |  |  |
| 43 | `REFERENCEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 44 | `ROUNDED` | CHAR(1) |  |  |  |  |
| 45 | `PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 46 | `PACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 47 | `RELATEDCOMPONENTSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 48 | `PICKUPQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `CALCULATIONSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 50 | `PRODUCED` | SMALLINT | NOT NULL |  |  |  |
| 51 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 52 | `COSTINGPLANTCODE` | CHAR(8) |  |  |  |  |
| 53 | `ASSEMBLYQTYADJPRC` | DECIMAL(5,2) |  |  |  |  |
| 54 | `ASSEMBLYFIXLEADTIMEADJ` | DECIMAL(10,5) |  |  |  |  |
| 55 | `ASSEMBLYVARLEADTIMEADJ` | DECIMAL(10,5) |  |  |  |  |
| 56 | `SUBCONTRACTORSUPPLYTYPE` | CHAR(2) |  |  |  |  |
| 57 | `CUSTOMERSUPPLYTYPE` | CHAR(2) |  |  |  |  |
| 58 | `PRODUCTIONRESERVATIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 59 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 60 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 61 | `RESERVATIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 62 | `REFERENCEITEM` | CHAR(2) |  |  |  |  |
| 63 | `WASTETYPE1` | CHAR(2) |  |  |  |  |
| 64 | `WASTE1` | DECIMAL(11,2) |  |  |  |  |
| 65 | `WASTETYPE2` | CHAR(2) |  |  |  |  |
| 66 | `WASTE2` | DECIMAL(11,2) |  |  |  |  |
| 67 | `RULECODE` | CHAR(10) |  |  |  |  |
| 68 | `RULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 69 | `INITIALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 70 | `FINALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 71 | `INITIALDATE` | DATE |  |  |  |  |
| 72 | `FINALDATE` | DATE |  |  |  |  |
| 73 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 74 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 75 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 76 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 77 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 78 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 79 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 80 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 81 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 82 | `BILLOFMATITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 83 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 84 | `COSTINGPLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 85 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 86 | `RESERVATIONWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 87 | `ENERGYCONSUMPTIONFACTOR` | DECIMAL(5,2) |  |  |  |  |
| 88 | `STARTINGTEMPERATURE` | DECIMAL(5,2) |  |  |  |  |
| 89 | `ENDINGTEMPERATURE` | DECIMAL(5,2) |  |  |  |  |
| 90 | `MINUTESINTEMPERATURE` | DECIMAL(5,2) |  |  |  |  |
| 91 | `NBROFBATHFLOWS` | DECIMAL(5,2) |  |  |  |  |
| 92 | `QUANTITYPERBATHFLOW` | DECIMAL(7,2) |  |  |  |  |
| 93 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 94 | `PACKAGINGQTYFROMSTEP` | SMALLINT | NOT NULL |  |  |  |
| 95 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 96 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 97 | `PRICECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 98 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 99 | `PRICETYPE` | CHAR(1) |  |  |  |  |
| 100 | `PRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 101 | `STATUS` | CHAR(1) | NOT NULL |  |  |  |
| 102 | `APPROVALDATE` | DATE |  |  |  |  |
| 103 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 104 | `RELEASEDATE` | DATE |  |  |  |  |
| 105 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 106 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 107 | `BOMCOMPONENTTYPECODE` | CHAR(10) |  |  |  |  |
| 108 | `SUPPLIERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 109 | `SUPPLIERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 110 | `PROVISIONAL` | SMALLINT | NOT NULL |  |  |  |
| 111 | `BOMCOMPONENTGROUPCODE` | CHAR(10) |  |  |  |  |
| 112 | `REFERENCEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 113 | `RULEAPPLICABILITY` | INTEGER | NOT NULL |  |  |  |
| 114 | `PROTOTYPEMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGBOMCOMPONENT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.BILLOFMATERIALCOMPANYCODE,
       t.BILLOFMATERIALNUMBERID,
       t.BILLOFMATERIALITEMTYPECODE,
       t.BILLOFMATERIALSUBCODE01,
       t.BILLOFMATERIALSUBCODE02,
       t.BILLOFMATERIALSUBCODE03,
       t.BILLOFMATERIALSUBCODE04,
       t.BILLOFMATERIALSUBCODE05,
       t.BILLOFMATERIALSUBCODE06,
       t.BILLOFMATERIALSUBCODE07,
       t.BILLOFMATERIALSUBCODE08,
       t.BILLOFMATERIALSUBCODE09
FROM   DB2ADMIN.LOGBOMCOMPONENT t
FETCH FIRST 100 ROWS ONLY;
```
