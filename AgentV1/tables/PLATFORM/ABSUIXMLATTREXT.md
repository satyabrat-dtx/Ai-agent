# DB2ADMIN.ABSUIXMLATTREXT

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `ABSUIXMLPATH`, `ABSUIXMLNAME`, `NAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 22682

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `ABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `NAME` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 3 | `UIXMLTYPE` | INTEGER | NOT NULL |  |  |  |
| 4 | `OPTIONS` | VARCHAR(2000) |  |  |  |  |
| 5 | `OTHERKEYS` | VARCHAR(1500) |  |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSUIXMLATTREXT2` (NAME, ABSUIXMLPATH)
- UNIQUE `ABSUIXMLATTREXT1` (NAME, ABSUIXMLNAME, ABSUIXMLPATH)
- `ABSUIXMLATTREXTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSUIXMLPATH,
       t.ABSUIXMLNAME,
       t.NAME,
       t.UIXMLTYPE,
       t.OPTIONS,
       t.OTHERKEYS,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSUIXMLATTREXT t
FETCH FIRST 100 ROWS ONLY;
```
