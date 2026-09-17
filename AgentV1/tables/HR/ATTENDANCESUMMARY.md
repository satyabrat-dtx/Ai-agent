# DB2ADMIN.ATTENDANCESUMMARY

- **Module**: `HR` (high confidence — table name starts with 'ATTENDANCE')
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `COMPANYCODE`, `PRLPROCESSTYPECODE`, `ATTENDANCETYPECODE`, `PRLPROCESSPERIOD`, `ATTDPROCESSPERIOD`, `EMPLOYEECODE`, `ATTDFROMDATE`, `ATTENDANCECODE`, `LEAVECODE`, `FROMCOSTCENTERBADLICODE`, `TOCOSTCENTERBADLICODE`, `BADLIFLAG`, `FLAGPAYABLE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 165747

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PRLPROCESSTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `ATTENDANCETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PRLPROCESSPERIOD` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `ATTDPROCESSPERIOD` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `ATTDFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 7 | `ATTDTODATE` | DATE |  |  |  |  |
| 8 | `ATTENDANCECODE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 9 | `LEAVECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 10 | `FROMCOSTCENTERBADLICODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 11 | `TOCOSTCENTERBADLICODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 12 | `BADLIFLAG` | INTEGER | NOT NULL | PK | primary_key |  |
| 13 | `TOTALPAYABLEDAYS` | DECIMAL(9,5) |  |  |  |  |
| 14 | `TOTALHRS` | DECIMAL(5,2) |  |  |  |  |
| 15 | `FLAGPAYABLE` | INTEGER | NOT NULL | PK | primary_key |  |
| 16 | `SPLPAYPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 17 | `PERFORMPAYPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 18 | `INCENTIVEPAYPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 19 | `DAILYAMT` | DECIMAL(9,2) |  |  |  |  |
| 20 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 21 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 22 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 23 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 24 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 25 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 26 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ATTENDANCETYPE_ATTENDANCETYPE` | `COMPANYCODE`, `ATTENDANCETYPECODE` | [`ATTENDANCETYPE`](../HR/ATTENDANCETYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ATTENDANCESUMMARY.COMPANYCODE = ATTENDANCETYPE.COMPANYCODE AND ATTENDANCESUMMARY.ATTENDANCETYPECODE = ATTENDANCETYPE.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ATTENDANCESUMMARY.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEE` | `COMPANYCODE`, `EMPLOYEECODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ATTENDANCESUMMARY.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ATTENDANCESUMMARY.EMPLOYEECODE = EMPLOYEE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ATTENDANCESUMMARYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PRLPROCESSTYPECODE,
       t.ATTENDANCETYPECODE,
       t.PRLPROCESSPERIOD,
       t.ATTDPROCESSPERIOD,
       t.EMPLOYEECODE,
       t.ATTDFROMDATE,
       t.ATTDTODATE,
       t.ATTENDANCECODE,
       t.LEAVECODE,
       t.FROMCOSTCENTERBADLICODE,
       t.TOCOSTCENTERBADLICODE
FROM   DB2ADMIN.ATTENDANCESUMMARY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
