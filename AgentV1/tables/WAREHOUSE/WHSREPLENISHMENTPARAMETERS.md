# DB2ADMIN.WHSREPLENISHMENTPARAMETERS

- **Module**: `WAREHOUSE` (low confidence — FK neighbourhood: 1 of 1 related tables are WAREHOUSE)
- **Roles**: `business_data`
- **Columns**: 43
- **Primary key**: `COMPANYCODE`, `WAREHOUSEGROUPCODE`, `PRDGROUPSTANDARDGROUPTYPECODE`, `PRODUCTGROUPCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 7070

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `WAREHOUSEGROUPCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PRDGROUPSTANDARDGROUPTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PRODUCTGROUPCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `REORDERPOINTCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 8 | `REORDERPOINTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 9 | `PURREORDERQUANTITYCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 10 | `PURREORDERQUANTITYPOLICYCODE` | CHAR(20) |  |  |  |  |
| 11 | `INTREORDERQUANTITYCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 12 | `INTREORDERQUANTITYPOLICYCODE` | CHAR(20) |  |  |  |  |
| 13 | `SBCREORDERQUANTITYCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 14 | `SBCREORDERQUANTITYPOLICYCODE` | CHAR(20) |  |  |  |  |
| 15 | `PROREORDERQUANTITYCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 16 | `PROREORDERQUANTITYPOLICYCODE` | CHAR(20) |  |  |  |  |
| 17 | `SAFETYSTOCKCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 18 | `SAFETYSTOCKPOLICYCODE` | CHAR(20) |  |  |  |  |
| 19 | `SAFETYSTOCKUSEDAYS` | INTEGER | NOT NULL |  |  |  |
| 20 | `SAFETYSTOCKDLVTIMEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 21 | `SAFETYSTOCKSERVICELEVEL` | INTEGER | NOT NULL |  |  |  |
| 22 | `PURCHASEORDERCOST` | DECIMAL(18,5) |  |  |  |  |
| 23 | `INTERNALORDERCOST` | DECIMAL(18,5) |  |  |  |  |
| 24 | `SUBCONTRACTORORDERCOST` | DECIMAL(18,5) |  |  |  |  |
| 25 | `PRODUCTIONORDERCOST` | DECIMAL(18,5) |  |  |  |  |
| 26 | `WHSMAINTENANCECOSTPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 27 | `COSTTYPEFORREORDERQTYCALC` | CHAR(1) |  |  |  |  |
| 28 | `PURCHASEPICKUPDAYS` | INTEGER | NOT NULL |  |  |  |
| 29 | `PURCHASEQUALITYCONTROLDAYS` | INTEGER | NOT NULL |  |  |  |
| 30 | `SALESPREPARATIONDAYS` | INTEGER | NOT NULL |  |  |  |
| 31 | `INTERNALPREPARATIONDAYS` | INTEGER | NOT NULL |  |  |  |
| 32 | `INTERNALPICKUPDAYS` | INTEGER | NOT NULL |  |  |  |
| 33 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 34 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 35 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 36 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 37 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 38 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 39 | `WAREHOUSEGROUPCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 40 | `PRDGRPSTDGROUPTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 41 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 42 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `WHSREPLENISHMENTPARAMETERS.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `WHSREPLENISHMENTPARAMETERS.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `STANDARDGROUP_PRODUCTGROUP` | `PRDGRPSTDGROUPTYPECOMPANYCODE`, `PRDGROUPSTANDARDGROUPTYPECODE`, `PRODUCTGROUPCODE` | [`STANDARDGROUP`](../CORE_MASTER/STANDARDGROUP.md) | `STANDARDGROUPTYPECOMPANYCODE`, `STANDARDGROUPTYPECODE`, `CODE` | RESTRICT | `WHSREPLENISHMENTPARAMETERS.PRDGRPSTDGROUPTYPECOMPANYCODE = STANDARDGROUP.STANDARDGROUPTYPECOMPANYCODE AND WHSREPLENISHMENTPARAMETERS.PRDGROUPSTANDARDGROUPTYPECODE = STANDARDGROUP.STANDARDGROUPTYPECODE AND WHSREPLENISHMENTPARAMETERS.PRODUCTGROUPCODE = STANDARDGROUP.CODE` |
| `WAREHOUSEREPLENISHMENTGROUP_WAREHOUSEGROUP` | `WAREHOUSEGROUPCOMPANYCODE`, `WAREHOUSEGROUPCODE` | [`WAREHOUSEREPLENISHMENTGROUP`](../WAREHOUSE/WAREHOUSEREPLENISHMENTGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WHSREPLENISHMENTPARAMETERS.WAREHOUSEGROUPCOMPANYCODE = WAREHOUSEREPLENISHMENTGROUP.COMPANYCODE AND WHSREPLENISHMENTPARAMETERS.WAREHOUSEGROUPCODE = WAREHOUSEREPLENISHMENTGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WHSREPLENISHMENTPARAMETERSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.WAREHOUSEGROUPCODE,
       t.PRDGROUPSTANDARDGROUPTYPECODE,
       t.PRODUCTGROUPCODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.REORDERPOINTCALCULATION,
       t.REORDERPOINTPOLICYCODE,
       t.PURREORDERQUANTITYCALCULATION,
       t.PURREORDERQUANTITYPOLICYCODE,
       t.INTREORDERQUANTITYCALCULATION
FROM   DB2ADMIN.WHSREPLENISHMENTPARAMETERS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
