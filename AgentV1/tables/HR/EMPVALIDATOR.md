# DB2ADMIN.EMPVALIDATOR

- **Module**: `HR` (medium confidence — table name starts with 'EMP')
- **Roles**: `business_data`
- **Columns**: 29
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `CATEGORYICSTABLECODE`, `CATEGORYCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 151602

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `CATEGORYICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CATEGORYCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SHIFTFLAG` | SMALLINT | NOT NULL |  |  |  |
| 5 | `NOMINATIONFLAG` | SMALLINT | NOT NULL |  |  |  |
| 6 | `LUMPSUMFLAG` | SMALLINT | NOT NULL |  |  |  |
| 7 | `LANGFLAG` | SMALLINT | NOT NULL |  |  |  |
| 8 | `FAMILYFLAG` | SMALLINT | NOT NULL |  |  |  |
| 9 | `EXPFLAG` | SMALLINT | NOT NULL |  |  |  |
| 10 | `EDUCATIONFLAG` | SMALLINT | NOT NULL |  |  |  |
| 11 | `ADDRFLAG` | SMALLINT | NOT NULL |  |  |  |
| 12 | `ACCESSCARDFLAG` | SMALLINT | NOT NULL |  |  |  |
| 13 | `DOCFLAG` | SMALLINT | NOT NULL |  |  |  |
| 14 | `MEMBERFLAG` | SMALLINT | NOT NULL |  |  |  |
| 15 | `SKILLFLAG` | SMALLINT | NOT NULL |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 22 | `TRAININGFLAG` | SMALLINT | NOT NULL |  |  |  |
| 23 | `BACKDATEEMPCREATION` | SMALLINT | NOT NULL |  |  |  |
| 24 | `NOOFDAYS` | INTEGER | NOT NULL |  |  |  |
| 25 | `MANPOWERPLANING` | SMALLINT | NOT NULL |  |  |  |
| 26 | `STATUSALLOWED` | CHAR(2) | NOT NULL |  |  |  |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 28 | `NATIONALIDFLAG` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `EMPVALIDATOR.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EMPVALIDATOR.COMPANYCODE = DIVISION.COMPANYCODE AND EMPVALIDATOR.DIVISIONCODE = DIVISION.CODE` |
| `ICSENTITY_CATEGORY` | `COMPANYCODE`, `CATEGORYICSTABLECODE`, `CATEGORYCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `EMPVALIDATOR.COMPANYCODE = ICSENTITY.COMPANYCODE AND EMPVALIDATOR.CATEGORYICSTABLECODE = ICSENTITY.ICSTABLECODE AND EMPVALIDATOR.CATEGORYCODE = ICSENTITY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EMPVALIDATORUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CATEGORYICSTABLECODE,
       t.CATEGORYCODE,
       t.SHIFTFLAG,
       t.NOMINATIONFLAG,
       t.LUMPSUMFLAG,
       t.LANGFLAG,
       t.FAMILYFLAG,
       t.EXPFLAG,
       t.EDUCATIONFLAG,
       t.ADDRFLAG
FROM   DB2ADMIN.EMPVALIDATOR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
