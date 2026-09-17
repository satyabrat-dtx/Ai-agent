# DB2ADMIN.SCDA_PRODUCTION_TIMES_LEVEL

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `IDENTIFIER`, `WORK_CENTER_CODE`, `OPERATION`, `PRODUCT_TYPE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 185021

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `WORK_CENTER_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `OPERATION` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `PRODUCT_TYPE` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `HANDLE_TIMES_BY` | CHAR(1) |  |  |  |  |
| 5 | `TABLENAME1` | VARCHAR(30) |  |  |  |  |
| 6 | `COLUMNNAME1` | VARCHAR(30) |  |  |  |  |
| 7 | `TABLENAME2` | VARCHAR(30) |  |  |  |  |
| 8 | `COLUMNNAME2` | VARCHAR(30) |  |  |  |  |
| 9 | `TABLENAME3` | VARCHAR(30) |  |  |  |  |
| 10 | `COLUMNNAME3` | VARCHAR(30) |  |  |  |  |
| 11 | `TABLENAME4` | VARCHAR(30) |  |  |  |  |
| 12 | `COLUMNNAME4` | VARCHAR(30) |  |  |  |  |
| 13 | `TABLENAME5` | VARCHAR(30) |  |  |  |  |
| 14 | `COLUMNNAME5` | VARCHAR(30) |  |  |  |  |
| 15 | `TABLENAME6` | VARCHAR(30) |  |  |  |  |
| 16 | `COLUMNNAME6` | VARCHAR(30) |  |  |  |  |
| 17 | `TABLENAME7` | VARCHAR(30) |  |  |  |  |
| 18 | `COLUMNNAME7` | VARCHAR(30) |  |  |  |  |
| 19 | `TABLENAME8` | VARCHAR(30) |  |  |  |  |
| 20 | `COLUMNNAME8` | VARCHAR(30) |  |  |  |  |
| 21 | `TABLENAME9` | VARCHAR(30) |  |  |  |  |
| 22 | `COLUMNNAME9` | VARCHAR(30) |  |  |  |  |
| 23 | `TABLENAME10` | VARCHAR(30) |  |  |  |  |
| 24 | `COLUMNNAME10` | VARCHAR(30) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.WORK_CENTER_CODE,
       t.OPERATION,
       t.PRODUCT_TYPE,
       t.HANDLE_TIMES_BY,
       t.TABLENAME1,
       t.COLUMNNAME1,
       t.TABLENAME2,
       t.COLUMNNAME2,
       t.TABLENAME3,
       t.COLUMNNAME3,
       t.TABLENAME4
FROM   DB2ADMIN.SCDA_PRODUCTION_TIMES_LEVEL t
FETCH FIRST 100 ROWS ONLY;
```
