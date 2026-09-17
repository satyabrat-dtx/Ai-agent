# DB2ADMIN.ACT_CMMN_HI_MIL_INST

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 8
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 234887

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER | NOT NULL |  |  |  |
| 2 | `NAME_` | VARCHAR(255) | NOT NULL |  |  |  |
| 3 | `TIME_STAMP_` | TIMESTAMP | NOT NULL |  |  |  |
| 4 | `CASE_INST_ID_` | VARCHAR(255) | NOT NULL |  |  |  |
| 5 | `CASE_DEF_ID_` | VARCHAR(255) | NOT NULL |  |  |  |
| 6 | `ELEMENT_ID_` | VARCHAR(255) | NOT NULL |  |  |  |
| 7 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.NAME_,
       t.TIME_STAMP_,
       t.CASE_INST_ID_,
       t.CASE_DEF_ID_,
       t.ELEMENT_ID_,
       t.TENANT_ID_
FROM   DB2ADMIN.ACT_CMMN_HI_MIL_INST t
FETCH FIRST 100 ROWS ONLY;
```
