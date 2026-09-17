# DB2ADMIN.LEAVEENCASHMENT

- **Module**: `HR` (high confidence — table name starts with 'LEAVE')
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `COMPANYCODE`, `EMPLOYEEIDCODE`, `LEAVECALENDARCALENDARCODE`, `LEAVECODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 167190

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LEAVECALENDARCALENDARCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LEAVECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `LINENO` | BIGINT | NOT NULL | PK | primary_key |  |
| 5 | `CALENDARYEAR` | INTEGER | NOT NULL |  |  |  |
| 6 | `PAYMENTMETHOD` | CHAR(1) | NOT NULL |  |  |  |
| 7 | `PAYROLLTYPECODE` | CHAR(4) |  |  |  |  |
| 8 | `PAYROLLPROCESSPRDNO` | INTEGER | NOT NULL |  |  |  |
| 9 | `CYRBALANCELEAVE` | DECIMAL(5,2) |  |  |  |  |
| 10 | `FLAGEARNINGORDED` | CHAR(1) |  | FK | foreign_key |  |
| 11 | `PRFORMULACODE` | CHAR(6) |  | FK | foreign_key |  |
| 12 | `PAYELEMENTCODE` | CHAR(6) |  | FK | foreign_key |  |
| 13 | `CYRENCASHEDLEAVE` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 14 | `AMTTRANSACTION` | DECIMAL(11,2) |  |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LEAVEENCASHMENT.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LEAVEENCASHMENT.COMPANYCODE = EMPLOYEE.COMPANYCODE AND LEAVEENCASHMENT.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `FORMULACODE_PRFORMULA` | `COMPANYCODE`, `PRFORMULACODE` | [`FORMULACODE`](../HR/FORMULACODE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LEAVEENCASHMENT.COMPANYCODE = FORMULACODE.COMPANYCODE AND LEAVEENCASHMENT.PRFORMULACODE = FORMULACODE.CODE` |
| `LEAVECALENDAR_LEAVECALENDAR` | `COMPANYCODE`, `LEAVECALENDARCALENDARCODE` | [`LEAVECALENDAR`](../HR/LEAVECALENDAR.md) | `COMPANYCODE`, `CALENDARCODE` | RESTRICT | `LEAVEENCASHMENT.COMPANYCODE = LEAVECALENDAR.COMPANYCODE AND LEAVEENCASHMENT.LEAVECALENDARCALENDARCODE = LEAVECALENDAR.CALENDARCODE` |
| `LEAVE_LEAVE` | `COMPANYCODE`, `LEAVECODE` | [`LEAVE`](../HR/LEAVE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LEAVEENCASHMENT.COMPANYCODE = LEAVE.COMPANYCODE AND LEAVEENCASHMENT.LEAVECODE = LEAVE.CODE` |
| `PAYELEMENT_PAYELEMENT` | `COMPANYCODE`, `FLAGEARNINGORDED`, `PAYELEMENTCODE` | [`PAYELEMENT`](../CORE_MASTER/PAYELEMENT.md) | `COMPANYCODE`, `PAYELEMENTTYPE`, `CODE` | RESTRICT | `LEAVEENCASHMENT.COMPANYCODE = PAYELEMENT.COMPANYCODE AND LEAVEENCASHMENT.FLAGEARNINGORDED = PAYELEMENT.PAYELEMENTTYPE AND LEAVEENCASHMENT.PAYELEMENTCODE = PAYELEMENT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LEAVEENCASHMENTUID` (ABSUNIQUEID)
- `LEAVEENCASH1` (COMPANYCODE, EMPLOYEEIDCODE, PAYROLLTYPECODE, PAYROLLPROCESSPRDNO)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.LEAVECALENDARCALENDARCODE,
       t.LEAVECODE,
       t.LINENO,
       t.CALENDARYEAR,
       t.PAYMENTMETHOD,
       t.PAYROLLTYPECODE,
       t.PAYROLLPROCESSPRDNO,
       t.CYRBALANCELEAVE,
       t.FLAGEARNINGORDED,
       t.PRFORMULACODE
FROM   DB2ADMIN.LEAVEENCASHMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
