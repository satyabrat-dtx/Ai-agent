# DB2ADMIN.PRCALCULATEDAMOUNTDETAILS

- **Module**: `HR` (low confidence — FK neighbourhood: 2 of 2 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `COMPANYCODE`, `EMPLOYEEIDCODE`, `ATTENDANCETYPECODE`, `PAYROLLTYPECODE`, `PROCESSPERIOD`, `PAYELEMENTTYPE`, `PAYELEMENTCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 167881

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ATTENDANCETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PAYROLLTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `PROCESSPERIOD` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `PAYELEMENTTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 6 | `PAYELEMENTCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 7 | `PROCESSPRFROMDATE` | DATE |  |  |  |  |
| 8 | `PROCESSPRTODATE` | DATE |  |  |  |  |
| 9 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 10 | `AMTCALCULATED` | DECIMAL(18,5) |  |  |  |  |
| 11 | `TEMPLATECODE` | CHAR(10) |  | FK | foreign_key |  |
| 12 | `PRIORITYNOFORPRINTING` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 13 | `FLAGPAYABLE` | INTEGER | NOT NULL |  |  |  |
| 14 | `FLAGAUTHORIZED` | INTEGER | NOT NULL |  |  |  |
| 15 | `FLAGLUMPSUMAMT` | INTEGER | NOT NULL |  |  |  |
| 16 | `FLAGATTENDANCEDEPENDENT` | INTEGER | NOT NULL |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ATTENDANCETYPE_ATTENDANCETYPE` | `COMPANYCODE`, `ATTENDANCETYPECODE` | [`ATTENDANCETYPE`](../HR/ATTENDANCETYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRCALCULATEDAMOUNTDETAILS.COMPANYCODE = ATTENDANCETYPE.COMPANYCODE AND PRCALCULATEDAMOUNTDETAILS.ATTENDANCETYPECODE = ATTENDANCETYPE.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRCALCULATEDAMOUNTDETAILS.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRCALCULATEDAMOUNTDETAILS.COMPANYCODE = EMPLOYEE.COMPANYCODE AND PRCALCULATEDAMOUNTDETAILS.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `PAYTEMPLATE_TEMPLATE` | `COMPANYCODE`, `TEMPLATECODE` | [`PAYTEMPLATE`](../HR/PAYTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRCALCULATEDAMOUNTDETAILS.COMPANYCODE = PAYTEMPLATE.COMPANYCODE AND PRCALCULATEDAMOUNTDETAILS.TEMPLATECODE = PAYTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRCALCULATEDAMOUNTDETAILSUID` (ABSUNIQUEID)
- `PRLCALAMTDET1` (COMPANYCODE, EMPLOYEEIDCODE, ATTENDANCETYPECODE, PAYROLLTYPECODE, PAYELEMENTTYPE, PAYELEMENTCODE)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.ATTENDANCETYPECODE,
       t.PAYROLLTYPECODE,
       t.PROCESSPERIOD,
       t.PAYELEMENTTYPE,
       t.PAYELEMENTCODE,
       t.PROCESSPRFROMDATE,
       t.PROCESSPRTODATE,
       t.COSTCENTERCODE,
       t.AMTCALCULATED,
       t.TEMPLATECODE
FROM   DB2ADMIN.PRCALCULATEDAMOUNTDETAILS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
