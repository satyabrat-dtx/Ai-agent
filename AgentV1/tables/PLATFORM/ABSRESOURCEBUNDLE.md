# DB2ADMIN.ABSRESOURCEBUNDLE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `NAME`, `RBKEY`, `LANGCODE`, `COUNTRYCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 28796

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RBTYPE` | INTEGER | NOT NULL |  |  |  |
| 1 | `NAME` | VARCHAR(100) | NOT NULL | PK | primary_key |  |
| 2 | `RBKEY` | VARCHAR(150) | NOT NULL | PK | primary_key |  |
| 3 | `LANGCODE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 4 | `COUNTRYCODE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 5 | `RBVALUE` | VARCHAR(1000) |  |  |  |  |
| 6 | `RBSTATUS` | INTEGER | NOT NULL |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSRESBUNDLEIDX1` (NAME, LANGCODE, COUNTRYCODE)
- `ABSRESBUNDLEIDX2` (RBKEY, LANGCODE, COUNTRYCODE)
- UNIQUE `ABSRESBUNDLEIDX3` (LANGCODE, NAME, COUNTRYCODE, RBKEY)
- `ABSRESOURCEBUNDLEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.RBTYPE,
       t.NAME,
       t.RBKEY,
       t.LANGCODE,
       t.COUNTRYCODE,
       t.RBVALUE,
       t.RBSTATUS,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSRESOURCEBUNDLE t
FETCH FIRST 100 ROWS ONLY;
```
