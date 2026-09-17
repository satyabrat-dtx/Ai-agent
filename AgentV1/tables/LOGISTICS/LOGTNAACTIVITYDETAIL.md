# DB2ADMIN.LOGTNAACTIVITYDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 81
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 194955

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TNAACTIVITYUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 1 | `TNAACTIVITYTNAHDRCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `TNAACTIVITYTNAHEADERCODE` | CHAR(10) | NOT NULL |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `SEQNO` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 5 | `ACTIVITYCODECODE` | CHAR(15) | NOT NULL |  |  |  |
| 6 | `REMARKS` | CHAR(50) |  |  |  |  |
| 7 | `TNASTARTDATE` | TIMESTAMP |  |  |  |  |
| 8 | `TNARECALCULATIONSTARTDATE` | TIMESTAMP |  |  |  |  |
| 9 | `TNAACTUALSTARTDATE` | TIMESTAMP |  |  |  |  |
| 10 | `TNAENDDATE` | TIMESTAMP |  |  |  |  |
| 11 | `TNARECALCULATIONENDDATE` | TIMESTAMP |  |  |  |  |
| 12 | `TNAACTUALENDDATE` | TIMESTAMP |  |  |  |  |
| 13 | `STARTDATE` | DATE |  |  |  |  |
| 14 | `ACTUALSTARTDATE` | DATE |  |  |  |  |
| 15 | `ENDDATE` | DATE |  |  |  |  |
| 16 | `ACTUALENDDATE` | DATE |  |  |  |  |
| 17 | `DURATIONREQD` | INTEGER | NOT NULL |  |  |  |
| 18 | `DURATIONUM` | INTEGER | NOT NULL |  |  |  |
| 19 | `ACTIVITYBASEDONCODE` | CHAR(15) |  |  |  |  |
| 20 | `BASEDONSTEP` | BIGINT | NOT NULL |  |  |  |
| 21 | `BASEDONTNAHEADERCODE` | CHAR(10) |  |  |  |  |
| 22 | `BASEDONSEQNO` | DECIMAL(5,0) |  |  |  |  |
| 23 | `CALENDARCODE` | CHAR(3) |  |  |  |  |
| 24 | `CALENDARCOLOR` | CHAR(16) |  |  |  |  |
| 25 | `SCHEDULEMEETING` | SMALLINT | NOT NULL |  |  |  |
| 26 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 27 | `RECALCULATEATCOMPLETITION` | INTEGER | NOT NULL |  |  |  |
| 28 | `ANNULLED` | SMALLINT | NOT NULL |  |  |  |
| 29 | `TASKMANAGERUSERID` | CHAR(50) |  |  |  |  |
| 30 | `USERRESPNSBLUSERID` | CHAR(50) |  |  |  |  |
| 31 | `MESSAGETYPE` | INTEGER | NOT NULL |  |  |  |
| 32 | `MESSAGETOUSERID` | CHAR(50) |  |  |  |  |
| 33 | `MESSAGEWHEN` | CHAR(90) |  |  |  |  |
| 34 | `SENDMAIL` | SMALLINT | NOT NULL |  |  |  |
| 35 | `MAILSUBJECT` | VARCHAR(255) |  |  |  |  |
| 36 | `MAILTEXT` | CLOB(1000000) |  |  |  |  |
| 37 | `PARENTENTITY` | INTEGER | NOT NULL |  |  |  |
| 38 | `DOCUMENTNUMBER` | VARCHAR(200) |  |  |  |  |
| 39 | `ACTIVITYGROUPCODE` | CHAR(10) |  |  |  |  |
| 40 | `ESCALATIONDURATIONREQD` | INTEGER | NOT NULL |  |  |  |
| 41 | `ESCALATIONDURATIONUM` | INTEGER | NOT NULL |  |  |  |
| 42 | `ESCALATIONUSERRESPNSBLUSERID` | CHAR(50) |  |  |  |  |
| 43 | `NOTIFICATIONPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 44 | `COMPLETITIONPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 45 | `COMPLETEDBYSKU` | SMALLINT | NOT NULL |  |  |  |
| 46 | `OPTIONALTASK` | SMALLINT | NOT NULL |  |  |  |
| 47 | `MANAGELOG` | SMALLINT | NOT NULL |  |  |  |
| 48 | `TOBEPROGRESSED` | SMALLINT | NOT NULL |  |  |  |
| 49 | `ACTIVITYRESULTTYPECODE` | CHAR(3) |  |  |  |  |
| 50 | `RESULTCODE` | CHAR(10) |  |  |  |  |
| 51 | `TASKRESULT` | INTEGER | NOT NULL |  |  |  |
| 52 | `TNADETAILPOLICYCODE` | CHAR(20) |  |  |  |  |
| 53 | `ENTITYENTITY` | CHAR(50) |  |  |  |  |
| 54 | `DECISIONTABLEGROUPFAMILY` | CHAR(15) |  |  |  |  |
| 55 | `DECISIONTABLEREFERENCEDENTITY` | CHAR(50) |  |  |  |  |
| 56 | `DECISIONTABLEDTRPKTOKEN` | CHAR(15) |  |  |  |  |
| 57 | `TNAFROMCOPY` | SMALLINT | NOT NULL |  |  |  |
| 58 | `ISFINAL` | SMALLINT | NOT NULL |  |  |  |
| 59 | `ISINITIAL` | SMALLINT | NOT NULL |  |  |  |
| 60 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 61 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 62 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 63 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 64 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 65 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 66 | `STEP` | BIGINT | NOT NULL |  |  |  |
| 67 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 68 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 69 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 70 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 71 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 72 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 73 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 74 | `UGGMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 75 | `UGGFORREAREQUIREDCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 76 | `UGGFORREASONREQUIREDCODE` | CHAR(3) |  |  |  |  |
| 77 | `UGGCOMPANY` | CHAR(3) |  |  |  |  |
| 78 | `UGGTYPE` | CHAR(3) |  |  |  |  |
| 79 | `UGGCODE` | CHAR(10) |  |  |  |  |
| 80 | `NOTE` | VARCHAR(200) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGTNAACTIVITYDETAIL.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.TNAACTIVITYUNIQUEID,
       t.TNAACTIVITYTNAHDRCOMPANYCODE,
       t.TNAACTIVITYTNAHEADERCODE,
       t.COMPANYCODE,
       t.SEQNO,
       t.ACTIVITYCODECODE,
       t.REMARKS,
       t.TNASTARTDATE,
       t.TNARECALCULATIONSTARTDATE,
       t.TNAACTUALSTARTDATE,
       t.TNAENDDATE,
       t.TNARECALCULATIONENDDATE
FROM   DB2ADMIN.LOGTNAACTIVITYDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
