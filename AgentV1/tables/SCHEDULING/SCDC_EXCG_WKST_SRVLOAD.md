# DB2ADMIN.SCDC_EXCG_WKST_SRVLOAD

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `no_primary_key`
- **Columns**: 3
- **Primary key**: _none declared_
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 193976

> No primary key declared; rows are not uniquely addressable by the schema.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SRV_IDENTIFIER` | SMALLINT |  |  |  |  |
| 1 | `SRV_WKST_CODE` | VARCHAR(10) |  |  |  |  |
| 2 | `SRV_DOWNLOAD_TYPE` | VARCHAR(6) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.SRV_IDENTIFIER,
       t.SRV_WKST_CODE,
       t.SRV_DOWNLOAD_TYPE
FROM   DB2ADMIN.SCDC_EXCG_WKST_SRVLOAD t
FETCH FIRST 100 ROWS ONLY;
```
