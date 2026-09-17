# DB2ADMIN.USACOSTCENTERGROUPDETAIL

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `USACOSTCENTERGROUPCOMPANYCODE`, `USACOSTCENTERGROUPGROUPCODE`, `COSTCENTERCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 107695

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `USACOSTCENTERGROUPCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `USACOSTCENTERGROUPGROUPCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `COSTCENTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `COSTCENTERCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `USACOSTCENTERGROUP_COSTCENTER` | `USACOSTCENTERGROUPCOMPANYCODE`, `USACOSTCENTERGROUPGROUPCODE` | [`USACOSTCENTERGROUP`](../LOCALIZATION/USACOSTCENTERGROUP.md) | `COMPANYCODE`, `GROUPCODE` | RESTRICT | `USACOSTCENTERGROUPDETAIL.USACOSTCENTERGROUPCOMPANYCODE = USACOSTCENTERGROUP.COMPANYCODE AND USACOSTCENTERGROUPDETAIL.USACOSTCENTERGROUPGROUPCODE = USACOSTCENTERGROUP.GROUPCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `USACOSTCENTERGROUPDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.USACOSTCENTERGROUPCOMPANYCODE,
       t.USACOSTCENTERGROUPGROUPCODE,
       t.COSTCENTERCOMPANYCODE,
       t.COSTCENTERCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.USACOSTCENTERGROUPDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
