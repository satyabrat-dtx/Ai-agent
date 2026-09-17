# DB2ADMIN.ACT_ID_TOKEN

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 8
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 233810

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(64) | NOT NULL | PK | primary_key |  |
| 1 | `REV_` | INTEGER |  |  |  |  |
| 2 | `TOKEN_VALUE_` | VARCHAR(255) |  |  |  |  |
| 3 | `TOKEN_DATE_` | TIMESTAMP |  |  |  |  |
| 4 | `IP_ADDRESS_` | VARCHAR(255) |  |  |  |  |
| 5 | `USER_AGENT_` | VARCHAR(255) |  |  |  |  |
| 6 | `USER_ID_` | VARCHAR(255) |  |  |  |  |
| 7 | `TOKEN_DATA_` | VARCHAR(2000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ID_,
       t.REV_,
       t.TOKEN_VALUE_,
       t.TOKEN_DATE_,
       t.IP_ADDRESS_,
       t.USER_AGENT_,
       t.USER_ID_,
       t.TOKEN_DATA_
FROM   DB2ADMIN.ACT_ID_TOKEN t
FETCH FIRST 100 ROWS ONLY;
```
