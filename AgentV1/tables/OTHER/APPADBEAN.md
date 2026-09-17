# DB2ADMIN.APPADBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 178
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 114387

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `PREVIOUSDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 5 | `LOGINCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `DESCRIPTIONCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 7 | `UGGGROUPTYPE1` | CHAR(10) |  |  |  |  |
| 8 | `USERGENERICGROUPCODES1` | VARCHAR(200) |  |  |  |  |
| 9 | `UGGGROUPTYPE2` | CHAR(10) |  |  |  |  |
| 10 | `USERGENERICGROUPCODES2` | VARCHAR(200) |  |  |  |  |
| 11 | `UGGGROUPTYPE3` | CHAR(10) |  |  |  |  |
| 12 | `USERGENERICGROUPCODES3` | VARCHAR(200) |  |  |  |  |
| 13 | `UGGGROUPTYPE4` | CHAR(10) |  |  |  |  |
| 14 | `USERGENERICGROUPCODES4` | VARCHAR(200) |  |  |  |  |
| 15 | `UGGGROUPTYPE5` | CHAR(10) |  |  |  |  |
| 16 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 17 | `USERGENERICGROUPCODES5` | VARCHAR(200) |  |  |  |  |
| 18 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 19 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 20 | `VIRTUALRETURNSUBCODE` | CHAR(30) |  |  |  |  |
| 21 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `LONGDESCRIPTION` | VARCHAR(100) |  |  | description | Long human-readable label. |
| 31 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 32 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 33 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 34 | `BASEPRIMARYUNITCODE` | CHAR(3) |  |  |  |  |
| 35 | `BASECOSTUNITCODE` | CHAR(3) |  |  |  |  |
| 36 | `BASESECONDARYUNITCODE` | CHAR(3) |  |  |  |  |
| 37 | `SECONDARYUNSTEADYCVSFACTOR` | DECIMAL(11,5) |  |  |  |  |
| 38 | `CONVERSIONFACTORTYPE` | CHAR(2) |  |  |  |  |
| 39 | `MULTIPLIER` | DECIMAL(11,5) |  |  |  |  |
| 40 | `CONVERSIONFACTORPOLICYCODE` | CHAR(20) |  |  |  |  |
| 41 | `CREATESELLINGITEM` | SMALLINT | NOT NULL |  |  |  |
| 42 | `CREATEPURCHASEORDERITEM` | SMALLINT | NOT NULL |  |  |  |
| 43 | `CREATEINTERNALORDERITEM` | SMALLINT | NOT NULL |  |  |  |
| 44 | `LOTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 45 | `EXISTENTLOTSLOADING` | CHAR(2) |  |  |  |  |
| 46 | `LOTCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 47 | `CHOOSELOTCODE` | CHAR(20) |  |  |  |  |
| 48 | `CHECKLOTCODE` | CHAR(20) |  |  |  |  |
| 49 | `LOTEXPIRATIONCODE` | CHAR(20) |  |  |  |  |
| 50 | `CONTAINERCONTROLLED` | CHAR(2) |  |  |  |  |
| 51 | `SEVERALCONTAINERTYPEALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 52 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 53 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 54 | `CHOOSECONTAINERCODE` | CHAR(20) |  |  |  |  |
| 55 | `ELEMENTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 56 | `ELEMENTCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 57 | `CHOOSEELEMENTSCODE` | CHAR(20) |  |  |  |  |
| 58 | `QUALITYCONTROLLED` | CHAR(2) |  |  |  |  |
| 59 | `QUALITYGROUPCODE` | CHAR(3) |  |  |  |  |
| 60 | `PROJECTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 61 | `STATISTICALGROUPCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 62 | `CUSTOMERCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 63 | `SUPPLIERCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 64 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 65 | `BARTYPECODE` | CHAR(2) |  |  |  |  |
| 66 | `BARCODE` | CHAR(30) |  |  |  |  |
| 67 | `DRAWINGNUMBER` | CHAR(100) |  |  |  |  |
| 68 | `MANUFACTURERCODE` | CHAR(15) |  |  |  |  |
| 69 | `COMPOSITIONCODE` | CHAR(8) |  |  |  |  |
| 70 | `INTRASTATCODE` | CHAR(8) |  |  |  |  |
| 71 | `LIFOGRPCODE` | CHAR(3) |  |  |  |  |
| 72 | `FOREUSESTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 73 | `FOREUSECODE` | CHAR(3) |  |  |  |  |
| 74 | `STOCKTAKESTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 75 | `STOCKTAKECODE` | CHAR(3) |  |  |  |  |
| 76 | `REPLENSTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 77 | `REPLENCODE` | CHAR(3) |  |  |  |  |
| 78 | `FAMILYGRPCODE` | CHAR(3) |  |  |  |  |
| 79 | `QAITEMGROUPCODE` | CHAR(10) |  |  |  |  |
| 80 | `STATUS` | CHAR(1) |  |  |  |  |
| 81 | `RUNAPPROVE` | SMALLINT | NOT NULL |  |  |  |
| 82 | `APPROVALDATE` | DATE |  |  |  |  |
| 83 | `APPROVALUSER` | CHAR(25) |  |  |  |  |
| 84 | `RUNACTIVATE` | SMALLINT | NOT NULL |  |  |  |
| 85 | `RELEASEDATE` | DATE |  |  |  |  |
| 86 | `RELEASEUSER` | CHAR(25) |  |  |  |  |
| 87 | `VALIDITYSTATUS` | CHAR(2) |  |  |  |  |
| 88 | `INITIALDATE` | DATE |  |  |  |  |
| 89 | `FINALDATE` | DATE |  |  |  |  |
| 90 | `RELATEDENTITYSTATUS` | CHAR(90) |  |  |  |  |
| 91 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 92 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 93 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 94 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 95 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 96 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 97 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 98 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 99 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 100 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 101 | `PRODUCTIONUOMTYPE` | CHAR(2) |  |  |  |  |
| 102 | `PRODUCTIONUNITCODE` | CHAR(3) |  |  |  |  |
| 103 | `STDPRODUCTIONBATCH` | DECIMAL(15,5) |  |  |  |  |
| 104 | `SUBCONTRACTORSUPPLYTYPE` | CHAR(2) |  |  |  |  |
| 105 | `CUSTOMERSUPPLYTYPE` | CHAR(2) |  |  |  |  |
| 106 | `COSTCATEGORYCODE` | CHAR(20) |  |  |  |  |
| 107 | `COSTLEVELCODE` | CHAR(3) |  |  |  |  |
| 108 | `WASTEPRODUCT` | CHAR(2) |  |  |  |  |
| 109 | `PRODUCTIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 110 | `BOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 111 | `BOMVIRTUALRETURNSUBCODE` | CHAR(30) |  |  |  |  |
| 112 | `BOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 113 | `BOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 114 | `BOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 115 | `BOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 116 | `BOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 117 | `BOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 118 | `BOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 119 | `BOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 120 | `BOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 121 | `RTGSUBCODE01` | CHAR(20) |  |  |  |  |
| 122 | `RTGVIRTUALRETURNSUBCODE` | CHAR(30) |  |  |  |  |
| 123 | `RTGSUBCODE02` | CHAR(10) |  |  |  |  |
| 124 | `RTGSUBCODE03` | CHAR(10) |  |  |  |  |
| 125 | `RTGSUBCODE04` | CHAR(10) |  |  |  |  |
| 126 | `RTGSUBCODE05` | CHAR(10) |  |  |  |  |
| 127 | `RTGSUBCODE06` | CHAR(10) |  |  |  |  |
| 128 | `RTGSUBCODE07` | CHAR(10) |  |  |  |  |
| 129 | `RTGSUBCODE08` | CHAR(10) |  |  |  |  |
| 130 | `RTGSUBCODE09` | CHAR(10) |  |  |  |  |
| 131 | `RTGSUBCODE10` | CHAR(10) |  |  |  |  |
| 132 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 133 | `PICKUPPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 134 | `CONSUMPTIONFACTOR` | DECIMAL(5,2) |  |  |  |  |
| 135 | `KEEPOLDPRICE` | SMALLINT | NOT NULL |  |  |  |
| 136 | `INTERNALPRICE` | DECIMAL(18,5) |  |  |  |  |
| 137 | `INTERNALPRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 138 | `VALIDFROMDATE` | DATE |  |  |  |  |
| 139 | `VALIDTODATE` | DATE |  |  |  |  |
| 140 | `INTPRICELISTCODE` | CHAR(8) |  |  |  |  |
| 141 | `INTPRICECOSTGROUPCODE` | CHAR(8) |  |  |  |  |
| 142 | `INTPRICEPLANTCODE` | CHAR(8) |  |  |  |  |
| 143 | `NUMBEROFKEYSTOINPUT` | INTEGER | NOT NULL |  |  |  |
| 144 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 145 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 146 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(40) |  |  |  |  |
| 147 | `PRODWASHSYMBOL01CODE` | CHAR(10) |  |  |  |  |
| 148 | `PRODWASHSYMBOL02CODE` | CHAR(10) |  |  |  |  |
| 149 | `PRODWASHSYMBOL03CODE` | CHAR(10) |  |  |  |  |
| 150 | `PRODWASHSYMBOL04CODE` | CHAR(10) |  |  |  |  |
| 151 | `PRODWASHSYMBOL05CODE` | CHAR(10) |  |  |  |  |
| 152 | `PRODWASHSYMBOL06CODE` | CHAR(10) |  |  |  |  |
| 153 | `MAXLAYLENGTH` | DECIMAL(7,2) |  |  |  |  |
| 154 | `MAXNOLAYERS` | INTEGER | NOT NULL |  |  |  |
| 155 | `WIDTHRANGEFROM` | DECIMAL(5,2) |  |  |  |  |
| 156 | `WIDTHRANGETO` | DECIMAL(5,2) |  |  |  |  |
| 157 | `GSMRANGEFROM` | DECIMAL(5,2) |  |  |  |  |
| 158 | `GSMRANGETO` | DECIMAL(5,2) |  |  |  |  |
| 159 | `SHRINKAGE` | DECIMAL(5,2) |  |  |  |  |
| 160 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 161 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 162 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 163 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 164 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 165 | `DIRTYFIELD` | CHAR(20) |  |  |  |  |
| 166 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 167 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 168 | `IMPOPERATIONUSER` | CHAR(25) |  |  |  |  |
| 169 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 170 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 171 | `IMPCREATIONUSER` | CHAR(25) |  |  |  |  |
| 172 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 173 | `IMPLASTUPDATEUSER` | CHAR(25) |  |  |  |  |
| 174 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 175 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 176 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 177 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.PREVIOUSDESCRIPTION,
       t.LOGINCOMPANYCODE,
       t.DESCRIPTIONCHANGED,
       t.UGGGROUPTYPE1,
       t.USERGENERICGROUPCODES1,
       t.UGGGROUPTYPE2,
       t.USERGENERICGROUPCODES2,
       t.UGGGROUPTYPE3
FROM   DB2ADMIN.APPADBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
