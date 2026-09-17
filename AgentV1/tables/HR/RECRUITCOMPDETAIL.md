# DB2ADMIN.RECRUITCOMPDETAIL

- **Module**: `HR` (high confidence — table name starts with 'RECRUIT')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `APPLNOCODE`, `COMPANYCODE`, `SERIALNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 159400

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `APPLNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `SERIALNUMBER` | BIGINT | NOT NULL | PK | primary_key |  |
| 3 | `MONTHLYSALARAY` | DECIMAL(10,0) | NOT NULL |  |  |  |
| 4 | `YEARLYSALARY` | DECIMAL(10,0) | NOT NULL |  |  |  |
| 5 | `COSTTOCOMPANY` | DECIMAL(10,0) | NOT NULL |  |  |  |
| 6 | `OTHERBENEFITS` | VARCHAR(250) |  |  |  |  |
| 7 | `EXPECTEDSALARY` | DECIMAL(10,0) | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `APPLICANTSDETAILS_APPLNO` | `COMPANYCODE`, `APPLNOCODE` | [`APPLICANTSDETAILS`](../HR/APPLICANTSDETAILS.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECRUITCOMPDETAIL.COMPANYCODE = APPLICANTSDETAILS.COMPANYCODE AND RECRUITCOMPDETAIL.APPLNOCODE = APPLICANTSDETAILS.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RECRUITCOMPDETAIL.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RECRUITCOMPDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.APPLNOCODE,
       t.COMPANYCODE,
       t.SERIALNUMBER,
       t.MONTHLYSALARAY,
       t.YEARLYSALARY,
       t.COSTTOCOMPANY,
       t.OTHERBENEFITS,
       t.EXPECTEDSALARY,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.RECRUITCOMPDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
