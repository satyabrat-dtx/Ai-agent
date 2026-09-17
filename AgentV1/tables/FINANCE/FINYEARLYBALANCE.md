# DB2ADMIN.FINYEARLYBALANCE

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `BUSINESSUNITCODE`, `FINANCIALYEARCODE`, `GLCODE`, `SLCUSTOMERSUPPLIERTYPE`, `SLCUSTOMERSUPPLIERCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 180892

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FINANCIALYEARCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `FINANCIALYEARCODE` | DECIMAL(4,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `GLCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `GLCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 6 | `SLCUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 7 | `SLCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 8 | `AMOUNTINCC` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINYEARLYBALANCE.COMPANYCODE = COMPANY.CODE` |
| `FINBUSINESSUNIT_BUSINESSUNIT` | `COMPANYCODE`, `BUSINESSUNITCODE` | [`FINBUSINESSUNIT`](../FINANCE/FINBUSINESSUNIT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINYEARLYBALANCE.COMPANYCODE = FINBUSINESSUNIT.COMPANYCODE AND FINYEARLYBALANCE.BUSINESSUNITCODE = FINBUSINESSUNIT.CODE` |
| `FINFINANCIALYEAR_FINANCIALYEAR` | `FINANCIALYEARCOMPANYCODE`, `FINANCIALYEARCODE` | [`FINFINANCIALYEAR`](../FINANCE/FINFINANCIALYEAR.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINYEARLYBALANCE.FINANCIALYEARCOMPANYCODE = FINFINANCIALYEAR.COMPANYCODE AND FINYEARLYBALANCE.FINANCIALYEARCODE = FINFINANCIALYEAR.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINYEARLYBALANCEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.FINANCIALYEARCOMPANYCODE,
       t.FINANCIALYEARCODE,
       t.GLCOMPANYCODE,
       t.GLCODE,
       t.SLCUSTOMERSUPPLIERTYPE,
       t.SLCUSTOMERSUPPLIERCODE,
       t.AMOUNTINCC,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.FINYEARLYBALANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
