# DB2ADMIN.DIVISIONCREDITCHECKLEVEL

- **Module**: `CORE_MASTER` (high confidence — table name starts with 'DIVISION')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 128944

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `CREDITCHECKLEVEL` | CHAR(2) | NOT NULL |  |  |  |
| 3 | `NOCREDITCHECK` | SMALLINT | NOT NULL |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `DIVISIONCREDITCHECKLEVEL.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DIVISIONCREDITCHECKLEVEL.COMPANYCODE = DIVISION.COMPANYCODE AND DIVISIONCREDITCHECKLEVEL.DIVISIONCODE = DIVISION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DIVISIONCREDITCHECKLEVELUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CREDITCHECKLEVEL,
       t.NOCREDITCHECK,
       t.ABSUNIQUEID
FROM   DB2ADMIN.DIVISIONCREDITCHECKLEVEL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
