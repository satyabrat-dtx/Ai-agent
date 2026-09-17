# DB2ADMIN.INTERVIEWEVALSHEET

- **Module**: `HR` (medium confidence — table name starts with 'INTERVIE')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `CODE`, `APPLNOCODE`
- **FK degree**: referenced by 2 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 170033

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | BIGINT | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `APPLNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `INTERVIEWDATE` | DATE | NOT NULL |  |  |  |
| 4 | `INTERVIEWFLAG` | INTEGER | NOT NULL |  |  |  |
| 5 | `DESCRIPTION` | CHAR(50) |  |  | description |  |
| 6 | `EVALUATIONDATE` | DATE |  |  |  |  |
| 7 | `EVALUATIONBYCODE` | CHAR(9) |  | FK | foreign_key |  |
| 8 | `COMMENTS` | CHAR(100) |  |  |  |  |
| 9 | `APPLICANTFLAG` | SMALLINT | NOT NULL |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `APPLICANTSDETAILS_APPLNO` | `COMPANYCODE`, `APPLNOCODE` | [`APPLICANTSDETAILS`](../HR/APPLICANTSDETAILS.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INTERVIEWEVALSHEET.COMPANYCODE = APPLICANTSDETAILS.COMPANYCODE AND INTERVIEWEVALSHEET.APPLNOCODE = APPLICANTSDETAILS.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `INTERVIEWEVALSHEET.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EVALUATIONBY` | `COMPANYCODE`, `EVALUATIONBYCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INTERVIEWEVALSHEET.COMPANYCODE = EMPLOYEE.COMPANYCODE AND INTERVIEWEVALSHEET.EVALUATIONBYCODE = EMPLOYEE.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `INTERVIEWEVALSHEET_EVALSHEETATT` | [`IESATTRIBUTERATING`](../HR/IESATTRIBUTERATING.md) | `INTERVIEWEVALSHEETCOMPANYCODE`, `INTERVIEWEVALSHEETCODE`, `INTERVIEWEVALSHEETAPPLNOCODE` | `IESATTRIBUTERATING.INTERVIEWEVALSHEETCOMPANYCODE = INTERVIEWEVALSHEET.COMPANYCODE AND IESATTRIBUTERATING.INTERVIEWEVALSHEETCODE = INTERVIEWEVALSHEET.CODE AND IESATTRIBUTERATING.INTERVIEWEVALSHEETAPPLNOCODE = INTERVIEWEVALSHEET.APPLNOCODE` |
| `INTERVIEWEVALSHEET_EVALSHEETRAT` | [`IESATTRIBUTESUMMARY`](../HR/IESATTRIBUTESUMMARY.md) | `INTERVIEWEVALSHEETCOMPANYCODE`, `INTERVIEWEVALSHEETCODE`, `INTERVIEWEVALSHEETAPPLNOCODE` | `IESATTRIBUTESUMMARY.INTERVIEWEVALSHEETCOMPANYCODE = INTERVIEWEVALSHEET.COMPANYCODE AND IESATTRIBUTESUMMARY.INTERVIEWEVALSHEETCODE = INTERVIEWEVALSHEET.CODE AND IESATTRIBUTESUMMARY.INTERVIEWEVALSHEETAPPLNOCODE = INTERVIEWEVALSHEET.APPLNOCODE` |

## Indexes

- `INTERVIEWEVALSHEETUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.APPLNOCODE,
       t.INTERVIEWDATE,
       t.INTERVIEWFLAG,
       t.DESCRIPTION,
       t.EVALUATIONDATE,
       t.EVALUATIONBYCODE,
       t.COMMENTS,
       t.APPLICANTFLAG,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.INTERVIEWEVALSHEET t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
