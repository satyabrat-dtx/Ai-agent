# DB2ADMIN.WRKPMREQUISICREATION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 38
- **Primary key**: `COMPANYCODE`, `LINENO`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 89519

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `WORKORDERCOUNTERCODE` | CHAR(15) |  |  |  |  |
| 4 | `WORKORDERCODE` | CHAR(15) |  |  |  |  |
| 5 | `ACTIVITYCOUNTERCODE` | CHAR(15) |  |  |  |  |
| 6 | `ACITIVITYCODE` | CHAR(15) |  |  |  |  |
| 7 | `ACTIVITYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 8 | `MACHINECOUNTERCODE` | CHAR(15) |  |  |  |  |
| 9 | `MACHINECODE` | CHAR(15) |  |  |  |  |
| 10 | `MACHINEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 11 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 12 | `DEPARTMENTDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 13 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 14 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 15 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 25 | `PLANNEDQUANITY` | DECIMAL(18,5) |  |  |  |  |
| 26 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 27 | `SALOGICALWAREHOUSEQTY` | DECIMAL(18,5) |  |  |  |  |
| 28 | `SALOGICALWAREHOUSEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 29 | `SDLOGICALWAREHOUSEQTY` | DECIMAL(18,5) |  |  |  |  |
| 30 | `SDLOGICALWAREHOUSEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 31 | `PENDINGQUANITY` | DECIMAL(18,5) |  |  |  |  |
| 32 | `ALREADYPRCREATEDQUANITY` | DECIMAL(18,5) |  |  |  |  |
| 33 | `POCREATEDQUANITY` | DECIMAL(18,5) |  |  |  |  |
| 34 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 35 | `DETAILLINENO` | DECIMAL(10,0) |  |  |  |  |
| 36 | `SPARELINENO` | DECIMAL(10,0) |  |  |  |  |
| 37 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKPMREQUISICREATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINENO,
       t.WORKORDERCOUNTERCODE,
       t.WORKORDERCODE,
       t.ACTIVITYCOUNTERCODE,
       t.ACITIVITYCODE,
       t.ACTIVITYDESCRIPTION,
       t.MACHINECOUNTERCODE,
       t.MACHINECODE,
       t.MACHINEDESCRIPTION,
       t.DEPARTMENTCODE
FROM   DB2ADMIN.WRKPMREQUISICREATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
