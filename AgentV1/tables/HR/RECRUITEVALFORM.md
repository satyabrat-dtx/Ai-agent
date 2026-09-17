# DB2ADMIN.RECRUITEVALFORM

- **Module**: `HR` (high confidence — table name starts with 'RECRUIT')
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `COMPANYCODE`, `APPLNOCODE`, `SERIALNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 159546

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `APPLNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SERIALNUMBER` | BIGINT | NOT NULL | PK | primary_key |  |
| 3 | `NAME` | CHAR(100) | NOT NULL |  |  |  |
| 4 | `PROPOSEDROLE` | CHAR(100) | NOT NULL |  |  |  |
| 5 | `COMPLETEDBYCODE` | CHAR(9) |  | FK | foreign_key |  |
| 6 | `REFDATE` | DATE | NOT NULL |  |  |  |
| 7 | `SUPERVISEDCANDIDATE` | CHAR(100) |  |  |  |  |
| 8 | `RESPONSIBILITIES` | CHAR(100) |  |  |  |  |
| 9 | `EMPDATEFROM` | DATE | NOT NULL |  |  |  |
| 10 | `EMPDATETO` | DATE | NOT NULL |  |  |  |
| 11 | `STRENGTHS` | CHAR(100) |  |  |  |  |
| 12 | `AREAIMPROVEMENTS` | CHAR(100) |  |  |  |  |
| 13 | `MANAGEMENT` | CHAR(100) |  |  |  |  |
| 14 | `COWORKERS` | CHAR(100) |  |  |  |  |
| 15 | `CUSTOMERS` | CHAR(100) |  |  |  |  |
| 16 | `CLOSESUPERVISION` | CHAR(100) |  |  |  |  |
| 17 | `MANAGEMENTSKILLS` | CHAR(100) |  |  |  |  |
| 18 | `MOTIVATION` | CHAR(100) |  |  |  |  |
| 19 | `LEAVEORGANIZATION` | CHAR(100) |  |  |  |  |
| 20 | `WORKENVIRONMENT` | CHAR(100) |  |  |  |  |
| 21 | `HIRING` | CHAR(100) |  |  |  |  |
| 22 | `CANDINFO` | CHAR(100) |  |  |  |  |
| 23 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 24 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 25 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 26 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 27 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 28 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `APPLICANTSDETAILS_APPLNO` | `COMPANYCODE`, `APPLNOCODE` | [`APPLICANTSDETAILS`](../HR/APPLICANTSDETAILS.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECRUITEVALFORM.COMPANYCODE = APPLICANTSDETAILS.COMPANYCODE AND RECRUITEVALFORM.APPLNOCODE = APPLICANTSDETAILS.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RECRUITEVALFORM.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_COMPLETEDBY` | `COMPANYCODE`, `COMPLETEDBYCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECRUITEVALFORM.COMPANYCODE = EMPLOYEE.COMPANYCODE AND RECRUITEVALFORM.COMPLETEDBYCODE = EMPLOYEE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RECRUITEVALFORMUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.APPLNOCODE,
       t.SERIALNUMBER,
       t.NAME,
       t.PROPOSEDROLE,
       t.COMPLETEDBYCODE,
       t.REFDATE,
       t.SUPERVISEDCANDIDATE,
       t.RESPONSIBILITIES,
       t.EMPDATEFROM,
       t.EMPDATETO,
       t.STRENGTHS
FROM   DB2ADMIN.RECRUITEVALFORM t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
