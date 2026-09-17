# DB2ADMIN.WRKFATHERCHILDCOMPONENT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 110
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 193321

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CHOOSER` | SMALLINT | NOT NULL |  |  |  |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 3 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `WRKFATHERCHILDBOMLINE` | INTEGER | NOT NULL |  |  |  |
| 6 | `OWNEDCOMPONENT` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `SEQUENCE` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 8 | `SUBSEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 9 | `COMPONENTINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 10 | `REFBOMSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 11 | `REFBOMSUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 12 | `REFBOMSTATUS` | CHAR(2) |  |  |  |  |
| 13 | `BOMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 14 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 15 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 16 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 17 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 27 | `VARIANTCODE` | CHAR(20) |  |  |  |  |
| 28 | `QUANTITYPER` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 29 | `COMPONENTUOMCODE` | CHAR(3) |  |  |  |  |
| 30 | `CALCULATEQTYCODE` | CHAR(20) |  |  |  |  |
| 31 | `COSTPER` | DECIMAL(18,5) |  |  |  |  |
| 32 | `COSTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 33 | `QUANTITYPERTYPE` | CHAR(2) |  |  |  |  |
| 34 | `ASSEMBLYUOMCODE` | CHAR(3) |  |  |  |  |
| 35 | `POLICYCHANGENATURE` | CHAR(2) |  |  |  |  |
| 36 | `REFERENCEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 37 | `ROUNDED` | CHAR(1) |  |  |  |  |
| 38 | `PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 39 | `PACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 40 | `RELATEDCOMPONENT` | DECIMAL(5,0) |  |  |  |  |
| 41 | `PICKUPQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 42 | `ENERGYCONSUMPTIONFACTOR` | DECIMAL(5,2) |  |  |  |  |
| 43 | `STARTINGTEMPERATURE` | DECIMAL(5,2) |  |  |  |  |
| 44 | `ENDINGTEMPERATURE` | DECIMAL(5,2) |  |  |  |  |
| 45 | `MINUTESINTEMPERATURE` | DECIMAL(5,2) |  |  |  |  |
| 46 | `NBROFBATHFLOWS` | DECIMAL(5,2) |  |  |  |  |
| 47 | `QUANTITYPERBATHFLOW` | DECIMAL(7,2) |  |  |  |  |
| 48 | `PACKAGINGQTYFROMSTEP` | SMALLINT | NOT NULL |  |  |  |
| 49 | `NEWCOMPONENT` | SMALLINT | NOT NULL |  |  |  |
| 50 | `CALCULATIONSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 51 | `PRODUCED` | SMALLINT | NOT NULL |  |  |  |
| 52 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 53 | `COSTINGPLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 54 | `COSTINGPLANTCODE` | CHAR(8) |  |  |  |  |
| 55 | `PRICECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 56 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 57 | `PRICETYPE` | CHAR(1) |  |  |  |  |
| 58 | `PRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 59 | `ASSEMBLYQTYADJPRC` | DECIMAL(5,2) |  |  |  |  |
| 60 | `ASSEMBLYFIXLEADTIMEADJ` | DECIMAL(10,5) |  |  |  |  |
| 61 | `ASSEMBLYVARLEADTIMEADJ` | DECIMAL(10,5) |  |  |  |  |
| 62 | `SUBCONTRACTORSUPPLYTYPE` | CHAR(2) |  |  |  |  |
| 63 | `CUSTOMERSUPPLYTYPE` | CHAR(2) |  |  |  |  |
| 64 | `PRODUCTIONRESERVATIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 65 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 66 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 67 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 68 | `RESERVATIONWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 69 | `RESERVATIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 70 | `REFERENCEITEM` | CHAR(2) |  |  |  |  |
| 71 | `RULES` | CLOB(24000) |  |  |  |  |
| 72 | `RULECODE` | CHAR(10) |  |  |  |  |
| 73 | `RULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 74 | `WASTETYPE1` | CHAR(2) |  |  |  |  |
| 75 | `WASTE1` | DECIMAL(11,2) |  |  |  |  |
| 76 | `WASTETYPE2` | CHAR(2) |  |  |  |  |
| 77 | `WASTE2` | DECIMAL(11,2) |  |  |  |  |
| 78 | `INITIALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 79 | `FINALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 80 | `INITIALDATE` | DATE |  |  |  |  |
| 81 | `FINALDATE` | DATE |  |  |  |  |
| 82 | `STATUS` | CHAR(1) | NOT NULL |  |  |  |
| 83 | `RUNAPPROVE` | SMALLINT | NOT NULL |  |  |  |
| 84 | `RUNACTIVATE` | SMALLINT | NOT NULL |  |  |  |
| 85 | `APPROVALDATE` | DATE |  |  |  |  |
| 86 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 87 | `RELEASEDATE` | DATE |  |  |  |  |
| 88 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 89 | `CHILDBOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 90 | `COMPONENTFATHERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 91 | `SOURCEITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 92 | `COMPONENTLEVEL` | INTEGER | NOT NULL |  |  |  |
| 93 | `COMPONENTMAYBEFATHER` | SMALLINT | NOT NULL |  |  |  |
| 94 | `NEWBOMALREADYEXISTS` | SMALLINT | NOT NULL |  |  |  |
| 95 | `GENERALSEQUENCE` | DECIMAL(18,5) |  |  |  |  |
| 96 | `CHECKFATHER` | SMALLINT | NOT NULL |  |  |  |
| 97 | `HASCHILDREN` | SMALLINT | NOT NULL |  |  |  |
| 98 | `HASDELETEDANCESTOR` | SMALLINT | NOT NULL |  |  |  |
| 99 | `FATHERSEQUENCE` | DECIMAL(18,5) |  |  |  |  |
| 100 | `BOMCOMPONENTTYPECODE` | CHAR(10) |  |  |  |  |
| 101 | `MANUALCOMPONENT` | SMALLINT | NOT NULL |  |  |  |
| 102 | `SUPPLIERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 103 | `SUPPLIERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 104 | `DIRECTIVESGB` | BLOB(1000000) |  |  |  |  |
| 105 | `SOURCEDIRECTIVESBOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 106 | `SOURCECMPFATHERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 107 | `PROVISIONAL` | SMALLINT | NOT NULL |  |  |  |
| 108 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 109 | `RULEAPPLICABILITY` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CHOOSER,
       t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.WRKFATHERCHILDBOMLINE,
       t.OWNEDCOMPONENT,
       t.SEQUENCE,
       t.SUBSEQUENCE,
       t.COMPONENTINCIDENCE,
       t.REFBOMSEQUENCE,
       t.REFBOMSUBSEQUENCE
FROM   DB2ADMIN.WRKFATHERCHILDCOMPONENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
