# DB2ADMIN.ABSREPORTDEFEXT

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 61069

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(50) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `SAVEASLINKED` | SMALLINT | NOT NULL |  |  |  |
| 2 | `TYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 3 | `EXPORTTOFILESYSTEM` | SMALLINT | NOT NULL |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSLINKEDSPOOLFILETYPE_TYPE` | `TYPECODE` | [`ABSLINKEDSPOOLFILETYPE`](../PLATFORM/ABSLINKEDSPOOLFILETYPE.md) | `CODE` | RESTRICT | `ABSREPORTDEFEXT.TYPECODE = ABSLINKEDSPOOLFILETYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSREPORTDEFEXTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.SAVEASLINKED,
       t.TYPECODE,
       t.EXPORTTOFILESYSTEM,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSREPORTDEFEXT t
FETCH FIRST 100 ROWS ONLY;
```
