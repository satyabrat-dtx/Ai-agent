# DB2ADMIN.RULECONFIGURATIONENTITY

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `USEDFOR`
- **FK degree**: referenced by 2 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 31041

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `USEDFOR` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 1 | `LABEL` | CHAR(50) | NOT NULL |  |  |  |
| 2 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `RULECONFIGURATIONENTITY_INPUTENTITIES` | [`INPUTENTITYLIST`](../PLATFORM/INPUTENTITYLIST.md) | `RULECONFIGURATIONENTITYUSEDFOR` | `INPUTENTITYLIST.RULECONFIGURATIONENTITYUSEDFOR = RULECONFIGURATIONENTITY.USEDFOR` |
| `RULECONFIGURATIONENTITY_OUTPUTENTITIES` | [`OUTPUTENTITYLIST`](../PLATFORM/OUTPUTENTITYLIST.md) | `RULECONFIGURATIONENTITYUSEDFOR` | `OUTPUTENTITYLIST.RULECONFIGURATIONENTITYUSEDFOR = RULECONFIGURATIONENTITY.USEDFOR` |

## Indexes

- `RULECONFIGURATIONENTITYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.USEDFOR,
       t.LABEL,
       t.ABSUNIQUEID
FROM   DB2ADMIN.RULECONFIGURATIONENTITY t
FETCH FIRST 100 ROWS ONLY;
```
