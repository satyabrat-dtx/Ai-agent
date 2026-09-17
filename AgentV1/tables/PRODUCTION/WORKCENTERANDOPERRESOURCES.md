# DB2ADMIN.WORKCENTERANDOPERRESOURCES

- **Module**: `PRODUCTION` (high confidence — table name starts with 'WORKCENTER')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `COMPANYCODE`, `WORKCENTERCODE`, `OPERATIONCODE`, `RESOURCECODE`, `COSTGROUPCODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 41688

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `WORKCENTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `OPERATIONCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `RESOURCECODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `COSTELEMENTITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `COSTELEMENTSUBCODE01` | CHAR(20) |  | FK | foreign_key |  |
| 6 | `COSTGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 7 | `REPETITIONNUMBER` | DECIMAL(2,0) | NOT NULL |  |  |  |
| 8 | `CONSUMPTION` | DECIMAL(15,5) |  |  |  |  |
| 9 | `TOTALCOST` | DECIMAL(18,5) |  |  |  |  |
| 10 | `ABSORPTIONTYPE` | CHAR(2) |  |  |  |  |
| 11 | `LOSS` | DECIMAL(17,6) |  |  |  |  |
| 12 | `LOSSTYPE` | CHAR(2) |  |  |  |  |
| 13 | `CONSUMPTIONUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `STEPQUANTITYTYPE` | CHAR(1) |  |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `COSTELEMENTCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `WORKCENTERANDOPERRESOURCES.COMPANYCODE = COMPANY.CODE` |
| `COSTELEMENT_COSTELEMENT` | `COSTELEMENTCOMPANYCODE`, `COSTELEMENTITEMTYPECODE`, `COSTELEMENTSUBCODE01` | [`COSTELEMENT`](../COSTING/COSTELEMENT.md) | `COMPANYCODE`, `ITEMTYPECODE`, `SUBCODE01` | RESTRICT | `WORKCENTERANDOPERRESOURCES.COSTELEMENTCOMPANYCODE = COSTELEMENT.COMPANYCODE AND WORKCENTERANDOPERRESOURCES.COSTELEMENTITEMTYPECODE = COSTELEMENT.ITEMTYPECODE AND WORKCENTERANDOPERRESOURCES.COSTELEMENTSUBCODE01 = COSTELEMENT.SUBCODE01` |
| `RESOURCES_RESOURCE` | `COMPANYCODE`, `RESOURCECODE` | [`RESOURCES`](../PRODUCTION/RESOURCES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WORKCENTERANDOPERRESOURCES.COMPANYCODE = RESOURCES.COMPANYCODE AND WORKCENTERANDOPERRESOURCES.RESOURCECODE = RESOURCES.CODE` |
| `UNITOFMEASURE_CONSUMPTIONUOM` | `CONSUMPTIONUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `WORKCENTERANDOPERRESOURCES.CONSUMPTIONUOMCODE = UNITOFMEASURE.CODE` |
| `WORKCENTER_WORKCENTER` | `COMPANYCODE`, `WORKCENTERCODE` | [`WORKCENTER`](../PRODUCTION/WORKCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WORKCENTERANDOPERRESOURCES.COMPANYCODE = WORKCENTER.COMPANYCODE AND WORKCENTERANDOPERRESOURCES.WORKCENTERCODE = WORKCENTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WORKCENTERANDOPERRESOURCESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.WORKCENTERCODE,
       t.OPERATIONCODE,
       t.RESOURCECODE,
       t.COSTELEMENTITEMTYPECODE,
       t.COSTELEMENTSUBCODE01,
       t.COSTGROUPCODE,
       t.REPETITIONNUMBER,
       t.CONSUMPTION,
       t.TOTALCOST,
       t.ABSORPTIONTYPE,
       t.LOSS
FROM   DB2ADMIN.WORKCENTERANDOPERRESOURCES t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
