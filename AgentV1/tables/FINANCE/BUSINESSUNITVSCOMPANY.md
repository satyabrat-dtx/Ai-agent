# DB2ADMIN.BUSINESSUNITVSCOMPANY

- **Module**: `FINANCE` (low confidence — FK neighbourhood: 1 of 1 related tables are FINANCE)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `FACTORYCODE`, `BUSINESSUNITCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 173688

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `FACTORYCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `FACTORYCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BUSINESSUNITVSCOMPANY.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BUSINESSUNITVSCOMPANY.COMPANYCODE = DIVISION.COMPANYCODE AND BUSINESSUNITVSCOMPANY.DIVISIONCODE = DIVISION.CODE` |
| `FINBUSINESSUNIT_BUSINESSUNIT` | `COMPANYCODE`, `BUSINESSUNITCODE` | [`FINBUSINESSUNIT`](../FINANCE/FINBUSINESSUNIT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BUSINESSUNITVSCOMPANY.COMPANYCODE = FINBUSINESSUNIT.COMPANYCODE AND BUSINESSUNITVSCOMPANY.BUSINESSUNITCODE = FINBUSINESSUNIT.CODE` |
| `PLANT_FACTORY` | `FACTORYCOMPANYCODE`, `FACTORYCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BUSINESSUNITVSCOMPANY.FACTORYCOMPANYCODE = PLANT.COMPANYCODE AND BUSINESSUNITVSCOMPANY.FACTORYCODE = PLANT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BUSINESSUNITVSCOMPANYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.FACTORYCOMPANYCODE,
       t.FACTORYCODE,
       t.BUSINESSUNITCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.BUSINESSUNITVSCOMPANY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
