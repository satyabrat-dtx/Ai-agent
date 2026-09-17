# DB2ADMIN.LOGGENERALLEDGERACCOUNT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 92
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 102477

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `CODE` | CHAR(10) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `ACCOUNTTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 8 | `ACCOUNTUSAGE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `TAXTREATMENT` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `SECURITYLEVELSYSTEMTABLECODE` | CHAR(5) |  |  |  |  |
| 11 | `SECURITYLEVELCODE` | CHAR(10) |  |  |  |  |
| 12 | `FIRSTGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 13 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 14 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 15 | `SECONDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 16 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 17 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 18 | `THIRDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 19 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 20 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 21 | `FOURTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 22 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 23 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 24 | `FIFTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 25 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 26 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 27 | `INITIALDATE` | DATE |  |  |  |  |
| 28 | `FINALDATE` | DATE |  |  |  |  |
| 29 | `INACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 30 | `TEXT` | VARCHAR(140) |  |  |  |  |
| 31 | `OPENITEMMAIN` | SMALLINT | NOT NULL |  |  |  |
| 32 | `SALESRELEVANT` | SMALLINT | NOT NULL |  |  |  |
| 33 | `ACCOUNTASSIGNMENTTEXTMANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 34 | `NOFOREIGNCURRENCYVALUATION` | SMALLINT | NOT NULL |  |  |  |
| 35 | `TAXCODECODE` | CHAR(5) |  |  |  |  |
| 36 | `TAXCODEMANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 37 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 38 | `CURRENCYMANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 39 | `ACCOUNTGROUPSTANDARDTABLECODE` | CHAR(5) |  |  |  |  |
| 40 | `ACCOUNTGROUPCODE` | CHAR(10) |  |  |  |  |
| 41 | `INTERESTGROUPSTANDARDTABLECODE` | CHAR(5) |  |  |  |  |
| 42 | `INTERESTGROUPCODE` | CHAR(10) |  |  |  |  |
| 43 | `ADRESSNUMBERNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 44 | `GROUPACCOUNT` | CHAR(10) |  |  |  |  |
| 45 | `CHECKCODECOSTCENTER` | CHAR(1) |  |  |  |  |
| 46 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 47 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 48 | `CHECKCODECOSTUNIT` | CHAR(1) |  |  |  |  |
| 49 | `COSTUNITCODE` | CHAR(20) |  |  |  |  |
| 50 | `CHECKCODEASSET` | CHAR(1) |  |  |  |  |
| 51 | `ASSETCODE` | CHAR(20) |  |  |  |  |
| 52 | `CHECKCODEPROFITCENTER` | CHAR(1) |  |  |  |  |
| 53 | `PROFITCENTERCODE` | CHAR(3) |  |  |  |  |
| 54 | `CHECKCODEWAREHOUSE` | CHAR(1) |  |  |  |  |
| 55 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 56 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 57 | `COSTTYPE` | CHAR(1) |  |  |  |  |
| 58 | `COSTTYPEPERC` | INTEGER | NOT NULL |  |  |  |
| 59 | `COSTELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 60 | `COSTELEMENTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 61 | `COSTELEMENTSUBCODE01` | CHAR(20) |  |  |  |  |
| 62 | `BALFIRSTLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 63 | `BALFIRSTCODE` | CHAR(4) |  |  |  |  |
| 64 | `BALSECONDLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 65 | `BALSECONDCODE` | CHAR(4) |  |  |  |  |
| 66 | `PLOFIRSTLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 67 | `PLOFIRSTCODE` | CHAR(4) |  |  |  |  |
| 68 | `PLOSECONDLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 69 | `PLOSECONDCODE` | CHAR(4) |  |  |  |  |
| 70 | `BABFIRSTLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 71 | `BABFIRSTCODE` | CHAR(4) |  |  |  |  |
| 72 | `BABSECONDLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 73 | `BABSECONDCODE` | CHAR(4) |  |  |  |  |
| 74 | `BWAFIRSTLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 75 | `BWAFIRSTCODE` | CHAR(4) |  |  |  |  |
| 76 | `BWASECONDLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 77 | `BWASECONDCODE` | CHAR(4) |  |  |  |  |
| 78 | `OTHFIRSTLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 79 | `OTHFIRSTCODE` | CHAR(4) |  |  |  |  |
| 80 | `OTHSECONDLINEREPORTCODE` | CHAR(3) |  |  |  |  |
| 81 | `OTHSECONDCODE` | CHAR(4) |  |  |  |  |
| 82 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 83 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 84 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 85 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 86 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 87 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 88 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 89 | `LOGUSER` | CHAR(25) |  |  | audit | User responsible for the audited change (change-log table). |
| 90 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 91 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGGENERALLEDGERACCOUNT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ACCOUNTTYPE,
       t.ACCOUNTUSAGE,
       t.TAXTREATMENT,
       t.SECURITYLEVELSYSTEMTABLECODE,
       t.SECURITYLEVELCODE
FROM   DB2ADMIN.LOGGENERALLEDGERACCOUNT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
