# DB2ADMIN.ARREARCALCULATEDAMOUNTDETAILS

- **Module**: `HR` (low confidence — FK neighbourhood: 2 of 3 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 29
- **Primary key**: `COMPANYCODE`, `EMPLOYEEIDCODE`, `ATTENDANCETYPECODE`, `PAYROLLTYPECODE`, `PROCESSPERIOD`, `ATTDPROCESSPERIOD`, `PAYELEMENTTYPE`, `PAYELEMENTCODE`, `ARREARNO`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 165008

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ATTENDANCETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PAYROLLTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `PROCESSPERIOD` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `ATTDPROCESSPERIOD` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `PAYELEMENTTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 7 | `PAYELEMENTCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 8 | `ARREARNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 9 | `INCREMENTNO` | INTEGER | NOT NULL |  |  |  |
| 10 | `PROCESSPRFROMDATE` | DATE |  |  |  |  |
| 11 | `PROCESSPRTODATE` | DATE |  |  |  |  |
| 12 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `COSTCENTERCODE` | CHAR(20) |  | FK | foreign_key |  |
| 14 | `AMTCALCULATED` | DECIMAL(18,5) |  |  |  |  |
| 15 | `TEMPLATECODE` | CHAR(10) |  | FK | foreign_key |  |
| 16 | `PRIORITYNOFORPRINTING` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 17 | `FLAGCORRORINCREMENT` | CHAR(1) | NOT NULL |  |  |  |
| 18 | `FLAGPAYABLE` | INTEGER | NOT NULL |  |  |  |
| 19 | `FLAGAUTHORIZED` | INTEGER | NOT NULL |  |  |  |
| 20 | `FLAGLUMPSUMAMT` | INTEGER | NOT NULL |  |  |  |
| 21 | `FLAGATTENDANCEDEPENDENT` | INTEGER | NOT NULL |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 27 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 28 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ATTENDANCETYPE_ATTENDANCETYPE` | `COMPANYCODE`, `ATTENDANCETYPECODE` | [`ATTENDANCETYPE`](../HR/ATTENDANCETYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ARREARCALCULATEDAMOUNTDETAILS.COMPANYCODE = ATTENDANCETYPE.COMPANYCODE AND ARREARCALCULATEDAMOUNTDETAILS.ATTENDANCETYPECODE = ATTENDANCETYPE.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ARREARCALCULATEDAMOUNTDETAILS.COMPANYCODE = COMPANY.CODE` |
| `COSTCENTER_COSTCENTER` | `COSTCENTERCOMPANYCODE`, `COSTCENTERCODE` | [`COSTCENTER`](../COSTING/COSTCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ARREARCALCULATEDAMOUNTDETAILS.COSTCENTERCOMPANYCODE = COSTCENTER.COMPANYCODE AND ARREARCALCULATEDAMOUNTDETAILS.COSTCENTERCODE = COSTCENTER.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ARREARCALCULATEDAMOUNTDETAILS.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ARREARCALCULATEDAMOUNTDETAILS.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `PAYTEMPLATE_TEMPLATE` | `COMPANYCODE`, `TEMPLATECODE` | [`PAYTEMPLATE`](../HR/PAYTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ARREARCALCULATEDAMOUNTDETAILS.COMPANYCODE = PAYTEMPLATE.COMPANYCODE AND ARREARCALCULATEDAMOUNTDETAILS.TEMPLATECODE = PAYTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EARCALCULATEDAMOUNTDETAILSUID` (ABSUNIQUEID)
- `ARRCALCAMTDET1` (COMPANYCODE, EMPLOYEEIDCODE, ATTENDANCETYPECODE, PAYROLLTYPECODE, PROCESSPERIOD, PAYELEMENTTYPE, PAYELEMENTCODE, FLAGAUTHORIZED)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.ATTENDANCETYPECODE,
       t.PAYROLLTYPECODE,
       t.PROCESSPERIOD,
       t.ATTDPROCESSPERIOD,
       t.PAYELEMENTTYPE,
       t.PAYELEMENTCODE,
       t.ARREARNO,
       t.INCREMENTNO,
       t.PROCESSPRFROMDATE,
       t.PROCESSPRTODATE
FROM   DB2ADMIN.ARREARCALCULATEDAMOUNTDETAILS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
