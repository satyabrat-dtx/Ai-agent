# DB2ADMIN.NOWEXTFUNCTIONLINK

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `CURRENTUIXMLPATH`, `CURRENTUIXMLNAME`, `CURRENTCODE`, `NEXTUIXMLPATH`, `NEXTUIXMLNAME`, `NEXTCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 17016

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CURRENTUIXMLPATH` | VARCHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CURRENTUIXMLNAME` | VARCHAR(54) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CURRENTCODE` | CHAR(2) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `NEXTUIXMLPATH` | VARCHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `NEXTUIXMLNAME` | VARCHAR(54) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `NEXTCODE` | CHAR(2) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `NOWEXTFUNCTION_CURRENT` | `CURRENTUIXMLPATH`, `CURRENTUIXMLNAME`, `CURRENTCODE` | [`NOWEXTFUNCTION`](../OTHER/NOWEXTFUNCTION.md) | `UIXMLPATH`, `UIXMLNAME`, `CODE` | RESTRICT | `NOWEXTFUNCTIONLINK.CURRENTUIXMLPATH = NOWEXTFUNCTION.UIXMLPATH AND NOWEXTFUNCTIONLINK.CURRENTUIXMLNAME = NOWEXTFUNCTION.UIXMLNAME AND NOWEXTFUNCTIONLINK.CURRENTCODE = NOWEXTFUNCTION.CODE` |
| `NOWEXTFUNCTION_NEXT` | `NEXTUIXMLPATH`, `NEXTUIXMLNAME`, `NEXTCODE` | [`NOWEXTFUNCTION`](../OTHER/NOWEXTFUNCTION.md) | `UIXMLPATH`, `UIXMLNAME`, `CODE` | RESTRICT | `NOWEXTFUNCTIONLINK.NEXTUIXMLPATH = NOWEXTFUNCTION.UIXMLPATH AND NOWEXTFUNCTIONLINK.NEXTUIXMLNAME = NOWEXTFUNCTION.UIXMLNAME AND NOWEXTFUNCTIONLINK.NEXTCODE = NOWEXTFUNCTION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `NOWEXTFUNCTIONLINKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CURRENTUIXMLPATH,
       t.CURRENTUIXMLNAME,
       t.CURRENTCODE,
       t.NEXTUIXMLPATH,
       t.NEXTUIXMLNAME,
       t.NEXTCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.NOWEXTFUNCTIONLINK t
FETCH FIRST 100 ROWS ONLY;
```
