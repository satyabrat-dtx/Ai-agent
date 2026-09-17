# DB2ADMIN.ROUTINGBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PRODUCTION` (high confidence — table name starts with 'ROUTING')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 106
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 74940

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
| 7 | `RTGSUBCODE01` | CHAR(20) |  |  |  |  |
| 8 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 9 | `RTGSUBCODE02` | CHAR(10) |  |  |  |  |
| 10 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `RTGSUBCODE03` | CHAR(10) |  |  |  |  |
| 12 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `RTGSUBCODE04` | CHAR(10) |  |  |  |  |
| 14 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `RTGSUBCODE05` | CHAR(10) |  |  |  |  |
| 16 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `RTGSUBCODE06` | CHAR(10) |  |  |  |  |
| 18 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `RTGSUBCODE07` | CHAR(10) |  |  |  |  |
| 20 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `RTGSUBCODE08` | CHAR(10) |  |  |  |  |
| 22 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `RTGSUBCODE09` | CHAR(10) |  |  |  |  |
| 24 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `RTGSUBCODE10` | CHAR(10) |  |  |  |  |
| 26 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 28 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 29 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 30 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 31 | `REFROUTINGSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 32 | `REFROUTINGNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 33 | `PRODUCTIONROUTINGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 34 | `PRODROUTINGSTARTDATE` | DATE |  |  |  |  |
| 35 | `PRODROUTINGENDDATE` | DATE |  |  |  |  |
| 36 | `PRODUCTIONREFERENCEROUTING` | SMALLINT | NOT NULL |  |  |  |
| 37 | `PRODREFROUTINGSTARTDATE` | DATE |  |  |  |  |
| 38 | `PRODREFROUTINGENDDATE` | DATE |  |  |  |  |
| 39 | `COSTCLCROUTINGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 40 | `COSTCALCROUTINGSTARTDATE` | DATE |  |  |  |  |
| 41 | `COSTCALCROUTINGENDDATE` | DATE |  |  |  |  |
| 42 | `TECHNICALROUTINGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 43 | `TECHROUTINGSTARTDATE` | DATE |  |  |  |  |
| 44 | `TECHROUTINGENDDATE` | DATE |  |  |  |  |
| 45 | `PLANNINGROUTINGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 46 | `PLANROUTINGSTARTDATE` | DATE |  |  |  |  |
| 47 | `PLANROUTINGENDDATE` | DATE |  |  |  |  |
| 48 | `BOMTYPECODE` | CHAR(6) |  |  |  |  |
| 49 | `CHECKCODE` | CHAR(2) |  |  |  |  |
| 50 | `USERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 51 | `GENERICREFERENCE` | CHAR(20) |  |  |  |  |
| 52 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 53 | `COSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 54 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 55 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 56 | `ROUTINGUOMTYPE` | CHAR(2) |  |  |  |  |
| 57 | `ROUTINGUOMCODE` | CHAR(3) |  |  |  |  |
| 58 | `STDPRODUCTIONBATCH` | DECIMAL(15,5) |  |  |  |  |
| 59 | `ROUTINGINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 60 | `RTGCOMMENTCRITERIA` | CHAR(2) |  |  |  |  |
| 61 | `RTGCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 62 | `RTGCOMMENTCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 63 | `RTGCOMMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 64 | `STATUS` | CHAR(1) |  |  |  |  |
| 65 | `APPROVALDATE` | DATE |  |  |  |  |
| 66 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 67 | `RELEASEDATE` | DATE |  |  |  |  |
| 68 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 69 | `PRDITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 70 | `PRDSUBCODE01` | CHAR(20) |  |  |  |  |
| 71 | `PRDSUBCODE02` | CHAR(10) |  |  |  |  |
| 72 | `PRDSUBCODE03` | CHAR(10) |  |  |  |  |
| 73 | `PRDSUBCODE04` | CHAR(10) |  |  |  |  |
| 74 | `PRDSUBCODE05` | CHAR(10) |  |  |  |  |
| 75 | `PRDSUBCODE06` | CHAR(10) |  |  |  |  |
| 76 | `PRDSUBCODE07` | CHAR(10) |  |  |  |  |
| 77 | `PRDSUBCODE08` | CHAR(10) |  |  |  |  |
| 78 | `PRDSUBCODE09` | CHAR(10) |  |  |  |  |
| 79 | `PRDSUBCODE10` | CHAR(10) |  |  |  |  |
| 80 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 81 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 82 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 83 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 84 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 85 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 86 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 87 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 88 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 89 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 90 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 91 | `IMPORTEDROUTING` | SMALLINT | NOT NULL |  |  |  |
| 92 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 93 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 94 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 95 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 96 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 97 | `PROTOTYPECOPYCONTEXT` | INTEGER | NOT NULL |  |  |  |
| 98 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 99 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 100 | `ORIGINPROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 101 | `ORIGINPROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 102 | `ORIGINSUFFIX` | CHAR(20) |  |  |  |  |
| 103 | `PROTOTYPEREF` | SMALLINT | NOT NULL |  |  |  |
| 104 | `ORIGINPROTOTYPE` | CHAR(20) |  |  |  |  |
| 105 | `ORIGINSUFFIXCODE` | CHAR(20) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `ROUTINGBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `ROUTINGBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.NUMBERID,
       t.ITEMTYPECODE,
       t.RTGSUBCODE01,
       t.SUBCODE01,
       t.RTGSUBCODE02,
       t.SUBCODE02,
       t.RTGSUBCODE03
FROM   DB2ADMIN.ROUTINGBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
