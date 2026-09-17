# DB2ADMIN.USAREPREQRELDEF

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `FROMRELLEVEL`, `TORELLEVEL`, `FBRELLEVEL`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 115148

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FROMRELLEVEL` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 1 | `TORELLEVEL` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 2 | `FBRELLEVEL` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 3 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 4 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 5 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 6 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `USAREPREQRELDEF_CHILDAUTH` | [`USAREPREQRELDEFAUTH`](../LOCALIZATION/USAREPREQRELDEFAUTH.md) | `USARRRELLEVELDEFFROMRELLEVEL`, `USARRRELLEVELDEFTORELLEVEL`, `USARRRELLVLDEFFALLBACKRELLVL` | `USAREPREQRELDEFAUTH.USARRRELLEVELDEFFROMRELLEVEL = USAREPREQRELDEF.FROMRELLEVEL AND USAREPREQRELDEFAUTH.USARRRELLEVELDEFTORELLEVEL = USAREPREQRELDEF.TORELLEVEL AND USAREPREQRELDEFAUTH.USARRRELLVLDEFFALLBACKRELLVL = USAREPREQRELDEF.FBRELLEVEL` |

## Indexes

- `USAREPREQRELDEFUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FROMRELLEVEL,
       t.TORELLEVEL,
       t.FBRELLEVEL,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.USAREPREQRELDEF t
FETCH FIRST 100 ROWS ONLY;
```
