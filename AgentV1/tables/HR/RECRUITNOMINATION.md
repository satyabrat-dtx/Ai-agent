# DB2ADMIN.RECRUITNOMINATION

- **Module**: `HR` (high confidence — table name starts with 'RECRUIT')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `APPLNOCODE`, `RLRELATIONTYPEICSTABLECODE`, `RELATIONRELATIONTYPECODE`, `NOMINATIONTYPEICSTABLECODE`, `NOMINATIONTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 159949

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `APPLNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `RLRELATIONTYPEICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `RELATIONRELATIONTYPECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `NOMINATIONTYPEICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `NOMINATIONTYPECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `DATEOFBIRTH` | DATE | NOT NULL |  |  |  |
| 7 | `AGE` | DECIMAL(2,0) | NOT NULL |  |  |  |
| 8 | `RELATIONNAME` | CHAR(15) |  |  |  |  |
| 9 | `WORKINGSAMECOMPANY` | INTEGER | NOT NULL |  |  |  |
| 10 | `RELATIVEEMPIDCODE` | CHAR(9) |  | FK | foreign_key |  |
| 11 | `NOMINATION` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 12 | `REMARKS` | CHAR(100) |  |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `APPLICANTSDETAILS_APPLNO` | `COMPANYCODE`, `APPLNOCODE` | [`APPLICANTSDETAILS`](../HR/APPLICANTSDETAILS.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECRUITNOMINATION.COMPANYCODE = APPLICANTSDETAILS.COMPANYCODE AND RECRUITNOMINATION.APPLNOCODE = APPLICANTSDETAILS.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RECRUITNOMINATION.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_RELATIVEEMPID` | `COMPANYCODE`, `RELATIVEEMPIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECRUITNOMINATION.COMPANYCODE = EMPLOYEE.COMPANYCODE AND RECRUITNOMINATION.RELATIVEEMPIDCODE = EMPLOYEE.CODE` |
| `ICSENTITY_NOMINATIONTYPE` | `COMPANYCODE`, `NOMINATIONTYPEICSTABLECODE`, `NOMINATIONTYPECODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `RECRUITNOMINATION.COMPANYCODE = ICSENTITY.COMPANYCODE AND RECRUITNOMINATION.NOMINATIONTYPEICSTABLECODE = ICSENTITY.ICSTABLECODE AND RECRUITNOMINATION.NOMINATIONTYPECODE = ICSENTITY.CODE` |
| `RECRUITRELATIVE_RELATION` | `COMPANYCODE`, `APPLNOCODE`, `RLRELATIONTYPEICSTABLECODE`, `RELATIONRELATIONTYPECODE` | [`RECRUITRELATIVE`](../HR/RECRUITRELATIVE.md) | `COMPANYCODE`, `APPLNOCODE`, `RELATIONTYPEICSTABLECODE`, `RELATIONTYPECODE` | RESTRICT | `RECRUITNOMINATION.COMPANYCODE = RECRUITRELATIVE.COMPANYCODE AND RECRUITNOMINATION.APPLNOCODE = RECRUITRELATIVE.APPLNOCODE AND RECRUITNOMINATION.RLRELATIONTYPEICSTABLECODE = RECRUITRELATIVE.RELATIONTYPEICSTABLECODE AND RECRUITNOMINATION.RELATIONRELATIONTYPECODE = RECRUITRELATIVE.RELATIONTYPECODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RECRUITNOMINATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.APPLNOCODE,
       t.RLRELATIONTYPEICSTABLECODE,
       t.RELATIONRELATIONTYPECODE,
       t.NOMINATIONTYPEICSTABLECODE,
       t.NOMINATIONTYPECODE,
       t.DATEOFBIRTH,
       t.AGE,
       t.RELATIONNAME,
       t.WORKINGSAMECOMPANY,
       t.RELATIVEEMPIDCODE,
       t.NOMINATION
FROM   DB2ADMIN.RECRUITNOMINATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
