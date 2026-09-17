# DB2ADMIN.COSTSIMPROFITELEMENTS

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `SIMULATIONCOUNTERCODE`, `SIMULATIONCODE`, `SUBUNIQUEID`, `PRODUCTINDEX`, `PLANTCODE`, `COSTGROUPCODE`, `COSTSCOSTGROUPCODE`, `PROFITELEMENTCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 196126

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SIMULATIONCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SIMULATIONCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SUBUNIQUEID` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `PRODUCTINDEX` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 5 | `PLANTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 6 | `COSTGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 7 | `COSTSCOSTGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 8 | `PROFITELEMENTCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 9 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 10 | `FINALPRICECONTRIBUTION` | CHAR(1) |  |  |  |  |
| 11 | `DISPLAYSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 12 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `PROFIT` | SMALLINT | NOT NULL |  |  |  |
| 14 | `COSTLEVELCODE` | CHAR(3) |  |  |  |  |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COSTSIMULATION_SIMULATION` | `COMPANYCODE`, `SIMULATIONCOUNTERCODE`, `SIMULATIONCODE` | [`COSTSIMULATION`](../COSTING/COSTSIMULATION.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `COSTSIMPROFITELEMENTS.COMPANYCODE = COSTSIMULATION.COMPANYCODE AND COSTSIMPROFITELEMENTS.SIMULATIONCOUNTERCODE = COSTSIMULATION.COUNTERCODE AND COSTSIMPROFITELEMENTS.SIMULATIONCODE = COSTSIMULATION.CODE` |
| `PROFITELEMENT_PROFITELEMENT` | `COMPANYCODE`, `PROFITELEMENTCODE` | [`PROFITELEMENT`](../COSTING/PROFITELEMENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `COSTSIMPROFITELEMENTS.COMPANYCODE = PROFITELEMENT.COMPANYCODE AND COSTSIMPROFITELEMENTS.PROFITELEMENTCODE = PROFITELEMENT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COSTSIMPROFITELEMENTSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SIMULATIONCOUNTERCODE,
       t.SIMULATIONCODE,
       t.SUBUNIQUEID,
       t.PRODUCTINDEX,
       t.PLANTCODE,
       t.COSTGROUPCODE,
       t.COSTSCOSTGROUPCODE,
       t.PROFITELEMENTCODE,
       t.SEQUENCE,
       t.FINALPRICECONTRIBUTION,
       t.DISPLAYSEQUENCE
FROM   DB2ADMIN.COSTSIMPROFITELEMENTS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
