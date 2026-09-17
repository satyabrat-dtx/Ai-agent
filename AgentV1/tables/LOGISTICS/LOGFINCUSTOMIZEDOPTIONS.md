# DB2ADMIN.LOGFINCUSTOMIZEDOPTIONS

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 76
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 227724

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PROPOSALCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 2 | `PROPOSALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 3 | `INTERBUCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `INTERBUCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 5 | `CHEQUEREASONGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `CHEQUEREASONGRPCODE` | CHAR(3) |  |  |  |  |
| 7 | `MAXLEVELPROPOSALAPPROVAL` | INTEGER | NOT NULL |  |  |  |
| 8 | `MAXLEVELINTERBUAPPROVAL` | INTEGER | NOT NULL |  |  |  |
| 9 | `COMPANYACT` | CHAR(1) | NOT NULL |  |  |  |
| 10 | `FINDOCTEMPLATELOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 11 | `IONIDENTIFICATION` | INTEGER | NOT NULL |  |  |  |
| 12 | `ADVANCEUGG` | INTEGER | NOT NULL |  |  |  |
| 13 | `GLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 14 | `GLCODE` | CHAR(20) |  |  |  |  |
| 15 | `BANKCONTRAGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 16 | `BANKCONTRAGLCODE` | CHAR(20) |  |  |  |  |
| 17 | `EXGRATEAPP` | SMALLINT | NOT NULL |  |  |  |
| 18 | `AUTORECONCILIATIONCODE` | CHAR(20) |  |  |  |  |
| 19 | `RECONCILIATIONSTARTDATE` | DATE |  |  |  |  |
| 20 | `ALLOWOPENFOREXLINE` | SMALLINT | NOT NULL |  |  |  |
| 21 | `REALIZEDFOREXGAINCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 22 | `REALIZEDFOREXGAINCODE` | CHAR(20) |  |  |  |  |
| 23 | `REALIZEDFOREXLOSSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 24 | `REALIZEDFOREXLOSSCODE` | CHAR(20) |  |  |  |  |
| 25 | `CLEARINGBY` | INTEGER | NOT NULL |  |  |  |
| 26 | `FINDOCUMENTLOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 27 | `LOGFORALLENTITIES` | SMALLINT | NOT NULL |  |  |  |
| 28 | `CONTRADOCTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `CONTRADOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 30 | `GAINLOSSDOCTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `GAINLOSSDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 32 | `FIRSTUGRPUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 33 | `FIRSTUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 34 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 35 | `SNDUGRPUGENGRPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 36 | `SNDUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 37 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 38 | `THIRDUGRPUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 39 | `THIRDUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 40 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 41 | `FRUGRPUGENGRPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 42 | `FRUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 43 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 44 | `FIFTHUGRPUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 45 | `FIFTHUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 46 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 47 | `SIXTHUGRPUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 48 | `SIXTHUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 49 | `SIXTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 50 | `SEUGRPUGENGRPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 51 | `SEUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 52 | `SEVENTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 53 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 54 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 55 | `AGENTHANDLING` | CHAR(2) |  |  |  |  |
| 56 | `AGENTCHECKCODE` | CHAR(20) |  |  |  |  |
| 57 | `OBEXCUTEDYEARCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 58 | `OBEXCUTEDYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 59 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 60 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 61 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 62 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 63 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 64 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 65 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 66 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 67 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 68 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 69 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 70 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 71 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 72 | `PERCENTAGE2NDSHIFT` | DECIMAL(5,2) |  |  |  |  |
| 73 | `PERCENTAGE3RDSHIFT` | DECIMAL(5,2) |  |  |  |  |
| 74 | `VALUEDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 75 | `ROUNDINGCRITERIATYPE` | CHAR(2) | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINCUSTOMIZEDOPTIONS.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PROPOSALCOUNTERCOMPANYCODE,
       t.PROPOSALCOUNTERCODE,
       t.INTERBUCOUNTERCOMPANYCODE,
       t.INTERBUCOUNTERCODE,
       t.CHEQUEREASONGRPCOMPANYCODE,
       t.CHEQUEREASONGRPCODE,
       t.MAXLEVELPROPOSALAPPROVAL,
       t.MAXLEVELINTERBUAPPROVAL,
       t.COMPANYACT,
       t.FINDOCTEMPLATELOGMANAGEMENT,
       t.IONIDENTIFICATION
FROM   DB2ADMIN.LOGFINCUSTOMIZEDOPTIONS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
