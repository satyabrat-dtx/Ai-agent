# DB2ADMIN.RECIPEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 114
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 67409

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 5 | `RECIPETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `RECIPETYPE` | CHAR(1) |  |  |  |  |
| 8 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 9 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 19 | `GENERICRECIPE` | SMALLINT | NOT NULL |  |  |  |
| 20 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 21 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 22 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 23 | `REFSUBCODE01` | CHAR(20) |  |  |  |  |
| 24 | `REFSUBCODE02` | CHAR(10) |  |  |  |  |
| 25 | `REFSUBCODE03` | CHAR(10) |  |  |  |  |
| 26 | `REFSUBCODE04` | CHAR(10) |  |  |  |  |
| 27 | `REFSUBCODE05` | CHAR(10) |  |  |  |  |
| 28 | `REFSUBCODE06` | CHAR(10) |  |  |  |  |
| 29 | `REFSUBCODE07` | CHAR(10) |  |  |  |  |
| 30 | `REFSUBCODE08` | CHAR(10) |  |  |  |  |
| 31 | `REFSUBCODE09` | CHAR(10) |  |  |  |  |
| 32 | `REFSUBCODE10` | CHAR(10) |  |  |  |  |
| 33 | `REFRECIPESUFFIXCODE` | CHAR(20) |  |  |  |  |
| 34 | `REFRECIPENUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 35 | `GENERICREFERENCE` | CHAR(20) |  |  |  |  |
| 36 | `VALIDFROMDATE` | DATE |  |  |  |  |
| 37 | `VALIDTODATE` | DATE |  |  |  |  |
| 38 | `MAXNUMBEROFUSES` | INTEGER | NOT NULL |  |  |  |
| 39 | `NUMBEROFUSES` | INTEGER | NOT NULL |  |  |  |
| 40 | `SOLUTIONPASTEUMCODE` | CHAR(3) |  |  |  |  |
| 41 | `SOLUTIONPASTEWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 42 | `RECIPEINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 43 | `SOLUTIONPASTEUMWEIGHTUMCODE` | CHAR(3) |  |  |  |  |
| 44 | `PRODUCTIONUMCODE` | CHAR(3) |  |  |  |  |
| 45 | `PRODUCTIONUMWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 46 | `PRODUCTIONUMWEIGHTUMCODE` | CHAR(3) |  |  |  |  |
| 47 | `BATCHSTANDARDSIZE` | DECIMAL(15,5) |  |  |  |  |
| 48 | `AVERAGELENGTH` | DECIMAL(15,5) |  |  |  |  |
| 49 | `BATCHAVERAGEUMCODE` | CHAR(3) |  |  |  |  |
| 50 | `DILUITIONPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 51 | `PICKUPPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 52 | `DRYRESIDUALPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 53 | `DRYRESIDUALQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 54 | `GLOBALWASTEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 55 | `BATHVOLUME` | DECIMAL(15,5) |  |  |  |  |
| 56 | `RESIDUALBATHVOLUME` | DECIMAL(15,5) |  |  |  |  |
| 57 | `VOLUMEUMCODE` | CHAR(3) |  |  |  |  |
| 58 | `COMPOSITIONCODE` | CHAR(10) |  |  |  |  |
| 59 | `LIQUORRATIO` | DECIMAL(5,2) |  |  |  |  |
| 60 | `MIXVOLUME` | DECIMAL(15,5) |  |  |  |  |
| 61 | `PRODUCTIONRESERVATIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 62 | `BINDERFLUIDSRATIO` | DECIMAL(5,2) |  |  |  |  |
| 63 | `BINDERMINPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 64 | `BINDERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 65 | `BSUBCODE01` | CHAR(20) |  |  |  |  |
| 66 | `BSUBCODE02` | CHAR(10) |  |  |  |  |
| 67 | `BSUBCODE03` | CHAR(10) |  |  |  |  |
| 68 | `BSUBCODE04` | CHAR(10) |  |  |  |  |
| 69 | `BSUBCODE05` | CHAR(10) |  |  |  |  |
| 70 | `BSUBCODE06` | CHAR(10) |  |  |  |  |
| 71 | `BSUBCODE07` | CHAR(10) |  |  |  |  |
| 72 | `BSUBCODE08` | CHAR(10) |  |  |  |  |
| 73 | `BSUBCODE09` | CHAR(10) |  |  |  |  |
| 74 | `BSUBCODE10` | CHAR(10) |  |  |  |  |
| 75 | `FILLERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 76 | `FSUBCODE01` | CHAR(20) |  |  |  |  |
| 77 | `FSUBCODE02` | CHAR(10) |  |  |  |  |
| 78 | `FSUBCODE03` | CHAR(10) |  |  |  |  |
| 79 | `FSUBCODE04` | CHAR(10) |  |  |  |  |
| 80 | `FSUBCODE05` | CHAR(10) |  |  |  |  |
| 81 | `FSUBCODE06` | CHAR(10) |  |  |  |  |
| 82 | `FSUBCODE07` | CHAR(10) |  |  |  |  |
| 83 | `FSUBCODE08` | CHAR(10) |  |  |  |  |
| 84 | `FSUBCODE09` | CHAR(10) |  |  |  |  |
| 85 | `FSUBCODE10` | CHAR(10) |  |  |  |  |
| 86 | `BINDERGROUPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 87 | `BINDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 88 | `FILLERGROUPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 89 | `FILLERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 90 | `STATUS` | CHAR(1) |  |  |  |  |
| 91 | `APPROVALDATE` | DATE |  |  |  |  |
| 92 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 93 | `CREATEHEADER` | CHAR(1) |  |  |  |  |
| 94 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 95 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 96 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 97 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 98 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 99 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 100 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 101 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 102 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 103 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 104 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 105 | `LIMITINPOBYNUMBEROFUSES` | SMALLINT | NOT NULL |  |  |  |
| 106 | `COSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 107 | `USESUBRECIPEHEADERVALUES` | SMALLINT | NOT NULL |  |  |  |
| 108 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 109 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 110 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 111 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 112 | `ARTICLESTATUSCODE` | CHAR(8) |  |  |  |  |
| 113 | `CREATEHEADERVIRTUAL` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RECIPEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.NUMBERID,
       t.RECIPETEMPLATECODE,
       t.ITEMTYPECODE,
       t.RECIPETYPE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04
FROM   DB2ADMIN.RECIPEBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
