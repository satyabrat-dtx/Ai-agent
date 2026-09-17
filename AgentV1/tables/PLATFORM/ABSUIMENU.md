# DB2ADMIN.ABSUIMENU

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `CODE`
- **FK degree**: referenced by 6 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 32046

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(20) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `MENUDESCR` | CHAR(50) | NOT NULL |  |  |  |
| 2 | `ALTERNATETEXT` | VARCHAR(100) | NOT NULL |  |  |  |
| 3 | `IMAGEPATHTREE` | VARCHAR(1000) |  |  |  |  |
| 4 | `IMAGENAMETREE` | VARCHAR(250) |  |  |  |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 10 | `IMAGETYPE` | INTEGER | NOT NULL |  |  |  |
| 11 | `FONTCSSTREECLASS` | CHAR(30) |  |  |  |  |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 6

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSUIMENU_ITEMS` | [`ABSUIMENUITEM`](../PLATFORM/ABSUIMENUITEM.md) | `ABSUIMENUCODE` | `ABSUIMENUITEM.ABSUIMENUCODE = ABSUIMENU.CODE` |
| `ABSUIMENU_MENU` | [`ABSUIMENUITEM`](../PLATFORM/ABSUIMENUITEM.md) | `MENUCODE` | `ABSUIMENUITEM.MENUCODE = ABSUIMENU.CODE` |
| `ABSUIMENU_MENU` | [`ABSUIINITIALMENU`](../PLATFORM/ABSUIINITIALMENU.md) | `MENUCODE` | `ABSUIINITIALMENU.MENUCODE = ABSUIMENU.CODE` |
| `ABSUIMENU_MENU2` | [`ABSUIINITIALMENU`](../PLATFORM/ABSUIINITIALMENU.md) | `MENU2CODE` | `ABSUIINITIALMENU.MENU2CODE = ABSUIMENU.CODE` |
| `ABSUIMENU_MENU3` | [`ABSUIINITIALMENU`](../PLATFORM/ABSUIINITIALMENU.md) | `MENU3CODE` | `ABSUIINITIALMENU.MENU3CODE = ABSUIMENU.CODE` |
| `ABSUIMENU_MENU4` | [`ABSUIINITIALMENU`](../PLATFORM/ABSUIINITIALMENU.md) | `MENU4CODE` | `ABSUIINITIALMENU.MENU4CODE = ABSUIMENU.CODE` |

## Indexes

- `ABSUIMENU01` (ALTERNATETEXT, MENUDESCR, CODE)
- `ABSUIMENUUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.MENUDESCR,
       t.ALTERNATETEXT,
       t.IMAGEPATHTREE,
       t.IMAGENAMETREE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.IMAGETYPE,
       t.FONTCSSTREECLASS
FROM   DB2ADMIN.ABSUIMENU t
FETCH FIRST 100 ROWS ONLY;
```
