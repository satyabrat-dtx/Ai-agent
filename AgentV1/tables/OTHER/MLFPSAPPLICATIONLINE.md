# DB2ADMIN.MLFPSAPPLICATIONLINE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `MLFPSAPPLICATIONCOMPANYCODE`, `MLFPSAPPLICATIONCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 140428

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MLFPSAPPLICATIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `MLFPSAPPLICATIONCODE` | CHAR(12) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SOURCE` | INTEGER | NOT NULL |  |  |  |
| 3 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `SHIPPINGBILLNO` | CHAR(15) |  |  |  |  |
| 5 | `SHIPPINGBILLDATE` | DATE |  |  |  |  |
| 6 | `NETTVALUEINR` | DECIMAL(18,5) |  |  |  |  |
| 7 | `BENEFITRECEIVED` | DECIMAL(18,5) |  |  |  |  |
| 8 | `BENEFITWITHCUT` | DECIMAL(18,5) |  |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `MLFPSAPPLICATION_LINE` | `MLFPSAPPLICATIONCOMPANYCODE`, `MLFPSAPPLICATIONCODE` | [`MLFPSAPPLICATION`](../OTHER/MLFPSAPPLICATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MLFPSAPPLICATIONLINE.MLFPSAPPLICATIONCOMPANYCODE = MLFPSAPPLICATION.COMPANYCODE AND MLFPSAPPLICATIONLINE.MLFPSAPPLICATIONCODE = MLFPSAPPLICATION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MLFPSAPPLICATIONLINEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.MLFPSAPPLICATIONCOMPANYCODE,
       t.MLFPSAPPLICATIONCODE,
       t.SOURCE,
       t.LINENO,
       t.SHIPPINGBILLNO,
       t.SHIPPINGBILLDATE,
       t.NETTVALUEINR,
       t.BENEFITRECEIVED,
       t.BENEFITWITHCUT,
       t.ABSUNIQUEID
FROM   DB2ADMIN.MLFPSAPPLICATIONLINE t
FETCH FIRST 100 ROWS ONLY;
```
