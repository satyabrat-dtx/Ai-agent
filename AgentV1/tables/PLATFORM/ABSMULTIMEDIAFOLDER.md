# DB2ADMIN.ABSMULTIMEDIAFOLDER

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `PATH`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 92199

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PATH` | VARCHAR(255) | NOT NULL | PK | primary_key |  |
| 1 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 2 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 3 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 4 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 6 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 7 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSMULTIMEDIAFOLDER_CHILDAUTH` | [`ABSMULTIMEDIAFOLDERAUTH`](../PLATFORM/ABSMULTIMEDIAFOLDERAUTH.md) | `ABSMULTIMEDIAFOLDERPATH` | `ABSMULTIMEDIAFOLDERAUTH.ABSMULTIMEDIAFOLDERPATH = ABSMULTIMEDIAFOLDER.PATH` |

## Indexes

- `ABSMULTIMEDIAFOLDERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PATH,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.ABSMULTIMEDIAFOLDER t
FETCH FIRST 100 ROWS ONLY;
```
