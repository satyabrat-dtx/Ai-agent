# DB2ADMIN.SCDA_CAL

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `CL_IDENTIFIER`, `CL_CAL`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 183762

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CL_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CL_CAL` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `CL_S_DESCR` | VARCHAR(28) |  |  |  |  |
| 3 | `CL_EFFICIENCYON_WC_OR_RES_LVL` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CL_IDENTIFIER,
       t.CL_CAL,
       t.CL_S_DESCR,
       t.CL_EFFICIENCYON_WC_OR_RES_LVL
FROM   DB2ADMIN.SCDA_CAL t
FETCH FIRST 100 ROWS ONLY;
```
