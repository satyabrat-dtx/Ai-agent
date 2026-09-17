# DB2ADMIN.EMPLOYEEWISELEDGER

- **Module**: `HR` (high confidence — table name starts with 'EMPLOYEE')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `COMPANYCODE`, `EMPLOYEEIDCODE`, `CALENDARYEARCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 166145

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEEIDCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `CALENDARYEARCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 3 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 4 | `EXITDATE` | DATE |  |  |  |  |
| 5 | `INTEREST` | DECIMAL(5,2) |  |  |  |  |
| 6 | `OPENINGBALANCE` | DECIMAL(17,4) |  |  |  |  |
| 7 | `INTERESTEARNED` | DECIMAL(5,2) |  |  |  |  |
| 8 | `TRANSFEROPENBALANCE` | DECIMAL(11,2) |  |  |  |  |
| 9 | `TRANSFERINTEREST` | DECIMAL(5,2) |  |  |  |  |
| 10 | `CURRENTYEARCONTRIBUTION` | DECIMAL(17,4) |  |  |  |  |
| 11 | `CLOSINGBALANCE` | DECIMAL(17,4) |  |  |  |  |
| 12 | `ANNUITYAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 13 | `CONTRIBUTIONPERCENTAGE` | INTEGER | NOT NULL |  |  |  |
| 14 | `SETTLEMENTAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 15 | `AUTHORIZEDFLAG` | CHAR(1) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `EMPLOYEEWISELEDGER.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EMPLOYEEWISELEDGERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.CALENDARYEARCODE,
       t.FROMDATE,
       t.EXITDATE,
       t.INTEREST,
       t.OPENINGBALANCE,
       t.INTERESTEARNED,
       t.TRANSFEROPENBALANCE,
       t.TRANSFERINTEREST,
       t.CURRENTYEARCONTRIBUTION,
       t.CLOSINGBALANCE
FROM   DB2ADMIN.EMPLOYEEWISELEDGER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
