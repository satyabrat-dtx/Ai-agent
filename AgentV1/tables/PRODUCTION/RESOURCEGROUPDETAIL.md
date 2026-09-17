# DB2ADMIN.RESOURCEGROUPDETAIL

- **Module**: `PRODUCTION` (low confidence — FK neighbourhood: 1 of 1 related tables are PRODUCTION)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `RESOURCEGROUPCOMPANYCODE`, `RESOURCEGROUPCODE`, `MAINRESOURCECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 95376

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RESOURCEGROUPCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `RESOURCEGROUPCODE` | CHAR(5) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `MAINRESOURCECODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 4 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 5 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 6 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `RESOURCEGROUP_DETAIL` | `RESOURCEGROUPCOMPANYCODE`, `RESOURCEGROUPCODE` | [`RESOURCEGROUP`](../PRODUCTION/RESOURCEGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RESOURCEGROUPDETAIL.RESOURCEGROUPCOMPANYCODE = RESOURCEGROUP.COMPANYCODE AND RESOURCEGROUPDETAIL.RESOURCEGROUPCODE = RESOURCEGROUP.CODE` |
| `RESOURCES_MAINRESOURCE` | `RESOURCEGROUPCOMPANYCODE`, `MAINRESOURCECODE` | [`RESOURCES`](../PRODUCTION/RESOURCES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RESOURCEGROUPDETAIL.RESOURCEGROUPCOMPANYCODE = RESOURCES.COMPANYCODE AND RESOURCEGROUPDETAIL.MAINRESOURCECODE = RESOURCES.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RESOURCEGROUPDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.RESOURCEGROUPCOMPANYCODE,
       t.RESOURCEGROUPCODE,
       t.MAINRESOURCECODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.RESOURCEGROUPDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
