# DB2ADMIN.EMPLOYEELANGUAGE

- **Module**: `HR` (high confidence — table name starts with 'EMPLOYEE')
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `EMPLOYEEIDCODE`, `LANGUAGEICSTABLECODE`, `LANGUAGECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 152668

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LANGUAGEICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LANGUAGECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `LANGUAGESPEAK` | INTEGER | NOT NULL |  |  |  |
| 5 | `LANGUAGEREAD` | INTEGER | NOT NULL |  |  |  |
| 6 | `LANGUAGEWRITE` | INTEGER | NOT NULL |  |  |  |
| 7 | `LANGUAGEMOTHERTONGUE` | INTEGER | NOT NULL |  |  |  |
| 8 | `REQUESTFLAG` | INTEGER | NOT NULL |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `EMPLOYEELANGUAGE.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EMPLOYEELANGUAGE.COMPANYCODE = EMPLOYEE.COMPANYCODE AND EMPLOYEELANGUAGE.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `ICSENTITY_LANGUAGE` | `COMPANYCODE`, `LANGUAGEICSTABLECODE`, `LANGUAGECODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `EMPLOYEELANGUAGE.COMPANYCODE = ICSENTITY.COMPANYCODE AND EMPLOYEELANGUAGE.LANGUAGEICSTABLECODE = ICSENTITY.ICSTABLECODE AND EMPLOYEELANGUAGE.LANGUAGECODE = ICSENTITY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EMPLOYEELANGUAGEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.LANGUAGEICSTABLECODE,
       t.LANGUAGECODE,
       t.LANGUAGESPEAK,
       t.LANGUAGEREAD,
       t.LANGUAGEWRITE,
       t.LANGUAGEMOTHERTONGUE,
       t.REQUESTFLAG,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.EMPLOYEELANGUAGE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
