# DB2ADMIN.COSTSIMHEADINGROUTEBOM

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `SIMULATIONCOUNTERCODE`, `SIMULATIONCODE`, `TABLEINDEX`, `SUBUNIQUEID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 196076

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SIMULATIONCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SIMULATIONCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `TABLEINDEX` | BIGINT | NOT NULL | PK | primary_key |  |
| 4 | `SUBUNIQUEID` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `PRODUCTINDEX` | DECIMAL(11,0) |  |  |  |  |
| 6 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 7 | `COSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 8 | `COSTSCOSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 9 | `ROUTINGINDEX` | DECIMAL(11,0) |  |  |  |  |
| 10 | `BOMINDEX` | DECIMAL(11,0) |  |  |  |  |
| 11 | `ROUTINGINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 12 | `BOMINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 13 | `COSTINBASECURRENCY` | DECIMAL(17,6) |  |  |  |  |
| 14 | `GOODSVALUEINBASECURRENCY` | DECIMAL(17,6) |  |  |  |  |
| 15 | `SELLINGVALUEINBASECURRENCY` | DECIMAL(17,6) |  |  |  |  |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COSTSIMULATION_SIMULATION` | `COMPANYCODE`, `SIMULATIONCOUNTERCODE`, `SIMULATIONCODE` | [`COSTSIMULATION`](../COSTING/COSTSIMULATION.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `COSTSIMHEADINGROUTEBOM.COMPANYCODE = COSTSIMULATION.COMPANYCODE AND COSTSIMHEADINGROUTEBOM.SIMULATIONCOUNTERCODE = COSTSIMULATION.COUNTERCODE AND COSTSIMHEADINGROUTEBOM.SIMULATIONCODE = COSTSIMULATION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COSTSIMHEADINGROUTEBOMUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SIMULATIONCOUNTERCODE,
       t.SIMULATIONCODE,
       t.TABLEINDEX,
       t.SUBUNIQUEID,
       t.PRODUCTINDEX,
       t.PLANTCODE,
       t.COSTGROUPCODE,
       t.COSTSCOSTGROUPCODE,
       t.ROUTINGINDEX,
       t.BOMINDEX,
       t.ROUTINGINCIDENCE
FROM   DB2ADMIN.COSTSIMHEADINGROUTEBOM t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
