# DB2ADMIN.AVAILABILITYPLANNINGSTATUS

- **Module**: `WAREHOUSE` (low confidence — FK neighbourhood: 1 of 1 related tables are WAREHOUSE)
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `IDENTIFIER`, `LOGICALWAREHOUSECODE`, `PROJECTCODE`, `PACKAGINGUOMCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 72144

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IDENTIFIER` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PROJECTCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `WARNINGS` | VARCHAR(960) |  |  |  |  |
| 5 | `PACKAGINGUOMCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `PRIMARYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `SECONDARYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `PLANBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 9 | `PLANBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 10 | `PLANBASEPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 11 | `NETBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 12 | `NETBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 13 | `NETBASEPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 14 | `RRBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 15 | `RRBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 16 | `RRBASEPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 17 | `TABSEQUENCENUMBER` | INTEGER | NOT NULL |  |  |  |
| 18 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 20 | `WAREHOUSELIST` | VARCHAR(4000) |  |  |  |  |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `AVAILABILITYPLANNINGSTATUS.COMPANYCODE = COMPANY.CODE` |
| `LOGICALWAREHOUSE_LOGICALWAREHOUSE` | `LOGICALWAREHOUSECOMPANYCODE`, `LOGICALWAREHOUSECODE` | [`LOGICALWAREHOUSE`](../WAREHOUSE/LOGICALWAREHOUSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `AVAILABILITYPLANNINGSTATUS.LOGICALWAREHOUSECOMPANYCODE = LOGICALWAREHOUSE.COMPANYCODE AND AVAILABILITYPLANNINGSTATUS.LOGICALWAREHOUSECODE = LOGICALWAREHOUSE.CODE` |
| `UNITOFMEASURE_PRIMARYUOM` | `PRIMARYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `AVAILABILITYPLANNINGSTATUS.PRIMARYUOMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_SECONDARYUOM` | `SECONDARYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `AVAILABILITYPLANNINGSTATUS.SECONDARYUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `AVAILABILITYPLANNINGSTATUSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IDENTIFIER,
       t.LOGICALWAREHOUSECODE,
       t.PROJECTCODE,
       t.WARNINGS,
       t.PACKAGINGUOMCODE,
       t.PRIMARYUOMCODE,
       t.SECONDARYUOMCODE,
       t.PLANBASEPRIMARYQUANTITY,
       t.PLANBASESECONDARYQUANTITY,
       t.PLANBASEPACKAGINGQUANTITY,
       t.NETBASEPRIMARYQUANTITY
FROM   DB2ADMIN.AVAILABILITYPLANNINGSTATUS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
