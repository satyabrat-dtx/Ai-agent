# DB2ADMIN.COSTSIMROUTECONSUMPTION

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 64
- **Primary key**: `COMPANYCODE`, `SIMULATIONCOUNTERCODE`, `SIMULATIONCODE`, `TABLEINDEX`, `SUBUNIQUEID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 196179

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SIMULATIONCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SIMULATIONCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `TABLEINDEX` | BIGINT | NOT NULL | PK | primary_key |  |
| 4 | `PRODUCTINDEX` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 5 | `PLANTCODE` | CHAR(8) | NOT NULL |  |  |  |
| 6 | `SUBUNIQUEID` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `COSTGROUPCODE` | CHAR(3) | NOT NULL |  |  |  |
| 8 | `COSTSCOSTGROUPCODE` | CHAR(3) | NOT NULL |  |  |  |
| 9 | `ROUTEINDEX` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 10 | `BOMINDEX` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 11 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 12 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 13 | `ITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 14 | `ITEMSUBCODE01` | CHAR(20) | NOT NULL |  |  |  |
| 15 | `ITEMSUBCODE02` | CHAR(10) |  |  |  |  |
| 16 | `ITEMSUBCODE03` | CHAR(10) |  |  |  |  |
| 17 | `ITEMSUBCODE04` | CHAR(10) |  |  |  |  |
| 18 | `ITEMSUBCODE05` | CHAR(10) |  |  |  |  |
| 19 | `ITEMSUBCODE06` | CHAR(10) |  |  |  |  |
| 20 | `ITEMSUBCODE07` | CHAR(10) |  |  |  |  |
| 21 | `ITEMSUBCODE08` | CHAR(10) |  |  |  |  |
| 22 | `ITEMSUBCODE09` | CHAR(10) |  |  |  |  |
| 23 | `ITEMSUBCODE10` | CHAR(10) |  |  |  |  |
| 24 | `COSTCATEGORYCODE` | CHAR(20) |  |  |  |  |
| 25 | `COSTLEVELCODE` | CHAR(3) |  |  |  |  |
| 26 | `COMPONENTPLANTCODE` | CHAR(8) |  |  |  |  |
| 27 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 28 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 29 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 30 | `PRODUCTIONRESERVATIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 31 | `COMPONENTPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 32 | `COSTPER` | DECIMAL(18,5) |  |  |  |  |
| 33 | `CURRENCYPER` | CHAR(4) |  |  |  |  |
| 34 | `QUANTITYPER` | DECIMAL(15,5) |  |  |  |  |
| 35 | `QUANTITYPERUOMCODE` | CHAR(3) |  |  |  |  |
| 36 | `QUANTITYREQUIRED` | DECIMAL(20,10) |  |  |  |  |
| 37 | `COSTPERUNIT` | DECIMAL(18,5) |  |  |  |  |
| 38 | `COSTCURRENCY` | CHAR(4) |  |  |  |  |
| 39 | `QUANTITYREQUIREDPRIMARYUOM` | DECIMAL(20,10) |  |  |  |  |
| 40 | `CALCULATIONSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 41 | `PRODUCED` | SMALLINT | NOT NULL |  |  |  |
| 42 | `WASTETYPE1` | CHAR(2) |  |  |  |  |
| 43 | `WASTE1` | DECIMAL(11,2) |  |  |  |  |
| 44 | `WASTETYPE2` | CHAR(2) |  |  |  |  |
| 45 | `WASTE2` | DECIMAL(11,2) |  |  |  |  |
| 46 | `BOMCALCULATEQTYNAME` | CHAR(100) |  |  |  |  |
| 47 | `BOMCALCULATEQTYCODE` | CHAR(20) |  |  |  |  |
| 48 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 49 | `COSTINBASECURRENCY` | DECIMAL(20,10) |  |  |  |  |
| 50 | `WASTEPRODUCT` | CHAR(2) |  |  |  |  |
| 51 | `CONSUMPTIONCALCULATIONTYPE` | CHAR(1) |  |  |  |  |
| 52 | `ADDITIONALCOST` | SMALLINT | NOT NULL |  |  |  |
| 53 | `SELLINGCOST` | SMALLINT | NOT NULL |  |  |  |
| 54 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 55 | `BOMPRICECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 56 | `BOMPRICE` | DECIMAL(18,5) |  |  |  |  |
| 57 | `BOMPRICETYPE` | CHAR(1) |  |  |  |  |
| 58 | `BOMPRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 59 | `BOMCOMPONENTTYPECODE` | CHAR(10) |  |  |  |  |
| 60 | `BOMSUPCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 61 | `BOMSUPCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 62 | `IPLPRICE` | DECIMAL(18,5) |  |  |  |  |
| 63 | `IPLUOMCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COSTSIMULATION_SIMULATION` | `COMPANYCODE`, `SIMULATIONCOUNTERCODE`, `SIMULATIONCODE` | [`COSTSIMULATION`](../COSTING/COSTSIMULATION.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `COSTSIMROUTECONSUMPTION.COMPANYCODE = COSTSIMULATION.COMPANYCODE AND COSTSIMROUTECONSUMPTION.SIMULATIONCOUNTERCODE = COSTSIMULATION.COUNTERCODE AND COSTSIMROUTECONSUMPTION.SIMULATIONCODE = COSTSIMULATION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COSTSIMROUTECONSUMPTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SIMULATIONCOUNTERCODE,
       t.SIMULATIONCODE,
       t.TABLEINDEX,
       t.PRODUCTINDEX,
       t.PLANTCODE,
       t.SUBUNIQUEID,
       t.COSTGROUPCODE,
       t.COSTSCOSTGROUPCODE,
       t.ROUTEINDEX,
       t.BOMINDEX,
       t.STEPNUMBER
FROM   DB2ADMIN.COSTSIMROUTECONSUMPTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
