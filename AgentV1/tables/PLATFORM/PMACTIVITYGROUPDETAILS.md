# DB2ADMIN.PMACTIVITYGROUPDETAILS

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 2 of 2 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `PMACTIVITYGROUPCOMPANYCODE`, `PMACTIVITYGROUPCOUNTERCODE`, `PMACTIVITYGROUPCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 83639

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PMACTIVITYGROUPCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PMACTIVITYGROUPCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PMACTIVITYGROUPCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINENO` | DECIMAL(10,0) | NOT NULL | PK | primary_key |  |
| 4 | `ACTIVITYCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 5 | `ACTIVITYCODE` | CHAR(15) |  | FK | foreign_key |  |
| 6 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 7 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `PREDECESSORACTIVITYCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 13 | `PREDECESSORACTIVITYCODE` | CHAR(15) |  |  |  |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 15 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 16 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DIVISION_DIVISION` | `PMACTIVITYGROUPCOMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMACTIVITYGROUPDETAILS.PMACTIVITYGROUPCOMPANYCODE = DIVISION.COMPANYCODE AND PMACTIVITYGROUPDETAILS.DIVISIONCODE = DIVISION.CODE` |
| `PMACTIVITYGROUP_DETAIL` | `PMACTIVITYGROUPCOMPANYCODE`, `PMACTIVITYGROUPCOUNTERCODE`, `PMACTIVITYGROUPCODE` | [`PMACTIVITYGROUP`](../PLATFORM/PMACTIVITYGROUP.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMACTIVITYGROUPDETAILS.PMACTIVITYGROUPCOMPANYCODE = PMACTIVITYGROUP.COMPANYCODE AND PMACTIVITYGROUPDETAILS.PMACTIVITYGROUPCOUNTERCODE = PMACTIVITYGROUP.COUNTERCODE AND PMACTIVITYGROUPDETAILS.PMACTIVITYGROUPCODE = PMACTIVITYGROUP.CODE` |
| `PMACTIVITY_ACTIVITY` | `PMACTIVITYGROUPCOMPANYCODE`, `ACTIVITYCOUNTERCODE`, `ACTIVITYCODE` | [`PMACTIVITY`](../PLATFORM/PMACTIVITY.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMACTIVITYGROUPDETAILS.PMACTIVITYGROUPCOMPANYCODE = PMACTIVITY.COMPANYCODE AND PMACTIVITYGROUPDETAILS.ACTIVITYCOUNTERCODE = PMACTIVITY.COUNTERCODE AND PMACTIVITYGROUPDETAILS.ACTIVITYCODE = PMACTIVITY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PMACTIVITYGROUPDETAILSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PMACTIVITYGROUPCOMPANYCODE,
       t.PMACTIVITYGROUPCOUNTERCODE,
       t.PMACTIVITYGROUPCODE,
       t.LINENO,
       t.ACTIVITYCOUNTERCODE,
       t.ACTIVITYCODE,
       t.SEQUENCE,
       t.STATUS,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.PMACTIVITYGROUPDETAILS t
FETCH FIRST 100 ROWS ONLY;
```
