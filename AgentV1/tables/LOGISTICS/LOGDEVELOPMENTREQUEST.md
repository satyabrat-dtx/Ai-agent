# DB2ADMIN.LOGDEVELOPMENTREQUEST

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 96
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 216104

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 1 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 4 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `COUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 6 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 7 | `EXISTINGCUSTOMER` | SMALLINT | NOT NULL |  |  |  |
| 8 | `CSMCODECUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 9 | `CSMCODECUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 10 | `CUSTOMERLEGALNAME1` | VARCHAR(270) | NOT NULL |  |  |  |
| 11 | `CUSTOMERPERSON` | CHAR(100) |  |  |  |  |
| 12 | `CUSTOMEREMAILADDRESS` | CHAR(100) |  |  |  |  |
| 13 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 14 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 15 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 16 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 17 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 18 | `DRDATE` | DATE | NOT NULL |  |  |  |
| 19 | `TYPE` | CHAR(2) | NOT NULL |  |  |  |
| 20 | `GRAPHICSCHANGES` | SMALLINT | NOT NULL |  |  |  |
| 21 | `PACKAGINGCHANGES` | SMALLINT | NOT NULL |  |  |  |
| 22 | `NEWPRODUCT` | SMALLINT | NOT NULL |  |  |  |
| 23 | `QAREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 24 | `REPLACEITEM` | SMALLINT | NOT NULL |  |  |  |
| 25 | `REASTDGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `REASONSTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 27 | `REASONCODE` | CHAR(3) |  |  |  |  |
| 28 | `APPEARANCESTDGRPTYPECMYCODE` | CHAR(3) |  |  |  |  |
| 29 | `APPEARANCESTDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 30 | `APPEARANCECODE` | CHAR(3) |  |  |  |  |
| 31 | `PRIORITY` | INTEGER | NOT NULL |  |  |  |
| 32 | `REQUESTORIGIN` | INTEGER | NOT NULL |  |  |  |
| 33 | `DEVELOPMENTNOTE` | VARCHAR(200) |  |  |  |  |
| 34 | `DELIVERYDATEREQUESTED` | DATE |  |  |  |  |
| 35 | `DELIVERYDATECONFIRMED` | DATE |  |  |  |  |
| 36 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 37 | `STATUSLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 38 | `STATUSLASTUPDATEDATE` | DATE |  |  |  |  |
| 39 | `APPROVALNOTE` | VARCHAR(500) |  |  |  |  |
| 40 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 41 | `PROJECTLEADERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 42 | `PROJECTLEADERCODE` | CHAR(50) |  |  |  |  |
| 43 | `SALESMANAGERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 44 | `SALESMANAGERCODE` | CHAR(50) |  |  |  |  |
| 45 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 46 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 47 | `CUSTOMERUNITPRICE` | DECIMAL(18,5) |  |  |  |  |
| 48 | `UNITPRICE` | DECIMAL(18,5) |  |  |  |  |
| 49 | `ESTIMATEDCOST` | DECIMAL(18,5) |  |  |  |  |
| 50 | `CALCULATEDCOST` | DECIMAL(18,5) |  |  |  |  |
| 51 | `FIRSTGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 52 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 53 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 54 | `SECONDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 55 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 56 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 57 | `THIRDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 58 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 59 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 60 | `FOURTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 61 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 62 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 63 | `FIFTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 64 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 65 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 66 | `STATISTICALGROUPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 67 | `STATISTICALGROUPINGCODE` | CHAR(6) |  |  |  |  |
| 68 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 69 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 70 | `PLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 71 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 72 | `BRANDCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 73 | `BRANDCODE` | CHAR(10) |  |  |  |  |
| 74 | `DEVELOPMENTGROUPCODE` | CHAR(10) |  |  |  |  |
| 75 | `SAMPLEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 76 | `CUTQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 77 | `SAMPLEUOMCODE` | CHAR(3) |  |  |  |  |
| 78 | `SAMPLEREFERENCE` | VARCHAR(500) |  |  |  |  |
| 79 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 80 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 81 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 82 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 83 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 84 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 85 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 86 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 87 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 88 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 89 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 90 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 91 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 92 | `STRUCTURALCHANGES` | SMALLINT | NOT NULL |  |  |  |
| 93 | `APPROVALREASTDGRPTYPECMYCODE` | CHAR(3) |  |  |  |  |
| 94 | `APPROVALREASTDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 95 | `APPROVALREASONCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGDEVELOPMENTREQUEST.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGDEVELOPMENTREQUESTDETAIL`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.TEMPLATECODE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.EXISTINGCUSTOMER,
       t.CSMCODECUSTOMERSUPPLIERTYPE,
       t.CSMCODECUSTOMERSUPPLIERCODE,
       t.CUSTOMERLEGALNAME1,
       t.CUSTOMERPERSON
FROM   DB2ADMIN.LOGDEVELOPMENTREQUEST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
