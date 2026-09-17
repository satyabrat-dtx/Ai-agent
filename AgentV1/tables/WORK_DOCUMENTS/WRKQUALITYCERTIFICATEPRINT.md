# DB2ADMIN.WRKQUALITYCERTIFICATEPRINT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `CREATIONTIMESTAMP`, `CREATIONUSER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 192987

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 2 | `CERTIFICATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 3 | `CERTIFICATEIDQCERTIFICATE` | CHAR(15) |  |  |  |  |
| 4 | `CERTIFICATEVERSION` | INTEGER | NOT NULL |  |  |  |
| 5 | `HEADERDATA` | BLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.CERTIFICATECOMPANYCODE,
       t.CERTIFICATEIDQCERTIFICATE,
       t.CERTIFICATEVERSION,
       t.HEADERDATA
FROM   DB2ADMIN.WRKQUALITYCERTIFICATEPRINT t
FETCH FIRST 100 ROWS ONLY;
```
