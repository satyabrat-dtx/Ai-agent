# DB2ADMIN.ITDEPOSITDETAIL

- **Module**: `HR` (low confidence — FK neighbourhood: 2 of 2 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `PROCESSPERIODNOPAYROLLCODE`, `PROCESSPERIODNOPROCESSPERIOD`, `FINANCIALYEARCODE`, `CHEQUENUMBER`, `BANKBSRCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 166692

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PROCESSPERIODNOPAYROLLCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PROCESSPERIODNOPROCESSPERIOD` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `FINANCIALYEARCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CHEQUENUMBER` | DECIMAL(9,0) | NOT NULL | PK | primary_key |  |
| 5 | `BANKBSRCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 6 | `DEPOSITDATE` | DATE | NOT NULL |  |  |  |
| 7 | `CHALLANNUMBER` | DECIMAL(15,0) | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ITDEPOSITDETAIL.COMPANYCODE = COMPANY.CODE` |
| `PAYROLLFINANCIALYEAR_FINANCIALYEAR` | `COMPANYCODE`, `FINANCIALYEARCODE` | [`PAYROLLFINANCIALYEAR`](../HR/PAYROLLFINANCIALYEAR.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITDEPOSITDETAIL.COMPANYCODE = PAYROLLFINANCIALYEAR.COMPANYCODE AND ITDEPOSITDETAIL.FINANCIALYEARCODE = PAYROLLFINANCIALYEAR.CODE` |
| `PAYROLLPROCESSPERIOD_PROCESSPERIODNO` | `COMPANYCODE`, `PROCESSPERIODNOPAYROLLCODE`, `PROCESSPERIODNOPROCESSPERIOD` | [`PAYROLLPROCESSPERIOD`](../HR/PAYROLLPROCESSPERIOD.md) | `COMPANYCODE`, `PAYROLLCODE`, `PROCESSPERIOD` | RESTRICT | `ITDEPOSITDETAIL.COMPANYCODE = PAYROLLPROCESSPERIOD.COMPANYCODE AND ITDEPOSITDETAIL.PROCESSPERIODNOPAYROLLCODE = PAYROLLPROCESSPERIOD.PAYROLLCODE AND ITDEPOSITDETAIL.PROCESSPERIODNOPROCESSPERIOD = PAYROLLPROCESSPERIOD.PROCESSPERIOD` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ITDEPOSITDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PROCESSPERIODNOPAYROLLCODE,
       t.PROCESSPERIODNOPROCESSPERIOD,
       t.FINANCIALYEARCODE,
       t.CHEQUENUMBER,
       t.BANKBSRCODE,
       t.DEPOSITDATE,
       t.CHALLANNUMBER,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.ITDEPOSITDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
