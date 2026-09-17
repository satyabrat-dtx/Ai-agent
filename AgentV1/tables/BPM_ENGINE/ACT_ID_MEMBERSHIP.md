# DB2ADMIN.ACT_ID_MEMBERSHIP

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 2
- **Primary key**: `USER_ID_`, `GROUP_ID_`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 233733

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `USER_ID_` | VARCHAR(64) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `GROUP_ID_` | VARCHAR(64) | NOT NULL | PK FK | primary_key foreign_key |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACT_FK_MEMB_GROUP` | `GROUP_ID_` | [`ACT_ID_GROUP`](../BPM_ENGINE/ACT_ID_GROUP.md) | `ID_` | NO ACTION | `ACT_ID_MEMBERSHIP.GROUP_ID_ = ACT_ID_GROUP.ID_` |
| `ACT_FK_MEMB_USER` | `USER_ID_` | [`ACT_ID_USER`](../BPM_ENGINE/ACT_ID_USER.md) | `ID_` | NO ACTION | `ACT_ID_MEMBERSHIP.USER_ID_ = ACT_ID_USER.ID_` |

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.USER_ID_,
       t.GROUP_ID_
FROM   DB2ADMIN.ACT_ID_MEMBERSHIP t
FETCH FIRST 100 ROWS ONLY;
```
