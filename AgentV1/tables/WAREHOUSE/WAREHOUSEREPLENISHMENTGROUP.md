# DB2ADMIN.WAREHOUSEREPLENISHMENTGROUP

- **Module**: `WAREHOUSE` (high confidence — table name starts with 'WAREHOUSE')
- **Roles**: `business_data`
- **Columns**: 34
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 21207

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `REORDERPOINTCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 6 | `REORDERPOINTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 7 | `PURREORDERQUANTITYCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 8 | `PURREORDERQUANTITYPOLICYCODE` | CHAR(20) |  |  |  |  |
| 9 | `INTREORDERQUANTITYCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 10 | `INTREORDERQUANTITYPOLICYCODE` | CHAR(20) |  |  |  |  |
| 11 | `SBCREORDERQUANTITYCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 12 | `SBCREORDERQUANTITYPOLICYCODE` | CHAR(20) |  |  |  |  |
| 13 | `PROREORDERQUANTITYCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 14 | `PROREORDERQUANTITYPOLICYCODE` | CHAR(20) |  |  |  |  |
| 15 | `SAFETYSTOCKCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 16 | `SAFETYSTOCKPOLICYCODE` | CHAR(20) |  |  |  |  |
| 17 | `SAFETYSTOCKUSEDAYS` | INTEGER | NOT NULL |  |  |  |
| 18 | `SAFETYSTOCKDLVTIMEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 19 | `SAFETYSTOCKSERVICELEVEL` | INTEGER | NOT NULL |  |  |  |
| 20 | `PURCHASEORDERCOST` | DECIMAL(18,5) |  |  |  |  |
| 21 | `INTERNALORDERCOST` | DECIMAL(18,5) |  |  |  |  |
| 22 | `SUBCONTRACTORORDERCOST` | DECIMAL(18,5) |  |  |  |  |
| 23 | `PRODUCTIONORDERCOST` | DECIMAL(18,5) |  |  |  |  |
| 24 | `WHSMAINTENANCECOSTPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 25 | `COSTTYPEFORREORDERQTYCALC` | CHAR(1) |  |  |  |  |
| 26 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 27 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 28 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 29 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 30 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 31 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 32 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 33 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `WAREHOUSEREPLENISHMENTGROUP.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `WAREHOUSEREPLENISHMENTGROUP.OWNINGCOMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `WAREHOUSEREPLENISHMENTGROUP_WAREHOUSEGROUP` | [`WHSREPLENISHMENTPARAMETERS`](../WAREHOUSE/WHSREPLENISHMENTPARAMETERS.md) | `WAREHOUSEGROUPCOMPANYCODE`, `WAREHOUSEGROUPCODE` | `WHSREPLENISHMENTPARAMETERS.WAREHOUSEGROUPCOMPANYCODE = WAREHOUSEREPLENISHMENTGROUP.COMPANYCODE AND WHSREPLENISHMENTPARAMETERS.WAREHOUSEGROUPCODE = WAREHOUSEREPLENISHMENTGROUP.CODE` |
| `WAREHOUSEREPLENISHMENTGROUP_REPLENISHMENTGROUP` | [`LOGICALWAREHOUSE`](../WAREHOUSE/LOGICALWAREHOUSE.md) | `REPLENISHMENTGROUPCOMPANYCODE`, `REPLENISHMENTGROUPCODE` | `LOGICALWAREHOUSE.REPLENISHMENTGROUPCOMPANYCODE = WAREHOUSEREPLENISHMENTGROUP.COMPANYCODE AND LOGICALWAREHOUSE.REPLENISHMENTGROUPCODE = WAREHOUSEREPLENISHMENTGROUP.CODE` |

## Indexes

- `WHSREPLENISHMENTGROUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.REORDERPOINTCALCULATION,
       t.REORDERPOINTPOLICYCODE,
       t.PURREORDERQUANTITYCALCULATION,
       t.PURREORDERQUANTITYPOLICYCODE,
       t.INTREORDERQUANTITYCALCULATION,
       t.INTREORDERQUANTITYPOLICYCODE,
       t.SBCREORDERQUANTITYCALCULATION
FROM   DB2ADMIN.WAREHOUSEREPLENISHMENTGROUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
