# DB2ADMIN.SUPERANNUATIONELIGIBILITY

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `COMPANYCODE`, `CALENDARYEARCODE`, `EMPLOYEEIDCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 168704

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CALENDARYEARCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 2 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `OPENINGBALANCE` | DECIMAL(17,4) |  |  |  |  |
| 4 | `CURRENTYEARCONTRIBUTION` | DECIMAL(17,4) |  |  |  |  |
| 5 | `INTERESTEARNED` | DECIMAL(17,4) |  |  |  |  |
| 6 | `TRANSFEROPENINGBALANCE` | DECIMAL(11,2) |  |  |  |  |
| 7 | `INTERESTPERCENTAGE` | DECIMAL(17,4) |  |  |  |  |
| 8 | `CLOSINGBALANCE` | DECIMAL(17,4) |  |  |  |  |
| 9 | `EXITDATE` | DATE |  |  |  |  |
| 10 | `CONTRIBUTIONPERCENTAGE` | INTEGER | NOT NULL |  |  |  |
| 11 | `SETTLEMENTAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 12 | `PAYMENTMODE` | CHAR(1) |  |  |  |  |
| 13 | `SETTLEMENTDATE` | DATE |  |  |  |  |
| 14 | `AUTHORIZEDFLAG` | CHAR(1) |  |  |  |  |
| 15 | `RECORDSTATUS` | SMALLINT | NOT NULL |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SUPERANNUATIONELIGIBILITY.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SUPERANNUATIONELIGIBILITY.COMPANYCODE = EMPLOYEE.COMPANYCODE AND SUPERANNUATIONELIGIBILITY.EMPLOYEEIDCODE = EMPLOYEE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SUPERANNUATIONELIGIBILITYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CALENDARYEARCODE,
       t.EMPLOYEEIDCODE,
       t.OPENINGBALANCE,
       t.CURRENTYEARCONTRIBUTION,
       t.INTERESTEARNED,
       t.TRANSFEROPENINGBALANCE,
       t.INTERESTPERCENTAGE,
       t.CLOSINGBALANCE,
       t.EXITDATE,
       t.CONTRIBUTIONPERCENTAGE,
       t.SETTLEMENTAMOUNT
FROM   DB2ADMIN.SUPERANNUATIONELIGIBILITY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
