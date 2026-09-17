# DB2ADMIN.APPAGENTSAVAILABILITYDEF

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `APPAGENTSCOMPANYCODE`, `APPAGENTSAGENTCODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 110745

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `APPAGENTSCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `APPAGENTSAGENTCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `WHSAVLGROUPCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `WAREHOUSEAVAILABILITYGROUPCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `APPAGENTS_APPAGENTSAVAILABILITYDEF` | `APPAGENTSCOMPANYCODE`, `APPAGENTSAGENTCODE` | [`APPAGENTS`](../SALES/APPAGENTS.md) | `COMPANYCODE`, `AGENTCODE` | RESTRICT | `APPAGENTSAVAILABILITYDEF.APPAGENTSCOMPANYCODE = APPAGENTS.COMPANYCODE AND APPAGENTSAVAILABILITYDEF.APPAGENTSAGENTCODE = APPAGENTS.AGENTCODE` |
| `AVAILABILITYWAREHOUSEGROUP_WAREHOUSEAVAILABILITYGROUP` | `WHSAVLGROUPCOMPANYCODE`, `WAREHOUSEAVAILABILITYGROUPCODE` | [`AVAILABILITYWAREHOUSEGROUP`](../CORE_MASTER/AVAILABILITYWAREHOUSEGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `APPAGENTSAVAILABILITYDEF.WHSAVLGROUPCOMPANYCODE = AVAILABILITYWAREHOUSEGROUP.COMPANYCODE AND APPAGENTSAVAILABILITYDEF.WAREHOUSEAVAILABILITYGROUPCODE = AVAILABILITYWAREHOUSEGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `APPAGENTSAVAILABILITYDEFUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.APPAGENTSCOMPANYCODE,
       t.APPAGENTSAGENTCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.WHSAVLGROUPCOMPANYCODE,
       t.WAREHOUSEAVAILABILITYGROUPCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.APPAGENTSAVAILABILITYDEF t
FETCH FIRST 100 ROWS ONLY;
```
