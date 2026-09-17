# DB2ADMIN.ACT_RU_EVENT_SUBSCR

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 17
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 231643

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `EVENT_TYPE_` | VARCHAR(255) | NOT NULL |  |  |  |
| 3 | `EVENT_NAME_` | VARCHAR(255) |  |  |  |  |
| 4 | `EXECUTION_ID_` | VARCHAR(64) |  | FK | foreign_key |  |
| 5 | `PROC_INST_ID_` | VARCHAR(64) |  |  |  |  |
| 6 | `ACTIVITY_ID_` | VARCHAR(64) |  |  |  |  |
| 7 | `CONFIGURATION_` | VARCHAR(255) |  |  |  |  |
| 8 | `CREATED_` | TIMESTAMP | NOT NULL |  |  |  |
| 9 | `PROC_DEF_ID_` | VARCHAR(64) |  |  |  |  |
| 10 | `SUB_SCOPE_ID_` | VARCHAR(64) |  |  |  |  |
| 11 | `SCOPE_ID_` | VARCHAR(64) |  |  |  |  |
| 12 | `SCOPE_DEFINITION_ID_` | VARCHAR(64) |  |  |  |  |
| 13 | `SCOPE_TYPE_` | VARCHAR(64) |  |  |  |  |
| 14 | `LOCK_TIME_` | TIMESTAMP |  |  |  |  |
| 15 | `LOCK_OWNER_` | VARCHAR(255) |  |  |  |  |
| 16 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACT_FK_EVENT_EXEC` | `EXECUTION_ID_` | [`ACT_RU_EXECUTION`](../BPM_ENGINE/ACT_RU_EXECUTION.md) | `ID_` | NO ACTION | `ACT_RU_EVENT_SUBSCR.EXECUTION_ID_ = ACT_RU_EXECUTION.ID_` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_EVENT_SUBSCR_CONFIG_` (CONFIGURATION_)
- `ACT_IDX_EVENT_SUBSCR_EXEC_ID` (EXECUTION_ID_)
- `ACT_IDX_EVENT_SUBSCR_SCOPEREF_` (SCOPE_ID_, SCOPE_TYPE_)

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.EVENT_TYPE_,
       t.EVENT_NAME_,
       t.EXECUTION_ID_,
       t.PROC_INST_ID_,
       t.ACTIVITY_ID_,
       t.CONFIGURATION_,
       t.CREATED_,
       t.PROC_DEF_ID_,
       t.SUB_SCOPE_ID_,
       t.SCOPE_ID_
FROM   DB2ADMIN.ACT_RU_EVENT_SUBSCR t
FETCH FIRST 100 ROWS ONLY;
```
