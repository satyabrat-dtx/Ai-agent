# DB2ADMIN.ACT_ADM_DATABASECHANGELOG

> **DO NOT QUERY FOR BUSINESS DATA.** Process-engine internal table; schema owned by Activiti/Flowable. No primary key declared; rows are not uniquely addressable by the schema.

- **Module**: `BPM_ENGINE` (high confidence — table name starts with 'ACT_')
- **Roles**: `bpm_engine_internal`, `no_primary_key`
- **Columns**: 14
- **Primary key**: _none declared_
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 235126

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID` | VARCHAR(255) | NOT NULL |  |  |  |
| 1 | `AUTHOR` | VARCHAR(255) | NOT NULL |  |  |  |
| 2 | `FILENAME` | VARCHAR(255) | NOT NULL |  |  |  |
| 3 | `DATEEXECUTED` | TIMESTAMP | NOT NULL |  |  |  |
| 4 | `ORDEREXECUTED` | INTEGER | NOT NULL |  |  |  |
| 5 | `EXECTYPE` | VARCHAR(10) | NOT NULL |  |  |  |
| 6 | `MD5SUM` | VARCHAR(35) |  |  |  |  |
| 7 | `DESCRIPTION` | VARCHAR(255) |  |  | description |  |
| 8 | `COMMENTS` | VARCHAR(255) |  |  |  |  |
| 9 | `TAG` | VARCHAR(255) |  |  |  |  |
| 10 | `LIQUIBASE` | VARCHAR(20) |  |  |  |  |
| 11 | `CONTEXTS` | VARCHAR(255) |  |  |  |  |
| 12 | `LABELS` | VARCHAR(255) |  |  |  |  |
| 13 | `DEPLOYMENT_ID` | VARCHAR(10) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ID,
       t.AUTHOR,
       t.FILENAME,
       t.DATEEXECUTED,
       t.ORDEREXECUTED,
       t.EXECTYPE,
       t.MD5SUM,
       t.DESCRIPTION,
       t.COMMENTS,
       t.TAG,
       t.LIQUIBASE,
       t.CONTEXTS
FROM   DB2ADMIN.ACT_ADM_DATABASECHANGELOG t
FETCH FIRST 100 ROWS ONLY;
```
