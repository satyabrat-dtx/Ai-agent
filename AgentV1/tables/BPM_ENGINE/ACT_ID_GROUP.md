# DB2ADMIN.ACT_ID_GROUP

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 4
- **Primary key**: `ID_`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 233710

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `NAME_` | VARCHAR(255) |  |  |  |  |
| 3 | `TYPE_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ACT_FK_MEMB_GROUP` | [`ACT_ID_MEMBERSHIP`](../BPM_ENGINE/ACT_ID_MEMBERSHIP.md) | `GROUP_ID_` | `ACT_ID_MEMBERSHIP.GROUP_ID_ = ACT_ID_GROUP.ID_` |

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.NAME_,
       t.TYPE_
FROM   DB2ADMIN.ACT_ID_GROUP t
FETCH FIRST 100 ROWS ONLY;
```
