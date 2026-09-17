# DB2ADMIN.BOND

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `FACTORYCODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 121251

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `FACTORYCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `FACTORYCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CODE` | CHAR(30) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `GPTYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `BONDDATE` | DATE |  |  |  |  |
| 7 | `BONDEXPDATE` | DATE |  |  |  |  |
| 8 | `BONDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 9 | `BONDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `BALANCEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `BALANCEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 12 | `LASTCLEARDT` | DATE |  |  |  |  |
| 13 | `FILENO` | CHAR(100) |  |  |  |  |
| 14 | `PARCONNAMECUSTOMERSUPPLIERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 15 | `PARCONNAMECUSTOMERSUPPLIERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 16 | `MAINBONDNO` | CHAR(50) |  |  |  |  |
| 17 | `MBAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 18 | `BNDATE` | DATE |  |  |  |  |
| 19 | `EXPDATE` | DATE |  |  |  |  |
| 20 | `NAMEEXC` | CHAR(100) |  |  |  |  |
| 21 | `NAMEPARTYCUSTOMERSUPPLIERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 22 | `NAMEPARTYCUSTOMERSUPPLIERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BOND.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BOND.COMPANYCODE = DIVISION.COMPANYCODE AND BOND.DIVISIONCODE = DIVISION.CODE` |
| `ORDERPARTNER_NAMEPARTY` | `COMPANYCODE`, `NAMEPARTYCUSTOMERSUPPLIERTYPE`, `NAMEPARTYCUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `BOND.COMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND BOND.NAMEPARTYCUSTOMERSUPPLIERTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND BOND.NAMEPARTYCUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |
| `ORDERPARTNER_PARCONNAME` | `COMPANYCODE`, `PARCONNAMECUSTOMERSUPPLIERTYPE`, `PARCONNAMECUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `BOND.COMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND BOND.PARCONNAMECUSTOMERSUPPLIERTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND BOND.PARCONNAMECUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |
| `PLANT_FACTORY` | `FACTORYCOMPANYCODE`, `FACTORYCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BOND.FACTORYCOMPANYCODE = PLANT.COMPANYCODE AND BOND.FACTORYCODE = PLANT.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `BOND_BOND` | [`AR3`](../SALES/AR3.md) | `COMPANYCODE`, `BONDDIVISIONCODE`, `BONDFACTORYCODE`, `BONDCODE` | `AR3.COMPANYCODE = BOND.COMPANYCODE AND AR3.BONDDIVISIONCODE = BOND.DIVISIONCODE AND AR3.BONDFACTORYCODE = BOND.FACTORYCODE AND AR3.BONDCODE = BOND.CODE` |
| `BOND_BOND` | [`AR4`](../SALES/AR4.md) | `COMPANYCODE`, `BONDDIVISIONCODE`, `BONDFACTORYCODE`, `BONDCODE` | `AR4.COMPANYCODE = BOND.COMPANYCODE AND AR4.BONDDIVISIONCODE = BOND.DIVISIONCODE AND AR4.BONDFACTORYCODE = BOND.FACTORYCODE AND AR4.BONDCODE = BOND.CODE` |

## Indexes

- `BONDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.FACTORYCOMPANYCODE,
       t.FACTORYCODE,
       t.CODE,
       t.GPTYPE,
       t.BONDDATE,
       t.BONDEXPDATE,
       t.BONDQUANTITY,
       t.BONDAMOUNT,
       t.BALANCEAMOUNT,
       t.BALANCEQUANTITY
FROM   DB2ADMIN.BOND t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
