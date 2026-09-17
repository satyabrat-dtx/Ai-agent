# DB2ADMIN.FINVOUPOSTINGERROR

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `ERRORTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 100210

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ERRORTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `VOUCHERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 2 | `VOUCHERDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 3 | `VOUCHERINTERNALVOUCHERCODE` | DECIMAL(15,0) |  |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINVOUPOSTINGERRORUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ERRORTIMESTAMP,
       t.VOUCHERCOMPANYCODE,
       t.VOUCHERDIVISIONCODE,
       t.VOUCHERINTERNALVOUCHERCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.FINVOUPOSTINGERROR t
FETCH FIRST 100 ROWS ONLY;
```
