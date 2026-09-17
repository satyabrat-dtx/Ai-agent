# DB2ADMIN.WRKRELEASECOMMENTS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `CREATIONTIMESTAMP`, `SALESRELEASELINECOMPANYCODE`, `SALESRELEASELINECODE`, `SALESRELEASELINELINE`, `SALESRELEASELINESUBLINE`, `SALRELEASELINECMPRELEASELINE`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 120445

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `SALESRELEASELINECOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `SALESRELEASELINECODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `SALESRELEASELINELINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 4 | `SALESRELEASELINESUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 5 | `SALRELEASELINECMPRELEASELINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 6 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 8 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 9 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.SALESRELEASELINECOMPANYCODE,
       t.SALESRELEASELINECODE,
       t.SALESRELEASELINELINE,
       t.SALESRELEASELINESUBLINE,
       t.SALRELEASELINECMPRELEASELINE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE
FROM   DB2ADMIN.WRKRELEASECOMMENTS t
FETCH FIRST 100 ROWS ONLY;
```
