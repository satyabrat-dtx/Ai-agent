# DB2ADMIN.RECRUITMEDICAL

- **Module**: `HR` (high confidence — table name starts with 'RECRUIT')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `APPLNOCODE`, `SERIALNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 159802

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `APPLNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SERIALNUMBER` | BIGINT | NOT NULL | PK | primary_key |  |
| 3 | `WEIGHTINKG` | DECIMAL(10,0) | NOT NULL |  |  |  |
| 4 | `HEIGHTINCMS` | DECIMAL(10,0) | NOT NULL |  |  |  |
| 5 | `BLOODGROUPICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 6 | `BLOODGROUPCODE` | CHAR(6) |  | FK | foreign_key |  |
| 7 | `PHYSICALDISABILITIES` | CHAR(100) |  |  |  |  |
| 8 | `ALLERGIES` | CHAR(100) |  |  |  |  |
| 9 | `COMMENTS` | CHAR(100) |  |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `APPLICANTSDETAILS_APPLNO` | `COMPANYCODE`, `APPLNOCODE` | [`APPLICANTSDETAILS`](../HR/APPLICANTSDETAILS.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECRUITMEDICAL.COMPANYCODE = APPLICANTSDETAILS.COMPANYCODE AND RECRUITMEDICAL.APPLNOCODE = APPLICANTSDETAILS.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RECRUITMEDICAL.COMPANYCODE = COMPANY.CODE` |
| `ICSENTITY_BLOODGROUP` | `COMPANYCODE`, `BLOODGROUPICSTABLECODE`, `BLOODGROUPCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `RECRUITMEDICAL.COMPANYCODE = ICSENTITY.COMPANYCODE AND RECRUITMEDICAL.BLOODGROUPICSTABLECODE = ICSENTITY.ICSTABLECODE AND RECRUITMEDICAL.BLOODGROUPCODE = ICSENTITY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RECRUITMEDICALUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.APPLNOCODE,
       t.SERIALNUMBER,
       t.WEIGHTINKG,
       t.HEIGHTINCMS,
       t.BLOODGROUPICSTABLECODE,
       t.BLOODGROUPCODE,
       t.PHYSICALDISABILITIES,
       t.ALLERGIES,
       t.COMMENTS,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.RECRUITMEDICAL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
