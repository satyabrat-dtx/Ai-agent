# DB2ADMIN.ABSUIMENUITEM

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `ABSUIMENUCODE`, `IDENTIFIER`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 26737

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUIMENUCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `IDENTIFIER` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `SEQUENCE` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 3 | `MENUCODE` | CHAR(20) |  | FK | foreign_key |  |
| 4 | `PROCESSCODE` | CHAR(50) |  | FK | foreign_key |  |
| 5 | `NEWWINDOW` | SMALLINT | NOT NULL |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSUIMENU_ITEMS` | `ABSUIMENUCODE` | [`ABSUIMENU`](../PLATFORM/ABSUIMENU.md) | `CODE` | RESTRICT | `ABSUIMENUITEM.ABSUIMENUCODE = ABSUIMENU.CODE` |
| `ABSUIMENU_MENU` | `MENUCODE` | [`ABSUIMENU`](../PLATFORM/ABSUIMENU.md) | `CODE` | RESTRICT | `ABSUIMENUITEM.MENUCODE = ABSUIMENU.CODE` |
| `ABSUIPROCESS_PROCESS` | `PROCESSCODE` | [`ABSUIPROCESS`](../PLATFORM/ABSUIPROCESS.md) | `CODE` | RESTRICT | `ABSUIMENUITEM.PROCESSCODE = ABSUIPROCESS.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSUIMENUITEMUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSUIMENUCODE,
       t.IDENTIFIER,
       t.SEQUENCE,
       t.MENUCODE,
       t.PROCESSCODE,
       t.NEWWINDOW,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.ABSUIMENUITEM t
FETCH FIRST 100 ROWS ONLY;
```
