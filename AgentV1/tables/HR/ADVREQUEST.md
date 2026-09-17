# DB2ADMIN.ADVREQUEST

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `CODE`, `ACCIDENTNOCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 164894

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `YEAR` | CHAR(4) |  |  |  |  |
| 2 | `CODE` | BIGINT | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `EMPLOYEENOCODE` | CHAR(9) |  | FK | foreign_key |  |
| 4 | `ACCIDENTNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `FLAGILLACC` | INTEGER | NOT NULL |  |  |  |
| 6 | `PAYMENTMODE` | INTEGER | NOT NULL |  |  |  |
| 7 | `AMTPAID` | INTEGER | NOT NULL |  |  |  |
| 8 | `CHEQUENO` | INTEGER | NOT NULL |  |  |  |
| 9 | `CHEQUEDATE` | DATE |  |  |  |  |
| 10 | `BANKNAME` | CHAR(30) |  |  |  |  |
| 11 | `PAYAPPROVEDBYCODE` | CHAR(9) |  | FK | foreign_key |  |
| 12 | `PAYDATE` | DATE | NOT NULL |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACCINTIMATION_ACCIDENTNO` | `COMPANYCODE`, `ACCIDENTNOCODE` | [`ACCINTIMATION`](../HR/ACCINTIMATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ADVREQUEST.COMPANYCODE = ACCINTIMATION.COMPANYCODE AND ADVREQUEST.ACCIDENTNOCODE = ACCINTIMATION.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ADVREQUEST.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEENO` | `COMPANYCODE`, `EMPLOYEENOCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ADVREQUEST.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ADVREQUEST.EMPLOYEENOCODE = EMPLOYEE.CODE` |
| `EMPLOYEE_PAYAPPROVEDBY` | `COMPANYCODE`, `PAYAPPROVEDBYCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ADVREQUEST.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ADVREQUEST.PAYAPPROVEDBYCODE = EMPLOYEE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ADVREQUESTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.YEAR,
       t.CODE,
       t.EMPLOYEENOCODE,
       t.ACCIDENTNOCODE,
       t.FLAGILLACC,
       t.PAYMENTMODE,
       t.AMTPAID,
       t.CHEQUENO,
       t.CHEQUEDATE,
       t.BANKNAME,
       t.PAYAPPROVEDBYCODE
FROM   DB2ADMIN.ADVREQUEST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
