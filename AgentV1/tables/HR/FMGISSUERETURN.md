# DB2ADMIN.FMGISSUERETURN

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `COMPANYCODE`, `FMGCODEFMGCODE`, `ASSETCODE`, `EMPLOYEEIDCODE`, `SERIALNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 156544

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `FMGCODEFMGCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ASSETCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 3 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SERIALNUMBER` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 5 | `MODELNUMBER` | CHAR(25) |  |  |  |  |
| 6 | `BRANDNAME` | CHAR(25) |  |  |  |  |
| 7 | `ASSETVALUE` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 8 | `REQUESTDATE` | DATE | NOT NULL |  |  |  |
| 9 | `APPROVEDBYCODE` | CHAR(9) |  | FK | foreign_key |  |
| 10 | `APPROVEDDATE` | DATE |  |  |  |  |
| 11 | `ISSUEDATE` | DATE |  |  |  |  |
| 12 | `DUEDATE` | DATE |  |  |  |  |
| 13 | `RETURNDATE` | DATE |  |  |  |  |
| 14 | `PHYSICALVERFDATE` | DATE |  |  |  |  |
| 15 | `REMARKS` | CHAR(25) |  |  |  |  |
| 16 | `REQPENDINGWITH` | CHAR(10) |  |  |  |  |
| 17 | `AUTHLEVEL` | CHAR(10) |  |  |  |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FMGISSUERETURN.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_APPROVEDBY` | `COMPANYCODE`, `APPROVEDBYCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FMGISSUERETURN.COMPANYCODE = EMPLOYEE.COMPANYCODE AND FMGISSUERETURN.APPROVEDBYCODE = EMPLOYEE.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FMGISSUERETURN.COMPANYCODE = EMPLOYEE.COMPANYCODE AND FMGISSUERETURN.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `FMGMASTER_FMGCODE` | `COMPANYCODE`, `FMGCODEFMGCODE` | [`FMGMASTER`](../HR/FMGMASTER.md) | `COMPANYCODE`, `FMGCODE` | RESTRICT | `FMGISSUERETURN.COMPANYCODE = FMGMASTER.COMPANYCODE AND FMGISSUERETURN.FMGCODEFMGCODE = FMGMASTER.FMGCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FMGISSUERETURNUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.FMGCODEFMGCODE,
       t.ASSETCODE,
       t.EMPLOYEEIDCODE,
       t.SERIALNUMBER,
       t.MODELNUMBER,
       t.BRANDNAME,
       t.ASSETVALUE,
       t.REQUESTDATE,
       t.APPROVEDBYCODE,
       t.APPROVEDDATE,
       t.ISSUEDATE
FROM   DB2ADMIN.FMGISSUERETURN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
