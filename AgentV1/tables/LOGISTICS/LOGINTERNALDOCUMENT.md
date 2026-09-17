# DB2ADMIN.LOGINTERNALDOCUMENT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 105
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 51373

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
| 6 | `PROVISIONALCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 7 | `PROVISIONALCODE` | CHAR(15) | NOT NULL |  |  |  |
| 8 | `PROVISIONALDOCUMENTDATE` | DATE | NOT NULL |  |  |  |
| 9 | `DEFINITIVECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 10 | `DEFINITIVECODE` | CHAR(15) |  |  |  |  |
| 11 | `DEFINITIVEDOCUMENTDATE` | DATE |  |  |  |  |
| 12 | `GOODSISSUEDATE` | DATE |  |  |  |  |
| 13 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 14 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 15 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 16 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 17 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 18 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 19 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 20 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 21 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 22 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 23 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 24 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 25 | `DESTINATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 26 | `TERMOFSHIPPINGANDRECEIVINGTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 27 | `DESTINATIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 28 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 29 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 30 | `TERMSOFDELIVERYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 31 | `TERMSOFSHIPPINGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 32 | `APPEARANCEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 33 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 34 | `AREACODE` | CHAR(3) |  |  |  |  |
| 35 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 36 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 37 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 38 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 39 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 40 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 41 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 42 | `TRUCKDRIVERCODE` | CHAR(3) |  |  |  |  |
| 43 | `NUMBERPLATE` | VARCHAR(80) |  |  |  |  |
| 44 | `TRANSPORTSTARTDATE` | DATE |  |  |  |  |
| 45 | `TRANSPORTSTARTTIME` | TIME |  |  |  |  |
| 46 | `NUMBERPARCEL` | DECIMAL(5,0) |  |  |  |  |
| 47 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 48 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 49 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 50 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 51 | `VOLUMEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 52 | `VOLUME` | DECIMAL(15,5) |  |  |  |  |
| 53 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 54 | `STOCKTRANSACTIONCREATED` | SMALLINT | NOT NULL |  |  |  |
| 55 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 56 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 57 | `CURRENTSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 58 | `LINESUSPENDED` | SMALLINT | NOT NULL |  |  |  |
| 59 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 60 | `RECEIVINGSTATUS` | CHAR(2) |  |  |  |  |
| 61 | `PRINTEDDOCUMENT` | SMALLINT | NOT NULL |  |  |  |
| 62 | `ORDERSOURCE` | CHAR(2) | NOT NULL |  |  |  |
| 63 | `PREVIOUSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 64 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 65 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 66 | `INTERNALORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 67 | `INTERNALORDERCODE` | CHAR(15) |  |  |  |  |
| 68 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 69 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 70 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 71 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 72 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 73 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 74 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 75 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 76 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 77 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 78 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 79 | `PROVISIONALCOUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 80 | `DEFINITIVECOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 81 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 82 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 83 | `DESTINATIONWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 84 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 85 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 86 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 87 | `AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 88 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 89 | `TRUCKDRIVERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 90 | `PREVIOUSCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 91 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 92 | `PMWORKORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 93 | `PMWORKORDERCODE` | CHAR(15) |  |  |  |  |
| 94 | `PMMACHINECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 95 | `PMMACHINECODE` | CHAR(15) |  |  |  |  |
| 96 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 97 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 98 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 99 | `DESTPHYSWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 100 | `DESTPHYSWHSCODE` | CHAR(8) |  |  |  |  |
| 101 | `DESTZONECODE` | CHAR(3) |  |  |  |  |
| 102 | `DESTLOCATIONCODE` | CHAR(10) |  |  |  |  |
| 103 | `WFMORDERSTATUS` | INTEGER | NOT NULL |  |  |  |
| 104 | `ORGANIZER` | CHAR(15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGINTERNALDOCUMENT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGINTERNALDOCUMENTBLOCKS`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGINTERNALDOCUMENTLINE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.TEMPLATECODE,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.PROVISIONALCOUNTERCODE,
       t.PROVISIONALCODE,
       t.PROVISIONALDOCUMENTDATE,
       t.DEFINITIVECOUNTERCODE,
       t.DEFINITIVECODE,
       t.DEFINITIVEDOCUMENTDATE
FROM   DB2ADMIN.LOGINTERNALDOCUMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
