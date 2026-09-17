# DB2ADMIN.BADLI

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `BADLICODE`, `FROMDESIGNATIONICSTABLECODE`, `FROMDESIGNATIONCODE`, `TODESIGNATIONICSTABLECODE`, `TODESIGNATIONCODE`, `EFFECTIVEFROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 150256

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BADLICODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `FROMDESIGNATIONICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `FROMDESIGNATIONCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `TODESIGNATIONICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `TODESIGNATIONCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 7 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 8 | `RATEPERDAY` | DECIMAL(5,2) | NOT NULL |  |  |  |
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
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BADLI.COMPANYCODE = COMPANY.CODE` |
| `ICSENTITY_FROMDESIGNATION` | `COMPANYCODE`, `FROMDESIGNATIONICSTABLECODE`, `FROMDESIGNATIONCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `BADLI.COMPANYCODE = ICSENTITY.COMPANYCODE AND BADLI.FROMDESIGNATIONICSTABLECODE = ICSENTITY.ICSTABLECODE AND BADLI.FROMDESIGNATIONCODE = ICSENTITY.CODE` |
| `ICSENTITY_TODESIGNATION` | `COMPANYCODE`, `TODESIGNATIONICSTABLECODE`, `TODESIGNATIONCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `BADLI.COMPANYCODE = ICSENTITY.COMPANYCODE AND BADLI.TODESIGNATIONICSTABLECODE = ICSENTITY.ICSTABLECODE AND BADLI.TODESIGNATIONCODE = ICSENTITY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BADLIUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BADLICODE,
       t.FROMDESIGNATIONICSTABLECODE,
       t.FROMDESIGNATIONCODE,
       t.TODESIGNATIONICSTABLECODE,
       t.TODESIGNATIONCODE,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.RATEPERDAY,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.BADLI t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
