# DB2ADMIN.PMACTIVITYDETAILS

- **Module**: `WAREHOUSE` (low confidence — FK neighbourhood: 1 of 1 related tables are WAREHOUSE)
- **Roles**: `business_data`
- **Columns**: 36
- **Primary key**: `PMACTIVITYCOMPANYCODE`, `PMACTIVITYCOUNTERCODE`, `PMACTIVITYCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 7 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 83522

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PMACTIVITYCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PMACTIVITYCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PMACTIVITYCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINENO` | DECIMAL(10,0) | NOT NULL | PK | primary_key |  |
| 4 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `ITEMTYPEAFICODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 7 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `PRODUCTSHORTDESC` | VARCHAR(80) |  |  |  |  |
| 17 | `UOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 18 | `QUANITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 19 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 20 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 21 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 22 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 23 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 25 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 26 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 27 | `SPARESPLANNEDCOST` | DECIMAL(18,5) |  |  |  |  |
| 28 | `SUBWAREHOUSECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 29 | `SUBWAREHOUSECODE` | CHAR(8) |  | FK | foreign_key |  |
| 30 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 31 | `LOGICALWAREHOUSECODE` | CHAR(8) |  | FK | foreign_key |  |
| 32 | `AVLWAREHOUSEGROUPCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 33 | `AVAILABILITYWAREHOUSEGROUPCODE` | CHAR(3) |  | FK | foreign_key |  |
| 34 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 35 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 7

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `AVAILABILITYWAREHOUSEGROUP_AVAILABILITYWAREHOUSEGROUP` | `AVLWAREHOUSEGROUPCOMPANYCODE`, `AVAILABILITYWAREHOUSEGROUPCODE` | [`AVAILABILITYWAREHOUSEGROUP`](../CORE_MASTER/AVAILABILITYWAREHOUSEGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMACTIVITYDETAILS.AVLWAREHOUSEGROUPCOMPANYCODE = AVAILABILITYWAREHOUSEGROUP.COMPANYCODE AND PMACTIVITYDETAILS.AVAILABILITYWAREHOUSEGROUPCODE = AVAILABILITYWAREHOUSEGROUP.CODE` |
| `DIVISION_DIVISION` | `PMACTIVITYCOMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMACTIVITYDETAILS.PMACTIVITYCOMPANYCODE = DIVISION.COMPANYCODE AND PMACTIVITYDETAILS.DIVISIONCODE = DIVISION.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMACTIVITYDETAILS.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND PMACTIVITYDETAILS.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `LOGICALWAREHOUSE_LOGICALWAREHOUSE` | `LOGICALWAREHOUSECOMPANYCODE`, `LOGICALWAREHOUSECODE` | [`LOGICALWAREHOUSE`](../WAREHOUSE/LOGICALWAREHOUSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMACTIVITYDETAILS.LOGICALWAREHOUSECOMPANYCODE = LOGICALWAREHOUSE.COMPANYCODE AND PMACTIVITYDETAILS.LOGICALWAREHOUSECODE = LOGICALWAREHOUSE.CODE` |
| `LOGICALWAREHOUSE_SUBWAREHOUSE` | `SUBWAREHOUSECOMPANYCODE`, `SUBWAREHOUSECODE` | [`LOGICALWAREHOUSE`](../WAREHOUSE/LOGICALWAREHOUSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMACTIVITYDETAILS.SUBWAREHOUSECOMPANYCODE = LOGICALWAREHOUSE.COMPANYCODE AND PMACTIVITYDETAILS.SUBWAREHOUSECODE = LOGICALWAREHOUSE.CODE` |
| `PMACTIVITY_DETAIL` | `PMACTIVITYCOMPANYCODE`, `PMACTIVITYCOUNTERCODE`, `PMACTIVITYCODE` | [`PMACTIVITY`](../PLATFORM/PMACTIVITY.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMACTIVITYDETAILS.PMACTIVITYCOMPANYCODE = PMACTIVITY.COMPANYCODE AND PMACTIVITYDETAILS.PMACTIVITYCOUNTERCODE = PMACTIVITY.COUNTERCODE AND PMACTIVITYDETAILS.PMACTIVITYCODE = PMACTIVITY.CODE` |
| `UNITOFMEASURE_UOM` | `UOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `PMACTIVITYDETAILS.UOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PMACTIVITYDETAILSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PMACTIVITYCOMPANYCODE,
       t.PMACTIVITYCOUNTERCODE,
       t.PMACTIVITYCODE,
       t.LINENO,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06
FROM   DB2ADMIN.PMACTIVITYDETAILS t
FETCH FIRST 100 ROWS ONLY;
```
