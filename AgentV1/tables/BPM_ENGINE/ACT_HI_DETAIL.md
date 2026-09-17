# DB2ADMIN.ACT_HI_DETAIL

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 15
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 233523

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `TYPE_` | VARCHAR(255) | NOT NULL |  |  |  |
| 2 | `PROC_INST_ID_` | VARCHAR(64) |  |  |  |  |
| 3 | `EXECUTION_ID_` | VARCHAR(64) |  |  |  |  |
| 4 | `TASK_ID_` | VARCHAR(64) |  |  |  |  |
| 5 | `ACT_INST_ID_` | VARCHAR(64) |  |  |  |  |
| 6 | `NAME_` | VARCHAR(255) | NOT NULL |  |  |  |
| 7 | `VAR_TYPE_` | VARCHAR(255) |  |  |  |  |
| 8 | `REV_` | INTEGER |  |  |  |  |
| 9 | `TIME_` | TIMESTAMP | NOT NULL |  |  |  |
| 10 | `BYTEARRAY_ID_` | VARCHAR(64) |  |  |  |  |
| 11 | `DOUBLE_` | DOUBLE |  |  |  |  |
| 12 | `LONG_` | BIGINT |  |  |  |  |
| 13 | `TEXT_` | VARCHAR(4000) |  |  |  |  |
| 14 | `TEXT2_` | VARCHAR(4000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_HI_DETAIL_PROC_INST` (PROC_INST_ID_)
- `ACT_IDX_HI_DETAIL_ACT_INST` (ACT_INST_ID_)
- `ACT_IDX_HI_DETAIL_TIME` (TIME_)
- `ACT_IDX_HI_DETAIL_NAME` (NAME_)
- `ACT_IDX_HI_DETAIL_TASK_ID` (TASK_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.TYPE_,
       t.PROC_INST_ID_,
       t.EXECUTION_ID_,
       t.TASK_ID_,
       t.ACT_INST_ID_,
       t.NAME_,
       t.VAR_TYPE_,
       t.REV_,
       t.TIME_,
       t.BYTEARRAY_ID_,
       t.DOUBLE_
FROM   DB2ADMIN.ACT_HI_DETAIL t
FETCH FIRST 100 ROWS ONLY;
```
