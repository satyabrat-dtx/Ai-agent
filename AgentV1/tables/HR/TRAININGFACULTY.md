# DB2ADMIN.TRAININGFACULTY

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `COMPANYCODE`, `FACULTYCODE`
- **FK degree**: referenced by 1 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 161449

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `FACULTYCODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 2 | `FIRSTNAME` | CHAR(25) | NOT NULL |  |  |  |
| 3 | `LASTNAME` | CHAR(25) |  |  |  |  |
| 4 | `ADDRESS` | VARCHAR(200) |  |  |  |  |
| 5 | `CITY` | VARCHAR(200) |  |  |  |  |
| 6 | `STATE` | VARCHAR(200) |  |  |  |  |
| 7 | `COUNTRY` | VARCHAR(200) |  |  |  |  |
| 8 | `PRIMARYPHONENO` | CHAR(12) | NOT NULL |  |  |  |
| 9 | `MOBILENO` | CHAR(12) |  |  |  |  |
| 10 | `FAXNUMBER` | CHAR(12) |  |  |  |  |
| 11 | `EMAILID` | CHAR(25) |  |  |  |  |
| 12 | `INSTITUTEICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 13 | `INSTITUTECODE` | CHAR(6) |  | FK | foreign_key |  |
| 14 | `QUALIFICATIONICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 15 | `QUALIFICATIONCODE` | CHAR(6) |  | FK | foreign_key |  |
| 16 | `SPECIALIZATIONICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 17 | `SPECIALIZATIONCODE` | CHAR(6) |  | FK | foreign_key |  |
| 18 | `BANKNAME` | CHAR(25) |  |  |  |  |
| 19 | `ACCOUNTNUMBER` | CHAR(12) |  |  |  |  |
| 20 | `PANNO` | CHAR(30) |  |  |  |  |
| 21 | `MICR` | CHAR(30) |  |  |  |  |
| 22 | `IFSC` | CHAR(30) |  |  |  |  |
| 23 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 24 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 25 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 26 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 27 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 28 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TRAININGFACULTY.COMPANYCODE = COMPANY.CODE` |
| `ICSENTITY_INSTITUTE` | `COMPANYCODE`, `INSTITUTEICSTABLECODE`, `INSTITUTECODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `TRAININGFACULTY.COMPANYCODE = ICSENTITY.COMPANYCODE AND TRAININGFACULTY.INSTITUTEICSTABLECODE = ICSENTITY.ICSTABLECODE AND TRAININGFACULTY.INSTITUTECODE = ICSENTITY.CODE` |
| `ICSENTITY_QUALIFICATION` | `COMPANYCODE`, `QUALIFICATIONICSTABLECODE`, `QUALIFICATIONCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `TRAININGFACULTY.COMPANYCODE = ICSENTITY.COMPANYCODE AND TRAININGFACULTY.QUALIFICATIONICSTABLECODE = ICSENTITY.ICSTABLECODE AND TRAININGFACULTY.QUALIFICATIONCODE = ICSENTITY.CODE` |
| `ICSENTITY_SPECIALIZATION` | `COMPANYCODE`, `SPECIALIZATIONICSTABLECODE`, `SPECIALIZATIONCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `TRAININGFACULTY.COMPANYCODE = ICSENTITY.COMPANYCODE AND TRAININGFACULTY.SPECIALIZATIONICSTABLECODE = ICSENTITY.ICSTABLECODE AND TRAININGFACULTY.SPECIALIZATIONCODE = ICSENTITY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TRAININGFACULTY_FACULTYCODE` | [`TRAININGSCHEDULEFACULTY`](../HR/TRAININGSCHEDULEFACULTY.md) | `TSDETAILTSCHEDULECOMPANYCODE`, `FACULTYCODEFACULTYCODE` | `TRAININGSCHEDULEFACULTY.TSDETAILTSCHEDULECOMPANYCODE = TRAININGFACULTY.COMPANYCODE AND TRAININGSCHEDULEFACULTY.FACULTYCODEFACULTYCODE = TRAININGFACULTY.FACULTYCODE` |

## Indexes

- `TRAININGFACULTYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.FACULTYCODE,
       t.FIRSTNAME,
       t.LASTNAME,
       t.ADDRESS,
       t.CITY,
       t.STATE,
       t.COUNTRY,
       t.PRIMARYPHONENO,
       t.MOBILENO,
       t.FAXNUMBER,
       t.EMAILID
FROM   DB2ADMIN.TRAININGFACULTY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
