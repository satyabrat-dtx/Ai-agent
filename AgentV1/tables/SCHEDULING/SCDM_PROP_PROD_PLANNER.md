# DB2ADMIN.SCDM_PROP_PROD_PLANNER

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `PPR_IDENTIFIER`, `PPR_PREQ_NO`, `PPR_PSTEP_ID`, `PPR_PROPERTY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186803

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PPR_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PPR_PREQ_NO` | VARCHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `PPR_PSTEP_ID` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `PPR_PROPERTY` | VARCHAR(5) | NOT NULL | PK | primary_key |  |
| 4 | `PPR_VALUE` | VARCHAR(90) |  |  |  |  |
| 5 | `PPR_UPD_CODE` | INTEGER |  |  |  |  |
| 6 | `PPR_USR_NAMECR` | VARCHAR(10) |  |  |  |  |
| 7 | `PPR_USR_TIMECR` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PPR_IDENTIFIER,
       t.PPR_PREQ_NO,
       t.PPR_PSTEP_ID,
       t.PPR_PROPERTY,
       t.PPR_VALUE,
       t.PPR_UPD_CODE,
       t.PPR_USR_NAMECR,
       t.PPR_USR_TIMECR
FROM   DB2ADMIN.SCDM_PROP_PROD_PLANNER t
FETCH FIRST 100 ROWS ONLY;
```
