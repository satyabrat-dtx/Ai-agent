# DB2ADMIN.REPLENISHMENTREQUISITIONIE

- **Module**: `WAREHOUSE` (low confidence — FK neighbourhood: 1 of 1 related tables are WAREHOUSE)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `COMPANYCODE`, `REQUISITIONTEMPLATECODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 129892

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `REQUISITIONTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `BUYERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `BUYERCODE` | CHAR(50) |  | FK | foreign_key |  |
| 5 | `REMARK` | VARCHAR(200) |  |  |  |  |
| 6 | `ORDERPRIORITY` | CHAR(2) |  |  |  |  |
| 7 | `REQUESTREASON` | VARCHAR(200) |  |  |  |  |
| 8 | `SUGGESTEDSUPPLIER` | CHAR(100) |  |  |  |  |
| 9 | `DEPARTMENTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `REPLENISHMENTREQUISITIONIE.COMPANYCODE = COMPANY.CODE` |
| `DEPARTMENT_DEPARTMENT` | `COMPANYCODE`, `DEPARTMENTCODE` | [`DEPARTMENT`](../WAREHOUSE/DEPARTMENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `REPLENISHMENTREQUISITIONIE.COMPANYCODE = DEPARTMENT.COMPANYCODE AND REPLENISHMENTREQUISITIONIE.DEPARTMENTCODE = DEPARTMENT.CODE` |
| `INITIALS_BUYER` | `BUYERCOMPANYCODE`, `BUYERCODE` | [`INITIALS`](../CORE_MASTER/INITIALS.md) | `COMPANYCODE`, `CODE` | RESTRICT | `REPLENISHMENTREQUISITIONIE.BUYERCOMPANYCODE = INITIALS.COMPANYCODE AND REPLENISHMENTREQUISITIONIE.BUYERCODE = INITIALS.CODE` |
| `REQUISITIONTEMPLATE_REQUISITIONTEMPLATE` | `COMPANYCODE`, `REQUISITIONTEMPLATECODE` | [`REQUISITIONTEMPLATE`](../CORE_MASTER/REQUISITIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `REPLENISHMENTREQUISITIONIE.COMPANYCODE = REQUISITIONTEMPLATE.COMPANYCODE AND REPLENISHMENTREQUISITIONIE.REQUISITIONTEMPLATECODE = REQUISITIONTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `REPLENISHMENTREQUISITIONIEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.REQUISITIONTEMPLATECODE,
       t.CODE,
       t.BUYERCOMPANYCODE,
       t.BUYERCODE,
       t.REMARK,
       t.ORDERPRIORITY,
       t.REQUESTREASON,
       t.SUGGESTEDSUPPLIER,
       t.DEPARTMENTCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.REPLENISHMENTREQUISITIONIE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
