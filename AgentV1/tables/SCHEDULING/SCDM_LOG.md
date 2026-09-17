# DB2ADMIN.SCDM_LOG

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `no_primary_key`
- **Columns**: 15
- **Primary key**: _none declared_
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188213

> No primary key declared; rows are not uniquely addressable by the schema.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LG_IDENTIFIER` | SMALLINT | NOT NULL |  |  |  |
| 1 | `LG_DATE_TIME` | TIMESTAMP |  |  |  |  |
| 2 | `LG_LOG_ORIGIN` | CHAR(1) |  |  |  |  |
| 3 | `LG_PREQ_NO` | VARCHAR(30) |  |  |  |  |
| 4 | `LG_PSTEP_ID` | SMALLINT |  |  |  |  |
| 5 | `LG_PSUBST_ID` | SMALLINT |  |  |  |  |
| 6 | `LG_REPROC_NO` | SMALLINT |  |  |  |  |
| 7 | `LG_OPERATION` | VARCHAR(14) |  |  |  |  |
| 8 | `LG_SCHEDULE_INFO` | CHAR(1) |  |  |  |  |
| 9 | `LG_RSC_CODE` | VARCHAR(8) |  |  |  |  |
| 10 | `LG_QTY` | DECIMAL(11,2) |  |  |  |  |
| 11 | `LG_SCH_START` | TIMESTAMP |  |  |  |  |
| 12 | `LG_SCH_END` | TIMESTAMP |  |  |  |  |
| 13 | `LG_REASON` | VARCHAR(50) |  |  |  |  |
| 14 | `LG_SCHED_TYPE` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.LG_IDENTIFIER,
       t.LG_DATE_TIME,
       t.LG_LOG_ORIGIN,
       t.LG_PREQ_NO,
       t.LG_PSTEP_ID,
       t.LG_PSUBST_ID,
       t.LG_REPROC_NO,
       t.LG_OPERATION,
       t.LG_SCHEDULE_INFO,
       t.LG_RSC_CODE,
       t.LG_QTY,
       t.LG_SCH_START
FROM   DB2ADMIN.SCDM_LOG t
FETCH FIRST 100 ROWS ONLY;
```
