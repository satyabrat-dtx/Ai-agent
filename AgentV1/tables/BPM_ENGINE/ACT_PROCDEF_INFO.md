# DB2ADMIN.ACT_PROCDEF_INFO

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 4
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 233218

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `PROC_DEF_ID_` | VARCHAR(64) | NOT NULL | FK | foreign_key |  |
| 2 | `REV_` | INTEGER |  |  |  |  |
| 3 | `INFO_JSON_ID_` | VARCHAR(64) |  | FK | foreign_key |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACT_FK_INFO_JSON_BA` | `INFO_JSON_ID_` | [`ACT_GE_BYTEARRAY`](../BPM_ENGINE/ACT_GE_BYTEARRAY.md) | `ID_` | NO ACTION | `ACT_PROCDEF_INFO.INFO_JSON_ID_ = ACT_GE_BYTEARRAY.ID_` |
| `ACT_FK_INFO_PROCDEF` | `PROC_DEF_ID_` | [`ACT_RE_PROCDEF`](../BPM_ENGINE/ACT_RE_PROCDEF.md) | `ID_` | NO ACTION | `ACT_PROCDEF_INFO.PROC_DEF_ID_ = ACT_RE_PROCDEF.ID_` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_INFO_PROCDEF` (PROC_DEF_ID_)

## Unique constraints

- `ACT_UNIQ_INFO_PROCDEF` (PROC_DEF_ID_)

## Starter query

```sql
SELECT t.ID_,
       t.PROC_DEF_ID_,
       t.REV_,
       t.INFO_JSON_ID_
FROM   DB2ADMIN.ACT_PROCDEF_INFO t
FETCH FIRST 100 ROWS ONLY;
```
