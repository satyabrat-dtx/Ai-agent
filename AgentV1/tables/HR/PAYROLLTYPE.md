# DB2ADMIN.PAYROLLTYPE

- **Module**: `HR` (high confidence — table name starts with 'PAYROLL')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 8 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 155410

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PAYROLLTYPE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 8

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PAYROLLTYPE_LINE` | [`PAYROLLTYPEDETAIL`](../HR/PAYROLLTYPEDETAIL.md) | `PAYROLLTYPECOMPANYCODE`, `PAYROLLTYPECODE` | `PAYROLLTYPEDETAIL.PAYROLLTYPECOMPANYCODE = PAYROLLTYPE.COMPANYCODE AND PAYROLLTYPEDETAIL.PAYROLLTYPECODE = PAYROLLTYPE.CODE` |
| `PAYROLLTYPE_PROCESSTYPE` | [`ATTENDANCECALCULATION`](../HR/ATTENDANCECALCULATION.md) | `COMPANYCODE`, `PROCESSTYPECODE` | `ATTENDANCECALCULATION.COMPANYCODE = PAYROLLTYPE.COMPANYCODE AND ATTENDANCECALCULATION.PROCESSTYPECODE = PAYROLLTYPE.CODE` |
| `PAYROLLTYPE_PAYROLL` | [`ATTENDANCECORRECTION`](../HR/ATTENDANCECORRECTION.md) | `COMPANYCODE`, `PAYROLLCODE` | `ATTENDANCECORRECTION.COMPANYCODE = PAYROLLTYPE.COMPANYCODE AND ATTENDANCECORRECTION.PAYROLLCODE = PAYROLLTYPE.CODE` |
| `PAYROLLTYPE_PAYROLL` | [`ATTENDANCEDETAIL`](../HR/ATTENDANCEDETAIL.md) | `COMPANYCODE`, `PAYROLLCODE` | `ATTENDANCEDETAIL.COMPANYCODE = PAYROLLTYPE.COMPANYCODE AND ATTENDANCEDETAIL.PAYROLLCODE = PAYROLLTYPE.CODE` |
| `PAYROLLTYPE_PAYROLL` | [`ATTENDANCEDETAILTEMPPEREMP`](../HR/ATTENDANCEDETAILTEMPPEREMP.md) | `COMPANYCODE`, `PAYROLLCODE` | `ATTENDANCEDETAILTEMPPEREMP.COMPANYCODE = PAYROLLTYPE.COMPANYCODE AND ATTENDANCEDETAILTEMPPEREMP.PAYROLLCODE = PAYROLLTYPE.CODE` |
| `PAYROLLTYPE_PAYROLLTYPE` | [`FULLANDFINAL`](../HR/FULLANDFINAL.md) | `COMPANYCODE`, `PAYROLLTYPECODE` | `FULLANDFINAL.COMPANYCODE = PAYROLLTYPE.COMPANYCODE AND FULLANDFINAL.PAYROLLTYPECODE = PAYROLLTYPE.CODE` |
| `PAYROLLTYPE_PAYROLLTYPE` | [`LUMPSUMENTRYHEADER`](../HR/LUMPSUMENTRYHEADER.md) | `COMPANYCODE`, `PAYROLLTYPECODE` | `LUMPSUMENTRYHEADER.COMPANYCODE = PAYROLLTYPE.COMPANYCODE AND LUMPSUMENTRYHEADER.PAYROLLTYPECODE = PAYROLLTYPE.CODE` |
| `PAYROLLTYPE_PAYROLL` | [`PRLPOSTINGSUMMARYEMPDETAIL`](../HR/PRLPOSTINGSUMMARYEMPDETAIL.md) | `COMPANYCODE`, `PAYROLLCODE` | `PRLPOSTINGSUMMARYEMPDETAIL.COMPANYCODE = PAYROLLTYPE.COMPANYCODE AND PRLPOSTINGSUMMARYEMPDETAIL.PAYROLLCODE = PAYROLLTYPE.CODE` |

## Indexes

- `PAYROLLTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PAYROLLTYPE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
