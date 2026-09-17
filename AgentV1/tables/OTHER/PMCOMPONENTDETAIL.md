# DB2ADMIN.PMCOMPONENTDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `PMBOMCOMPANYCODE`, `PMBOMCOUNTERCODE`, `PMBOMCODE`, `PMMACHINESECTIONCODE`, `PMSECTIONCOMPONENTCODE`, `DETAILCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 111421

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PMBOMCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PMBOMCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PMBOMCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PMMACHINESECTIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PMSECTIONCOMPONENTCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `DETAILCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PMBOMCOMPONENTDETAIL_DETAIL` | `PMBOMCOMPANYCODE`, `DETAILCODE` | [`PMBOMCOMPONENTDETAIL`](../OTHER/PMBOMCOMPONENTDETAIL.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMCOMPONENTDETAIL.PMBOMCOMPANYCODE = PMBOMCOMPONENTDETAIL.COMPANYCODE AND PMCOMPONENTDETAIL.DETAILCODE = PMBOMCOMPONENTDETAIL.CODE` |
| `PMSECTIONCOMPONENT_DETAIL` | `PMBOMCOMPANYCODE`, `PMBOMCOUNTERCODE`, `PMBOMCODE`, `PMMACHINESECTIONCODE`, `PMSECTIONCOMPONENTCODE` | [`PMSECTIONCOMPONENT`](../OTHER/PMSECTIONCOMPONENT.md) | `PMMACHINESECTIONPMBOMCMYCODE`, `PMMACHINESECTIONPMBOMCNTCODE`, `PMMACHINESECTIONPMBOMCODE`, `PMMACHINESECTIONSECTIONCODE`, `COMPONENTCODE` | RESTRICT | `PMCOMPONENTDETAIL.PMBOMCOMPANYCODE = PMSECTIONCOMPONENT.PMMACHINESECTIONPMBOMCMYCODE AND PMCOMPONENTDETAIL.PMBOMCOUNTERCODE = PMSECTIONCOMPONENT.PMMACHINESECTIONPMBOMCNTCODE AND PMCOMPONENTDETAIL.PMBOMCODE = PMSECTIONCOMPONENT.PMMACHINESECTIONPMBOMCODE AND PMCOMPONENTDETAIL.PMMACHINESECTIONCODE = PMSECTIONCOMPONENT.PMMACHINESECTIONSECTIONCODE AND PMCOMPONENTDETAIL.PMSECTIONCOMPONENTCODE = PMSECTIONCOMPONENT.COMPONENTCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PMCOMPONENTDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PMBOMCOMPANYCODE,
       t.PMBOMCOUNTERCODE,
       t.PMBOMCODE,
       t.PMMACHINESECTIONCODE,
       t.PMSECTIONCOMPONENTCODE,
       t.DETAILCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.PMCOMPONENTDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
