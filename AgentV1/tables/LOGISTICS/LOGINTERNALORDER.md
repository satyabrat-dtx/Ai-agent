# DB2ADMIN.LOGINTERNALORDER

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 71
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 51762

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 1 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 4 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 5 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 6 | `COUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 7 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 8 | `ORDERDATE` | DATE | NOT NULL |  |  |  |
| 9 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 10 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 11 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 12 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 13 | `DESCRIPTION` | VARCHAR(200) |  |  | description |  |
| 14 | `INITIALDATE` | DATE |  |  |  |  |
| 15 | `FINALDATE` | DATE |  |  |  |  |
| 16 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 17 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 18 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 19 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 20 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 21 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 22 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 23 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 24 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 25 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 26 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 27 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 28 | `AREACODE` | CHAR(3) |  |  |  |  |
| 29 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 30 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 31 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 32 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 33 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 34 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 35 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 36 | `REQUIREDDUEDATE` | DATE |  |  |  |  |
| 37 | `CONFIRMEDDUEDATE` | DATE |  |  |  |  |
| 38 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 39 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 40 | `CURRENTSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 41 | `LINESUSPENDED` | SMALLINT | NOT NULL |  |  |  |
| 42 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 43 | `ORDERSOURCE` | CHAR(2) | NOT NULL |  |  |  |
| 44 | `PREVIOUSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 45 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 46 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 47 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 48 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 49 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 50 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 51 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 52 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 53 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 54 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 55 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 56 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 57 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 58 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 59 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 60 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 61 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 62 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 63 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 64 | `AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 65 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 66 | `PREVIOUSCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 67 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 68 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 69 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 70 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGINTERNALORDER.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGINTERNALORDERASSORTMENT`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGINTERNALORDERBLOCKS`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGINTERNALORDERDELIVERY`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGINTERNALORDERLINE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGINTERNALORDERTEMPLATE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.TEMPLATECODE,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.COUNTERCODE,
       t.CODE,
       t.ORDERDATE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.LIFECYCLECODE,
       t.DELIVERYPOINTUNIQUEID
FROM   DB2ADMIN.LOGINTERNALORDER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
