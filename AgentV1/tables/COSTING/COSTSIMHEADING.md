# DB2ADMIN.COSTSIMHEADING

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 37
- **Primary key**: `COMPANYCODE`, `SIMULATIONCOUNTERCODE`, `SIMULATIONCODE`, `TABLEINDEX`, `SUBUNIQUEID`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 196006

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
| 9 | `AVERAGECOSTINBASECURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 10 | `GOODSVALUEINBASECURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 11 | `SELLINGVALUEINBASECURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 12 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 13 | `PRODUCTSUBCODE01` | CHAR(20) |  |  |  |  |
| 14 | `PRODUCTSUBCODE02` | CHAR(10) |  |  |  |  |
| 15 | `PRODUCTSUBCODE03` | CHAR(10) |  |  |  |  |
| 16 | `PRODUCTSUBCODE04` | CHAR(10) |  |  |  |  |
| 17 | `PRODUCTSUBCODE05` | CHAR(10) |  |  |  |  |
| 18 | `PRODUCTSUBCODE06` | CHAR(10) |  |  |  |  |
| 19 | `PRODUCTSUBCODE07` | CHAR(10) |  |  |  |  |
| 20 | `PRODUCTSUBCODE08` | CHAR(10) |  |  |  |  |
| 21 | `PRODUCTSUBCODE09` | CHAR(10) |  |  |  |  |
| 22 | `PRODUCTSUBCODE10` | CHAR(10) |  |  |  |  |
| 23 | `INDLEVEL` | INTEGER | NOT NULL |  |  |  |
| 24 | `CALCULATEDDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `CALCULATEDPRICE` | DECIMAL(18,5) |  |  |  |  |
| 26 | `CALCULATEDPROFIT` | DECIMAL(18,5) |  |  |  |  |
| 27 | `SELLINGPRICE` | DECIMAL(18,5) |  |  |  |  |
| 28 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 29 | `SOLSALESORDERCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 30 | `SOLSALESORDERCODE` | CHAR(15) |  | FK | foreign_key |  |
| 31 | `SOLORDERLINE` | DECIMAL(7,0) |  | FK | foreign_key |  |
| 32 | `SOLORDERSUBLINE` | DECIMAL(3,0) |  | FK | foreign_key |  |
| 33 | `SOLCOMPONENTORDERLINE` | DECIMAL(3,0) |  | FK | foreign_key |  |
| 34 | `SOLUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 35 | `SOLUSERPRIMARYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 36 | `SOLCANCELLEDUSERPRMQUANTITY` | DECIMAL(15,5) |  |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COSTSIMULATION_SIMULATION` | `COMPANYCODE`, `SIMULATIONCOUNTERCODE`, `SIMULATIONCODE` | [`COSTSIMULATION`](../COSTING/COSTSIMULATION.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `COSTSIMHEADING.COMPANYCODE = COSTSIMULATION.COMPANYCODE AND COSTSIMHEADING.SIMULATIONCOUNTERCODE = COSTSIMULATION.COUNTERCODE AND COSTSIMHEADING.SIMULATIONCODE = COSTSIMULATION.CODE` |
| `SALESORDERLINE_SOL` | `COMPANYCODE`, `SOLSALESORDERCOUNTERCODE`, `SOLSALESORDERCODE`, `SOLORDERLINE`, `SOLORDERSUBLINE`, `SOLCOMPONENTORDERLINE` | [`SALESORDERLINE`](../SALES/SALESORDERLINE.md) | `SALESORDERCOMPANYCODE`, `SALESORDERCOUNTERCODE`, `SALESORDERCODE`, `ORDERLINE`, `ORDERSUBLINE`, `COMPONENTORDERLINE` | RESTRICT | `COSTSIMHEADING.COMPANYCODE = SALESORDERLINE.SALESORDERCOMPANYCODE AND COSTSIMHEADING.SOLSALESORDERCOUNTERCODE = SALESORDERLINE.SALESORDERCOUNTERCODE AND COSTSIMHEADING.SOLSALESORDERCODE = SALESORDERLINE.SALESORDERCODE AND COSTSIMHEADING.SOLORDERLINE = SALESORDERLINE.ORDERLINE AND COSTSIMHEADING.SOLORDERSUBLINE = SALESORDERLINE.ORDERSUBLINE AND COSTSIMHEADING.SOLCOMPONENTORDERLINE = SALESORDERLINE.COMPONENTORDERLINE` |
| `UNITOFMEASURE_SOLUSERPRIMARYUOM` | `SOLUSERPRIMARYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `COSTSIMHEADING.SOLUSERPRIMARYUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COSTSIMHEADINGUID` (ABSUNIQUEID)

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
       t.AVERAGECOSTINBASECURRENCY,
       t.GOODSVALUEINBASECURRENCY,
       t.SELLINGVALUEINBASECURRENCY
FROM   DB2ADMIN.COSTSIMHEADING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
