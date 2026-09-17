# DB2ADMIN.BUDGETDEFINITION

- **Module**: `COSTING` (low confidence — FK neighbourhood: 1 of 1 related tables are COSTING)
- **Roles**: `business_data`
- **Columns**: 42
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `PLANTCODE`, `PERPERIODIZEDCALENDARTYPECODE`, `PERIODPERIODIZEDCALENDARYEAR`, `PERIODCODE`, `COSTCENTERCODE`, `TYPEOFBUDGET`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 9 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 128799

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `PLANTCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `PLANTCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PERPERIODIZEDCALENDARTYPECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `PERIODPERIODIZEDCALENDARYEAR` | DECIMAL(4,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `PERIODCODE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `COSTCENTERCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 8 | `COSTCENTERCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 9 | `TYPEOFBUDGET` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 10 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `ITEMTYPEAFICODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `PRDGRPUSERGENGRPTECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `PRDGRPUSERGENGROUPTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `PRODUCTGROUPCODE` | CHAR(10) |  | FK | foreign_key |  |
| 15 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 16 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `UOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 26 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 27 | `AMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 28 | `APPROVED` | SMALLINT | NOT NULL |  |  |  |
| 29 | `BUDGETTYPE` | CHAR(2) |  |  |  |  |
| 30 | `USEDBUDGETAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 31 | `PENDINGBUDGETAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 32 | `NUMBERID` | INTEGER | NOT NULL | PK | primary_key |  |
| 33 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 34 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 35 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 36 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 37 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 38 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 39 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 40 | `PENDINGALLOCATION` | SMALLINT | NOT NULL |  |  |  |
| 41 | `TRANSFERREDAMOUNT` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 9

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BUDGETDEFINITION.COMPANYCODE = COMPANY.CODE` |
| `COSTCENTER_COSTCENTER` | `COSTCENTERCOMPANYCODE`, `COSTCENTERCODE` | [`COSTCENTER`](../COSTING/COSTCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BUDGETDEFINITION.COSTCENTERCOMPANYCODE = COSTCENTER.COMPANYCODE AND BUDGETDEFINITION.COSTCENTERCODE = COSTCENTER.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `BUDGETDEFINITION.CURRENCYCODE = CURRENCY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BUDGETDEFINITION.COMPANYCODE = DIVISION.COMPANYCODE AND BUDGETDEFINITION.DIVISIONCODE = DIVISION.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BUDGETDEFINITION.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND BUDGETDEFINITION.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `PERIOD_PERIOD` | `PERPERIODIZEDCALENDARTYPECODE`, `PERIODPERIODIZEDCALENDARYEAR`, `PERIODCODE` | [`PERIOD`](../WAREHOUSE/PERIOD.md) | `PERIODIZEDCALENDARTYPECODE`, `PERIODIZEDCALENDARYEAR`, `CODE` | RESTRICT | `BUDGETDEFINITION.PERPERIODIZEDCALENDARTYPECODE = PERIOD.PERIODIZEDCALENDARTYPECODE AND BUDGETDEFINITION.PERIODPERIODIZEDCALENDARYEAR = PERIOD.PERIODIZEDCALENDARYEAR AND BUDGETDEFINITION.PERIODCODE = PERIOD.CODE` |
| `PLANT_PLANT` | `PLANTCOMPANYCODE`, `PLANTCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BUDGETDEFINITION.PLANTCOMPANYCODE = PLANT.COMPANYCODE AND BUDGETDEFINITION.PLANTCODE = PLANT.CODE` |
| `UNITOFMEASURE_UOM` | `UOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `BUDGETDEFINITION.UOMCODE = UNITOFMEASURE.CODE` |
| `USERGENERICGROUP_PRODUCTGROUP` | `PRDGRPUSERGENGRPTECOMPANYCODE`, `PRDGRPUSERGENGROUPTYPECODE`, `PRODUCTGROUPCODE` | [`USERGENERICGROUP`](../CORE_MASTER/USERGENERICGROUP.md) | `USERGENGROUPTYPECOMPANYCODE`, `USERGENERICGROUPTYPECODE`, `CODE` | RESTRICT | `BUDGETDEFINITION.PRDGRPUSERGENGRPTECOMPANYCODE = USERGENERICGROUP.USERGENGROUPTYPECOMPANYCODE AND BUDGETDEFINITION.PRDGRPUSERGENGROUPTYPECODE = USERGENERICGROUP.USERGENERICGROUPTYPECODE AND BUDGETDEFINITION.PRODUCTGROUPCODE = USERGENERICGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BUDGETDEFINITIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.PLANTCOMPANYCODE,
       t.PLANTCODE,
       t.PERPERIODIZEDCALENDARTYPECODE,
       t.PERIODPERIODIZEDCALENDARYEAR,
       t.PERIODCODE,
       t.COSTCENTERCOMPANYCODE,
       t.COSTCENTERCODE,
       t.TYPEOFBUDGET,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE
FROM   DB2ADMIN.BUDGETDEFINITION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
