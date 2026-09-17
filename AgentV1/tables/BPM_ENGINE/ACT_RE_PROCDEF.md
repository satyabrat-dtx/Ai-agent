# DB2ADMIN.ACT_RE_PROCDEF

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 18
- **Primary key**: `ID_`
- **FK degree**: referenced by 8 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 233132

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `CATEGORY_` | VARCHAR(255) |  |  |  |  |
| 3 | `NAME_` | VARCHAR(255) |  |  |  |  |
| 4 | `KEY_` | VARCHAR(255) | NOT NULL |  |  |  |
| 5 | `VERSION_` | INTEGER | NOT NULL |  |  |  |
| 6 | `DEPLOYMENT_ID_` | VARCHAR(64) |  |  |  |  |
| 7 | `RESOURCE_NAME_` | VARCHAR(4000) |  |  |  |  |
| 8 | `DGRM_RESOURCE_NAME_` | VARCHAR(4000) |  |  |  |  |
| 9 | `DESCRIPTION_` | VARCHAR(4000) |  |  |  |  |
| 10 | `HAS_START_FORM_KEY_` | SMALLINT |  |  |  |  |
| 11 | `HAS_GRAPHICAL_NOTATION_` | SMALLINT |  |  |  |  |
| 12 | `SUSPENSION_STATE_` | INTEGER |  |  |  |  |
| 13 | `TENANT_ID_` | VARCHAR(255) | NOT NULL |  |  |  |
| 14 | `DERIVED_FROM_` | VARCHAR(64) |  |  |  |  |
| 15 | `DERIVED_FROM_ROOT_` | VARCHAR(64) |  |  |  |  |
| 16 | `DERIVED_VERSION_` | INTEGER | NOT NULL |  |  |  |
| 17 | `ENGINE_VERSION_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 8

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ACT_FK_ATHRZ_PROCEDEF` | [`ACT_RU_IDENTITYLINK`](../BPM_ENGINE/ACT_RU_IDENTITYLINK.md) | `PROC_DEF_ID_` | `ACT_RU_IDENTITYLINK.PROC_DEF_ID_ = ACT_RE_PROCDEF.ID_` |
| `ACT_FK_TASK_PROCDEF` | [`ACT_RU_TASK`](../BPM_ENGINE/ACT_RU_TASK.md) | `PROC_DEF_ID_` | `ACT_RU_TASK.PROC_DEF_ID_ = ACT_RE_PROCDEF.ID_` |
| `ACT_FK_JOB_PROC_DEF` | [`ACT_RU_JOB`](../BPM_ENGINE/ACT_RU_JOB.md) | `PROC_DEF_ID_` | `ACT_RU_JOB.PROC_DEF_ID_ = ACT_RE_PROCDEF.ID_` |
| `ACT_FK_TIMER_JOB_PROC_DEF` | [`ACT_RU_TIMER_JOB`](../BPM_ENGINE/ACT_RU_TIMER_JOB.md) | `PROC_DEF_ID_` | `ACT_RU_TIMER_JOB.PROC_DEF_ID_ = ACT_RE_PROCDEF.ID_` |
| `ACT_FK_SUSPENDED_JOB_PROC_DEF` | [`ACT_RU_SUSPENDED_JOB`](../BPM_ENGINE/ACT_RU_SUSPENDED_JOB.md) | `PROC_DEF_ID_` | `ACT_RU_SUSPENDED_JOB.PROC_DEF_ID_ = ACT_RE_PROCDEF.ID_` |
| `ACT_FK_DEADLETTER_JOB_PROC_DEF` | [`ACT_RU_DEADLETTER_JOB`](../BPM_ENGINE/ACT_RU_DEADLETTER_JOB.md) | `PROC_DEF_ID_` | `ACT_RU_DEADLETTER_JOB.PROC_DEF_ID_ = ACT_RE_PROCDEF.ID_` |
| `ACT_FK_EXE_PROCDEF` | [`ACT_RU_EXECUTION`](../BPM_ENGINE/ACT_RU_EXECUTION.md) | `PROC_DEF_ID_` | `ACT_RU_EXECUTION.PROC_DEF_ID_ = ACT_RE_PROCDEF.ID_` |
| `ACT_FK_INFO_PROCDEF` | [`ACT_PROCDEF_INFO`](../BPM_ENGINE/ACT_PROCDEF_INFO.md) | `PROC_DEF_ID_` | `ACT_PROCDEF_INFO.PROC_DEF_ID_ = ACT_RE_PROCDEF.ID_` |

## Check constraints

- `SQL250408061220620`: `HAS_START_FORM_KEY_ in (1,0)`
- `SQL250408061220630`: `HAS_GRAPHICAL_NOTATION_ in (1,0)`

## Unique constraints

- `ACT_UNIQ_PROCDEF` (KEY_, VERSION_, DERIVED_VERSION_, TENANT_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.CATEGORY_,
       t.NAME_,
       t.KEY_,
       t.VERSION_,
       t.DEPLOYMENT_ID_,
       t.RESOURCE_NAME_,
       t.DGRM_RESOURCE_NAME_,
       t.DESCRIPTION_,
       t.HAS_START_FORM_KEY_,
       t.HAS_GRAPHICAL_NOTATION_
FROM   DB2ADMIN.ACT_RE_PROCDEF t
FETCH FIRST 100 ROWS ONLY;
```
