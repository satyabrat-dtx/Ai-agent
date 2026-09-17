# DB2ADMIN.LOGPRODUCTIONPROGRESSTEMPLATE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 66
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 216306

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `PROGRESSTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `PROGRESSTMPGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 7 | `PROGRESSTEMPLATEGROUPCODE` | CHAR(8) |  |  |  |  |
| 8 | `PROGRESSOPERATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 9 | `GENERATEFORPRODDEM` | SMALLINT | NOT NULL |  |  |  |
| 10 | `PRODUCTIONORDERIDENTIFICATION` | CHAR(1) | NOT NULL |  |  |  |
| 11 | `STEPIDENTIFICATION` | CHAR(1) | NOT NULL |  |  |  |
| 12 | `PRODUCTIONDEMAND` | CHAR(1) | NOT NULL |  |  |  |
| 13 | `NOTPRECREATEDELEMENT` | CHAR(1) | NOT NULL |  |  |  |
| 14 | `EXTOPLINEDATA` | CHAR(1) | NOT NULL |  |  |  |
| 15 | `AUTOMATICQUEUEPROGRESS` | SMALLINT | NOT NULL |  |  |  |
| 16 | `AUTQUEUEPROGRESSTMPCMYCODE` | CHAR(3) |  |  |  |  |
| 17 | `AUTQUEUEPROGRESSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 18 | `AUTOMATICEXTOPDOC` | SMALLINT | NOT NULL |  |  |  |
| 19 | `SUPPLIERINVOICEDATA` | CHAR(1) |  |  |  |  |
| 20 | `SUPPLIERSHIPPINGDATA` | CHAR(1) |  |  |  |  |
| 21 | `INVOICEDVALUE` | CHAR(1) |  |  |  |  |
| 22 | `PERFORMRESERVATIONBACKFLUSH` | CHAR(1) |  |  |  |  |
| 23 | `BACKFLUSHNEGQTY` | SMALLINT | NOT NULL |  |  |  |
| 24 | `DEMANDORDRECALCULATIONCODE` | CHAR(20) |  |  |  |  |
| 25 | `RECALCULATEONLYQTY` | SMALLINT | NOT NULL |  |  |  |
| 26 | `PERFORMRECALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 27 | `TEMPLATESERVICECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 28 | `TEMPLATESERVICECODE` | CHAR(3) |  |  |  |  |
| 29 | `TMPRETURNSERVICECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 30 | `TEMPLATERETURNSERVICECODE` | CHAR(3) |  |  |  |  |
| 31 | `RECALCPRODDEMCODE` | CHAR(20) |  |  |  |  |
| 32 | `DATETOUPDATE` | INTEGER | NOT NULL |  |  |  |
| 33 | `RECALCNEXTSTEP` | INTEGER | NOT NULL |  |  |  |
| 34 | `CONSUMELEADTIMENEXTSTEP` | SMALLINT | NOT NULL |  |  |  |
| 35 | `RECALCPREVIOUSSTEP` | INTEGER | NOT NULL |  |  |  |
| 36 | `CONSUMELEADTIMEPREVSTEP` | SMALLINT | NOT NULL |  |  |  |
| 37 | `RECALCQUANTITY` | SMALLINT | NOT NULL |  |  |  |
| 38 | `RECALCEFFECTIVEDATEQUANTITY` | SMALLINT | NOT NULL |  |  |  |
| 39 | `MACHINEDOWNTIMEDURATION` | DECIMAL(15,5) |  |  |  |  |
| 40 | `MACHINEDOWNTIMEUOM` | CHAR(1) |  |  |  |  |
| 41 | `STEPCHOOSELOGICCODE` | CHAR(20) |  |  |  |  |
| 42 | `AUTOCLOSEOPENNEXTSTEPCODE` | CHAR(20) |  |  |  |  |
| 43 | `AUTOPROGRESSPREVSTEPCODE` | CHAR(20) |  |  |  |  |
| 44 | `QTYCALCFROMPROVIDEDTIMECODE` | CHAR(20) |  |  |  |  |
| 45 | `RECALCRULEFORSCHEDULEDQTYCODE` | CHAR(20) |  |  |  |  |
| 46 | `RECALCRULEFORSCHEDDATESCODE` | CHAR(20) |  |  |  |  |
| 47 | `FORCINGDATACODE` | CHAR(20) |  |  |  |  |
| 48 | `SHIPPINGBILLMANAGEMENTCODE` | CHAR(20) |  |  |  |  |
| 49 | `INVOICECONTROLOFEXTOPERCODE` | CHAR(20) |  |  |  |  |
| 50 | `MQMUPDATESCODE` | CHAR(20) |  |  |  |  |
| 51 | `CALCSERVICETRANSACTIONCODE` | CHAR(20) |  |  |  |  |
| 52 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 53 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 54 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 55 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 56 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 57 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 58 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 59 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 60 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 61 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 62 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 63 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 64 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 65 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGPRODUCTIONPROGRESSTEMPLATE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.PROGRESSTYPE,
       t.PROGRESSTMPGROUPCOMPANYCODE,
       t.PROGRESSTEMPLATEGROUPCODE,
       t.PROGRESSOPERATIONTYPE,
       t.GENERATEFORPRODDEM,
       t.PRODUCTIONORDERIDENTIFICATION,
       t.STEPIDENTIFICATION
FROM   DB2ADMIN.LOGPRODUCTIONPROGRESSTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
