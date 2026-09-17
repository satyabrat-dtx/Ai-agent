# DB2ADMIN.RECIPETEMPLATEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 110
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 87877

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `CODE` | CHAR(3) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `FIRST` | SMALLINT | NOT NULL |  |  |  |
| 4 | `FROMPRECREATE` | SMALLINT | NOT NULL |  |  |  |
| 5 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 6 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 7 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 8 | `RECIPETYPE` | CHAR(1) |  |  |  |  |
| 9 | `CALCULATEDCONSUMPTIONTYPE` | CHAR(2) |  |  |  |  |
| 10 | `REFERENCERECIPEREQUIRED` | CHAR(2) |  |  |  |  |
| 11 | `COMPONENTTYPE` | CHAR(2) |  |  |  |  |
| 12 | `SOLUTIONPASTEUMCODE` | CHAR(3) |  |  |  |  |
| 13 | `SOLUTIONPASTEWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 14 | `SOLUTIONPASTEWEIGHTUMCODE` | CHAR(3) |  |  |  |  |
| 15 | `WATERMANAGEMENTFORCOMPONENT` | SMALLINT | NOT NULL |  |  |  |
| 16 | `WATERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 17 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 18 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `REFERENCETYPEREQUIRED` | CHAR(2) |  |  |  |  |
| 28 | `CHECKCODE` | CHAR(2) |  |  |  |  |
| 29 | `USERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 30 | `HOLDRECIPETYPE` | CHAR(1) |  |  |  |  |
| 31 | `GROUPSTRUCTUREHANDLED` | CHAR(2) |  |  |  |  |
| 32 | `CHECKGROUPCODE` | CHAR(3) |  |  |  |  |
| 33 | `REACTIVEDYEING` | CHAR(2) |  |  |  |  |
| 34 | `DYESTUFFCHEMICALRATIO` | DECIMAL(5,2) |  |  |  |  |
| 35 | `ALKALIRATIO` | DECIMAL(5,2) |  |  |  |  |
| 36 | `HOLDBINDERTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 37 | `HOLDBINDERTYPECODE` | CHAR(3) |  |  |  |  |
| 38 | `HANDLEPRODUCTIONUM` | CHAR(2) |  |  |  |  |
| 39 | `HOLDFILLERTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 40 | `HOLDFILLERTYPECODE` | CHAR(3) |  |  |  |  |
| 41 | `BATCHSTANDARDSIZE` | CHAR(2) |  |  |  |  |
| 42 | `HOLDWATERTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 43 | `HOLDWATERTYPECODE` | CHAR(3) |  |  |  |  |
| 44 | `HANDLEAVERAGELENGTH` | CHAR(2) |  |  |  |  |
| 45 | `PRODUCTIONUMWEIGHT` | CHAR(2) |  |  |  |  |
| 46 | `PICKUPPERCENTAGE` | CHAR(2) |  |  |  |  |
| 47 | `DRYRESIDUALPERCENTAGE` | CHAR(2) |  |  |  |  |
| 48 | `DRYRESIDUALQUANTITY` | CHAR(2) |  |  |  |  |
| 49 | `GLOBALWASTEPERCENTAGE` | CHAR(2) |  |  |  |  |
| 50 | `RESIDUALBATHVOLUME` | CHAR(2) |  |  |  |  |
| 51 | `BATHVOLUME` | CHAR(2) |  |  |  |  |
| 52 | `LIQUORRATIO` | CHAR(2) |  |  |  |  |
| 53 | `DILUITIONPERCENTAGE` | CHAR(2) |  |  |  |  |
| 54 | `COMPONENTCONSUMPTIONRULL` | CHAR(2) |  |  |  |  |
| 55 | `COMPONENTCONSUMPTIONTYPE` | CHAR(2) |  |  |  |  |
| 56 | `QUANTITYFORSTEPWEIGHT` | CHAR(2) |  |  |  |  |
| 57 | `QUANTITYFORSTEPLENGTH` | CHAR(2) |  |  |  |  |
| 58 | `CALCULATIONFORMULACODE` | CHAR(20) |  |  |  |  |
| 59 | `MIXVOLUME` | CHAR(2) |  |  |  |  |
| 60 | `CONSUMPTIONTITLE` | CHAR(20) |  |  |  |  |
| 61 | `CONSUMPTIONTYPETITLE` | CHAR(15) |  |  |  |  |
| 62 | `WATERLINECOLORCOLOR` | CHAR(30) |  |  |  |  |
| 63 | `EXPLOSIONLINECOLORCOLOR` | CHAR(30) |  |  |  |  |
| 64 | `HANDLETOTALLINE` | CHAR(2) |  |  |  |  |
| 65 | `TOTALLINEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 66 | `TOTALLINECOLORCOLOR` | CHAR(30) |  |  |  |  |
| 67 | `TOTALLINEUMCODE` | CHAR(3) |  |  |  |  |
| 68 | `HANDLEBINDERINHEADER` | CHAR(2) |  |  |  |  |
| 69 | `BINDERMINPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 70 | `BINDERFLUIDSRATIO` | DECIMAL(5,2) |  |  |  |  |
| 71 | `BINDERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 72 | `BSUBCODE01` | CHAR(20) |  |  |  |  |
| 73 | `BSUBCODE02` | CHAR(10) |  |  |  |  |
| 74 | `BSUBCODE03` | CHAR(10) |  |  |  |  |
| 75 | `BSUBCODE04` | CHAR(10) |  |  |  |  |
| 76 | `BSUBCODE05` | CHAR(10) |  |  |  |  |
| 77 | `BSUBCODE06` | CHAR(10) |  |  |  |  |
| 78 | `BSUBCODE07` | CHAR(10) |  |  |  |  |
| 79 | `BSUBCODE08` | CHAR(10) |  |  |  |  |
| 80 | `BSUBCODE09` | CHAR(10) |  |  |  |  |
| 81 | `BSUBCODE10` | CHAR(10) |  |  |  |  |
| 82 | `HANDLEFILLERINHEADER` | CHAR(2) |  |  |  |  |
| 83 | `DIRTYFIELD` | CHAR(20) |  |  |  |  |
| 84 | `FILLERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 85 | `FSUBCODE01` | CHAR(20) |  |  |  |  |
| 86 | `FSUBCODE02` | CHAR(10) |  |  |  |  |
| 87 | `FSUBCODE03` | CHAR(10) |  |  |  |  |
| 88 | `FSUBCODE04` | CHAR(10) |  |  |  |  |
| 89 | `FSUBCODE05` | CHAR(10) |  |  |  |  |
| 90 | `FSUBCODE06` | CHAR(10) |  |  |  |  |
| 91 | `FSUBCODE07` | CHAR(10) |  |  |  |  |
| 92 | `FSUBCODE08` | CHAR(10) |  |  |  |  |
| 93 | `FSUBCODE09` | CHAR(10) |  |  |  |  |
| 94 | `FSUBCODE10` | CHAR(10) |  |  |  |  |
| 95 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 96 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 97 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 98 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 99 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 100 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 101 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 102 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 103 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 104 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 105 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 106 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 107 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 108 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 109 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RECIPETEMPLATEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.CODE,
       t.FIRST,
       t.FROMPRECREATE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.RECIPETYPE,
       t.CALCULATEDCONSUMPTIONTYPE,
       t.REFERENCERECIPEREQUIRED,
       t.COMPONENTTYPE
FROM   DB2ADMIN.RECIPETEMPLATEBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
