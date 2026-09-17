# DB2ADMIN.WRKPRDCOSTROUTECONSUMPTION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 66
- **Primary key**: `UNIQUEID`, `TABLEINDEX`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 79481

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `TABLEINDEX` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `PRODUCTINDEX` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 4 | `PLANTCODE` | CHAR(8) | NOT NULL |  |  |  |
| 5 | `COSTGROUPCODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `COSTSCOSTGROUPCODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `ROUTEINDEX` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 8 | `BOMINDEX` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 9 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 10 | `ITEMNATURE` | CHAR(1) |  |  |  |  |
| 11 | `ITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 12 | `RUNNINGDATE` | DATE |  |  |  |  |
| 13 | `ITEMSUBCODE01` | CHAR(20) | NOT NULL |  |  |  |
| 14 | `ITEMSUBCODE02` | CHAR(10) |  |  |  |  |
| 15 | `ITEMSUBCODE03` | CHAR(10) |  |  |  |  |
| 16 | `ITEMSUBCODE04` | CHAR(10) |  |  |  |  |
| 17 | `ITEMSUBCODE05` | CHAR(10) |  |  |  |  |
| 18 | `ITEMSUBCODE06` | CHAR(10) |  |  |  |  |
| 19 | `ITEMSUBCODE07` | CHAR(10) |  |  |  |  |
| 20 | `INDLEVEL` | INTEGER | NOT NULL |  |  |  |
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
| 50 | `ENDCALCULATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 51 | `WASTEPRODUCT` | CHAR(2) |  |  |  |  |
| 52 | `CONSUMPTIONCALCULATIONTYPE` | CHAR(1) |  |  |  |  |
| 53 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 54 | `ADDITIONALCOST` | SMALLINT | NOT NULL |  |  |  |
| 55 | `SELLINGCOST` | SMALLINT | NOT NULL |  |  |  |
| 56 | `SUBUNIQUEID` | INTEGER | NOT NULL |  |  |  |
| 57 | `BOMPRICECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 58 | `BOMPRICE` | DECIMAL(18,5) |  |  |  |  |
| 59 | `BOMPRICETYPE` | CHAR(1) |  |  |  |  |
| 60 | `BOMPRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 61 | `BOMCOMPONENTTYPECODE` | CHAR(10) |  |  |  |  |
| 62 | `BOMSUPCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 63 | `BOMSUPCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 64 | `IPLPRICE` | DECIMAL(18,5) |  |  |  |  |
| 65 | `IPLUOMCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKPRDCSTRTECONS01` (UNIQUEID, PLANTCODE, COSTGROUPCODE, COSTSCOSTGROUPCODE, PRODUCTINDEX)
- `WRKPRDCOSTROUTECONSUMPTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.TABLEINDEX,
       t.COMPANYCODE,
       t.PRODUCTINDEX,
       t.PLANTCODE,
       t.COSTGROUPCODE,
       t.COSTSCOSTGROUPCODE,
       t.ROUTEINDEX,
       t.BOMINDEX,
       t.STEPNUMBER,
       t.ITEMNATURE,
       t.ITEMTYPECODE
FROM   DB2ADMIN.WRKPRDCOSTROUTECONSUMPTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
