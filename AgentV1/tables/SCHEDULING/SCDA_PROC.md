# DB2ADMIN.SCDA_PROC

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `PR_IDENTIFIER`, `PR_WKCT_PROC`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 183854

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PR_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PR_WKCT_PROC` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `PR_S_DESCR` | VARCHAR(28) |  |  |  |  |
| 3 | `PR_ALTERNATIVE_UM_HANDLED` | CHAR(1) |  |  |  |  |
| 4 | `PR_RULE_FOR_GROUPING_MQM` | VARCHAR(10) |  |  |  |  |
| 5 | `PR_RULE_FOR_GROUPING_MCM` | VARCHAR(10) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PR_IDENTIFIER,
       t.PR_WKCT_PROC,
       t.PR_S_DESCR,
       t.PR_ALTERNATIVE_UM_HANDLED,
       t.PR_RULE_FOR_GROUPING_MQM,
       t.PR_RULE_FOR_GROUPING_MCM
FROM   DB2ADMIN.SCDA_PROC t
FETCH FIRST 100 ROWS ONLY;
```
