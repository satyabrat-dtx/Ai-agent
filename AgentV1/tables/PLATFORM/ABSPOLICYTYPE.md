# DB2ADMIN.ABSPOLICYTYPE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `CODE`
- **FK degree**: referenced by 3 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 25879

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(30) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `NAME` | CHAR(50) | NOT NULL |  |  |  |
| 2 | `DESCRIPTION` | VARCHAR(100) | NOT NULL |  | description |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSPOLICYTYPE_ABSPOLICY` | [`OUTPUTENTITYLIST`](../PLATFORM/OUTPUTENTITYLIST.md) | `ABSPOLICYCODE` | `OUTPUTENTITYLIST.ABSPOLICYCODE = ABSPOLICYTYPE.CODE` |
| `ABSPOLICYTYPE_IMPLEMENTATIONS` | [`ABSPOLICYIMPL`](../PLATFORM/ABSPOLICYIMPL.md) | `ABSPOLICYTYPECODE` | `ABSPOLICYIMPL.ABSPOLICYTYPECODE = ABSPOLICYTYPE.CODE` |
| `ABSPOLICYTYPE_ABSPOLICYTYPE` | [`COSTCUSTOMIZEDOPTIONS`](../COSTING/COSTCUSTOMIZEDOPTIONS.md) | `ABSPOLICYTYPECODE` | `COSTCUSTOMIZEDOPTIONS.ABSPOLICYTYPECODE = ABSPOLICYTYPE.CODE` |

## Indexes

- `ABSPOLICYTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.NAME,
       t.DESCRIPTION,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSPOLICYTYPE t
FETCH FIRST 100 ROWS ONLY;
```
