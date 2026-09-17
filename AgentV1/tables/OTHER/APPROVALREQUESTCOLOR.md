# DB2ADMIN.APPROVALREQUESTCOLOR

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `COLORCOLORFOLDERCOMPANYCODE`, `COLORCOLORFOLDERCODE`, `COLORCODE`, `CODE`, `VERSION`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 211683

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COLORCOLORFOLDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `COLORCOLORFOLDERCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `COLORCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `VERSION` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COLOR_APPROVALREQUESTCOLORLINK` | `COLORCOLORFOLDERCOMPANYCODE`, `COLORCOLORFOLDERCODE`, `COLORCODE` | [`COLOR`](../OTHER/COLOR.md) | `COLORFOLDERCOMPANYCODE`, `COLORFOLDERCODE`, `CODE` | RESTRICT | `APPROVALREQUESTCOLOR.COLORCOLORFOLDERCOMPANYCODE = COLOR.COLORFOLDERCOMPANYCODE AND APPROVALREQUESTCOLOR.COLORCOLORFOLDERCODE = COLOR.COLORFOLDERCODE AND APPROVALREQUESTCOLOR.COLORCODE = COLOR.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `APPROVALREQUESTCOLORUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COLORCOLORFOLDERCOMPANYCODE,
       t.COLORCOLORFOLDERCODE,
       t.COLORCODE,
       t.CODE,
       t.VERSION,
       t.ABSUNIQUEID
FROM   DB2ADMIN.APPROVALREQUESTCOLOR t
FETCH FIRST 100 ROWS ONLY;
```
