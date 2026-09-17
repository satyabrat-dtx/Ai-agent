# DB2ADMIN.INPUTENTITYLIST

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 2 of 2 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `RULECONFIGURATIONENTITYUSEDFOR`, `ENTITYCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 30882

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RULECONFIGURATIONENTITYUSEDFOR` | CHAR(2) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ENTITYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DUMMY` | SMALLINT | NOT NULL |  |  |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `RULECONFIGURATIONENTITY_INPUTENTITIES` | `RULECONFIGURATIONENTITYUSEDFOR` | [`RULECONFIGURATIONENTITY`](../PLATFORM/RULECONFIGURATIONENTITY.md) | `USEDFOR` | RESTRICT | `INPUTENTITYLIST.RULECONFIGURATIONENTITYUSEDFOR = RULECONFIGURATIONENTITY.USEDFOR` |
| `RULEENTITY_ENTITY` | `ENTITYCODE` | [`RULEENTITY`](../PLATFORM/RULEENTITY.md) | `CODE` | RESTRICT | `INPUTENTITYLIST.ENTITYCODE = RULEENTITY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INPUTENTITYLISTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.RULECONFIGURATIONENTITYUSEDFOR,
       t.ENTITYCODE,
       t.DUMMY,
       t.ABSUNIQUEID
FROM   DB2ADMIN.INPUTENTITYLIST t
FETCH FIRST 100 ROWS ONLY;
```
