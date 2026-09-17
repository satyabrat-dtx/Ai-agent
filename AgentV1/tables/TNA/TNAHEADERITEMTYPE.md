# DB2ADMIN.TNAHEADERITEMTYPE

- **Module**: `TNA` (low confidence — table name starts with 'TNA')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `TNAHEADERCOMPANYCODE`, `TNAHEADERCODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 195740

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TNAHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TNAHEADERCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TNAHEADERITEMTYPE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND TNAHEADERITEMTYPE.ITEMTYPECODE = ITEMTYPE.CODE` |
| `TNAHEADER_ITEMTYPELINE` | `TNAHEADERCOMPANYCODE`, `TNAHEADERCODE` | [`TNAHEADER`](../TNA/TNAHEADER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TNAHEADERITEMTYPE.TNAHEADERCOMPANYCODE = TNAHEADER.COMPANYCODE AND TNAHEADERITEMTYPE.TNAHEADERCODE = TNAHEADER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TNAHEADERITEMTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TNAHEADERCOMPANYCODE,
       t.TNAHEADERCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.TNAHEADERITEMTYPE t
FETCH FIRST 100 ROWS ONLY;
```
