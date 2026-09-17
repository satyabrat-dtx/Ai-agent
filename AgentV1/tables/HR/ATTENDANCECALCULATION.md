# DB2ADMIN.ATTENDANCECALCULATION

- **Module**: `HR` (high confidence — table name starts with 'ATTENDANCE')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `PROCESSPERIOD`, `ATTENDANCEPERIOD`, `EMPLOYEECODE`, `PROCESSTYPECODE`, `ATTENDANCETYPECODE`, `PAYELEMENTPAYELEMENTTYPE`, `PAYELEMENTCODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 165263

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PROCESSPERIOD` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `ATTENDANCEPERIOD` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PROCESSTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `ATTENDANCETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `PAYELEMENTPAYELEMENTTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `PAYELEMENTCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 8 | `ELEVALUE` | DECIMAL(11,4) | NOT NULL |  |  |  |
| 9 | `CORRECTIONFLAG` | CHAR(1) |  |  |  |  |
| 10 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ATTENDANCETYPE_ATTENDANCETYPE` | `COMPANYCODE`, `ATTENDANCETYPECODE` | [`ATTENDANCETYPE`](../HR/ATTENDANCETYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ATTENDANCECALCULATION.COMPANYCODE = ATTENDANCETYPE.COMPANYCODE AND ATTENDANCECALCULATION.ATTENDANCETYPECODE = ATTENDANCETYPE.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ATTENDANCECALCULATION.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEE` | `COMPANYCODE`, `EMPLOYEECODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ATTENDANCECALCULATION.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ATTENDANCECALCULATION.EMPLOYEECODE = EMPLOYEE.CODE` |
| `PAYELEMENT_PAYELEMENT` | `COMPANYCODE`, `PAYELEMENTPAYELEMENTTYPE`, `PAYELEMENTCODE` | [`PAYELEMENT`](../CORE_MASTER/PAYELEMENT.md) | `COMPANYCODE`, `PAYELEMENTTYPE`, `CODE` | RESTRICT | `ATTENDANCECALCULATION.COMPANYCODE = PAYELEMENT.COMPANYCODE AND ATTENDANCECALCULATION.PAYELEMENTPAYELEMENTTYPE = PAYELEMENT.PAYELEMENTTYPE AND ATTENDANCECALCULATION.PAYELEMENTCODE = PAYELEMENT.CODE` |
| `PAYROLLTYPE_PROCESSTYPE` | `COMPANYCODE`, `PROCESSTYPECODE` | [`PAYROLLTYPE`](../HR/PAYROLLTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ATTENDANCECALCULATION.COMPANYCODE = PAYROLLTYPE.COMPANYCODE AND ATTENDANCECALCULATION.PROCESSTYPECODE = PAYROLLTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ATTENDANCECALCULATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PROCESSPERIOD,
       t.ATTENDANCEPERIOD,
       t.EMPLOYEECODE,
       t.PROCESSTYPECODE,
       t.ATTENDANCETYPECODE,
       t.PAYELEMENTPAYELEMENTTYPE,
       t.PAYELEMENTCODE,
       t.ELEVALUE,
       t.CORRECTIONFLAG,
       t.FROMDATE,
       t.CREATIONDATETIME
FROM   DB2ADMIN.ATTENDANCECALCULATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
