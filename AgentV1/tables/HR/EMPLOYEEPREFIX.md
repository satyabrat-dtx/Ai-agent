# DB2ADMIN.EMPLOYEEPREFIX

- **Module**: `HR` (high confidence — table name starts with 'EMPLOYEE')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `CATEGORYICSTABLECODE`, `CATEGORYCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 152820

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `CATEGORYICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CATEGORYCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CODE` | CHAR(3) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `FLAG` | INTEGER | NOT NULL |  |  |  |
| 6 | `STARTINGNO` | DECIMAL(6,0) |  |  |  |  |
| 7 | `CURRENTNO` | DECIMAL(6,0) |  |  |  |  |
| 8 | `PADDINGREQUIRED` | INTEGER | NOT NULL |  |  |  |
| 9 | `NOOFZEROSPADDED` | INTEGER | NOT NULL |  |  |  |
| 10 | `LOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 11 | `TERMSOFLOGCODE` | CHAR(2) |  | FK | foreign_key |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `EMPLOYEEPREFIX.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EMPLOYEEPREFIX.COMPANYCODE = DIVISION.COMPANYCODE AND EMPLOYEEPREFIX.DIVISIONCODE = DIVISION.CODE` |
| `ICSENTITY_CATEGORY` | `COMPANYCODE`, `CATEGORYICSTABLECODE`, `CATEGORYCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `EMPLOYEEPREFIX.COMPANYCODE = ICSENTITY.COMPANYCODE AND EMPLOYEEPREFIX.CATEGORYICSTABLECODE = ICSENTITY.ICSTABLECODE AND EMPLOYEEPREFIX.CATEGORYCODE = ICSENTITY.CODE` |
| `NETTOLOG_TERMSOFLOG` | `COMPANYCODE`, `TERMSOFLOGCODE` | [`NETTOLOG`](../LOCALIZATION/NETTOLOG.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EMPLOYEEPREFIX.COMPANYCODE = NETTOLOG.COMPANYCODE AND EMPLOYEEPREFIX.TERMSOFLOGCODE = NETTOLOG.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EMPLOYEEPREFIXUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CATEGORYICSTABLECODE,
       t.CATEGORYCODE,
       t.CODE,
       t.FLAG,
       t.STARTINGNO,
       t.CURRENTNO,
       t.PADDINGREQUIRED,
       t.NOOFZEROSPADDED,
       t.LOGMANAGEMENT,
       t.TERMSOFLOGCODE
FROM   DB2ADMIN.EMPLOYEEPREFIX t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
