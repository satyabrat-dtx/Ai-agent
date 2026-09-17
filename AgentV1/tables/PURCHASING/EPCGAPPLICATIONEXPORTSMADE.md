# DB2ADMIN.EPCGAPPLICATIONEXPORTSMADE

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `EPCGAPPLICATIONCOMPANYCODE`, `EPCGAPPLICATIONCODE`, `LINENO`, `LICENSINGYEAR`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 138013

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EPCGAPPLICATIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EPCGAPPLICATIONCODE` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LICENSINGYEAR` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `AMTOFEXPORTSAMEPRD` | DECIMAL(18,5) |  |  |  |  |
| 5 | `AMTOFEXPORTSIMILARPRD` | DECIMAL(18,5) |  |  |  |  |
| 6 | `AMTOFALTERNATEPRD` | DECIMAL(18,5) |  |  |  |  |
| 7 | `TOTALOFPRODUCTEXPORTS` | DECIMAL(18,5) |  |  |  |  |
| 8 | `AVERAGEEXPORTOBLGNTN` | INTEGER | NOT NULL |  |  |  |
| 9 | `PRODUCTSEXPORTED` | CHAR(100) |  |  |  |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EPCGAPPLICATION_EXPORTSMADELINE` | `EPCGAPPLICATIONCOMPANYCODE`, `EPCGAPPLICATIONCODE` | [`EPCGAPPLICATION`](../PURCHASING/EPCGAPPLICATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EPCGAPPLICATIONEXPORTSMADE.EPCGAPPLICATIONCOMPANYCODE = EPCGAPPLICATION.COMPANYCODE AND EPCGAPPLICATIONEXPORTSMADE.EPCGAPPLICATIONCODE = EPCGAPPLICATION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EPCGAPPLICATIONEXPORTSMADEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EPCGAPPLICATIONCOMPANYCODE,
       t.EPCGAPPLICATIONCODE,
       t.LICENSINGYEAR,
       t.LINENO,
       t.AMTOFEXPORTSAMEPRD,
       t.AMTOFEXPORTSIMILARPRD,
       t.AMTOFALTERNATEPRD,
       t.TOTALOFPRODUCTEXPORTS,
       t.AVERAGEEXPORTOBLGNTN,
       t.PRODUCTSEXPORTED,
       t.ABSUNIQUEID
FROM   DB2ADMIN.EPCGAPPLICATIONEXPORTSMADE t
FETCH FIRST 100 ROWS ONLY;
```
