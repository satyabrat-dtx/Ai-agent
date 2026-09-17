# DB2ADMIN.LOGPRODUCT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 196
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 50440

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 5 | `SUBCODE02` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 6 | `SUBCODE03` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 7 | `SUBCODE04` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 9 | `SUBCODE06` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 10 | `SUBCODE07` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 11 | `SUBCODE08` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 12 | `SUBCODE09` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 13 | `SUBCODE10` | CHAR(10) | NOT NULL |  | generic_classification_code |  |
| 14 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 15 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 16 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 17 | `BASEPRIMARYUNITCODE` | CHAR(3) |  |  |  |  |
| 18 | `BASECOSTUNITCODE` | CHAR(3) |  |  |  |  |
| 19 | `BASESECONDARYUNITCODE` | CHAR(3) |  |  |  |  |
| 20 | `SECONDARYUNSTEADYCVSFACTOR` | DECIMAL(11,5) |  |  |  |  |
| 21 | `CONVERSIONFACTORTYPE` | CHAR(2) |  |  |  |  |
| 22 | `MULTIPLIER` | DECIMAL(11,5) |  |  |  |  |
| 23 | `CONVERSIONFACTORPOLICYCODE` | CHAR(20) |  |  |  |  |
| 24 | `LOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 25 | `EXISTENTLOTSLOADING` | CHAR(2) | NOT NULL |  |  |  |
| 26 | `LOTCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 27 | `CHOOSELOTCODE` | CHAR(20) |  |  |  |  |
| 28 | `CHECKLOTCODE` | CHAR(20) |  |  |  |  |
| 29 | `LOTEXPIRATIONCODE` | CHAR(20) |  |  |  |  |
| 30 | `CONTAINERCONTROLLED` | CHAR(2) | NOT NULL |  |  |  |
| 31 | `SEVERALCONTAINERTYPEALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 32 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 33 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 34 | `CHOOSECONTAINERCODE` | CHAR(20) |  |  |  |  |
| 35 | `ELEMENTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 36 | `ELEMENTCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 37 | `CHOOSEELEMENTSCODE` | CHAR(20) |  |  |  |  |
| 38 | `QUALITYCONTROLLED` | CHAR(2) | NOT NULL |  |  |  |
| 39 | `QUALITYGROUPCODE` | CHAR(3) |  |  |  |  |
| 40 | `PROJECTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 41 | `STATISTICALGROUPCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 42 | `CUSTOMERCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 43 | `SUPPLIERCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 44 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 45 | `BARTYPECODE` | CHAR(2) |  |  |  |  |
| 46 | `BARCODE` | VARCHAR(50) |  |  |  |  |
| 47 | `DRAWINGNUMBER` | CHAR(100) |  |  |  |  |
| 48 | `MANUFACTURERCODE` | CHAR(15) |  |  |  |  |
| 49 | `COMPOSITIONCODE` | CHAR(10) |  |  |  |  |
| 50 | `INTRASTATCODE` | CHAR(11) |  |  |  |  |
| 51 | `LIFOGRPCODE` | CHAR(3) |  |  |  |  |
| 52 | `FOREUSESTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 53 | `FOREUSECODE` | CHAR(3) |  |  |  |  |
| 54 | `STOCKTAKESTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 55 | `STOCKTAKECODE` | CHAR(3) |  |  |  |  |
| 56 | `REPLENSTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 57 | `REPLENCODE` | CHAR(3) |  |  |  |  |
| 58 | `FAMILYGRPCODE` | CHAR(3) |  |  |  |  |
| 59 | `STATUS` | CHAR(1) | NOT NULL |  |  |  |
| 60 | `APPROVALDATE` | DATE |  |  |  |  |
| 61 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 62 | `RELEASEDATE` | DATE |  |  |  |  |
| 63 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 64 | `VALIDITYSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 65 | `INITIALDATE` | DATE |  |  |  |  |
| 66 | `FINALDATE` | DATE |  |  |  |  |
| 67 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 68 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 69 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 70 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 71 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 72 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 73 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 74 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 75 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 76 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 77 | `PRODUCTIONUOMTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 78 | `PRODUCTIONUNITCODE` | CHAR(3) |  |  |  |  |
| 79 | `STDPRODUCTIONBATCH` | DECIMAL(15,5) |  |  |  |  |
| 80 | `SUBCONTRACTORSUPPLYTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 81 | `CUSTOMERSUPPLYTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 82 | `COSTCATEGORYCODE` | CHAR(20) |  |  |  |  |
| 83 | `COSTLEVELCODE` | CHAR(3) |  |  |  |  |
| 84 | `WASTEPRODUCT` | CHAR(2) |  |  |  |  |
| 85 | `PRODUCTIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 86 | `BOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 87 | `BOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 88 | `BOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 89 | `BOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 90 | `BOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 91 | `BOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 92 | `BOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 93 | `BOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 94 | `BOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 95 | `BOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 96 | `RTGSUBCODE01` | CHAR(20) |  |  |  |  |
| 97 | `RTGSUBCODE02` | CHAR(10) |  |  |  |  |
| 98 | `RTGSUBCODE03` | CHAR(10) |  |  |  |  |
| 99 | `RTGSUBCODE04` | CHAR(10) |  |  |  |  |
| 100 | `RTGSUBCODE05` | CHAR(10) |  |  |  |  |
| 101 | `RTGSUBCODE06` | CHAR(10) |  |  |  |  |
| 102 | `RTGSUBCODE07` | CHAR(10) |  |  |  |  |
| 103 | `RTGSUBCODE08` | CHAR(10) |  |  |  |  |
| 104 | `RTGSUBCODE09` | CHAR(10) |  |  |  |  |
| 105 | `RTGSUBCODE10` | CHAR(10) |  |  |  |  |
| 106 | `PICKUPPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 107 | `CONSUMPTIONFACTOR` | DECIMAL(5,2) |  |  |  |  |
| 108 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 109 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 110 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 111 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 112 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 113 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 114 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 115 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 116 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 117 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 118 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 119 | `LOTCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 120 | `CONTAINERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 121 | `ELEMENTCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 122 | `QUALITYGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 123 | `MANUFACTURERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 124 | `COMPOSITIONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 125 | `LIFOGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 126 | `FOREUSESTDGRPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 127 | `STOCKTAKESTDGRPTYPECMYCODE` | CHAR(3) |  |  |  |  |
| 128 | `REPLENSTDGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 129 | `FAMILYGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 130 | `FIRSTGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 131 | `SECONDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 132 | `THIRDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 133 | `FOURTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 134 | `FIFTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 135 | `COSTCATEGORYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 136 | `COSTLEVELCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 137 | `PRODWASHSYMBOL01CODE` | CHAR(10) |  |  |  |  |
| 138 | `PRODWASHSYMBOL02CODE` | CHAR(10) |  |  |  |  |
| 139 | `PRODWASHSYMBOL03CODE` | CHAR(10) |  |  |  |  |
| 140 | `PRODWASHSYMBOL04CODE` | CHAR(10) |  |  |  |  |
| 141 | `PRODWASHSYMBOL05CODE` | CHAR(10) |  |  |  |  |
| 142 | `PRODWASHSYMBOL06CODE` | CHAR(10) |  |  |  |  |
| 143 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 144 | `QAITEMGROUPCODE` | CHAR(10) |  |  |  |  |
| 145 | `MAXLAYLENGTH` | DECIMAL(8,3) |  |  |  |  |
| 146 | `MAXNOLAYERS` | INTEGER | NOT NULL |  |  |  |
| 147 | `WIDTHRANGEFROM` | DECIMAL(5,2) |  |  |  |  |
| 148 | `WIDTHRANGETO` | DECIMAL(5,2) |  |  |  |  |
| 149 | `GSMRANGEFROM` | DECIMAL(5,2) |  |  |  |  |
| 150 | `GSMRANGETO` | DECIMAL(5,2) |  |  |  |  |
| 151 | `SHRINKAGE` | DECIMAL(5,2) |  |  |  |  |
| 152 | `QAITEMGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 153 | `TAKEALLQADEFINITIONS` | SMALLINT | NOT NULL |  |  |  |
| 154 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 155 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 156 | `BUDGETGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 157 | `BUDGETUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 158 | `BUDGETUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 159 | `ARTICLESTATUSCODE` | CHAR(8) |  |  |  |  |
| 160 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 161 | `CHECKELEMENTSCODE` | CHAR(20) |  |  |  |  |
| 162 | `ORIGINCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 163 | `PRODUCTIONBOMRULECODE` | CHAR(10) |  |  |  |  |
| 164 | `PRODUCTIONBOMRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 165 | `COSTINGBOMRULECODE` | CHAR(10) |  |  |  |  |
| 166 | `COSTINGBOMRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 167 | `TECHNICALBOMRULECODE` | CHAR(10) |  |  |  |  |
| 168 | `TECHNICALBOMRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 169 | `PLANNINGBOMRULECODE` | CHAR(10) |  |  |  |  |
| 170 | `PLANNINGBOMRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 171 | `PRODUCTIONROUTINGRULECODE` | CHAR(10) |  |  |  |  |
| 172 | `PROROUTINGRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 173 | `COSTINGROUTINGRULECODE` | CHAR(10) |  |  |  |  |
| 174 | `COSTINGROUTINGRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 175 | `TECHNICALROUTINGRULECODE` | CHAR(10) |  |  |  |  |
| 176 | `TECHNICALROUTINGRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 177 | `PLANNINGROUTINGRULECODE` | CHAR(10) |  |  |  |  |
| 178 | `PLANNINGROUTINGRULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 179 | `ORIGINVERSIONCHANGEREASONCODE` | CHAR(8) |  |  |  |  |
| 180 | `DRCOUNTER` | CHAR(8) |  |  |  |  |
| 181 | `DRCODE` | CHAR(15) |  |  |  |  |
| 182 | `DRLINE` | DECIMAL(5,0) |  |  |  |  |
| 183 | `MARKERLENGTHUOMCODE` | CHAR(3) |  |  |  |  |
| 184 | `AUTONETWEIGHTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 185 | `QRCODE` | CHAR(200) |  |  |  |  |
| 186 | `MAKEORBUY` | INTEGER | NOT NULL |  |  |  |
| 187 | `ALLOWEDPRODUCTSKETCHGROUPKEY` | VARCHAR(250) |  |  |  |  |
| 188 | `NOTTRANSACTIONABLE` | SMALLINT | NOT NULL |  |  |  |
| 189 | `TIMETYPE` | INTEGER | NOT NULL |  |  |  |
| 190 | `FIXEDHOURS` | DECIMAL(10,5) |  |  |  |  |
| 191 | `SPEED` | DECIMAL(15,5) |  |  |  |  |
| 192 | `SPEEDUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 193 | `PRODUCTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 194 | `PRODWASHSYMBOLLABELCODE` | CHAR(10) |  |  |  |  |
| 195 | `ORIGINPROTOTYPE` | CHAR(20) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGPRODUCT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGPRODUCTSTATUSPOLICIES`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)
- child `LOGPRODUCTALLOWEDVALUES`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.LOGPRODUCT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
