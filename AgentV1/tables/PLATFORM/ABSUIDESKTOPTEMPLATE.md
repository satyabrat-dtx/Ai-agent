# DB2ADMIN.ABSUIDESKTOPTEMPLATE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `USERID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 114018

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `USERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `DESCRIPTION` | CHAR(50) | NOT NULL |  | description |  |
| 2 | `GROUP1` | BLOB(1000000) |  |  |  |  |
| 3 | `GROUP2` | BLOB(1000000) |  |  |  |  |
| 4 | `GROUP3` | BLOB(1000000) |  |  |  |  |
| 5 | `GROUP4` | BLOB(1000000) |  |  |  |  |
| 6 | `GROUP5` | BLOB(1000000) |  |  |  |  |
| 7 | `GROUP6` | BLOB(1000000) |  |  |  |  |
| 8 | `GROUP7` | BLOB(1000000) |  |  |  |  |
| 9 | `GROUP8` | BLOB(1000000) |  |  |  |  |
| 10 | `GROUP9` | BLOB(1000000) |  |  |  |  |
| 11 | `GROUP10` | BLOB(1000000) |  |  |  |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSUIDESKTOPTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.USERID,
       t.DESCRIPTION,
       t.GROUP1,
       t.GROUP2,
       t.GROUP3,
       t.GROUP4,
       t.GROUP5,
       t.GROUP6,
       t.GROUP7,
       t.GROUP8,
       t.GROUP9,
       t.GROUP10
FROM   DB2ADMIN.ABSUIDESKTOPTEMPLATE t
FETCH FIRST 100 ROWS ONLY;
```
