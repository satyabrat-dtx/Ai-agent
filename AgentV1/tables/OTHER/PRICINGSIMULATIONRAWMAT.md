# DB2ADMIN.PRICINGSIMULATIONRAWMAT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `PRICINGSIMULATIONCOMPANYCODE`, `PRICINGSIMULATIONNUMBERID`, `LINENUMBER`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 105130

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PRICINGSIMULATIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PRICINGSIMULATIONNUMBERID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINENUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `FIKDLONGDESC` | CHAR(200) |  |  |  |  |
| 4 | `PRODUCTINDEX` | DECIMAL(11,0) |  |  |  |  |
| 5 | `CONSUMPTION` | DECIMAL(20,10) |  |  |  |  |
| 6 | `STANDARDCOST` | DECIMAL(20,10) |  |  |  |  |
| 7 | `WEIGHTEDCOST` | DECIMAL(20,10) |  |  |  |  |
| 8 | `DYNAMICCOST` | DECIMAL(20,10) |  |  |  |  |
| 9 | `LASTCOST` | DECIMAL(20,10) |  |  |  |  |
| 10 | `INTERNALPRICELISTCOST` | DECIMAL(20,10) |  |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PRICINGSIMULATION_RAWMAT` | `PRICINGSIMULATIONCOMPANYCODE`, `PRICINGSIMULATIONNUMBERID` | [`PRICINGSIMULATION`](../OTHER/PRICINGSIMULATION.md) | `COMPANYCODE`, `NUMBERID` | RESTRICT | `PRICINGSIMULATIONRAWMAT.PRICINGSIMULATIONCOMPANYCODE = PRICINGSIMULATION.COMPANYCODE AND PRICINGSIMULATIONRAWMAT.PRICINGSIMULATIONNUMBERID = PRICINGSIMULATION.NUMBERID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRICINGSIMULATIONRAWMATUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PRICINGSIMULATIONCOMPANYCODE,
       t.PRICINGSIMULATIONNUMBERID,
       t.LINENUMBER,
       t.FIKDLONGDESC,
       t.PRODUCTINDEX,
       t.CONSUMPTION,
       t.STANDARDCOST,
       t.WEIGHTEDCOST,
       t.DYNAMICCOST,
       t.LASTCOST,
       t.INTERNALPRICELISTCOST,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PRICINGSIMULATIONRAWMAT t
FETCH FIRST 100 ROWS ONLY;
```
