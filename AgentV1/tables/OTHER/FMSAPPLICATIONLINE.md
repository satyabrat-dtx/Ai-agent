# DB2ADMIN.FMSAPPLICATIONLINE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `FMSAPPLICATIONCOMPANYCODE`, `FMSAPPLICATIONCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 138784

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FMSAPPLICATIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FMSAPPLICATIONCODE` | CHAR(12) | NOT NULL | PK FK | primary_key foreign_key |  |
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
| `FMSAPPLICATION_LINE` | `FMSAPPLICATIONCOMPANYCODE`, `FMSAPPLICATIONCODE` | [`FMSAPPLICATION`](../OTHER/FMSAPPLICATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FMSAPPLICATIONLINE.FMSAPPLICATIONCOMPANYCODE = FMSAPPLICATION.COMPANYCODE AND FMSAPPLICATIONLINE.FMSAPPLICATIONCODE = FMSAPPLICATION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FMSAPPLICATIONLINEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FMSAPPLICATIONCOMPANYCODE,
       t.FMSAPPLICATIONCODE,
       t.SOURCE,
       t.LINENO,
       t.SHIPPINGBILLNO,
       t.SHIPPINGBILLDATE,
       t.NETTVALUEINR,
       t.BENEFITRECEIVED,
       t.BENEFITWITHCUT,
       t.ABSUNIQUEID
FROM   DB2ADMIN.FMSAPPLICATIONLINE t
FETCH FIRST 100 ROWS ONLY;
```
