# DB2ADMIN.ACT_RU_ENTITYLINK

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 15
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 231480

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `CREATE_TIME_` | TIMESTAMP |  |  |  |  |
| 3 | `LINK_TYPE_` | VARCHAR(255) |  |  |  |  |
| 4 | `SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 5 | `SUB_SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 6 | `SCOPE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 7 | `SCOPE_DEFINITION_ID_` | VARCHAR(255) |  |  |  |  |
| 8 | `PARENT_ELEMENT_ID_` | VARCHAR(255) |  |  |  |  |
| 9 | `REF_SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 10 | `REF_SCOPE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 11 | `REF_SCOPE_DEFINITION_ID_` | VARCHAR(255) |  |  |  |  |
| 12 | `ROOT_SCOPE_ID_` | VARCHAR(255) |  |  |  |  |
| 13 | `ROOT_SCOPE_TYPE_` | VARCHAR(255) |  |  |  |  |
| 14 | `HIERARCHY_TYPE_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACT_IDX_ENT_LNK_SCOPE` (SCOPE_ID_, SCOPE_TYPE_, LINK_TYPE_)
- `ACT_IDX_ENT_LNK_REF_SCOPE` (REF_SCOPE_ID_, REF_SCOPE_TYPE_, LINK_TYPE_)
- `ACT_IDX_ENT_LNK_ROOT_SCOPE` (ROOT_SCOPE_ID_, ROOT_SCOPE_TYPE_, LINK_TYPE_)
- `ACT_IDX_ENT_LNK_SCOPE_DEF` (SCOPE_DEFINITION_ID_, SCOPE_TYPE_, LINK_TYPE_)

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.CREATE_TIME_,
       t.LINK_TYPE_,
       t.SCOPE_ID_,
       t.SUB_SCOPE_ID_,
       t.SCOPE_TYPE_,
       t.SCOPE_DEFINITION_ID_,
       t.PARENT_ELEMENT_ID_,
       t.REF_SCOPE_ID_,
       t.REF_SCOPE_TYPE_,
       t.REF_SCOPE_DEFINITION_ID_
FROM   DB2ADMIN.ACT_RU_ENTITYLINK t
FETCH FIRST 100 ROWS ONLY;
```
