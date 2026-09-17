# DB2ADMIN.LOGSTOCKTRANSACTIONTEMPLATE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 115
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 209123

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `CODE` | CHAR(3) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `STOCKTRANSACTIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `ONHANDUPDATE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `ADJUSTQUANTITY` | SMALLINT | NOT NULL |  |  |  |
| 11 | `ALLOWITEMELEMENTPARTIALISSUE` | SMALLINT | NOT NULL |  |  |  |
| 12 | `TRANSFERELEMENTALLOCATIONCHECK` | SMALLINT | NOT NULL |  |  |  |
| 13 | `HEADERONLYPRIMARYKEY` | SMALLINT | NOT NULL |  |  |  |
| 14 | `RETURNTRANSACTION` | SMALLINT | NOT NULL |  |  |  |
| 15 | `INTERCOMPANYUSE` | INTEGER | NOT NULL |  |  |  |
| 16 | `PORTFOLIOCONTROL` | SMALLINT | NOT NULL |  |  |  |
| 17 | `EXISTENTLOTSLOADING` | CHAR(2) |  |  |  |  |
| 18 | `LOTRECEIVEDQUANTITYUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 19 | `PURCHASEORDERREOPEN` | SMALLINT | NOT NULL |  |  |  |
| 20 | `IMMEDIATEAVAILABILITYCONTROL` | CHAR(2) | NOT NULL |  |  |  |
| 21 | `STOCKTRANSACTIONAVCHECKCODE` | CHAR(20) |  |  |  |  |
| 22 | `AVAILABILITYFORMULACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `AVAILABILITYFORMULACODE` | CHAR(3) |  |  |  |  |
| 24 | `PRINTONREGISTER` | SMALLINT | NOT NULL |  |  |  |
| 25 | `REUSEELEMENTS` | SMALLINT | NOT NULL |  |  |  |
| 26 | `ELEMENTSTATUSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 27 | `ELEMENTSTATUSCODE` | CHAR(3) |  |  |  |  |
| 28 | `TMPGRPSTDGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `TMPGROUPSTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 30 | `TEMPLATEGROUPCODE` | CHAR(3) |  |  |  |  |
| 31 | `CHECKSTOCKTRANSACTIONCODE` | CHAR(20) |  |  |  |  |
| 32 | `CUSTOMSTOCKTRANSACTIONCODE` | CHAR(20) |  |  |  |  |
| 33 | `ENTRYDOCUMENTTOGENERATE` | CHAR(2) | NOT NULL |  |  |  |
| 34 | `PROPROGRESSTMPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 35 | `PRODUCTIONPROGRESSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 36 | `PRDPROGRESSTMPFORUPDCMYCODE` | CHAR(3) |  |  |  |  |
| 37 | `PRDPROGRESSTEMPLATEFORUPDCODE` | CHAR(3) |  |  |  |  |
| 38 | `PERFORMRESERVATIONBACKFLUSH` | CHAR(1) |  |  |  |  |
| 39 | `INTRASTATTRANSACTIONNATURECODE` | CHAR(2) |  |  |  |  |
| 40 | `GENERATEAUTOMATICQATEST` | SMALLINT | NOT NULL |  |  |  |
| 41 | `CONSIDERBASEQUANTITIES` | SMALLINT | NOT NULL |  |  |  |
| 42 | `AUTOCNTELEMENTCREATION` | SMALLINT | NOT NULL |  |  |  |
| 43 | `ITEMDESCRIPTIONREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 44 | `INTERNALDOCUMENTREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 45 | `EXTERNALDOCUMENTREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 46 | `ORDERCODEREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 47 | `CUSTOMERCODEREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 48 | `SUPPLIERCODEREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 49 | `COSTCENTERCODEREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 50 | `PROJECTCODEREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 51 | `STATISTICALGROUPREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 52 | `WEIGHTSREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 53 | `LOCATIONNATUREMANAGEMENT` | CHAR(90) |  |  |  |  |
| 54 | `HISTORYUSEUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 55 | `LASTTRANSACTIONDATEUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 56 | `LASTENTRYDATEUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 57 | `INCREASETRANSACTIONCOUNTER` | SMALLINT | NOT NULL |  |  |  |
| 58 | `LOTCOSTUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 59 | `LOTCOSTFORCLOSUREUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 60 | `LATESTINBOUNDCOSTUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 61 | `DYNAMICAVERAGECOSTUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 62 | `WEIGHTEDAVERAGECOSTUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 63 | `HIFOCOSTUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 64 | `EDITABLEUNITVALUE` | SMALLINT | NOT NULL |  |  |  |
| 65 | `VALUATIONPRIORITY` | DECIMAL(2,0) |  |  |  |  |
| 66 | `PROVISIONALVALUATION` | CHAR(2) | NOT NULL |  |  |  |
| 67 | `CLOSINGVALUATION` | CHAR(2) | NOT NULL |  |  |  |
| 68 | `ITEMDESCRIPTIONMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 69 | `ISSUEPROVVALUATIONUSINGLOTCOST` | SMALLINT | NOT NULL |  |  |  |
| 70 | `ISSUECLOSVALUATIONUSINGLOTCOST` | SMALLINT | NOT NULL |  |  |  |
| 71 | `QUALITYLEVELMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 72 | `DONOTOVERRIDEZEROLOTCOST` | SMALLINT | NOT NULL |  |  |  |
| 73 | `USELOTCOSTFORCLOSURE` | SMALLINT | NOT NULL |  |  |  |
| 74 | `LOCATIONMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 75 | `PURCHASEPRICEVARIANCE` | SMALLINT | NOT NULL |  |  |  |
| 76 | `VALUEADJUSTMENTTRANSACTION` | SMALLINT | NOT NULL |  |  |  |
| 77 | `POSITIVEADJUSTMENTTMPCMYCODE` | CHAR(3) |  |  |  |  |
| 78 | `POSITIVEADJUSTMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 79 | `NEGATIVEADJUSTMENTTMPCMYCODE` | CHAR(3) |  |  |  |  |
| 80 | `NEGATIVEADJUSTMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 81 | `LOTMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 82 | `CONTAINERMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 83 | `CONTAINERELEMENTMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 84 | `INTERNALDOCUMENTMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 85 | `EXTERNALDOCUMENTMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 86 | `ORDERCODEMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 87 | `CUSTOMERCODEMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 88 | `SUPPLIERCODEMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 89 | `COSTCENTERCODEMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 90 | `PROJECTCODEMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 91 | `STATISTICALGROUPMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 92 | `PRIMARYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 93 | `PRIMARYMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 94 | `SECONDARYMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 95 | `PACKAGINGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 96 | `ACTUALCOSTVALUATIONTYPE` | CHAR(1) |  |  |  |  |
| 97 | `SECONDVALUATIONTYPE` | CHAR(1) |  |  |  |  |
| 98 | `ACTUALCOSTVALUATIONCODE` | CHAR(20) |  |  |  |  |
| 99 | `AFFECTSCATEGORYCOSTS` | SMALLINT | NOT NULL |  |  |  |
| 100 | `HASITEMADDITIONALCOSTS` | SMALLINT | NOT NULL |  |  |  |
| 101 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 102 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 103 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 104 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 105 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 106 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 107 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 108 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 109 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 110 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 111 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 112 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 113 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 114 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGSTOCKTRANSACTIONTEMPLATE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.STOCKTRANSACTIONTYPE,
       t.ONHANDUPDATE,
       t.STOCKTYPECODE,
       t.ADJUSTQUANTITY,
       t.ALLOWITEMELEMENTPARTIALISSUE
FROM   DB2ADMIN.LOGSTOCKTRANSACTIONTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
