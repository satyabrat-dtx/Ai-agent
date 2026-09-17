# DB2ADMIN.ABSSPOOLFILEDATA

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `ABSSPOOLFILEABSOUTQUEUENAME`, `ABSSPOOLFILESPOOLID`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 29112

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSSPOOLFILEABSOUTQUEUENAME` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ABSSPOOLFILESPOOLID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SEQUENCE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `DATA` | BLOB(1000000) | NOT NULL |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSSPOOLFILE_SPLITDATA` | `ABSSPOOLFILEABSOUTQUEUENAME`, `ABSSPOOLFILESPOOLID` | [`ABSSPOOLFILE`](../PLATFORM/ABSSPOOLFILE.md) | `ABSOUTQUEUENAME`, `SPOOLID` | RESTRICT | `ABSSPOOLFILEDATA.ABSSPOOLFILEABSOUTQUEUENAME = ABSSPOOLFILE.ABSOUTQUEUENAME AND ABSSPOOLFILEDATA.ABSSPOOLFILESPOOLID = ABSSPOOLFILE.SPOOLID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSSPOOLFILEDATAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSSPOOLFILEABSOUTQUEUENAME,
       t.ABSSPOOLFILESPOOLID,
       t.SEQUENCE,
       t.DATA,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSSPOOLFILEDATA t
FETCH FIRST 100 ROWS ONLY;
```
