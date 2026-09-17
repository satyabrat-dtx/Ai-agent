# DB2ADMIN.EPCGAPPGROUPCOMPANYEXPORTS

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `EPCGAPPLICATIONCOMPANYCODE`, `EPCGAPPLICATIONCODE`, `LINENO`, `LICENSINGYEAR`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 138104

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EPCGAPPLICATIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EPCGAPPLICATIONCODE` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LICENSINGYEAR` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `DIRECTEXPORT` | DECIMAL(18,5) |  |  |  |  |
| 5 | `VALUEOFGROUPCMPEXPORTS3RDPARTY` | DECIMAL(18,5) |  |  |  |  |
| 6 | `TOTALOFGROUPCOMPANYEXPORTS` | DECIMAL(18,5) |  |  |  |  |
| 7 | `PRODUCTSEXPORTED` | CHAR(100) |  |  |  |  |
| 8 | `PRODUCTPARTICULARS` | CHAR(100) |  |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EPCGAPPLICATION_GROUPCMPEXPORTSLINE` | `EPCGAPPLICATIONCOMPANYCODE`, `EPCGAPPLICATIONCODE` | [`EPCGAPPLICATION`](../PURCHASING/EPCGAPPLICATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EPCGAPPGROUPCOMPANYEXPORTS.EPCGAPPLICATIONCOMPANYCODE = EPCGAPPLICATION.COMPANYCODE AND EPCGAPPGROUPCOMPANYEXPORTS.EPCGAPPLICATIONCODE = EPCGAPPLICATION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EPCGAPPGRPCOMPANYEXPORTSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EPCGAPPLICATIONCOMPANYCODE,
       t.EPCGAPPLICATIONCODE,
       t.LICENSINGYEAR,
       t.LINENO,
       t.DIRECTEXPORT,
       t.VALUEOFGROUPCMPEXPORTS3RDPARTY,
       t.TOTALOFGROUPCOMPANYEXPORTS,
       t.PRODUCTSEXPORTED,
       t.PRODUCTPARTICULARS,
       t.ABSUNIQUEID
FROM   DB2ADMIN.EPCGAPPGROUPCOMPANYEXPORTS t
FETCH FIRST 100 ROWS ONLY;
```
