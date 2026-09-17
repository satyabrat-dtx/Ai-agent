# DB2ADMIN.ACCESSCARDREQUEST

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `EMPLOYEEIDCODE`, `SERIALNO`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 149522

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `OLDACCESSCARDNO` | CHAR(50) |  |  |  |  |
| 3 | `CARDLOSTDATE` | DATE | NOT NULL |  |  |  |
| 4 | `REASON` | CHAR(50) |  |  |  |  |
| 5 | `SERIALNO` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 6 | `NEWACCESSCARDNO` | CHAR(50) |  |  |  |  |
| 7 | `ISSUEDATE` | DATE |  |  |  |  |
| 8 | `AUTHORIZEDBYCODE` | CHAR(9) |  | FK | foreign_key |  |
| 9 | `REQPENDINGWITH` | CHAR(10) |  |  |  |  |
| 10 | `AUTHLEVEL` | CHAR(10) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ACCESSCARDREQUEST.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_AUTHORIZEDBY` | `COMPANYCODE`, `AUTHORIZEDBYCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ACCESSCARDREQUEST.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ACCESSCARDREQUEST.AUTHORIZEDBYCODE = EMPLOYEE.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ACCESSCARDREQUEST.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ACCESSCARDREQUEST.EMPLOYEEIDCODE = EMPLOYEE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACCESSCARDREQUESTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.OLDACCESSCARDNO,
       t.CARDLOSTDATE,
       t.REASON,
       t.SERIALNO,
       t.NEWACCESSCARDNO,
       t.ISSUEDATE,
       t.AUTHORIZEDBYCODE,
       t.REQPENDINGWITH,
       t.AUTHLEVEL,
       t.CREATIONDATETIME
FROM   DB2ADMIN.ACCESSCARDREQUEST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
