# DB2ADMIN.SCDM_JOB_MESSAGES

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `JM_IDENTIFIER`, `JM_PREQ_NO`, `JM_PSTEP_ID`, `JM_PSUBST_ID`, `JM_REPROC_NO`, `JM_TABLE_INDEX`, `JM_TO_WK_STATION`, `JM_FROM_WK_STATION`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187946

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `JM_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `JM_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `JM_PSTEP_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `JM_PSUBST_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 4 | `JM_REPROC_NO` | SMALLINT | NOT NULL | PK | primary_key |  |
| 5 | `JM_TABLE_INDEX` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `JM_TO_WK_STATION` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 7 | `JM_FROM_WK_STATION` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 8 | `JM_MESSAGES` | VARCHAR(2000) | NOT NULL |  |  |  |
| 9 | `JM_DATE_TIME` | TIMESTAMP | NOT NULL |  |  |  |
| 10 | `JM_STATUS` | VARCHAR(120) | NOT NULL |  |  |  |
| 11 | `JM_JOB_MSG_EVNT` | VARCHAR(120) | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.JM_IDENTIFIER,
       t.JM_PREQ_NO,
       t.JM_PSTEP_ID,
       t.JM_PSUBST_ID,
       t.JM_REPROC_NO,
       t.JM_TABLE_INDEX,
       t.JM_TO_WK_STATION,
       t.JM_FROM_WK_STATION,
       t.JM_MESSAGES,
       t.JM_DATE_TIME,
       t.JM_STATUS,
       t.JM_JOB_MSG_EVNT
FROM   DB2ADMIN.SCDM_JOB_MESSAGES t
FETCH FIRST 100 ROWS ONLY;
```
