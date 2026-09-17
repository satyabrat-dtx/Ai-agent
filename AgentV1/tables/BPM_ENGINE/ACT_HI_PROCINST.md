# DB2ADMIN.ACT_HI_PROCINST

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 21
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 233366

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `PROC_INST_ID_` | VARCHAR(64) | NOT NULL |  |  |  |
| 3 | `BUSINESS_KEY_` | VARCHAR(255) |  |  |  |  |
| 4 | `PROC_DEF_ID_` | VARCHAR(64) | NOT NULL |  |  |  |
| 5 | `START_TIME_` | TIMESTAMP | NOT NULL |  |  |  |
| 6 | `END_TIME_` | TIMESTAMP |  |  |  |  |
| 7 | `DURATION_` | BIGINT |  |  |  |  |
| 8 | `START_USER_ID_` | VARCHAR(255) |  |  |  |  |
| 9 | `START_ACT_ID_` | VARCHAR(255) |  |  |  |  |
| 10 | `END_ACT_ID_` | VARCHAR(255) |  |  |  |  |
| 11 | `SUPER_PROCESS_INSTANCE_ID_` | VARCHAR(64) |  |  |  |  |
| 12 | `DELETE_REASON_` | VARCHAR(4000) |  |  |  |  |
| 13 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |
| 14 | `NAME_` | VARCHAR(255) |  |  |  |  |
| 15 | `CALLBACK_ID_` | VARCHAR(255) |  |  |  |  |
| 16 | `CALLBACK_TYPE_` | VARCHAR(255) |  |  |  |  |
| 17 | `REFERENCE_ID_` | VARCHAR(255) |  |  |  |  |
| 18 | `REFERENCE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 19 | `PROPAGATED_STAGE_INST_ID_` | VARCHAR(255) |  |  |  |  |
| 20 | `BUSINESS_STATUS_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_HI_PRO_INST_END` (END_TIME_)
- `ACT_IDX_HI_PRO_I_BUSKEY` (BUSINESS_KEY_)
- `ACT_IDX_HI_PRO_SUPER_PROCINST` (SUPER_PROCESS_INSTANCE_ID_)

## Unique constraints

- `PROC_INST_ID_` (PROC_INST_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.PROC_INST_ID_,
       t.BUSINESS_KEY_,
       t.PROC_DEF_ID_,
       t.START_TIME_,
       t.END_TIME_,
       t.DURATION_,
       t.START_USER_ID_,
       t.START_ACT_ID_,
       t.END_ACT_ID_,
       t.SUPER_PROCESS_INSTANCE_ID_
FROM   DB2ADMIN.ACT_HI_PROCINST t
FETCH FIRST 100 ROWS ONLY;
```
