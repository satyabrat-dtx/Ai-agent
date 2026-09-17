# DB2ADMIN.ACT_ID_USER

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 9
- **Primary key**: `ID_`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 233755

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `FIRST_` | VARCHAR(255) |  |  |  |  |
| 3 | `LAST_` | VARCHAR(255) |  |  |  |  |
| 4 | `DISPLAY_NAME_` | VARCHAR(255) |  |  |  |  |
| 5 | `EMAIL_` | VARCHAR(255) |  |  |  |  |
| 6 | `PWD_` | VARCHAR(255) |  |  |  |  |
| 7 | `PICTURE_ID_` | VARCHAR(64) |  |  |  |  |
| 8 | `TENANT_ID_` | VARCHAR(255) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ACT_FK_MEMB_USER` | [`ACT_ID_MEMBERSHIP`](../BPM_ENGINE/ACT_ID_MEMBERSHIP.md) | `USER_ID_` | `ACT_ID_MEMBERSHIP.USER_ID_ = ACT_ID_USER.ID_` |

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.FIRST_,
       t.LAST_,
       t.DISPLAY_NAME_,
       t.EMAIL_,
       t.PWD_,
       t.PICTURE_ID_,
       t.TENANT_ID_
FROM   DB2ADMIN.ACT_ID_USER t
FETCH FIRST 100 ROWS ONLY;
```
