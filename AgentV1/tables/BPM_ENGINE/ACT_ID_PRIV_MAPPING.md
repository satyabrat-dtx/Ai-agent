# DB2ADMIN.ACT_ID_PRIV_MAPPING

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 4
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 233866

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `PRIV_ID_` | VARCHAR(64) | NOT NULL | FK | foreign_key |  |
| 2 | `USER_ID_` | VARCHAR(255) |  |  |  |  |
| 3 | `GROUP_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACT_FK_PRIV_MAPPING` | `PRIV_ID_` | [`ACT_ID_PRIV`](../BPM_ENGINE/ACT_ID_PRIV.md) | `ID_` | NO ACTION | `ACT_ID_PRIV_MAPPING.PRIV_ID_ = ACT_ID_PRIV.ID_` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_PRIV_USER` (USER_ID_)
- `ACT_IDX_PRIV_GROUP` (GROUP_ID_)
- `ACT_IDX_PRIV_MAPPING` (PRIV_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.PRIV_ID_,
       t.USER_ID_,
       t.GROUP_ID_
FROM   DB2ADMIN.ACT_ID_PRIV_MAPPING t
FETCH FIRST 100 ROWS ONLY;
```
