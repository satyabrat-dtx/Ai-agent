# DB2ADMIN.COSTROUTECONSUMPTIONBYDATE

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 62
- **Primary key**: `COMPANYCODE`, `PRODUCTINDEX`, `PLANTCODE`, `COSTGROUPCODE`, `COSTSCOSTGROUPCODE`, `VALIDITYDATE`, `ROUTEINDEX`, `BOMINDEX`, `LINENUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 238184

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PRODUCTINDEX` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `PLANTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `COSTGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `COSTSCOSTGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `VALIDITYDATE` | DATE | NOT NULL | PK | primary_key |  |
| 6 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 7 | `ROUTEINDEX` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 8 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 9 | `BOMINDEX` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 10 | `ITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 11 | `LINENUMBER` | BIGINT | NOT NULL | PK | primary_key |  |
| 12 | `ITEMSUBCODE01` | CHAR(20) | NOT NULL |  |  |  |
| 13 | `ITEMSUBCODE02` | CHAR(10) |  |  |  |  |
| 14 | `ITEMSUBCODE03` | CHAR(10) |  |  |  |  |
| 15 | `ITEMSUBCODE04` | CHAR(10) |  |  |  |  |
| 16 | `ITEMSUBCODE05` | CHAR(10) |  |  |  |  |
| 17 | `ITEMSUBCODE06` | CHAR(10) |  |  |  |  |
| 18 | `ITEMSUBCODE07` | CHAR(10) |  |  |  |  |
| 19 | `ITEMSUBCODE08` | CHAR(10) |  |  |  |  |
| 20 | `ITEMSUBCODE09` | CHAR(10) |  |  |  |  |
| 21 | `ITEMSUBCODE10` | CHAR(10) |  |  |  |  |
| 22 | `COSTCATEGORYCODE` | CHAR(20) |  |  |  |  |
| 23 | `COSTLEVELCODE` | CHAR(3) |  |  |  |  |
| 24 | `COMPONENTPLANTCODE` | CHAR(8) |  |  |  |  |
| 25 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 26 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 27 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 28 | `PRODUCTIONRESERVATIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 29 | `COMPONENTPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 30 | `COSTPER` | DECIMAL(18,5) |  |  |  |  |
| 31 | `CURRENCYPER` | CHAR(4) |  |  |  |  |
| 32 | `QUANTITYPER` | DECIMAL(15,5) |  |  |  |  |
| 33 | `QUANTITYPERUOMCODE` | CHAR(3) |  |  |  |  |
| 34 | `QUANTITYREQUIRED` | DECIMAL(20,10) |  |  |  |  |
| 35 | `COSTPERUNIT` | DECIMAL(18,5) |  |  |  |  |
| 36 | `COSTCURRENCY` | CHAR(4) |  |  |  |  |
| 37 | `QUANTITYREQUIREDPRIMARYUOM` | DECIMAL(20,10) |  |  |  |  |
| 38 | `CALCULATIONSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 39 | `PRODUCED` | SMALLINT | NOT NULL |  |  |  |
| 40 | `WASTETYPE1` | CHAR(2) |  |  |  |  |
| 41 | `WASTE1` | DECIMAL(11,2) |  |  |  |  |
| 42 | `WASTETYPE2` | CHAR(2) |  |  |  |  |
| 43 | `WASTE2` | DECIMAL(11,2) |  |  |  |  |
| 44 | `BOMCALCULATEQTYNAME` | CHAR(100) |  |  |  |  |
| 45 | `BOMCALCULATEQTYCODE` | CHAR(20) |  |  |  |  |
| 46 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 47 | `COSTINBASECURRENCY` | DECIMAL(20,10) |  |  |  |  |
| 48 | `WASTEPRODUCT` | CHAR(2) |  |  |  |  |
| 49 | `CONSUMPTIONCALCULATIONTYPE` | CHAR(1) |  |  |  |  |
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
| 61 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COSTROUTECONSUMPTIONBYDATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PRODUCTINDEX,
       t.PLANTCODE,
       t.COSTGROUPCODE,
       t.COSTSCOSTGROUPCODE,
       t.VALIDITYDATE,
       t.STEPNUMBER,
       t.ROUTEINDEX,
       t.ITEMNATURE,
       t.BOMINDEX,
       t.ITEMTYPECODE,
       t.LINENUMBER
FROM   DB2ADMIN.COSTROUTECONSUMPTIONBYDATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
