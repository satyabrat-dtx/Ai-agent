# DB2ADMIN.APPRAISALCALENDAR

- **Module**: `HR` (low confidence — FK neighbourhood: 2 of 2 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `COMPANYCODE`, `APPCALCODE`
- **FK degree**: referenced by 2 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 149718

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `APPCALCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `STARTDATE` | DATE | NOT NULL |  |  |  |
| 3 | `ENDDATE` | DATE |  |  |  |  |
| 4 | `CATEGORYICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 5 | `CATEGORYCODE` | CHAR(6) |  | FK | foreign_key |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `APPRAISALCALENDAR.COMPANYCODE = COMPANY.CODE` |
| `ICSENTITY_CATEGORY` | `COMPANYCODE`, `CATEGORYICSTABLECODE`, `CATEGORYCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `APPRAISALCALENDAR.COMPANYCODE = ICSENTITY.COMPANYCODE AND APPRAISALCALENDAR.CATEGORYICSTABLECODE = ICSENTITY.ICSTABLECODE AND APPRAISALCALENDAR.CATEGORYCODE = ICSENTITY.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `APPRAISALCALENDAR_APPCALCODE` | [`KRAHEADER`](../HR/KRAHEADER.md) | `COMPANYCODE`, `APPCALCODEAPPCALCODE` | `KRAHEADER.COMPANYCODE = APPRAISALCALENDAR.COMPANYCODE AND KRAHEADER.APPCALCODEAPPCALCODE = APPRAISALCALENDAR.APPCALCODE` |
| `APPRAISALCALENDAR_APPCALCODE` | [`PERFORMANCEAPP`](../HR/PERFORMANCEAPP.md) | `COMPANYCODE`, `APPCALCODEAPPCALCODE` | `PERFORMANCEAPP.COMPANYCODE = APPRAISALCALENDAR.COMPANYCODE AND PERFORMANCEAPP.APPCALCODEAPPCALCODE = APPRAISALCALENDAR.APPCALCODE` |

## Indexes

- `APPRAISALCALENDARUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.APPCALCODE,
       t.STARTDATE,
       t.ENDDATE,
       t.CATEGORYICSTABLECODE,
       t.CATEGORYCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.APPRAISALCALENDAR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
