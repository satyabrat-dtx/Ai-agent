# DB2ADMIN.WORKCENTERANDOPERTOOLS

- **Module**: `PRODUCTION` (high confidence — table name starts with 'WORKCENTER')
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `COMPANYCODE`, `WORKCENTERCODE`, `OPERATIONCODE`, `TOOLITEMTYPECODE`, `TOOLSUBCODE01`, `COSTGROUPCODE`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 24477

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `WORKCENTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `OPERATIONCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `TOOLITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `TOOLSUBCODE01` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `COSTELEMENTITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `COSTELEMENTSUBCODE01` | CHAR(20) |  | FK | foreign_key |  |
| 7 | `COSTGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 8 | `REPETITIONNUMBER` | DECIMAL(2,0) | NOT NULL |  |  |  |
| 9 | `CONSUMPTION` | DECIMAL(15,5) |  |  |  |  |
| 10 | `TOTALCOST` | DECIMAL(18,5) |  |  |  |  |
| 11 | `ABSORPTIONTYPE` | CHAR(2) |  |  |  |  |
| 12 | `LOSS` | DECIMAL(17,6) |  |  |  |  |
| 13 | `LOSSTYPE` | CHAR(2) |  |  |  |  |
| 14 | `CONSUMPTIONUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 15 | `STEPQUANTITYTYPE` | CHAR(1) |  |  |  |  |
| 16 | `USAGEPERCENTAGE` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 17 | `SCHEDULINGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `TOOLITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 23 | `TOOLCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 24 | `COSTELEMENTCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 25 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 26 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 27 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `WORKCENTERANDOPERTOOLS.COMPANYCODE = COMPANY.CODE` |
| `COSTELEMENT_COSTELEMENT` | `COSTELEMENTCOMPANYCODE`, `COSTELEMENTITEMTYPECODE`, `COSTELEMENTSUBCODE01` | [`COSTELEMENT`](../COSTING/COSTELEMENT.md) | `COMPANYCODE`, `ITEMTYPECODE`, `SUBCODE01` | RESTRICT | `WORKCENTERANDOPERTOOLS.COSTELEMENTCOMPANYCODE = COSTELEMENT.COMPANYCODE AND WORKCENTERANDOPERTOOLS.COSTELEMENTITEMTYPECODE = COSTELEMENT.ITEMTYPECODE AND WORKCENTERANDOPERTOOLS.COSTELEMENTSUBCODE01 = COSTELEMENT.SUBCODE01` |
| `ITEMTYPE_TOOLITEMTYPE` | `TOOLITEMTYPECOMPANYCODE`, `TOOLITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WORKCENTERANDOPERTOOLS.TOOLITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND WORKCENTERANDOPERTOOLS.TOOLITEMTYPECODE = ITEMTYPE.CODE` |
| `TOOL_TOOL` | `TOOLCOMPANYCODE`, `TOOLITEMTYPECODE`, `TOOLSUBCODE01` | [`TOOL`](../CORE_MASTER/TOOL.md) | `COMPANYCODE`, `ITEMTYPECODE`, `SUBCODE01` | RESTRICT | `WORKCENTERANDOPERTOOLS.TOOLCOMPANYCODE = TOOL.COMPANYCODE AND WORKCENTERANDOPERTOOLS.TOOLITEMTYPECODE = TOOL.ITEMTYPECODE AND WORKCENTERANDOPERTOOLS.TOOLSUBCODE01 = TOOL.SUBCODE01` |
| `UNITOFMEASURE_CONSUMPTIONUOM` | `CONSUMPTIONUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `WORKCENTERANDOPERTOOLS.CONSUMPTIONUOMCODE = UNITOFMEASURE.CODE` |
| `WORKCENTER_WORKCENTER` | `COMPANYCODE`, `WORKCENTERCODE` | [`WORKCENTER`](../PRODUCTION/WORKCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WORKCENTERANDOPERTOOLS.COMPANYCODE = WORKCENTER.COMPANYCODE AND WORKCENTERANDOPERTOOLS.WORKCENTERCODE = WORKCENTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WORKCENTERANDOPERTOOLSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.WORKCENTERCODE,
       t.OPERATIONCODE,
       t.TOOLITEMTYPECODE,
       t.TOOLSUBCODE01,
       t.COSTELEMENTITEMTYPECODE,
       t.COSTELEMENTSUBCODE01,
       t.COSTGROUPCODE,
       t.REPETITIONNUMBER,
       t.CONSUMPTION,
       t.TOTALCOST,
       t.ABSORPTIONTYPE
FROM   DB2ADMIN.WORKCENTERANDOPERTOOLS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
