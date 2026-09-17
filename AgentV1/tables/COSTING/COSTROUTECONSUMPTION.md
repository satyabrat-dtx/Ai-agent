# DB2ADMIN.COSTROUTECONSUMPTION

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 61
- **Primary key**: `TABLEINDEX`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 70954

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TABLEINDEX` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `PRODUCTINDEX` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 3 | `PLANTCODE` | CHAR(8) | NOT NULL |  |  |  |
| 4 | `COSTGROUPCODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `COSTSCOSTGROUPCODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `ROUTEINDEX` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 7 | `BOMINDEX` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 8 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 9 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 10 | `ITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 11 | `ITEMSUBCODE01` | CHAR(20) | NOT NULL |  |  |  |
| 12 | `ITEMSUBCODE02` | CHAR(10) |  |  |  |  |
| 13 | `ITEMSUBCODE03` | CHAR(10) |  |  |  |  |
| 14 | `ITEMSUBCODE04` | CHAR(10) |  |  |  |  |
| 15 | `ITEMSUBCODE05` | CHAR(10) |  |  |  |  |
| 16 | `ITEMSUBCODE06` | CHAR(10) |  |  |  |  |
| 17 | `ITEMSUBCODE07` | CHAR(10) |  |  |  |  |
| 18 | `ITEMSUBCODE08` | CHAR(10) |  |  |  |  |
| 19 | `ITEMSUBCODE09` | CHAR(10) |  |  |  |  |
| 20 | `ITEMSUBCODE10` | CHAR(10) |  |  |  |  |
| 21 | `COSTCATEGORYCODE` | CHAR(20) |  |  |  |  |
| 22 | `COSTLEVELCODE` | CHAR(3) |  |  |  |  |
| 23 | `COMPONENTPLANTCODE` | CHAR(8) |  |  |  |  |
| 24 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 25 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 26 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 27 | `PRODUCTIONRESERVATIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 28 | `COMPONENTPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 29 | `COSTPER` | DECIMAL(18,5) |  |  |  |  |
| 30 | `CURRENCYPER` | CHAR(4) |  |  |  |  |
| 31 | `QUANTITYPER` | DECIMAL(15,5) |  |  |  |  |
| 32 | `QUANTITYPERUOMCODE` | CHAR(3) |  |  |  |  |
| 33 | `QUANTITYREQUIRED` | DECIMAL(20,10) |  |  |  |  |
| 34 | `COSTPERUNIT` | DECIMAL(18,5) |  |  |  |  |
| 35 | `COSTCURRENCY` | CHAR(4) |  |  |  |  |
| 36 | `QUANTITYREQUIREDPRIMARYUOM` | DECIMAL(20,10) |  |  |  |  |
| 37 | `CALCULATIONSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 38 | `PRODUCED` | SMALLINT | NOT NULL |  |  |  |
| 39 | `WASTETYPE1` | CHAR(2) |  |  |  |  |
| 40 | `WASTE1` | DECIMAL(11,2) |  |  |  |  |
| 41 | `WASTETYPE2` | CHAR(2) |  |  |  |  |
| 42 | `WASTE2` | DECIMAL(11,2) |  |  |  |  |
| 43 | `BOMCALCULATEQTYNAME` | CHAR(100) |  |  |  |  |
| 44 | `BOMCALCULATEQTYCODE` | CHAR(20) |  |  |  |  |
| 45 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 46 | `COSTINBASECURRENCY` | DECIMAL(20,10) |  |  |  |  |
| 47 | `WASTEPRODUCT` | CHAR(2) |  |  |  |  |
| 48 | `CONSUMPTIONCALCULATIONTYPE` | CHAR(1) |  |  |  |  |
| 49 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 50 | `ADDITIONALCOST` | SMALLINT | NOT NULL |  |  |  |
| 51 | `SELLINGCOST` | SMALLINT | NOT NULL |  |  |  |
| 52 | `BOMPRICECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 53 | `BOMPRICE` | DECIMAL(18,5) |  |  |  |  |
| 54 | `BOMPRICETYPE` | CHAR(1) |  |  |  |  |
| 55 | `BOMPRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 56 | `BOMCOMPONENTTYPECODE` | CHAR(10) |  |  |  |  |
| 57 | `BOMSUPCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 58 | `BOMSUPCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 59 | `IPLPRICE` | DECIMAL(18,5) |  |  |  |  |
| 60 | `IPLUOMCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COSTROUTECONSUMPTIONUID` (ABSUNIQUEID)
- `COSTROUTECONS01` (COMPANYCODE, PRODUCTINDEX, PLANTCODE, COSTGROUPCODE, COSTSCOSTGROUPCODE, ITEMNATURE, PRODUCED)

## Starter query

```sql
SELECT t.TABLEINDEX,
       t.COMPANYCODE,
       t.PRODUCTINDEX,
       t.PLANTCODE,
       t.COSTGROUPCODE,
       t.COSTSCOSTGROUPCODE,
       t.ROUTEINDEX,
       t.BOMINDEX,
       t.STEPNUMBER,
       t.ITEMNATURE,
       t.ITEMTYPECODE,
       t.ITEMSUBCODE01
FROM   DB2ADMIN.COSTROUTECONSUMPTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
