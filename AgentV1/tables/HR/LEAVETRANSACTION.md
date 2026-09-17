# DB2ADMIN.LEAVETRANSACTION

- **Module**: `HR` (high confidence — table name starts with 'LEAVE')
- **Roles**: `business_data`
- **Columns**: 29
- **Primary key**: `COMPANYCODE`, `LEAVECALENDARCALENDARCODE`, `EMPLOYEECODE`, `LEAVECODE`, `SERIALNUMBER`
- **FK degree**: referenced by 1 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 170189

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `LEAVECALENDARCALENDARCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LEAVECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SERIALNUMBER` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 5 | `DATELEAVEFROM` | DATE |  |  |  |  |
| 6 | `DATELEAVETO` | DATE |  |  |  |  |
| 7 | `NOOFLEAVEDAYS` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 8 | `NOOFHOURS` | DECIMAL(7,3) |  |  |  |  |
| 9 | `SESSIONLEAVEFROM` | INTEGER | NOT NULL |  |  |  |
| 10 | `SESSIONLEAVETO` | INTEGER | NOT NULL |  |  |  |
| 11 | `NOTIFYDATE` | DATE |  |  |  |  |
| 12 | `LEAVEDONATEDTOCODE` | CHAR(9) |  | FK | foreign_key |  |
| 13 | `NOOFLEAVEDAYSDONATED` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 14 | `ADJUSTMENTFLAG` | INTEGER | NOT NULL |  |  |  |
| 15 | `NOOFADJUSTMENTLEAVEDAYS` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 16 | `TRANSACTIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 17 | `LEAVEREASON` | CHAR(100) |  |  |  |  |
| 18 | `FLAGAUTHORIZED` | INTEGER | NOT NULL |  |  |  |
| 19 | `REQPENDINGWITH` | CHAR(10) |  |  |  |  |
| 20 | `AUTHLEVEL` | CHAR(10) |  |  |  |  |
| 21 | `APPROVEDBYCODE` | CHAR(9) |  | FK | foreign_key |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 27 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 28 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LEAVETRANSACTION.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_APPROVEDBY` | `COMPANYCODE`, `APPROVEDBYCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LEAVETRANSACTION.COMPANYCODE = EMPLOYEE.COMPANYCODE AND LEAVETRANSACTION.APPROVEDBYCODE = EMPLOYEE.CODE` |
| `EMPLOYEE_EMPLOYEE` | `COMPANYCODE`, `EMPLOYEECODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LEAVETRANSACTION.COMPANYCODE = EMPLOYEE.COMPANYCODE AND LEAVETRANSACTION.EMPLOYEECODE = EMPLOYEE.CODE` |
| `EMPLOYEE_LEAVEDONATEDTO` | `COMPANYCODE`, `LEAVEDONATEDTOCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LEAVETRANSACTION.COMPANYCODE = EMPLOYEE.COMPANYCODE AND LEAVETRANSACTION.LEAVEDONATEDTOCODE = EMPLOYEE.CODE` |
| `LEAVECALENDAR_LEAVECALENDAR` | `COMPANYCODE`, `LEAVECALENDARCALENDARCODE` | [`LEAVECALENDAR`](../HR/LEAVECALENDAR.md) | `COMPANYCODE`, `CALENDARCODE` | RESTRICT | `LEAVETRANSACTION.COMPANYCODE = LEAVECALENDAR.COMPANYCODE AND LEAVETRANSACTION.LEAVECALENDARCALENDARCODE = LEAVECALENDAR.CALENDARCODE` |
| `LEAVE_LEAVE` | `COMPANYCODE`, `LEAVECODE` | [`LEAVE`](../HR/LEAVE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LEAVETRANSACTION.COMPANYCODE = LEAVE.COMPANYCODE AND LEAVETRANSACTION.LEAVECODE = LEAVE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `LEAVETRANSACTION_CANCELLATION` | [`LEAVECANCELLATION`](../HR/LEAVECANCELLATION.md) | `COMPANYCODE`, `LEAVECALENDARCALENDARCODE`, `EMPLOYEECODE`, `LEAVECODE`, `CANCELLATIONSERIALNUMBER` | `LEAVECANCELLATION.COMPANYCODE = LEAVETRANSACTION.COMPANYCODE AND LEAVECANCELLATION.LEAVECALENDARCALENDARCODE = LEAVETRANSACTION.LEAVECALENDARCALENDARCODE AND LEAVECANCELLATION.EMPLOYEECODE = LEAVETRANSACTION.EMPLOYEECODE AND LEAVECANCELLATION.LEAVECODE = LEAVETRANSACTION.LEAVECODE AND LEAVECANCELLATION.CANCELLATIONSERIALNUMBER = LEAVETRANSACTION.SERIALNUMBER` |

## Indexes

- `LEAVETRANSACTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.LEAVECALENDARCALENDARCODE,
       t.EMPLOYEECODE,
       t.LEAVECODE,
       t.SERIALNUMBER,
       t.DATELEAVEFROM,
       t.DATELEAVETO,
       t.NOOFLEAVEDAYS,
       t.NOOFHOURS,
       t.SESSIONLEAVEFROM,
       t.SESSIONLEAVETO,
       t.NOTIFYDATE
FROM   DB2ADMIN.LEAVETRANSACTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
