# DB2ADMIN.LOGEXTOPDOCUMENT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 76
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 210991

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 4 | `PROVCOUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `PROVCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 6 | `PROVISIONALCODE` | CHAR(15) | NOT NULL |  |  |  |
| 7 | `PROVISIONALDOCUMENTDATE` | DATE | NOT NULL |  |  |  |
| 8 | `DEFINITIVECOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 9 | `DEFINITIVECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 10 | `DEFINITIVECODE` | CHAR(15) |  |  |  |  |
| 11 | `DEFINITIVEDOCUMENTDATE` | DATE |  |  |  |  |
| 12 | `GOODSISSUEDATE` | DATE |  |  |  |  |
| 13 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 14 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 15 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 16 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 17 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 18 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 19 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 20 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 21 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 22 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 23 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 24 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 25 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 27 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 28 | `TERMSOFDELIVERYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 29 | `TERMSOFSHIPPINGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 30 | `APPEARANCEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 31 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 32 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 33 | `AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 34 | `AREACODE` | CHAR(3) |  |  |  |  |
| 35 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 36 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 37 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 38 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 39 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 40 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 41 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 42 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 43 | `TRUCKDRIVERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 44 | `TRUCKDRIVERCODE` | CHAR(3) |  |  |  |  |
| 45 | `NUMBERPLATE` | VARCHAR(80) |  |  |  |  |
| 46 | `TRANSPORTSTARTDATE` | DATE |  |  |  |  |
| 47 | `TRANSPORTSTARTTIME` | TIME |  |  |  |  |
| 48 | `NUMBERPARCEL` | DECIMAL(5,0) |  |  |  |  |
| 49 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 50 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 51 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 52 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 53 | `VOLUMEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 54 | `VOLUME` | DECIMAL(15,5) |  |  |  |  |
| 55 | `CURRENTSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 56 | `LINESUSPENDED` | SMALLINT | NOT NULL |  |  |  |
| 57 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 58 | `RECEIVINGSTATUS` | CHAR(2) |  |  |  |  |
| 59 | `PRINTEDDOCUMENT` | SMALLINT | NOT NULL |  |  |  |
| 60 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 61 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 62 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 63 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 64 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 65 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 66 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 67 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 68 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 69 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 70 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 71 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 72 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 73 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 74 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 75 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGEXTOPDOCUMENT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGEXTOPDOCUMENTLINE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGEXTOPDOCUMENTCOMMENT`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.ORDERTYPE,
       t.PROVCOUNTERCOMPANYCODE,
       t.PROVCOUNTERCODE,
       t.PROVISIONALCODE,
       t.PROVISIONALDOCUMENTDATE,
       t.DEFINITIVECOUNTERCOMPANYCODE,
       t.DEFINITIVECOUNTERCODE,
       t.DEFINITIVECODE,
       t.DEFINITIVEDOCUMENTDATE
FROM   DB2ADMIN.LOGEXTOPDOCUMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
