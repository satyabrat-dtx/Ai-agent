# DB2ADMIN.BOMCOMPONENTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'BOM')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 155
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 45267

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `SKIPBOMCOMPONENT` | SMALLINT | NOT NULL |  |  |  |
| 2 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 3 | `OWNEDCOMPONENT` | CHAR(2) |  |  |  |  |
| 4 | `BILLOFMATERIALITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `BILLOFMATERIALSUBCODE01` | CHAR(20) |  |  |  |  |
| 6 | `BILLOFMATERIALSUBCODE02` | CHAR(10) |  |  |  |  |
| 7 | `BILLOFMATERIALSUBCODE03` | CHAR(10) |  |  |  |  |
| 8 | `BILLOFMATERIALSUBCODE04` | CHAR(10) |  |  |  |  |
| 9 | `BILLOFMATERIALSUBCODE05` | CHAR(10) |  |  |  |  |
| 10 | `BILLOFMATERIALSUBCODE06` | CHAR(10) |  |  |  |  |
| 11 | `BILLOFMATERIALSUBCODE07` | CHAR(10) |  |  |  |  |
| 12 | `BILLOFMATERIALSUBCODE08` | CHAR(10) |  |  |  |  |
| 13 | `BILLOFMATERIALSUBCODE09` | CHAR(10) |  |  |  |  |
| 14 | `BILLOFMATERIALSUBCODE10` | CHAR(10) |  |  |  |  |
| 15 | `BILLOFMATERIALSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 16 | `SEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 17 | `SUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 18 | `COMPONENTINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 19 | `REFBOMSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 20 | `REFBOMSUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 21 | `REFBOMSTATUS` | CHAR(2) |  |  |  |  |
| 22 | `BOMNATURE` | CHAR(1) |  |  |  |  |
| 23 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 24 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 25 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 35 | `VARIANTCODE` | CHAR(20) |  |  |  |  |
| 36 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 37 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 38 | `CALCULATEQTYCODE` | CHAR(20) |  |  |  |  |
| 39 | `QUANTITYPERTYPE` | CHAR(2) |  |  |  |  |
| 40 | `QUANTITYPER` | DECIMAL(15,5) |  |  |  |  |
| 41 | `COMPONENTUOMCODE` | CHAR(3) |  |  |  |  |
| 42 | `COSTPER` | DECIMAL(18,5) |  |  |  |  |
| 43 | `COSTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 44 | `ASSEMBLYUOMCODE` | CHAR(3) |  |  |  |  |
| 45 | `POLICYCHANGENATURE` | CHAR(2) |  |  |  |  |
| 46 | `REFERENCEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `ROUNDED` | CHAR(1) |  |  |  |  |
| 48 | `PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `PACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 50 | `RELATEDCOMPONENTSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 51 | `PICKUPQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 52 | `CALCULATIONSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 53 | `PRODUCED` | SMALLINT | NOT NULL |  |  |  |
| 54 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 55 | `COSTINGPLANTCODE` | CHAR(8) |  |  |  |  |
| 56 | `ASSEMBLYQTYADJPRC` | DECIMAL(5,2) |  |  |  |  |
| 57 | `ASSEMBLYFIXLEADTIMEADJ` | DECIMAL(10,5) |  |  |  |  |
| 58 | `ASSEMBLYVARLEADTIMEADJ` | DECIMAL(10,5) |  |  |  |  |
| 59 | `SUBCONTRACTORSUPPLYTYPE` | CHAR(2) |  |  |  |  |
| 60 | `CUSTOMERSUPPLYTYPE` | CHAR(2) |  |  |  |  |
| 61 | `PRODUCTIONRESERVATIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 62 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 63 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 64 | `RESERVATIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 65 | `REFERENCEITEM` | CHAR(2) |  |  |  |  |
| 66 | `WASTETYPE1` | CHAR(2) |  |  |  |  |
| 67 | `WASTE1` | DECIMAL(11,2) |  |  |  |  |
| 68 | `WASTETYPE2` | CHAR(2) |  |  |  |  |
| 69 | `WASTE2` | DECIMAL(11,2) |  |  |  |  |
| 70 | `RULECODE` | CHAR(10) |  |  |  |  |
| 71 | `RULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 72 | `INITIALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 73 | `FINALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 74 | `INITIALDATE` | DATE |  |  |  |  |
| 75 | `FINALDATE` | DATE |  |  |  |  |
| 76 | `RESETREFBOMLINK` | SMALLINT | NOT NULL |  |  |  |
| 77 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 78 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 79 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 80 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 81 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 82 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 83 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 84 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 85 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 86 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 87 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 88 | `ENERGYCONSUMPTIONFACTOR` | DECIMAL(5,2) |  |  |  |  |
| 89 | `STARTINGTEMPERATURE` | DECIMAL(5,2) |  |  |  |  |
| 90 | `ENDINGTEMPERATURE` | DECIMAL(5,2) |  |  |  |  |
| 91 | `MINUTESINTEMPERATURE` | DECIMAL(5,2) |  |  |  |  |
| 92 | `NBROFBATHFLOWS` | DECIMAL(5,2) |  |  |  |  |
| 93 | `QUANTITYPERBATHFLOW` | DECIMAL(7,2) |  |  |  |  |
| 94 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 95 | `PACKAGINGQTYFROMSTEP` | SMALLINT | NOT NULL |  |  |  |
| 96 | `PRICECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 97 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 98 | `PRICETYPE` | CHAR(1) |  |  |  |  |
| 99 | `PRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 100 | `FORCEDIRTYSEQUENCEDRULES` | SMALLINT | NOT NULL |  |  |  |
| 101 | `STATUS` | CHAR(1) |  |  |  |  |
| 102 | `APPROVALDATE` | DATE |  |  |  |  |
| 103 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 104 | `RUNAPPROVE` | SMALLINT | NOT NULL |  |  |  |
| 105 | `RELEASEDATE` | DATE |  |  |  |  |
| 106 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 107 | `RUNACTIVATE` | SMALLINT | NOT NULL |  |  |  |
| 108 | `BOMCOMPONENTTYPECODE` | CHAR(10) |  |  |  |  |
| 109 | `SUPPLIERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 110 | `SUPPLIERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 111 | `QUICKRULECHECK1` | SMALLINT | NOT NULL |  |  |  |
| 112 | `QUICKRULECHECK2` | SMALLINT | NOT NULL |  |  |  |
| 113 | `QUICKRULECHECK3` | SMALLINT | NOT NULL |  |  |  |
| 114 | `QUICKRULECHECK4` | SMALLINT | NOT NULL |  |  |  |
| 115 | `QUICKRULECHECK5` | SMALLINT | NOT NULL |  |  |  |
| 116 | `QUICKRULECHECK6` | SMALLINT | NOT NULL |  |  |  |
| 117 | `QUICKRULECHECK7` | SMALLINT | NOT NULL |  |  |  |
| 118 | `QUICKRULECHECK8` | SMALLINT | NOT NULL |  |  |  |
| 119 | `QUICKRULECHECK9` | SMALLINT | NOT NULL |  |  |  |
| 120 | `QUICKRULECHECK10` | SMALLINT | NOT NULL |  |  |  |
| 121 | `QUICKRULECHECK11` | SMALLINT | NOT NULL |  |  |  |
| 122 | `QUICKRULECHECK12` | SMALLINT | NOT NULL |  |  |  |
| 123 | `QUICKRULECHECK13` | SMALLINT | NOT NULL |  |  |  |
| 124 | `QUICKRULECHECK14` | SMALLINT | NOT NULL |  |  |  |
| 125 | `QUICKRULECHECK15` | SMALLINT | NOT NULL |  |  |  |
| 126 | `QUICKRULECHECK16` | SMALLINT | NOT NULL |  |  |  |
| 127 | `QUICKRULECHECK17` | SMALLINT | NOT NULL |  |  |  |
| 128 | `QUICKRULECHECK18` | SMALLINT | NOT NULL |  |  |  |
| 129 | `QUICKRULECHECK19` | SMALLINT | NOT NULL |  |  |  |
| 130 | `QUICKRULECHECK20` | SMALLINT | NOT NULL |  |  |  |
| 131 | `SHOWNATLEASTONETIME` | SMALLINT | NOT NULL |  |  |  |
| 132 | `LASTITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 133 | `PROVISIONAL` | SMALLINT | NOT NULL |  |  |  |
| 134 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 135 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 136 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 137 | `BOMCOMPONENTGROUPCODE` | CHAR(10) |  |  |  |  |
| 138 | `REFERENCEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 139 | `RULEAPPLICABILITY` | INTEGER | NOT NULL |  |  |  |
| 140 | `RUNSUSPEND` | SMALLINT | NOT NULL |  |  |  |
| 141 | `PROTOTYPEMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 142 | `DIRECTIVESGB` | BLOB(1000000) |  |  |  |  |
| 143 | `CMPFATHERPRODUCTSUBCODE01` | CHAR(10) |  |  |  |  |
| 144 | `CMPFATHERPRODUCTSUBCODE02` | CHAR(10) |  |  |  |  |
| 145 | `CMPFATHERPRODUCTSUBCODE03` | CHAR(10) |  |  |  |  |
| 146 | `CMPFATHERPRODUCTSUBCODE04` | CHAR(10) |  |  |  |  |
| 147 | `CMPFATHERPRODUCTSUBCODE05` | CHAR(10) |  |  |  |  |
| 148 | `CMPFATHERPRODUCTSUBCODE06` | CHAR(10) |  |  |  |  |
| 149 | `CMPFATHERPRODUCTSUBCODE07` | CHAR(10) |  |  |  |  |
| 150 | `CMPFATHERPRODUCTSUBCODE08` | CHAR(10) |  |  |  |  |
| 151 | `CMPFATHERPRODUCTSUBCODE09` | CHAR(10) |  |  |  |  |
| 152 | `CMPFATHERPRODUCTSUBCODE10` | CHAR(10) |  |  |  |  |
| 153 | `DIRECTIVESCONTEXTGB` | BLOB(1000000) |  |  |  |  |
| 154 | `FIELDTODIRTY` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `BOMCOMPONENTBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `BOMCOMPONENTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.SKIPBOMCOMPONENT,
       t.IMPORTAUTOCOUNTER,
       t.OWNEDCOMPONENT,
       t.BILLOFMATERIALITEMTYPECODE,
       t.BILLOFMATERIALSUBCODE01,
       t.BILLOFMATERIALSUBCODE02,
       t.BILLOFMATERIALSUBCODE03,
       t.BILLOFMATERIALSUBCODE04,
       t.BILLOFMATERIALSUBCODE05,
       t.BILLOFMATERIALSUBCODE06,
       t.BILLOFMATERIALSUBCODE07
FROM   DB2ADMIN.BOMCOMPONENTBEAN t
FETCH FIRST 100 ROWS ONLY;
```
