# DB2ADMIN.ROUTINGSTEPBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PRODUCTION` (high confidence — table name starts with 'ROUTING')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 74
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 45454

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `OWNEDSTEP` | CHAR(2) |  |  |  |  |
| 3 | `ROUTINGITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `ROUTINGSUBCODE01` | CHAR(20) |  |  |  |  |
| 5 | `ROUTINGSUBCODE02` | CHAR(10) |  |  |  |  |
| 6 | `ROUTINGSUBCODE03` | CHAR(10) |  |  |  |  |
| 7 | `ROUTINGSUBCODE04` | CHAR(10) |  |  |  |  |
| 8 | `ROUTINGSUBCODE05` | CHAR(10) |  |  |  |  |
| 9 | `ROUTINGSUBCODE06` | CHAR(10) |  |  |  |  |
| 10 | `ROUTINGSUBCODE07` | CHAR(10) |  |  |  |  |
| 11 | `ROUTINGSUBCODE08` | CHAR(10) |  |  |  |  |
| 12 | `ROUTINGSUBCODE09` | CHAR(10) |  |  |  |  |
| 13 | `ROUTINGSUBCODE10` | CHAR(10) |  |  |  |  |
| 14 | `ROUTINGSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 15 | `SEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 16 | `SUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 17 | `STEPINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 18 | `REFROUTINGSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 19 | `REFROUTINGSUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 20 | `REFROUTINGSTATUS` | CHAR(2) |  |  |  |  |
| 21 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 22 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 23 | `WORKCENTERANDOPERATTRIBUTESCOD` | CHAR(20) |  |  |  |  |
| 24 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 25 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 26 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 27 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 28 | `INITIALIZEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 29 | `STANDARDSTEPQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `STANDARDSTEPQTYUOMCODE` | CHAR(3) |  |  |  |  |
| 31 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 32 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 33 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 39 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 40 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 41 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 42 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 43 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 44 | `PRERULECODE` | CHAR(10) |  |  |  |  |
| 45 | `RULECODE` | CHAR(10) |  |  |  |  |
| 46 | `RULEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 47 | `OVERLAPPINGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 48 | `OVERLAPPINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `OVERLAPPINGUOMCATEGORY` | CHAR(1) |  |  |  |  |
| 50 | `INITIALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 51 | `FINALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 52 | `INITIALDATE` | DATE |  |  |  |  |
| 53 | `FINALDATE` | DATE |  |  |  |  |
| 54 | `ROUTINGUOMTYPE` | CHAR(2) |  |  |  |  |
| 55 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 56 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 57 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 58 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 59 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 60 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 61 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 62 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 63 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 64 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 65 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 66 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 67 | `FORCEDIRTYSEQUENCEDRULES` | SMALLINT | NOT NULL |  |  |  |
| 68 | `PROVISIONAL` | SMALLINT | NOT NULL |  |  |  |
| 69 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 70 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 71 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 72 | `RULEAPPLICABILITY` | INTEGER | NOT NULL |  |  |  |
| 73 | `PROTOTYPEBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **ROUTING**.`ABSUNIQUEID` (high confidence — name = 'ROUTING' + known child suffix 'STEP')
  - JOIN predicate: `ROUTINGSTEPBEAN.FATHERID = ROUTING.ABSUNIQUEID`

## Indexes

- `ROUTINGSTEPBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.OWNEDSTEP,
       t.ROUTINGITEMTYPECODE,
       t.ROUTINGSUBCODE01,
       t.ROUTINGSUBCODE02,
       t.ROUTINGSUBCODE03,
       t.ROUTINGSUBCODE04,
       t.ROUTINGSUBCODE05,
       t.ROUTINGSUBCODE06,
       t.ROUTINGSUBCODE07,
       t.ROUTINGSUBCODE08
FROM   DB2ADMIN.ROUTINGSTEPBEAN t
FETCH FIRST 100 ROWS ONLY;
```
