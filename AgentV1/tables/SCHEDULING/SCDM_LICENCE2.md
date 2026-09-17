# DB2ADMIN.SCDM_LICENCE2

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `no_primary_key`
- **Columns**: 3
- **Primary key**: _none declared_
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187535

> No primary key declared; rows are not uniquely addressable by the schema.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LIC_LIC_STR` | VARCHAR(2000) | NOT NULL |  |  |  |
| 1 | `LIC_VER_NUM` | SMALLINT | NOT NULL |  |  |  |
| 2 | `LIC_LIC_STR_UPD` | VARCHAR(2000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.LIC_LIC_STR,
       t.LIC_VER_NUM,
       t.LIC_LIC_STR_UPD
FROM   DB2ADMIN.SCDM_LICENCE2 t
FETCH FIRST 100 ROWS ONLY;
```
