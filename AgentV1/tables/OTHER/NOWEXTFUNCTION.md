# DB2ADMIN.NOWEXTFUNCTION

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `UIXMLPATH`, `UIXMLNAME`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 17732

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `UIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(2) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `NOWEXTFUNCTION_CURRENT` | [`NOWEXTFUNCTIONLINK`](../OTHER/NOWEXTFUNCTIONLINK.md) | `CURRENTUIXMLPATH`, `CURRENTUIXMLNAME`, `CURRENTCODE` | `NOWEXTFUNCTIONLINK.CURRENTUIXMLPATH = NOWEXTFUNCTION.UIXMLPATH AND NOWEXTFUNCTIONLINK.CURRENTUIXMLNAME = NOWEXTFUNCTION.UIXMLNAME AND NOWEXTFUNCTIONLINK.CURRENTCODE = NOWEXTFUNCTION.CODE` |
| `NOWEXTFUNCTION_NEXT` | [`NOWEXTFUNCTIONLINK`](../OTHER/NOWEXTFUNCTIONLINK.md) | `NEXTUIXMLPATH`, `NEXTUIXMLNAME`, `NEXTCODE` | `NOWEXTFUNCTIONLINK.NEXTUIXMLPATH = NOWEXTFUNCTION.UIXMLPATH AND NOWEXTFUNCTIONLINK.NEXTUIXMLNAME = NOWEXTFUNCTION.UIXMLNAME AND NOWEXTFUNCTIONLINK.NEXTCODE = NOWEXTFUNCTION.CODE` |
| `NOWEXTFUNCTION_FUN` | [`NOWEXTFUNCTIONAUTH`](../OTHER/NOWEXTFUNCTIONAUTH.md) | `FUNUIXMLPATH`, `FUNUIXMLNAME`, `FUNCODE` | `NOWEXTFUNCTIONAUTH.FUNUIXMLPATH = NOWEXTFUNCTION.UIXMLPATH AND NOWEXTFUNCTIONAUTH.FUNUIXMLNAME = NOWEXTFUNCTION.UIXMLNAME AND NOWEXTFUNCTIONAUTH.FUNCODE = NOWEXTFUNCTION.CODE` |

## Indexes

- `NOWEXTFUNCTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.UIXMLPATH,
       t.UIXMLNAME,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ABSUNIQUEID
FROM   DB2ADMIN.NOWEXTFUNCTION t
FETCH FIRST 100 ROWS ONLY;
```
