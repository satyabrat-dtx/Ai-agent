# DB2ADMIN.ADIMAGE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `NAME`
- **FK degree**: referenced by 3 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 6564

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `NAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `LABEL` | CHAR(50) | NOT NULL |  |  |  |
| 2 | `DIRECTORY` | VARCHAR(100) |  |  |  |  |
| 3 | `EXTENSION` | CHAR(5) |  |  |  |  |
| 4 | `IMAGETYPE` | CHAR(1) |  |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ADIMAGE_PAGE` | [`ADADDITIONALDATA`](../CORE_MASTER/ADADDITIONALDATA.md) | `PAGENAME` | `ADADDITIONALDATA.PAGENAME = ADIMAGE.NAME` |
| `ADIMAGE_PAGEON` | [`ADADDITIONALDATA`](../CORE_MASTER/ADADDITIONALDATA.md) | `PAGEONNAME` | `ADADDITIONALDATA.PAGEONNAME = ADIMAGE.NAME` |
| `ADIMAGE_PAGE` | [`DYNAMICFIELDSCONFIG`](../OTHER/DYNAMICFIELDSCONFIG.md) | `PAGENAME` | `DYNAMICFIELDSCONFIG.PAGENAME = ADIMAGE.NAME` |

## Indexes

- `ADIMAGEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.NAME,
       t.LABEL,
       t.DIRECTORY,
       t.EXTENSION,
       t.IMAGETYPE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ADIMAGE t
FETCH FIRST 100 ROWS ONLY;
```
