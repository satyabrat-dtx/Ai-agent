# DB2ADMIN.PURCHASEBUDGETDEFINITION

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 41
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `PLANTCODE`, `PERPERIODIZEDCALENDARTYPECODE`, `PERIODPERIODIZEDCALENDARYEAR`, `PERIODCODE`, `COSTCENTERCODE`, `TYPEOFBUDGET`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 192439

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `PLANTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `PLANTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `PERPERIODIZEDCALENDARTYPECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `PERIODPERIODIZEDCALENDARYEAR` | DECIMAL(4,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `PERIODCODE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `BUDGETSTARTDATE` | DATE | NOT NULL |  |  |  |
| 8 | `BUDGETENDDATE` | DATE | NOT NULL |  |  |  |
| 9 | `COSTCENTERCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 10 | `COSTCENTERCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 11 | `TYPEOFBUDGET` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 12 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `ITEMTYPEAFICODE` | CHAR(3) |  | FK | foreign_key |  |
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
| 24 | `BUDGETGROUPCOMPANY` | CHAR(3) |  | FK | foreign_key |  |
| 25 | `BUDGETUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  | FK | foreign_key |  |
| 26 | `BUDGETUSERGRPCODE` | CHAR(10) |  | FK | foreign_key |  |
| 27 | `UOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 28 | `AMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 29 | `APPROVED` | SMALLINT | NOT NULL |  |  |  |
| 30 | `BUDGETTYPE` | CHAR(2) |  |  |  |  |
| 31 | `USEDBUDGETAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 32 | `PENDINGBUDGETAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 33 | `NUMBERID` | INTEGER | NOT NULL | PK | primary_key |  |
| 34 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 35 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 36 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 37 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 38 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 39 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 40 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PURCHASEBUDGETDEFINITION.COMPANYCODE = COMPANY.CODE` |
| `COSTCENTER_COSTCENTER` | `COSTCENTERCOMPANYCODE`, `COSTCENTERCODE` | [`COSTCENTER`](../COSTING/COSTCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASEBUDGETDEFINITION.COSTCENTERCOMPANYCODE = COSTCENTER.COMPANYCODE AND PURCHASEBUDGETDEFINITION.COSTCENTERCODE = COSTCENTER.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASEBUDGETDEFINITION.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND PURCHASEBUDGETDEFINITION.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `PERIOD_PERIOD` | `PERPERIODIZEDCALENDARTYPECODE`, `PERIODPERIODIZEDCALENDARYEAR`, `PERIODCODE` | [`PERIOD`](../WAREHOUSE/PERIOD.md) | `PERIODIZEDCALENDARTYPECODE`, `PERIODIZEDCALENDARYEAR`, `CODE` | RESTRICT | `PURCHASEBUDGETDEFINITION.PERPERIODIZEDCALENDARTYPECODE = PERIOD.PERIODIZEDCALENDARTYPECODE AND PURCHASEBUDGETDEFINITION.PERIODPERIODIZEDCALENDARYEAR = PERIOD.PERIODIZEDCALENDARYEAR AND PURCHASEBUDGETDEFINITION.PERIODCODE = PERIOD.CODE` |
| `UNITOFMEASURE_UOM` | `UOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `PURCHASEBUDGETDEFINITION.UOMCODE = UNITOFMEASURE.CODE` |
| `USERGENERICGROUP_BUDGETUSERGRP` | `BUDGETGROUPCOMPANY`, `BUDGETUSERGRPUSERGENGRPTYPECOD`, `BUDGETUSERGRPCODE` | [`USERGENERICGROUP`](../CORE_MASTER/USERGENERICGROUP.md) | `USERGENGROUPTYPECOMPANYCODE`, `USERGENERICGROUPTYPECODE`, `CODE` | RESTRICT | `PURCHASEBUDGETDEFINITION.BUDGETGROUPCOMPANY = USERGENERICGROUP.USERGENGROUPTYPECOMPANYCODE AND PURCHASEBUDGETDEFINITION.BUDGETUSERGRPUSERGENGRPTYPECOD = USERGENERICGROUP.USERGENERICGROUPTYPECODE AND PURCHASEBUDGETDEFINITION.BUDGETUSERGRPCODE = USERGENERICGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASEBUDGETDEFINITIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.PLANTCOMPANYCODE,
       t.PLANTCODE,
       t.PERPERIODIZEDCALENDARTYPECODE,
       t.PERIODPERIODIZEDCALENDARYEAR,
       t.PERIODCODE,
       t.BUDGETSTARTDATE,
       t.BUDGETENDDATE,
       t.COSTCENTERCOMPANYCODE,
       t.COSTCENTERCODE,
       t.TYPEOFBUDGET
FROM   DB2ADMIN.PURCHASEBUDGETDEFINITION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
