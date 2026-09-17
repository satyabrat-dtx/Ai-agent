# DB2ADMIN.RECRUITIES

- **Module**: `HR` (high confidence — table name starts with 'RECRUIT')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `APPLNOCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 159704

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `APPLNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CODE` | BIGINT | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `NAME` | CHAR(100) | NOT NULL |  |  |  |
| 4 | `POSAPPLIEDFOR` | CHAR(10) | NOT NULL |  |  |  |
| 5 | `CURRENTORGANIZATIONICSTBCODE` | CHAR(4) |  | FK | foreign_key |  |
| 6 | `CURRENTORGANIZATIONCODE` | CHAR(6) |  | FK | foreign_key |  |
| 7 | `DESIGNATIONICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 8 | `DESIGNATIONCODE` | CHAR(6) |  | FK | foreign_key |  |
| 9 | `EXPYEARSINCO` | DECIMAL(10,0) | NOT NULL |  |  |  |
| 10 | `TOTALEXPYRS` | DECIMAL(10,0) |  |  |  |  |
| 11 | `AGE` | DECIMAL(10,0) |  |  |  |  |
| 12 | `SOURCE` | INTEGER | NOT NULL |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `APPLICANTSDETAILS_APPLNO` | `COMPANYCODE`, `APPLNOCODE` | [`APPLICANTSDETAILS`](../HR/APPLICANTSDETAILS.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECRUITIES.COMPANYCODE = APPLICANTSDETAILS.COMPANYCODE AND RECRUITIES.APPLNOCODE = APPLICANTSDETAILS.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RECRUITIES.COMPANYCODE = COMPANY.CODE` |
| `ICSENTITY_CURRENTORGANIZATION` | `COMPANYCODE`, `CURRENTORGANIZATIONICSTBCODE`, `CURRENTORGANIZATIONCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `RECRUITIES.COMPANYCODE = ICSENTITY.COMPANYCODE AND RECRUITIES.CURRENTORGANIZATIONICSTBCODE = ICSENTITY.ICSTABLECODE AND RECRUITIES.CURRENTORGANIZATIONCODE = ICSENTITY.CODE` |
| `ICSENTITY_DESIGNATION` | `COMPANYCODE`, `DESIGNATIONICSTABLECODE`, `DESIGNATIONCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `RECRUITIES.COMPANYCODE = ICSENTITY.COMPANYCODE AND RECRUITIES.DESIGNATIONICSTABLECODE = ICSENTITY.ICSTABLECODE AND RECRUITIES.DESIGNATIONCODE = ICSENTITY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RECRUITIESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.APPLNOCODE,
       t.CODE,
       t.NAME,
       t.POSAPPLIEDFOR,
       t.CURRENTORGANIZATIONICSTBCODE,
       t.CURRENTORGANIZATIONCODE,
       t.DESIGNATIONICSTABLECODE,
       t.DESIGNATIONCODE,
       t.EXPYEARSINCO,
       t.TOTALEXPYRS,
       t.AGE
FROM   DB2ADMIN.RECRUITIES t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
