# DB2ADMIN.SCDM_WKC_PROC

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `WP_IDENTIFIER`, `WP_WKCNTER`, `WP_WKCT_PROC`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 187274

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WP_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `WP_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `WP_WKCT_PROC` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `WP_S_DESCR` | VARCHAR(28) |  |  |  |  |
| 4 | `WP_L_DESCR` | VARCHAR(60) |  |  |  |  |
| 5 | `WP_RESOURCEOCCUPATION` | CHAR(1) |  |  |  |  |
| 6 | `WP_GROUP_TYPE` | CHAR(1) |  |  |  |  |
| 7 | `WP_USEALLRESOURCEPARTS` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.WP_IDENTIFIER,
       t.WP_WKCNTER,
       t.WP_WKCT_PROC,
       t.WP_S_DESCR,
       t.WP_L_DESCR,
       t.WP_RESOURCEOCCUPATION,
       t.WP_GROUP_TYPE,
       t.WP_USEALLRESOURCEPARTS
FROM   DB2ADMIN.SCDM_WKC_PROC t
FETCH FIRST 100 ROWS ONLY;
```
