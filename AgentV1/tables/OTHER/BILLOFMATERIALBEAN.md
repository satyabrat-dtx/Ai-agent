# DB2ADMIN.BILLOFMATERIALBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 115
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 74793

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 3 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 4 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 5 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `BOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 8 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 9 | `VIRTUALRETURNSUBCODE` | CHAR(30) |  |  |  |  |
| 10 | `BOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 11 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `BOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 13 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `BOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 15 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `BOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 17 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `BOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 19 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `BOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 21 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `BOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 23 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `BOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 25 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `BOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 27 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `BOMCODE` | VARCHAR(120) |  |  |  |  |
| 29 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 30 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 31 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 32 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 33 | `REFBOMCODE` | VARCHAR(120) |  |  |  |  |
| 34 | `REFBOMSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 35 | `REFBOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 36 | `RESETREFBOMLINK` | SMALLINT | NOT NULL |  |  |  |
| 37 | `COPYBOMSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 38 | `COPYBOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 39 | `PRODUCTIONBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 40 | `PRODBOMSTARTDATE` | DATE |  |  |  |  |
| 41 | `PRODBOMENDDATE` | DATE |  |  |  |  |
| 42 | `PRODUCTIONREFERENCEBOM` | SMALLINT | NOT NULL |  |  |  |
| 43 | `PRODREFBOMSTARTDATE` | DATE |  |  |  |  |
| 44 | `PRODREFBOMENDDATE` | DATE |  |  |  |  |
| 45 | `COSTCALCULATIONBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 46 | `COSTCALCBOMSTARTDATE` | DATE |  |  |  |  |
| 47 | `COSTCALCBOMENDDATE` | DATE |  |  |  |  |
| 48 | `TECHNICALBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 49 | `TECHBOMSTARTDATE` | DATE |  |  |  |  |
| 50 | `TECHBOMENDDATE` | DATE |  |  |  |  |
| 51 | `PLANNINGBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 52 | `PLANBOMSTARTDATE` | DATE |  |  |  |  |
| 53 | `PLANBOMENDDATE` | DATE |  |  |  |  |
| 54 | `BOMTYPECODE` | CHAR(6) |  |  |  |  |
| 55 | `CHECKCODE` | CHAR(2) |  |  |  |  |
| 56 | `USERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 57 | `GENERICREFERENCE` | CHAR(20) |  |  |  |  |
| 58 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 59 | `COSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 60 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 61 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 62 | `BOMUOMTYPE` | CHAR(2) |  |  |  |  |
| 63 | `BOMUOMCODE` | CHAR(3) |  |  |  |  |
| 64 | `BOMQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 65 | `BOMINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 66 | `BOMCOMMENTCRITERIA` | CHAR(2) |  |  |  |  |
| 67 | `HEADERCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 68 | `COMMENTCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 69 | `COMMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 70 | `STATUS` | CHAR(1) |  |  |  |  |
| 71 | `RUNAPPROVE` | SMALLINT | NOT NULL |  |  |  |
| 72 | `APPROVALDATE` | DATE |  |  |  |  |
| 73 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 74 | `RUNACTIVATE` | SMALLINT | NOT NULL |  |  |  |
| 75 | `RELEASEDATE` | DATE |  |  |  |  |
| 76 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 77 | `PRDITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 78 | `PRDSUBCODE01` | CHAR(20) |  |  |  |  |
| 79 | `PRDSUBCODE02` | CHAR(10) |  |  |  |  |
| 80 | `PRDSUBCODE03` | CHAR(10) |  |  |  |  |
| 81 | `PRDSUBCODE04` | CHAR(10) |  |  |  |  |
| 82 | `PRDSUBCODE05` | CHAR(10) |  |  |  |  |
| 83 | `PRDSUBCODE06` | CHAR(10) |  |  |  |  |
| 84 | `PRDSUBCODE07` | CHAR(10) |  |  |  |  |
| 85 | `PRDSUBCODE08` | CHAR(10) |  |  |  |  |
| 86 | `PRDSUBCODE09` | CHAR(10) |  |  |  |  |
| 87 | `PRDSUBCODE10` | CHAR(10) |  |  |  |  |
| 88 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 89 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 90 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 91 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 92 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 93 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 94 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 95 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 96 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 97 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 98 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 99 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 100 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 101 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 102 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 103 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 104 | `PROTOTYPECOPYCONTEXT` | INTEGER | NOT NULL |  |  |  |
| 105 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 106 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 107 | `ORIGINPROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 108 | `ORIGINPROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 109 | `ORIGINSUFFIX` | CHAR(20) |  |  |  |  |
| 110 | `PROTOTYPEREF` | SMALLINT | NOT NULL |  |  |  |
| 111 | `PROTOTYPECOPY` | SMALLINT | NOT NULL |  |  |  |
| 112 | `ORIGINPROTOTYPE` | CHAR(20) |  |  |  |  |
| 113 | `ORIGINSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 114 | `PRODUCTUNIQUEID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `BILLOFMATERIALBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `BILLOFMATERIALBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.NUMBERID,
       t.ITEMTYPECODE,
       t.BOMSUBCODE01,
       t.SUBCODE01,
       t.VIRTUALRETURNSUBCODE,
       t.BOMSUBCODE02,
       t.SUBCODE02
FROM   DB2ADMIN.BILLOFMATERIALBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
