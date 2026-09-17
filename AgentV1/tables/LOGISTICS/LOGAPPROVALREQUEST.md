# DB2ADMIN.LOGAPPROVALREQUEST

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 76
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 212251

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 1 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `TEMPLATECODE` | CHAR(10) |  |  |  |  |
| 4 | `REQUESTCODE` | CHAR(10) | NOT NULL |  |  |  |
| 5 | `VERSION` | INTEGER | NOT NULL |  |  |  |
| 6 | `APPROVALREQUESTDATE` | DATE | NOT NULL |  |  |  |
| 7 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 8 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 9 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 10 | `PHYSICALREFERENCE` | SMALLINT | NOT NULL |  |  |  |
| 11 | `CSMCODECUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 12 | `CSMCODECUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 13 | `SHIPPABLE` | SMALLINT | NOT NULL |  |  |  |
| 14 | `BUYERCODECUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 15 | `BUYERCODECUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 16 | `APPROVALNOTE` | VARCHAR(500) |  |  |  |  |
| 17 | `PRIORITY` | INTEGER | NOT NULL |  |  |  |
| 18 | `DELIVERYDATEREQUESTED` | DATE |  |  |  |  |
| 19 | `DELIVERYDATECONFIRMED` | DATE |  |  |  |  |
| 20 | `REQUESTORIGIN` | INTEGER | NOT NULL |  |  |  |
| 21 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 22 | `APPROVALDATE` | DATE |  |  |  |  |
| 23 | `APPROVALUSERUSERID` | CHAR(50) |  |  |  |  |
| 24 | `COMPANY` | CHAR(3) |  |  |  |  |
| 25 | `TYPE` | CHAR(3) |  |  |  |  |
| 26 | `CODE` | CHAR(10) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 27 | `INITIALTESTSNUMBER` | INTEGER | NOT NULL |  |  |  |
| 28 | `CUTQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 29 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 30 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 32 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 33 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 39 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 40 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 41 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 42 | `ITEMKEY` | VARCHAR(200) |  |  |  |  |
| 43 | `ITEMDESCRIPTION` | CHAR(200) |  |  |  |  |
| 44 | `PDCODECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 45 | `PDCODECODE` | CHAR(15) |  |  |  |  |
| 46 | `LOTCODECODE` | CHAR(35) |  |  |  |  |
| 47 | `ELEMENTSCODECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 48 | `ELEMENTSCODESUBCODEKEY` | CHAR(20) |  |  |  |  |
| 49 | `ELEMENTSCODECODE` | CHAR(15) |  |  |  |  |
| 50 | `ENTITYFATHERTYPE` | INTEGER | NOT NULL |  |  |  |
| 51 | `FATHERCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 52 | `FATHERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 53 | `FATHERCODE` | CHAR(15) |  |  |  |  |
| 54 | `FATHERLINE` | DECIMAL(7,0) |  |  |  |  |
| 55 | `FATHERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 56 | `FATHERCOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 57 | `FATHERDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 58 | `FATHERUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 59 | `FATHERAPPROVALREQUESTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 60 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 61 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 62 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 63 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 64 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 65 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 66 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 67 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 68 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 69 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 70 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 71 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 72 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 73 | `DRCODE` | CHAR(8) |  |  |  |  |
| 74 | `DRLINE` | CHAR(15) |  |  |  |  |
| 75 | `ORIGINDRLINENR` | DECIMAL(5,0) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGAPPROVALREQUEST.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGAPPROVALREQUESTDETAIL`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.TEMPLATECODE,
       t.REQUESTCODE,
       t.VERSION,
       t.APPROVALREQUESTDATE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.PHYSICALREFERENCE,
       t.CSMCODECUSTOMERSUPPLIERTYPE
FROM   DB2ADMIN.LOGAPPROVALREQUEST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
