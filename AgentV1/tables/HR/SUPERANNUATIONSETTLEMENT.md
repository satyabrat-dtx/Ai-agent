# DB2ADMIN.SUPERANNUATIONSETTLEMENT

- **Module**: `HR` (low confidence — FK neighbourhood: 2 of 2 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 26
- **Primary key**: `COMPANYCODE`, `EMPLOYEEIDCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 168758

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 2 | `LASTPROCESSCALENDARCODE` | CHAR(6) |  | FK | foreign_key |  |
| 3 | `CLOSINGBALANCE` | DECIMAL(17,4) |  |  |  |  |
| 4 | `SETTLEMENTTYPE` | INTEGER | NOT NULL |  |  |  |
| 5 | `SETTLEMENTDATE` | DATE |  |  |  |  |
| 6 | `ANNUITYCONTRIBUTION` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 7 | `SUPERANNUATIONTAX` | DECIMAL(11,2) |  |  |  |  |
| 8 | `ANNUITYAMOUNT` | DECIMAL(11,2) |  |  |  |  |
| 9 | `SETTLEMENTAMOUNT` | DECIMAL(11,2) |  |  |  |  |
| 10 | `PAYMENTMODE` | CHAR(1) | NOT NULL |  |  |  |
| 11 | `PROCESSPERIODNOPAYROLLCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `PROCESSPERIODNOPROCESSPERIOD` | INTEGER | NOT NULL | FK | foreign_key |  |
| 13 | `CHEQUENO` | CHAR(15) |  |  |  |  |
| 14 | `CHEQUEDATE` | DATE |  |  |  |  |
| 15 | `BANKNAME` | CHAR(15) |  |  |  |  |
| 16 | `AUTHORIZEDCODE` | CHAR(9) |  | FK | foreign_key |  |
| 17 | `AUTHORIZEDDATE` | DATE |  |  |  |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 24 | `STEP` | CHAR(1) |  |  |  |  |
| 25 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SUPERANNUATIONSETTLEMENT.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_AUTHORIZED` | `COMPANYCODE`, `AUTHORIZEDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SUPERANNUATIONSETTLEMENT.COMPANYCODE = EMPLOYEE.COMPANYCODE AND SUPERANNUATIONSETTLEMENT.AUTHORIZEDCODE = EMPLOYEE.CODE` |
| `PAYROLLPROCESSPERIOD_PROCESSPERIODNO` | `COMPANYCODE`, `PROCESSPERIODNOPAYROLLCODE`, `PROCESSPERIODNOPROCESSPERIOD` | [`PAYROLLPROCESSPERIOD`](../HR/PAYROLLPROCESSPERIOD.md) | `COMPANYCODE`, `PAYROLLCODE`, `PROCESSPERIOD` | RESTRICT | `SUPERANNUATIONSETTLEMENT.COMPANYCODE = PAYROLLPROCESSPERIOD.COMPANYCODE AND SUPERANNUATIONSETTLEMENT.PROCESSPERIODNOPAYROLLCODE = PAYROLLPROCESSPERIOD.PAYROLLCODE AND SUPERANNUATIONSETTLEMENT.PROCESSPERIODNOPROCESSPERIOD = PAYROLLPROCESSPERIOD.PROCESSPERIOD` |
| `SUPERANNUATIONCALENDAR_LASTPROCESSCALENDAR` | `COMPANYCODE`, `LASTPROCESSCALENDARCODE` | [`SUPERANNUATIONCALENDAR`](../HR/SUPERANNUATIONCALENDAR.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SUPERANNUATIONSETTLEMENT.COMPANYCODE = SUPERANNUATIONCALENDAR.COMPANYCODE AND SUPERANNUATIONSETTLEMENT.LASTPROCESSCALENDARCODE = SUPERANNUATIONCALENDAR.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SUPERANNUATIONSETTLEMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.LASTPROCESSCALENDARCODE,
       t.CLOSINGBALANCE,
       t.SETTLEMENTTYPE,
       t.SETTLEMENTDATE,
       t.ANNUITYCONTRIBUTION,
       t.SUPERANNUATIONTAX,
       t.ANNUITYAMOUNT,
       t.SETTLEMENTAMOUNT,
       t.PAYMENTMODE,
       t.PROCESSPERIODNOPAYROLLCODE
FROM   DB2ADMIN.SUPERANNUATIONSETTLEMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
