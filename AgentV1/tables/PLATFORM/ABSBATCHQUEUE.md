# DB2ADMIN.ABSBATCHQUEUE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `NAME`
- **FK degree**: referenced by 3 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 113

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `NAME` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 1 | `DESCRIPTION` | VARCHAR(250) |  |  | description |  |
| 2 | `ACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 3 | `MAXACTIVEJOBS` | INTEGER | NOT NULL |  |  |  |
| 4 | `BEGINTIME` | TIME |  |  |  |  |
| 5 | `ENDTIME` | TIME |  |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 7 | `ALLOWEDIPS` | VARCHAR(250) |  |  |  |  |
| 8 | `NODEINSTANCEIDS` | VARCHAR(250) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSBATCHQUEUE_DEFAULTBATCHQUEUE` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `DEFAULTBATCHQUEUENAME` | `ABSUSERDEF.DEFAULTBATCHQUEUENAME = ABSBATCHQUEUE.NAME` |
| `ABSBATCHQUEUE_DEFAULTBATCHQUEUE` | [`ABSSYSTEMPROPERTIES`](../PLATFORM/ABSSYSTEMPROPERTIES.md) | `DEFAULTBATCHQUEUENAME` | `ABSSYSTEMPROPERTIES.DEFAULTBATCHQUEUENAME = ABSBATCHQUEUE.NAME` |
| `ABSBATCHQUEUE_DFTJOBQUEUEPLANNING` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `DFTJOBQUEUEPLANNINGNAME` | `ITEMTYPE.DFTJOBQUEUEPLANNINGNAME = ABSBATCHQUEUE.NAME` |

## Indexes

- `ABSBATCHQUEUEUID` (ABSUNIQUEID)
- `ABSBATCHQUEUEIDX1` (ACTIVE, MAXACTIVEJOBS)

## Starter query

```sql
SELECT t.NAME,
       t.DESCRIPTION,
       t.ACTIVE,
       t.MAXACTIVEJOBS,
       t.BEGINTIME,
       t.ENDTIME,
       t.ABSUNIQUEID,
       t.ALLOWEDIPS,
       t.NODEINSTANCEIDS
FROM   DB2ADMIN.ABSBATCHQUEUE t
FETCH FIRST 100 ROWS ONLY;
```
