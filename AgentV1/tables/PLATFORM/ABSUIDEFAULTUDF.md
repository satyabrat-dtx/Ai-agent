# DB2ADMIN.ABSUIDEFAULTUDF

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `MODULENAME`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 216221

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MODULENAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `CODE` | CHAR(30) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `DESCRIPTION` | VARCHAR(100) | NOT NULL |  | description |  |
| 3 | `MANAGEDCLASSTYPE` | INTEGER | NOT NULL |  |  |  |
| 4 | `JNDINAME` | CHAR(100) | NOT NULL |  |  |  |
| 5 | `METHODNAME` | CHAR(50) | NOT NULL |  |  |  |
| 6 | `TECHDESCRIPTION` | VARCHAR(700) |  |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSUIDEFAULTUDFUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.MODULENAME,
       t.CODE,
       t.DESCRIPTION,
       t.MANAGEDCLASSTYPE,
       t.JNDINAME,
       t.METHODNAME,
       t.TECHDESCRIPTION,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSUIDEFAULTUDF t
FETCH FIRST 100 ROWS ONLY;
```
