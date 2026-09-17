# DB2ADMIN.LOGPRODUCTIONRESERVATIONGROUP

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 83
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 206739

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `ITEMNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `COMPONENTTYPE` | CHAR(2) |  |  |  |  |
| 7 | `ISSUETRANSACTIONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `ISSUETRANSACTIONCODE` | CHAR(3) |  |  |  |  |
| 9 | `RETURNTRANSACTIONCODE` | CHAR(3) |  |  |  |  |
| 10 | `ENTRYTRANSACTIONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `ENTRYTRANSACTIONCODE` | CHAR(3) |  |  |  |  |
| 12 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 13 | `ISSUEDATECRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 14 | `PERIODRESCREATIONTYPECODE` | CHAR(3) |  |  |  |  |
| 15 | `RESERVATIONSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 16 | `PLANNEDSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 17 | `STOCKTYPEFIRSTEVOLUTIONCODE` | CHAR(3) |  |  |  |  |
| 18 | `STOCKTYPESECONDEVOLUTIONCODE` | CHAR(3) |  |  |  |  |
| 19 | `STOCKTYPETHIRDEVOLUTIONCODE` | CHAR(3) |  |  |  |  |
| 20 | `STOCKTYPEFOURTHEVOLUTIONCODE` | CHAR(3) |  |  |  |  |
| 21 | `EXTISSUERESSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 22 | `EXTENTRYRESSTOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 23 | `STEPDATETOUSEFORISSUEDATE` | INTEGER | NOT NULL |  |  |  |
| 24 | `IMMEDIATEAVAILABILITYCHECK` | CHAR(2) | NOT NULL |  |  |  |
| 25 | `ALTERNATIVEITEMCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 26 | `RESERVATIONINORDERGROUPED` | SMALLINT | NOT NULL |  |  |  |
| 27 | `ACCEPTDIFFERENTCONSUPTION` | SMALLINT | NOT NULL |  |  |  |
| 28 | `REQUISITIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 29 | `ISSUETYPE` | CHAR(5) | NOT NULL |  |  |  |
| 30 | `AUTOMATICISSUEQTYTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 31 | `AUTOMATICCLOSURE` | CHAR(2) | NOT NULL |  |  |  |
| 32 | `SUMMARIZEDISSUEQUANTITY` | CHAR(2) | NOT NULL |  |  |  |
| 33 | `SUMMARIZEDTYPE` | CHAR(2) |  |  |  |  |
| 34 | `RESERVATIONRECALCULATETYPE` | CHAR(2) |  |  |  |  |
| 35 | `TRYCALCRESDATEOVERLAP` | SMALLINT | NOT NULL |  |  |  |
| 36 | `PROGRESSTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 37 | `PROGRESSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 38 | `AUTOMATICRECALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 39 | `EDITABLERESERVATIONITEM` | CHAR(2) | NOT NULL |  |  |  |
| 40 | `EDITABLERESERVATIONWAREHOUSE` | CHAR(2) | NOT NULL |  |  |  |
| 41 | `EDITABLERESERVATIONQTY` | CHAR(2) | NOT NULL |  |  |  |
| 42 | `ALLOCATIONMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 43 | `ALLOCATIONTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 44 | `ALLOCATIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 45 | `EXTERNALALLTMPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 46 | `EXTERNALALLOCATIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 47 | `CLOSEASSOCIATEDALLOCATIONS` | SMALLINT | NOT NULL |  |  |  |
| 48 | `AVLWAREHOUSEGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 49 | `AVAILABILITYWAREHOUSEGROUPCODE` | CHAR(3) |  |  |  |  |
| 50 | `ORIGINALLOCATIONWAREHOUSE` | SMALLINT | NOT NULL |  |  |  |
| 51 | `ALLQUANTITYTOMODIFY` | CHAR(2) |  |  |  |  |
| 52 | `ALLOCATIONBALANCEDETAIL` | CHAR(2) |  |  |  |  |
| 53 | `CHANGEALLOCATIONQTY` | CHAR(2) | NOT NULL |  |  |  |
| 54 | `CHANGEALLOCATIONLOCATION` | CHAR(2) | NOT NULL |  |  |  |
| 55 | `CHANGEALLOCATIONWAREHOUSE` | CHAR(2) | NOT NULL |  |  |  |
| 56 | `CHANGEALLOCATIONCONTAINER` | CHAR(2) | NOT NULL |  |  |  |
| 57 | `CHANGEALLOCATIONITEM` | CHAR(2) | NOT NULL |  |  |  |
| 58 | `CHANGEALLOCATIONLOT` | CHAR(2) | NOT NULL |  |  |  |
| 59 | `CHANGEALLOCATIONELEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 60 | `CHECKRESERVATIONCODE` | CHAR(20) |  |  |  |  |
| 61 | `CUSTOMERMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 62 | `PROJECTMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 63 | `STATISTICALGROUPMANAGEMENT` | CHAR(2) | NOT NULL |  |  |  |
| 64 | `SPLITTINGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 65 | `SPLITPOLICYCODE` | CHAR(20) |  |  |  |  |
| 66 | `PERIODICQTYRULECODE` | CHAR(10) |  |  |  |  |
| 67 | `BACKFLUSHCODE` | CHAR(20) |  |  |  |  |
| 68 | `ALTERNATIVERESERVATIONRULECODE` | CHAR(20) |  |  |  |  |
| 69 | `KEEPORIGINALLINK` | SMALLINT | NOT NULL |  |  |  |
| 70 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 71 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 72 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 73 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 74 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 75 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 76 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 77 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 78 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 79 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 80 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 81 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 82 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGPRODUCTIONRESERVATIONGROUP.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ITEMNATURE,
       t.COMPONENTTYPE,
       t.ISSUETRANSACTIONCOMPANYCODE,
       t.ISSUETRANSACTIONCODE,
       t.RETURNTRANSACTIONCODE,
       t.ENTRYTRANSACTIONCOMPANYCODE,
       t.ENTRYTRANSACTIONCODE
FROM   DB2ADMIN.LOGPRODUCTIONRESERVATIONGROUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
