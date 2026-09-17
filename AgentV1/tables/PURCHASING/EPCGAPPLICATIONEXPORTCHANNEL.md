# DB2ADMIN.EPCGAPPLICATIONEXPORTCHANNEL

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `EPCGAPPLICATIONCOMPANYCODE`, `EPCGAPPLICATIONCODE`, `LINENO`, `LICENSINGYEAR`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 137910

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EPCGAPPLICATIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EPCGAPPLICATIONCODE` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LICENSINGYEAR` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `DIRECTEXPORTBYAPPLFIRM` | DECIMAL(18,5) |  |  |  |  |
| 5 | `THIRDPARTYEXPORT` | DECIMAL(18,5) |  |  |  |  |
| 6 | `THROUGHGROUPCOMPANY` | DECIMAL(18,5) |  |  |  |  |
| 7 | `TOTALOFEXPORTCHANNEL` | DECIMAL(18,5) |  |  |  |  |
| 8 | `PRODUCTSEXPORTED` | CHAR(100) |  |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EPCGAPPLICATION_EXPORTCHANNELLINE` | `EPCGAPPLICATIONCOMPANYCODE`, `EPCGAPPLICATIONCODE` | [`EPCGAPPLICATION`](../PURCHASING/EPCGAPPLICATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EPCGAPPLICATIONEXPORTCHANNEL.EPCGAPPLICATIONCOMPANYCODE = EPCGAPPLICATION.COMPANYCODE AND EPCGAPPLICATIONEXPORTCHANNEL.EPCGAPPLICATIONCODE = EPCGAPPLICATION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EPCGAPPEXPORTCHANNELUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EPCGAPPLICATIONCOMPANYCODE,
       t.EPCGAPPLICATIONCODE,
       t.LICENSINGYEAR,
       t.LINENO,
       t.DIRECTEXPORTBYAPPLFIRM,
       t.THIRDPARTYEXPORT,
       t.THROUGHGROUPCOMPANY,
       t.TOTALOFEXPORTCHANNEL,
       t.PRODUCTSEXPORTED,
       t.ABSUNIQUEID
FROM   DB2ADMIN.EPCGAPPLICATIONEXPORTCHANNEL t
FETCH FIRST 100 ROWS ONLY;
```
