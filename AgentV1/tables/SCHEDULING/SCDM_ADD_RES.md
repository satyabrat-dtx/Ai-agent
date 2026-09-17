# DB2ADMIN.SCDM_ADD_RES

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `AR_IDENTIFIER`, `AR_ADD_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185624

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `AR_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `AR_ADD_CODE` | VARCHAR(5) | NOT NULL | PK | primary_key |  |
| 2 | `AR_S_DESCR` | VARCHAR(28) |  |  |  |  |
| 3 | `AR_L_DESCR` | VARCHAR(60) |  |  |  |  |
| 4 | `AR_CONSUM_ZONE` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.AR_IDENTIFIER,
       t.AR_ADD_CODE,
       t.AR_S_DESCR,
       t.AR_L_DESCR,
       t.AR_CONSUM_ZONE
FROM   DB2ADMIN.SCDM_ADD_RES t
FETCH FIRST 100 ROWS ONLY;
```
