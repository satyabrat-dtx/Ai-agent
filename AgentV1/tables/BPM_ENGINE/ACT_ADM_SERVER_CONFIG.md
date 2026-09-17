# DB2ADMIN.ACT_ADM_SERVER_CONFIG

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`
- **Columns**: 11
- **Primary key**: `ID_`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 235154

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID_` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `NAME_` | VARCHAR(50) |  |  |  |  |
| 2 | `DESCRIPTION_` | VARCHAR(255) |  |  |  |  |
| 3 | `SERVER_ADDRESS_` | VARCHAR(100) |  |  |  |  |
| 4 | `PORT_` | INTEGER |  |  |  |  |
| 5 | `CONTEXT_ROOT_` | VARCHAR(100) |  |  |  |  |
| 6 | `REST_ROOT_` | VARCHAR(100) |  |  |  |  |
| 7 | `USER_NAME_` | VARCHAR(100) |  |  |  |  |
| 8 | `PASSWORD_` | VARCHAR(100) |  |  |  |  |
| 9 | `ENDPOINT_TYPE_` | INTEGER |  |  |  |  |
| 10 | `TENANT_ID_` | VARCHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ID_,
       t.NAME_,
       t.DESCRIPTION_,
       t.SERVER_ADDRESS_,
       t.PORT_,
       t.CONTEXT_ROOT_,
       t.REST_ROOT_,
       t.USER_NAME_,
       t.PASSWORD_,
       t.ENDPOINT_TYPE_,
       t.TENANT_ID_
FROM   DB2ADMIN.ACT_ADM_SERVER_CONFIG t
FETCH FIRST 100 ROWS ONLY;
```
