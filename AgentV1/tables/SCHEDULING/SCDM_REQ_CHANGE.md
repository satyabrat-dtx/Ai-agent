# DB2ADMIN.SCDM_REQ_CHANGE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `RC_IDENTIFIER`, `RC_PREQ_NO`, `RC_PSTEP_ID`, `RC_UPD_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186909

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RC_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `RC_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `RC_PSTEP_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `RC_UPD_CODE` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `RC_CHANGE_TYPE` | CHAR(1) |  |  |  |  |
| 5 | `RC_REACTIVATE` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.RC_IDENTIFIER,
       t.RC_PREQ_NO,
       t.RC_PSTEP_ID,
       t.RC_UPD_CODE,
       t.RC_CHANGE_TYPE,
       t.RC_REACTIVATE
FROM   DB2ADMIN.SCDM_REQ_CHANGE t
FETCH FIRST 100 ROWS ONLY;
```
