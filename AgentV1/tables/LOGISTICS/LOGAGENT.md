# DB2ADMIN.LOGAGENT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 65
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 52475

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
| 7 | `COMMISSIONLIQUIDATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 8 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 9 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 10 | `COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 11 | `ADDRESSLINE1` | VARCHAR(150) |  |  |  |  |
| 12 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 13 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 14 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 15 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 16 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 17 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 18 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 19 | `TRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 20 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 21 | `ADDRESSFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 22 | `PERSON` | VARCHAR(200) |  |  |  |  |
| 23 | `ROLEINTHECOMPANY` | VARCHAR(200) |  |  |  |  |
| 24 | `PHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 25 | `FAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 26 | `EMAILADDRESS` | VARCHAR(200) |  |  |  |  |
| 27 | `BOOKLINE01` | VARCHAR(200) |  |  |  |  |
| 28 | `BOOKLINE02` | VARCHAR(200) |  |  |  |  |
| 29 | `BOOKLINE03` | VARCHAR(200) |  |  |  |  |
| 30 | `BOOKLINE04` | VARCHAR(200) |  |  |  |  |
| 31 | `BOOKLINE05` | VARCHAR(200) |  |  |  |  |
| 32 | `DOCUMENTTYPEFORMAIL` | CHAR(90) |  |  |  |  |
| 33 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 34 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 35 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 36 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 37 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 38 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 39 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 40 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 41 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 42 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 43 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 44 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 45 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 46 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 47 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 48 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 49 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 50 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 51 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 52 | `FIRSTGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 53 | `SECONDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 54 | `THIRDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 55 | `FOURTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 56 | `FIFTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 57 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 58 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 59 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 60 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 61 | `SALESAGENTTYPECODE` | CHAR(2) |  |  |  |  |
| 62 | `PAYMENTLIQUIDATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 63 | `INVOICELIQUIDATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 64 | `ENASARCOPOSITION` | CHAR(20) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGAGENT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.COMMISSIONLIQUIDATIONTYPE,
       t.SUPPLIERTYPE,
       t.SUPPLIERCODE,
       t.COUNTRYCODE,
       t.ADDRESSLINE1
FROM   DB2ADMIN.LOGAGENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
