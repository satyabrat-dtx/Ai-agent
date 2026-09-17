# DB2ADMIN.SCDM_CAP_RSC_CHANGE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `CRG_IDENTIFIER`, `CRG_CAPACTY_RESRV`, `CRG_UPD_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186937

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CRG_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CRG_CAPACTY_RESRV` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `CRG_UPD_CODE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `CRG_CHANGE_TYPE` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CRG_IDENTIFIER,
       t.CRG_CAPACTY_RESRV,
       t.CRG_UPD_CODE,
       t.CRG_CHANGE_TYPE
FROM   DB2ADMIN.SCDM_CAP_RSC_CHANGE t
FETCH FIRST 100 ROWS ONLY;
```
