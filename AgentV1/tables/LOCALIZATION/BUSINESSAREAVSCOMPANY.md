# DB2ADMIN.BUSINESSAREAVSCOMPANY

- **Module**: `LOCALIZATION` (low confidence — FK neighbourhood: 1 of 1 related tables are LOCALIZATION)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `FACTORYCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 121341

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `FACTORYCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `FACTORYCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `BUSINESSAREACODE` | CHAR(50) |  | FK | foreign_key |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BUSINESSAREAMASTER_BUSINESSAREA` | `BUSINESSAREACODE` | [`BUSINESSAREAMASTER`](../LOCALIZATION/BUSINESSAREAMASTER.md) | `CODE` | RESTRICT | `BUSINESSAREAVSCOMPANY.BUSINESSAREACODE = BUSINESSAREAMASTER.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BUSINESSAREAVSCOMPANY.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BUSINESSAREAVSCOMPANY.COMPANYCODE = DIVISION.COMPANYCODE AND BUSINESSAREAVSCOMPANY.DIVISIONCODE = DIVISION.CODE` |
| `PLANT_FACTORY` | `FACTORYCOMPANYCODE`, `FACTORYCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BUSINESSAREAVSCOMPANY.FACTORYCOMPANYCODE = PLANT.COMPANYCODE AND BUSINESSAREAVSCOMPANY.FACTORYCODE = PLANT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BUSINESSAREAVSCOMPANYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.FACTORYCOMPANYCODE,
       t.FACTORYCODE,
       t.BUSINESSAREACODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.BUSINESSAREAVSCOMPANY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
