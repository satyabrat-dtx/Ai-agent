# DB2ADMIN.ACT_CMMN_HI_CASE_INST

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 18
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 234840

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER | NOT NULL |  |  |  |
| 2 | `BUSINESS_KEY_` | VARCHAR(255) |  |  |  |  |
| 3 | `NAME_` | VARCHAR(255) |  |  |  |  |
| 4 | `PARENT_ID_` | VARCHAR(255) |  |  |  |  |
| 5 | `CASE_DEF_ID_` | VARCHAR(255) |  |  |  |  |
| 6 | `STATE_` | VARCHAR(255) |  |  |  |  |
| 7 | `START_TIME_` | TIMESTAMP |  |  |  |  |
| 8 | `END_TIME_` | TIMESTAMP |  |  |  |  |
| 9 | `START_USER_ID_` | VARCHAR(255) |  |  |  |  |
| 10 | `CALLBACK_ID_` | VARCHAR(255) |  |  |  |  |
| 11 | `CALLBACK_TYPE_` | VARCHAR(255) |  |  |  |  |
| 12 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |
| 13 | `REFERENCE_ID_` | VARCHAR(255) |  |  |  |  |
| 14 | `REFERENCE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 15 | `LAST_REACTIVATION_TIME_` | TIMESTAMP(3) |  |  |  |  |
| 16 | `LAST_REACTIVATION_USER_ID_` | VARCHAR(255) |  |  |  |  |
| 17 | `BUSINESS_STATUS_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_HI_CASE_INST_END` (END_TIME_)

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.BUSINESS_KEY_,
       t.NAME_,
       t.PARENT_ID_,
       t.CASE_DEF_ID_,
       t.STATE_,
       t.START_TIME_,
       t.END_TIME_,
       t.START_USER_ID_,
       t.CALLBACK_ID_,
       t.CALLBACK_TYPE_
FROM   DB2ADMIN.ACT_CMMN_HI_CASE_INST t
FETCH FIRST 100 ROWS ONLY;
```
