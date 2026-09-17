# DB2ADMIN.RECRUITMEMBERSHIP

- **Module**: `HR` (high confidence — table name starts with 'RECRUIT')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPANYCODE`, `APPLNOCODE`, `SNO`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 159850

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `APPLNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SNO` | BIGINT | NOT NULL | PK | primary_key |  |
| 3 | `MEMBERSHIPINSTITUTEICSTBCODE` | CHAR(4) |  | FK | foreign_key |  |
| 4 | `MEMBERSHIPINSTITUTECODE` | CHAR(6) |  | FK | foreign_key |  |
| 5 | `COUNTRYICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 6 | `COUNTRYCODE` | CHAR(6) |  | FK | foreign_key |  |
| 7 | `STATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `LOCATIONCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `MEMBERSHIPFROM` | DATE |  |  |  |  |
| 10 | `MEMBERSHIPTO` | DATE |  |  |  |  |
| 11 | `MEMBERSHIPNO` | CHAR(15) |  |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `APPLICANTSDETAILS_APPLNO` | `COMPANYCODE`, `APPLNOCODE` | [`APPLICANTSDETAILS`](../HR/APPLICANTSDETAILS.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECRUITMEMBERSHIP.COMPANYCODE = APPLICANTSDETAILS.COMPANYCODE AND RECRUITMEMBERSHIP.APPLNOCODE = APPLICANTSDETAILS.CODE` |
| `CITY_LOCATION` | `LOCATIONCODE` | [`CITY`](../HR/CITY.md) | `CODE` | RESTRICT | `RECRUITMEMBERSHIP.LOCATIONCODE = CITY.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RECRUITMEMBERSHIP.COMPANYCODE = COMPANY.CODE` |
| `ICSENTITY_COUNTRY` | `COMPANYCODE`, `COUNTRYICSTABLECODE`, `COUNTRYCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `RECRUITMEMBERSHIP.COMPANYCODE = ICSENTITY.COMPANYCODE AND RECRUITMEMBERSHIP.COUNTRYICSTABLECODE = ICSENTITY.ICSTABLECODE AND RECRUITMEMBERSHIP.COUNTRYCODE = ICSENTITY.CODE` |
| `ICSENTITY_MEMBERSHIPINSTITUTE` | `COMPANYCODE`, `MEMBERSHIPINSTITUTEICSTBCODE`, `MEMBERSHIPINSTITUTECODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `RECRUITMEMBERSHIP.COMPANYCODE = ICSENTITY.COMPANYCODE AND RECRUITMEMBERSHIP.MEMBERSHIPINSTITUTEICSTBCODE = ICSENTITY.ICSTABLECODE AND RECRUITMEMBERSHIP.MEMBERSHIPINSTITUTECODE = ICSENTITY.CODE` |
| `STATE_STATE` | `STATECODE` | [`STATE`](../HR/STATE.md) | `CODE` | RESTRICT | `RECRUITMEMBERSHIP.STATECODE = STATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RECRUITMEMBERSHIPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.APPLNOCODE,
       t.SNO,
       t.MEMBERSHIPINSTITUTEICSTBCODE,
       t.MEMBERSHIPINSTITUTECODE,
       t.COUNTRYICSTABLECODE,
       t.COUNTRYCODE,
       t.STATECODE,
       t.LOCATIONCODE,
       t.MEMBERSHIPFROM,
       t.MEMBERSHIPTO,
       t.MEMBERSHIPNO
FROM   DB2ADMIN.RECRUITMEMBERSHIP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
