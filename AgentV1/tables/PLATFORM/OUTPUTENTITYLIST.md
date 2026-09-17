# DB2ADMIN.OUTPUTENTITYLIST

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `RULECONFIGURATIONENTITYUSEDFOR`, `ENTITYCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 30916

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RULECONFIGURATIONENTITYUSEDFOR` | CHAR(2) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ENTITYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ABSPOLICYCODE` | CHAR(30) |  | FK | foreign_key |  |
| 3 | `DUMMY` | SMALLINT | NOT NULL |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSPOLICYTYPE_ABSPOLICY` | `ABSPOLICYCODE` | [`ABSPOLICYTYPE`](../PLATFORM/ABSPOLICYTYPE.md) | `CODE` | RESTRICT | `OUTPUTENTITYLIST.ABSPOLICYCODE = ABSPOLICYTYPE.CODE` |
| `RULECONFIGURATIONENTITY_OUTPUTENTITIES` | `RULECONFIGURATIONENTITYUSEDFOR` | [`RULECONFIGURATIONENTITY`](../PLATFORM/RULECONFIGURATIONENTITY.md) | `USEDFOR` | RESTRICT | `OUTPUTENTITYLIST.RULECONFIGURATIONENTITYUSEDFOR = RULECONFIGURATIONENTITY.USEDFOR` |
| `RULEENTITY_ENTITY` | `ENTITYCODE` | [`RULEENTITY`](../PLATFORM/RULEENTITY.md) | `CODE` | RESTRICT | `OUTPUTENTITYLIST.ENTITYCODE = RULEENTITY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `OUTPUTENTITYLISTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.RULECONFIGURATIONENTITYUSEDFOR,
       t.ENTITYCODE,
       t.ABSPOLICYCODE,
       t.DUMMY,
       t.ABSUNIQUEID
FROM   DB2ADMIN.OUTPUTENTITYLIST t
FETCH FIRST 100 ROWS ONLY;
```
