# DB2ADMIN.ESSEMPLOYEENOMINATION

- **Module**: `HR` (low confidence — FK neighbourhood: 2 of 2 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `EMPLOYEEIDCODE`, `RELATIONSHIPRLTEICSTABLECODE`, `RELATIONSHIPRELATIONTYPECODE`, `NOMINATIONTYPEICSTABLECODE`, `NOMINATIONTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 183109

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `RELATIONSHIPRLTEICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `RELATIONSHIPRELATIONTYPECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `NOMINATIONTYPEICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `NOMINATIONTYPECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `RELATIONNAME` | CHAR(15) |  |  |  |  |
| 7 | `AGE` | DECIMAL(2,0) | NOT NULL |  |  |  |
| 8 | `DATEOFBIRTH` | DATE | NOT NULL |  |  |  |
| 9 | `NOMINATION` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 10 | `REMARKS` | CHAR(100) |  |  |  |  |
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

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ESSEMPLOYEENOMINATION.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEEFAMILY_RELATIONSHIP` | `COMPANYCODE`, `EMPLOYEEIDCODE`, `RELATIONSHIPRLTEICSTABLECODE`, `RELATIONSHIPRELATIONTYPECODE` | [`EMPLOYEEFAMILY`](../HR/EMPLOYEEFAMILY.md) | `COMPANYCODE`, `EMPLOYEEIDCODE`, `RELATIONTYPEICSTABLECODE`, `RELATIONTYPECODE` | RESTRICT | `ESSEMPLOYEENOMINATION.COMPANYCODE = EMPLOYEEFAMILY.COMPANYCODE AND ESSEMPLOYEENOMINATION.EMPLOYEEIDCODE = EMPLOYEEFAMILY.EMPLOYEEIDCODE AND ESSEMPLOYEENOMINATION.RELATIONSHIPRLTEICSTABLECODE = EMPLOYEEFAMILY.RELATIONTYPEICSTABLECODE AND ESSEMPLOYEENOMINATION.RELATIONSHIPRELATIONTYPECODE = EMPLOYEEFAMILY.RELATIONTYPECODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ESSEMPLOYEENOMINATION.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ESSEMPLOYEENOMINATION.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `ICSENTITY_NOMINATIONTYPE` | `COMPANYCODE`, `NOMINATIONTYPEICSTABLECODE`, `NOMINATIONTYPECODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `ESSEMPLOYEENOMINATION.COMPANYCODE = ICSENTITY.COMPANYCODE AND ESSEMPLOYEENOMINATION.NOMINATIONTYPEICSTABLECODE = ICSENTITY.ICSTABLECODE AND ESSEMPLOYEENOMINATION.NOMINATIONTYPECODE = ICSENTITY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ESSEMPLOYEENOMINATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.RELATIONSHIPRLTEICSTABLECODE,
       t.RELATIONSHIPRELATIONTYPECODE,
       t.NOMINATIONTYPEICSTABLECODE,
       t.NOMINATIONTYPECODE,
       t.RELATIONNAME,
       t.AGE,
       t.DATEOFBIRTH,
       t.NOMINATION,
       t.REMARKS,
       t.REQUESTFLAG
FROM   DB2ADMIN.ESSEMPLOYEENOMINATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
