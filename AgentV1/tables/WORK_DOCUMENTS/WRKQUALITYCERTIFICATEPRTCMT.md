# DB2ADMIN.WRKQUALITYCERTIFICATEPRTCMT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `CREATIONTIMESTAMP`, `CREATIONUSER`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 193013

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 2 | `SEQUENCE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `ORIGIN` | INTEGER | NOT NULL |  |  |  |
| 4 | `COMMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `COMMENTORDERTYPE` | CHAR(1) |  |  |  |  |
| 6 | `COMMENTCODE` | CHAR(12) |  |  |  |  |
| 7 | `COMMENTTEXT` | LONG VARCHAR |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.SEQUENCE,
       t.ORIGIN,
       t.COMMENTCOMPANYCODE,
       t.COMMENTORDERTYPE,
       t.COMMENTCODE,
       t.COMMENTTEXT
FROM   DB2ADMIN.WRKQUALITYCERTIFICATEPRTCMT t
FETCH FIRST 100 ROWS ONLY;
```
