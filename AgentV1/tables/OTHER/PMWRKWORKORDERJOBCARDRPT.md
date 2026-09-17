# DB2ADMIN.PMWRKWORKORDERJOBCARDRPT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 54
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 84505

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `WORKORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 4 | `WORKORDERCODE` | CHAR(15) |  |  |  |  |
| 5 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 6 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 7 | `DIVISONCODE` | CHAR(8) |  |  |  |  |
| 8 | `PLANEDSCHDDATE` | DATE |  |  |  |  |
| 9 | `WORKORDERDATE` | DATE |  |  |  |  |
| 10 | `WORKORDERSTATUS` | INTEGER | NOT NULL |  |  |  |
| 11 | `PMBOMCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 12 | `PMBOMCODE` | CHAR(15) |  |  |  |  |
| 13 | `ACTIVITYGROUPCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 14 | `ACTIVITYGROUPCODE` | CHAR(15) |  |  |  |  |
| 15 | `ACTIVITYCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 16 | `ACTIVITYCODE` | CHAR(15) |  |  |  |  |
| 17 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 18 | `SUBSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 19 | `STARTDATE` | TIMESTAMP |  |  |  |  |
| 20 | `ENDDATE` | TIMESTAMP |  |  |  |  |
| 21 | `PLANNEDDURATIONUOM` | INTEGER | NOT NULL |  |  |  |
| 22 | `PLANNEDDURATION` | DECIMAL(15,5) |  |  |  |  |
| 23 | `ACTUALDURATIONUOM` | INTEGER | NOT NULL |  |  |  |
| 24 | `ACTUALDURATION` | DECIMAL(15,5) |  |  |  |  |
| 25 | `ASSIGNEDTOUSERID` | CHAR(50) |  |  |  |  |
| 26 | `WORKORDERDETAILSTATUS` | INTEGER | NOT NULL |  |  |  |
| 27 | `REMARKS` | VARCHAR(1000) |  |  |  |  |
| 28 | `ITEMTYPECODE` | CHAR(8) |  |  |  |  |
| 29 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 30 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 39 | `FULLITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 40 | `QUANTITYUOM` | CHAR(3) |  |  |  |  |
| 41 | `PLANNEDQUANTITY` | DECIMAL(18,5) |  |  |  |  |
| 42 | `USEDQUANTITY` | DECIMAL(18,5) |  |  |  |  |
| 43 | `PRVMNTCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 44 | `PRVMNTCODE` | CHAR(15) |  |  |  |  |
| 45 | `BREAKDOWNENTRYCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 46 | `BREAKDOWNENTRYCODE` | CHAR(15) |  |  |  |  |
| 47 | `WORKORDERFOR` | CHAR(30) |  |  |  |  |
| 48 | `SYMPTOM` | VARCHAR(1000) |  |  |  |  |
| 49 | `WORKORDERMACHINECOUNTER` | CHAR(8) |  |  |  |  |
| 50 | `WORKORDERMACHINECODE` | CHAR(15) |  |  |  |  |
| 51 | `SCHEDULEID` | INTEGER | NOT NULL |  |  |  |
| 52 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 53 | `ACTIVITYDESCRIPTION` | VARCHAR(200) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PMWRKWORKORDERJOBCARDRPTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINENO,
       t.WORKORDERCOUNTERCODE,
       t.WORKORDERCODE,
       t.PLANTCODE,
       t.DEPARTMENTCODE,
       t.DIVISONCODE,
       t.PLANEDSCHDDATE,
       t.WORKORDERDATE,
       t.WORKORDERSTATUS,
       t.PMBOMCOUNTERCODE
FROM   DB2ADMIN.PMWRKWORKORDERJOBCARDRPT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
