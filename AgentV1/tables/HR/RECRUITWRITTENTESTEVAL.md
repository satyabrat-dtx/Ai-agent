# DB2ADMIN.RECRUITWRITTENTESTEVAL

- **Module**: `HR` (high confidence — table name starts with 'RECRUIT')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPANYCODE`, `APPLICANTNOCODE`, `INTERVIEWNO`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 160438

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `APPLICANTNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `INTERVIEWNO` | BIGINT | NOT NULL | PK | primary_key |  |
| 3 | `WRITTENFLAG` | INTEGER | NOT NULL |  |  |  |
| 4 | `INTERVIEWDATE` | DATE |  |  |  |  |
| 5 | `DESCRIPTION` | CHAR(50) |  |  | description |  |
| 6 | `SCORE` | CHAR(100) |  |  |  |  |
| 7 | `RATING` | CHAR(100) |  |  |  |  |
| 8 | `EVALUATIONDATE` | DATE |  |  |  |  |
| 9 | `EVALUATIONBYCODE` | CHAR(9) |  | FK | foreign_key |  |
| 10 | `COMMENTS` | CHAR(100) |  |  |  |  |
| 11 | `APPLICANTFLAG` | SMALLINT | NOT NULL |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `APPLICANTSDETAILS_APPLICANTNO` | `COMPANYCODE`, `APPLICANTNOCODE` | [`APPLICANTSDETAILS`](../HR/APPLICANTSDETAILS.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECRUITWRITTENTESTEVAL.COMPANYCODE = APPLICANTSDETAILS.COMPANYCODE AND RECRUITWRITTENTESTEVAL.APPLICANTNOCODE = APPLICANTSDETAILS.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RECRUITWRITTENTESTEVAL.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EVALUATIONBY` | `COMPANYCODE`, `EVALUATIONBYCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECRUITWRITTENTESTEVAL.COMPANYCODE = EMPLOYEE.COMPANYCODE AND RECRUITWRITTENTESTEVAL.EVALUATIONBYCODE = EMPLOYEE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RECRUITWRITTENTESTEVALUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.APPLICANTNOCODE,
       t.INTERVIEWNO,
       t.WRITTENFLAG,
       t.INTERVIEWDATE,
       t.DESCRIPTION,
       t.SCORE,
       t.RATING,
       t.EVALUATIONDATE,
       t.EVALUATIONBYCODE,
       t.COMMENTS,
       t.APPLICANTFLAG
FROM   DB2ADMIN.RECRUITWRITTENTESTEVAL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
