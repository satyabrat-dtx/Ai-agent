# DB2ADMIN.ABSLINKEDSPOOLFILETYPE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `CODE`
- **FK degree**: referenced by 3 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 61034

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `DESCRIPTION` | CHAR(50) | NOT NULL |  | description |  |
| 2 | `KEEPONLYONEBYTYPE` | SMALLINT | NOT NULL |  |  |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 4 | `LINKSPOOLTODOCCODE` | CHAR(20) |  |  |  |  |
| 5 | `DESTINATIONFOLDER` | VARCHAR(250) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSLINKEDSPOOLFILETYPE_TYPE` | [`ABSLINKEDSPOOLFILE`](../PLATFORM/ABSLINKEDSPOOLFILE.md) | `TYPECODE` | `ABSLINKEDSPOOLFILE.TYPECODE = ABSLINKEDSPOOLFILETYPE.CODE` |
| `ABSLINKEDSPOOLFILETYPE_TYPE` | [`ABSREPORTDEFEXT`](../PLATFORM/ABSREPORTDEFEXT.md) | `TYPECODE` | `ABSREPORTDEFEXT.TYPECODE = ABSLINKEDSPOOLFILETYPE.CODE` |
| `ABSLINKEDSPOOLFILETYPE_LINKEDSPOOLFILETYPE` | [`EINVOICECUSTOMIZEDOPTIONS`](../EINVOICING/EINVOICECUSTOMIZEDOPTIONS.md) | `LINKEDSPOOLFILETYPECODE` | `EINVOICECUSTOMIZEDOPTIONS.LINKEDSPOOLFILETYPECODE = ABSLINKEDSPOOLFILETYPE.CODE` |

## Indexes

- `ABSLINKEDSPOOLFILETYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.DESCRIPTION,
       t.KEEPONLYONEBYTYPE,
       t.ABSUNIQUEID,
       t.LINKSPOOLTODOCCODE,
       t.DESTINATIONFOLDER
FROM   DB2ADMIN.ABSLINKEDSPOOLFILETYPE t
FETCH FIRST 100 ROWS ONLY;
```
