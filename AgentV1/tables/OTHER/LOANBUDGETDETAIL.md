# DB2ADMIN.LOANBUDGETDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `FACTORYCODE`, `LOANTYPE`, `LOANCODE`, `EFFECTIVEFROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 154607

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `FACTORYCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `FACTORYCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `LOANTYPE` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `LOANCODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 6 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 7 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 8 | `BUDGETLIMITAMOUNT` | DECIMAL(15,2) |  |  |  |  |
| 9 | `VERIFICATIONAPPLICABLEFLAG` | INTEGER | NOT NULL |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LOANBUDGETDETAIL.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LOANBUDGETDETAIL.COMPANYCODE = DIVISION.COMPANYCODE AND LOANBUDGETDETAIL.DIVISIONCODE = DIVISION.CODE` |
| `PLANT_FACTORY` | `FACTORYCOMPANYCODE`, `FACTORYCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LOANBUDGETDETAIL.FACTORYCOMPANYCODE = PLANT.COMPANYCODE AND LOANBUDGETDETAIL.FACTORYCODE = PLANT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LOANBUDGETDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.FACTORYCOMPANYCODE,
       t.FACTORYCODE,
       t.LOANTYPE,
       t.LOANCODE,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.BUDGETLIMITAMOUNT,
       t.VERIFICATIONAPPLICABLEFLAG,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.LOANBUDGETDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
