# DB2ADMIN.LOCATIONSEGMENTSLISTSUBCODE

- **Module**: `WAREHOUSE` (low confidence — FK neighbourhood: 1 of 1 related tables are WAREHOUSE)
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `LOCATIONSEGMENTSLISTCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 13789

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LOCATIONSEGMENTSLISTCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `DUMMY` | INTEGER | NOT NULL |  |  |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `LOCATIONSEGMENTSLIST_LOCATIONSEGMENTSLISTSUBCODE` | `LOCATIONSEGMENTSLISTCODE` | [`LOCATIONSEGMENTSLIST`](../WAREHOUSE/LOCATIONSEGMENTSLIST.md) | `CODE` | RESTRICT | `LOCATIONSEGMENTSLISTSUBCODE.LOCATIONSEGMENTSLISTCODE = LOCATIONSEGMENTSLIST.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LOCSEGMENTSLISTSUBCODEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.LOCATIONSEGMENTSLISTCODE,
       t.CODE,
       t.DUMMY,
       t.ABSUNIQUEID
FROM   DB2ADMIN.LOCATIONSEGMENTSLISTSUBCODE t
FETCH FIRST 100 ROWS ONLY;
```
