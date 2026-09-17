# DB2ADMIN.SUPERANNUATIONCALENDAR

- **Module**: `HR` (low confidence — FK neighbourhood: 3 of 3 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 161102

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(6) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `FROMDATE` | DATE | NOT NULL |  |  | Inclusive start of a validity period. |
| 3 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 4 | `ONROLLINTERESTPER` | DECIMAL(5,2) |  |  |  |  |
| 5 | `EXITEMPINTERESTPER` | DECIMAL(5,2) |  |  |  |  |
| 6 | `INTERESTPAIDON` | INTEGER | NOT NULL |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SUPERANNUATIONCALENDAR.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SUPERANNUATIONCALENDAR_CALYEAR` | [`FULLANDFINAL`](../HR/FULLANDFINAL.md) | `COMPANYCODE`, `CALYEARCODE` | `FULLANDFINAL.COMPANYCODE = SUPERANNUATIONCALENDAR.COMPANYCODE AND FULLANDFINAL.CALYEARCODE = SUPERANNUATIONCALENDAR.CODE` |
| `SUPERANNUATIONCALENDAR_LASTPROCESSCALENDAR` | [`SUPERANNUATIONSETTLEMENT`](../HR/SUPERANNUATIONSETTLEMENT.md) | `COMPANYCODE`, `LASTPROCESSCALENDARCODE` | `SUPERANNUATIONSETTLEMENT.COMPANYCODE = SUPERANNUATIONCALENDAR.COMPANYCODE AND SUPERANNUATIONSETTLEMENT.LASTPROCESSCALENDARCODE = SUPERANNUATIONCALENDAR.CODE` |
| `SUPERANNUATIONCALENDAR_CALYEAR` | [`SUPERANNUATIONYEARLYPROCESS`](../HR/SUPERANNUATIONYEARLYPROCESS.md) | `COMPANYCODE`, `CALYEARCODE` | `SUPERANNUATIONYEARLYPROCESS.COMPANYCODE = SUPERANNUATIONCALENDAR.COMPANYCODE AND SUPERANNUATIONYEARLYPROCESS.CALYEARCODE = SUPERANNUATIONCALENDAR.CODE` |

## Indexes

- `SUPERANNUATIONCALENDARUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.FROMDATE,
       t.TODATE,
       t.ONROLLINTERESTPER,
       t.EXITEMPINTERESTPER,
       t.INTERESTPAIDON,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.SUPERANNUATIONCALENDAR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
