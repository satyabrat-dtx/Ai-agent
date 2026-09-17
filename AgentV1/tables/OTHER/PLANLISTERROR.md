# DB2ADMIN.PLANLISTERROR

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `ERRORTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 28907

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ERRORTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `PLANLISTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 2 | `PLANLISTGROUPNUMBER` | BIGINT |  |  |  |  |
| 3 | `STEPOFERROR` | CHAR(1) |  |  |  |  |
| 4 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 6 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 7 | `DELIVERYDATE` | DATE |  |  |  |  |
| 8 | `PRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 9 | `PRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ERRORTIMESTAMP,
       t.PLANLISTCOMPANYCODE,
       t.PLANLISTGROUPNUMBER,
       t.STEPOFERROR,
       t.ITEMTYPECODE,
       t.ITEMCODE,
       t.WAREHOUSECODE,
       t.DELIVERYDATE,
       t.PRIMARYQUANTITY,
       t.PRIMARYUOMCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PLANLISTERROR t
FETCH FIRST 100 ROWS ONLY;
```
