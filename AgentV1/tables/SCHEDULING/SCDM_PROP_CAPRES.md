# DB2ADMIN.SCDM_PROP_CAPRES

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `CP_IDENTIFIER`, `CP_CAPACTY_RESRV`, `CP_PROPERTY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185762

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CP_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CP_CAPACTY_RESRV` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `CP_PROPERTY` | VARCHAR(5) | NOT NULL | PK | primary_key |  |
| 3 | `CP_VALUE` | VARCHAR(90) |  |  |  |  |
| 4 | `CP_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 5 | `CP_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CP_IDENTIFIER,
       t.CP_CAPACTY_RESRV,
       t.CP_PROPERTY,
       t.CP_VALUE,
       t.CP_USR_NAMECG,
       t.CP_USR_TIMECG
FROM   DB2ADMIN.SCDM_PROP_CAPRES t
FETCH FIRST 100 ROWS ONLY;
```
