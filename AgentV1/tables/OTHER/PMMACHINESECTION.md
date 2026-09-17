# DB2ADMIN.PMMACHINESECTION

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `PMBOMCOMPANYCODE`, `PMBOMCOUNTERCODE`, `PMBOMCODE`, `SECTIONCODE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 111468

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PMBOMCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PMBOMCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PMBOMCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SECTIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PMBOMSECTION_SECTION` | `PMBOMCOMPANYCODE`, `SECTIONCODE` | [`PMBOMSECTION`](../OTHER/PMBOMSECTION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMMACHINESECTION.PMBOMCOMPANYCODE = PMBOMSECTION.COMPANYCODE AND PMMACHINESECTION.SECTIONCODE = PMBOMSECTION.CODE` |
| `PMBOM_SECTION` | `PMBOMCOMPANYCODE`, `PMBOMCOUNTERCODE`, `PMBOMCODE` | [`PMBOM`](../CORE_MASTER/PMBOM.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMMACHINESECTION.PMBOMCOMPANYCODE = PMBOM.COMPANYCODE AND PMMACHINESECTION.PMBOMCOUNTERCODE = PMBOM.COUNTERCODE AND PMMACHINESECTION.PMBOMCODE = PMBOM.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PMMACHINESECTION_COMPONENT` | [`PMSECTIONCOMPONENT`](../OTHER/PMSECTIONCOMPONENT.md) | `PMMACHINESECTIONPMBOMCMYCODE`, `PMMACHINESECTIONPMBOMCNTCODE`, `PMMACHINESECTIONPMBOMCODE`, `PMMACHINESECTIONSECTIONCODE` | `PMSECTIONCOMPONENT.PMMACHINESECTIONPMBOMCMYCODE = PMMACHINESECTION.PMBOMCOMPANYCODE AND PMSECTIONCOMPONENT.PMMACHINESECTIONPMBOMCNTCODE = PMMACHINESECTION.PMBOMCOUNTERCODE AND PMSECTIONCOMPONENT.PMMACHINESECTIONPMBOMCODE = PMMACHINESECTION.PMBOMCODE AND PMSECTIONCOMPONENT.PMMACHINESECTIONSECTIONCODE = PMMACHINESECTION.SECTIONCODE` |

## Indexes

- `PMMACHINESECTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PMBOMCOMPANYCODE,
       t.PMBOMCOUNTERCODE,
       t.PMBOMCODE,
       t.SECTIONCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.PMMACHINESECTION t
FETCH FIRST 100 ROWS ONLY;
```
