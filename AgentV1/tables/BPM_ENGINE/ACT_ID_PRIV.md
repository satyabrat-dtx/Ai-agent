# DB2ADMIN.ACT_ID_PRIV

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 2
- **Primary key**: `ID_`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 233837

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `NAME_` | VARCHAR(255) | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ACT_FK_PRIV_MAPPING` | [`ACT_ID_PRIV_MAPPING`](../BPM_ENGINE/ACT_ID_PRIV_MAPPING.md) | `PRIV_ID_` | `ACT_ID_PRIV_MAPPING.PRIV_ID_ = ACT_ID_PRIV.ID_` |

## Unique constraints

- `ACT_UNIQ_PRIV_NAME` (NAME_)

## Starter query

```sql
SELECT t.ID_,
       t.NAME_
FROM   DB2ADMIN.ACT_ID_PRIV t
FETCH FIRST 100 ROWS ONLY;
```
