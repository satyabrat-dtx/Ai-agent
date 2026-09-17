# DB2ADMIN.ESSEMPLOYEEFAMILY

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `EMPLOYEEIDCODE`, `RELATIONTYPEICSTABLECODE`, `RELATIONTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 182953

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `RELATIONTYPEICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `RELATIONTYPECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `RELATIVESLONGNAME` | CHAR(25) | NOT NULL |  |  |  |
| 5 | `RELATIVESSHORTNAME` | CHAR(10) | NOT NULL |  |  |  |
| 6 | `RELATIVESDATEOFBIRTH` | DATE |  |  |  |  |
| 7 | `RELATIVESOCCUPATIONICSTBCODE` | CHAR(4) |  | FK | foreign_key |  |
| 8 | `RELATIVESOCCUPATIONCODE` | CHAR(6) |  | FK | foreign_key |  |
| 9 | `DEPENDENCY` | INTEGER | NOT NULL |  |  |  |
| 10 | `RELATIVEEMLOYEEIDCODE` | CHAR(9) |  | FK | foreign_key |  |
| 11 | `REQUESTFLAG` | INTEGER | NOT NULL |  |  |  |
| 12 | `REQPENDINGWITH` | CHAR(10) |  |  |  |  |
| 13 | `AUTHLEVEL` | CHAR(10) |  |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ESSEMPLOYEEFAMILY.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ESSEMPLOYEEFAMILY.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ESSEMPLOYEEFAMILY.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `EMPLOYEE_RELATIVEEMLOYEEID` | `COMPANYCODE`, `RELATIVEEMLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ESSEMPLOYEEFAMILY.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ESSEMPLOYEEFAMILY.RELATIVEEMLOYEEIDCODE = EMPLOYEE.CODE` |
| `ICSENTITY_RELATIONTYPE` | `COMPANYCODE`, `RELATIONTYPEICSTABLECODE`, `RELATIONTYPECODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `ESSEMPLOYEEFAMILY.COMPANYCODE = ICSENTITY.COMPANYCODE AND ESSEMPLOYEEFAMILY.RELATIONTYPEICSTABLECODE = ICSENTITY.ICSTABLECODE AND ESSEMPLOYEEFAMILY.RELATIONTYPECODE = ICSENTITY.CODE` |
| `ICSENTITY_RELATIVESOCCUPATION` | `COMPANYCODE`, `RELATIVESOCCUPATIONICSTBCODE`, `RELATIVESOCCUPATIONCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `ESSEMPLOYEEFAMILY.COMPANYCODE = ICSENTITY.COMPANYCODE AND ESSEMPLOYEEFAMILY.RELATIVESOCCUPATIONICSTBCODE = ICSENTITY.ICSTABLECODE AND ESSEMPLOYEEFAMILY.RELATIVESOCCUPATIONCODE = ICSENTITY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ESSEMPLOYEEFAMILYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.RELATIONTYPEICSTABLECODE,
       t.RELATIONTYPECODE,
       t.RELATIVESLONGNAME,
       t.RELATIVESSHORTNAME,
       t.RELATIVESDATEOFBIRTH,
       t.RELATIVESOCCUPATIONICSTBCODE,
       t.RELATIVESOCCUPATIONCODE,
       t.DEPENDENCY,
       t.RELATIVEEMLOYEEIDCODE,
       t.REQUESTFLAG
FROM   DB2ADMIN.ESSEMPLOYEEFAMILY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
