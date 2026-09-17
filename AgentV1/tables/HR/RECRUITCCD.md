# DB2ADMIN.RECRUITCCD

- **Module**: `HR` (high confidence — table name starts with 'RECRUIT')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `APPLNOCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 159350

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `APPLNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CCNAMEICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 3 | `CCNAMECODE` | CHAR(6) |  | FK | foreign_key |  |
| 4 | `ADDRESS` | CHAR(100) |  |  |  |  |
| 5 | `PHONE` | CHAR(15) |  |  |  |  |
| 6 | `FAX` | CHAR(15) |  |  |  |  |
| 7 | `WEBSITE` | CHAR(100) |  |  |  |  |
| 8 | `REPORTINGTO` | CHAR(100) | NOT NULL |  |  |  |
| 9 | `ROLESRES` | CHAR(100) | NOT NULL |  |  |  |
| 10 | `CONTRIBUTION` | CHAR(100) |  |  |  |  |
| 11 | `NOITCEPERIOD` | DECIMAL(10,0) | NOT NULL |  |  |  |
| 12 | `EXPECTEDDATETOJOIN` | DATE | NOT NULL |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `APPLICANTSDETAILS_APPLNO` | `COMPANYCODE`, `APPLNOCODE` | [`APPLICANTSDETAILS`](../HR/APPLICANTSDETAILS.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECRUITCCD.COMPANYCODE = APPLICANTSDETAILS.COMPANYCODE AND RECRUITCCD.APPLNOCODE = APPLICANTSDETAILS.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RECRUITCCD.COMPANYCODE = COMPANY.CODE` |
| `ICSENTITY_CCNAME` | `COMPANYCODE`, `CCNAMEICSTABLECODE`, `CCNAMECODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `RECRUITCCD.COMPANYCODE = ICSENTITY.COMPANYCODE AND RECRUITCCD.CCNAMEICSTABLECODE = ICSENTITY.ICSTABLECODE AND RECRUITCCD.CCNAMECODE = ICSENTITY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RECRUITCCDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.APPLNOCODE,
       t.CCNAMEICSTABLECODE,
       t.CCNAMECODE,
       t.ADDRESS,
       t.PHONE,
       t.FAX,
       t.WEBSITE,
       t.REPORTINGTO,
       t.ROLESRES,
       t.CONTRIBUTION,
       t.NOITCEPERIOD
FROM   DB2ADMIN.RECRUITCCD t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
