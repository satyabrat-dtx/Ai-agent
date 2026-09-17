# DB2ADMIN.DEPBAPPLICATIONLINE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `DEPBAPPLICATIONCOMPANYCODE`, `DEPBAPPLICATIONDIVISIONCODE`, `DEPBAPPLICATIONCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 137098

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DEPBAPPLICATIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `DEPBAPPLICATIONDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DEPBAPPLICATIONCODE` | CHAR(12) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SOURCE` | INTEGER | NOT NULL |  |  |  |
| 4 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `SHIPPINGBILLNO` | CHAR(15) |  |  |  |  |
| 6 | `SHIPPINGBILLDATE` | DATE |  |  |  |  |
| 7 | `NETTVALUEINR` | DECIMAL(18,5) |  |  |  |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DEPBAPPLICATION_LINE` | `DEPBAPPLICATIONCOMPANYCODE`, `DEPBAPPLICATIONDIVISIONCODE`, `DEPBAPPLICATIONCODE` | [`DEPBAPPLICATION`](../ITEM_MASTER/DEPBAPPLICATION.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `DEPBAPPLICATIONLINE.DEPBAPPLICATIONCOMPANYCODE = DEPBAPPLICATION.COMPANYCODE AND DEPBAPPLICATIONLINE.DEPBAPPLICATIONDIVISIONCODE = DEPBAPPLICATION.DIVISIONCODE AND DEPBAPPLICATIONLINE.DEPBAPPLICATIONCODE = DEPBAPPLICATION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DEPBAPPLICATIONLINEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DEPBAPPLICATIONCOMPANYCODE,
       t.DEPBAPPLICATIONDIVISIONCODE,
       t.DEPBAPPLICATIONCODE,
       t.SOURCE,
       t.LINENO,
       t.SHIPPINGBILLNO,
       t.SHIPPINGBILLDATE,
       t.NETTVALUEINR,
       t.ABSUNIQUEID
FROM   DB2ADMIN.DEPBAPPLICATIONLINE t
FETCH FIRST 100 ROWS ONLY;
```
