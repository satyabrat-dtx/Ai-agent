# DB2ADMIN.ABSAVAILABLELANGUAGE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `CODE`
- **FK degree**: referenced by 2 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 81

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(2) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `DESCRIPTION` | CHAR(50) |  |  | description |  |
| 2 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSAVAILABLELANGUAGE_LANGUAGE` | [`ABSCOMPANY`](../PLATFORM/ABSCOMPANY.md) | `LANGUAGECODE` | `ABSCOMPANY.LANGUAGECODE = ABSAVAILABLELANGUAGE.CODE` |
| `ABSAVAILABLELANGUAGE_LANGUAGE` | [`ABSMAILBOX`](../PLATFORM/ABSMAILBOX.md) | `LANGUAGECODE` | `ABSMAILBOX.LANGUAGECODE = ABSAVAILABLELANGUAGE.CODE` |

## Indexes

- `ABSAVAILABLELANGUAGEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.DESCRIPTION,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSAVAILABLELANGUAGE t
FETCH FIRST 100 ROWS ONLY;
```
