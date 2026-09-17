# DB2ADMIN.WRKPMCONSUMPTIONMAC

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 38
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 89310

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `WORKORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 4 | `WORKORDERCODE` | CHAR(15) |  |  |  |  |
| 5 | `WORKORDERDATE` | DATE |  |  |  |  |
| 6 | `WORKORDERTYPE` | CHAR(20) |  |  |  |  |
| 7 | `PMBOMCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 8 | `PMBOMCODE` | CHAR(15) |  |  |  |  |
| 9 | `MACHINEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 10 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 11 | `COSTCENTERDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 12 | `WORKPLACE` | CHAR(15) |  |  |  |  |
| 13 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 14 | `PLANNINGGROUP` | CHAR(15) |  |  |  |  |
| 15 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 16 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 17 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 27 | `ACTUALQUANITY` | DECIMAL(18,5) |  |  |  |  |
| 28 | `PLANNEDQUANITY` | DECIMAL(18,5) |  |  |  |  |
| 29 | `PURCHASERATE` | DECIMAL(18,5) |  |  |  |  |
| 30 | `AVERAGECOST` | DECIMAL(18,5) |  |  |  |  |
| 31 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 32 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 33 | `ACTIVITYTYPE` | CHAR(3) |  |  |  |  |
| 34 | `PMWORKORDERDETAILLINENO` | DECIMAL(10,0) |  |  |  |  |
| 35 | `PMWORKORDACTIVITYSPARESLINENO` | DECIMAL(10,0) |  |  |  |  |
| 36 | `CREATEREQUISITIONFOR` | DECIMAL(15,5) |  |  |  |  |
| 37 | `CREATEINTERNALDOCUMENTFOR` | DECIMAL(15,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKPMCONSUMPTIONMACUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINENO,
       t.WORKORDERCOUNTERCODE,
       t.WORKORDERCODE,
       t.WORKORDERDATE,
       t.WORKORDERTYPE,
       t.PMBOMCOUNTERCODE,
       t.PMBOMCODE,
       t.MACHINEDESCRIPTION,
       t.COSTCENTERCODE,
       t.COSTCENTERDESCRIPTION
FROM   DB2ADMIN.WRKPMCONSUMPTIONMAC t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
