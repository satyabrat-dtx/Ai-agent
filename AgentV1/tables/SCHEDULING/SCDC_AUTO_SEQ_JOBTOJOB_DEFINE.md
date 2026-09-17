# DB2ADMIN.SCDC_AUTO_SEQ_JOBTOJOB_DEFINE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `AJ_IDENTIFIER`, `AJ_WKST_CODE`, `AJ_CFGNAME`, `AJ_FROM_CASE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189684

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `AJ_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `AJ_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `AJ_CFGNAME` | VARCHAR(14) | NOT NULL | PK | primary_key |  |
| 3 | `AJ_FROM_CASE` | SMALLINT | NOT NULL | PK | primary_key |  |
| 4 | `AJ_TO_CASE` | SMALLINT |  |  |  |  |
| 5 | `AJ_ADD_TO_SCORE` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.AJ_IDENTIFIER,
       t.AJ_WKST_CODE,
       t.AJ_CFGNAME,
       t.AJ_FROM_CASE,
       t.AJ_TO_CASE,
       t.AJ_ADD_TO_SCORE
FROM   DB2ADMIN.SCDC_AUTO_SEQ_JOBTOJOB_DEFINE t
FETCH FIRST 100 ROWS ONLY;
```
