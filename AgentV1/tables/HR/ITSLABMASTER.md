# DB2ADMIN.ITSLABMASTER

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `FINANCIALYEARCODE`, `SENIORCITIZEN`, `GENDER`, `SLABFROM`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 157230

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `FINANCIALYEARCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SENIORCITIZEN` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `GENDER` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `SLABFROM` | DECIMAL(17,2) | NOT NULL | PK | primary_key |  |
| 5 | `SLABTO` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 6 | `ITPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 7 | `SURCHARGEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 8 | `CESSPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 9 | `HIGHERCESSPER` | DECIMAL(5,2) |  |  |  |  |
| 10 | `REBATEAMT` | DECIMAL(15,5) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ITSLABMASTER.COMPANYCODE = COMPANY.CODE` |
| `PAYROLLFINANCIALYEAR_FINANCIALYEAR` | `COMPANYCODE`, `FINANCIALYEARCODE` | [`PAYROLLFINANCIALYEAR`](../HR/PAYROLLFINANCIALYEAR.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITSLABMASTER.COMPANYCODE = PAYROLLFINANCIALYEAR.COMPANYCODE AND ITSLABMASTER.FINANCIALYEARCODE = PAYROLLFINANCIALYEAR.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ITSLABMASTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.FINANCIALYEARCODE,
       t.SENIORCITIZEN,
       t.GENDER,
       t.SLABFROM,
       t.SLABTO,
       t.ITPERCENTAGE,
       t.SURCHARGEPERCENTAGE,
       t.CESSPERCENTAGE,
       t.HIGHERCESSPER,
       t.REBATEAMT,
       t.CREATIONDATETIME
FROM   DB2ADMIN.ITSLABMASTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
