# DB2ADMIN.ACT_CMMN_RU_MIL_INST

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 7
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 234794

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `NAME_` | VARCHAR(255) | NOT NULL |  |  |  |
| 2 | `TIME_STAMP_` | TIMESTAMP | NOT NULL |  |  |  |
| 3 | `CASE_INST_ID_` | VARCHAR(255) | NOT NULL | FK | foreign_key |  |
| 4 | `CASE_DEF_ID_` | VARCHAR(255) | NOT NULL | FK | foreign_key |  |
| 5 | `ELEMENT_ID_` | VARCHAR(255) | NOT NULL |  |  |  |
| 6 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACT_FK_MIL_CASE_DEF` | `CASE_DEF_ID_` | [`ACT_CMMN_CASEDEF`](../BPM_ENGINE/ACT_CMMN_CASEDEF.md) | `ID_` | NO ACTION | `ACT_CMMN_RU_MIL_INST.CASE_DEF_ID_ = ACT_CMMN_CASEDEF.ID_` |
| `ACT_FK_MIL_CASE_INST` | `CASE_INST_ID_` | [`ACT_CMMN_RU_CASE_INST`](../BPM_ENGINE/ACT_CMMN_RU_CASE_INST.md) | `ID_` | NO ACTION | `ACT_CMMN_RU_MIL_INST.CASE_INST_ID_ = ACT_CMMN_RU_CASE_INST.ID_` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_MIL_CASE_DEF` (CASE_DEF_ID_)
- `ACT_IDX_MIL_CASE_INST` (CASE_INST_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.NAME_,
       t.TIME_STAMP_,
       t.CASE_INST_ID_,
       t.CASE_DEF_ID_,
       t.ELEMENT_ID_,
       t.TENANT_ID_
FROM   DB2ADMIN.ACT_CMMN_RU_MIL_INST t
FETCH FIRST 100 ROWS ONLY;
```
