# DB2ADMIN.COSTHEADING

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 40
- **Primary key**: `TABLEINDEX`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 5894

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TABLEINDEX` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) |  | FK | foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `PRODUCTINDEX` | DECIMAL(11,0) |  |  |  |  |
| 3 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 4 | `COSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 5 | `COSTSCOSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 6 | `AVERAGECOSTINBASECURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 7 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 8 | `PRODUCTSUBCODE01` | CHAR(20) |  |  |  |  |
| 9 | `PRODUCTSUBCODE02` | CHAR(10) |  |  |  |  |
| 10 | `PRODUCTSUBCODE03` | CHAR(10) |  |  |  |  |
| 11 | `PRODUCTSUBCODE04` | CHAR(10) |  |  |  |  |
| 12 | `PRODUCTSUBCODE05` | CHAR(10) |  |  |  |  |
| 13 | `PRODUCTSUBCODE06` | CHAR(10) |  |  |  |  |
| 14 | `PRODUCTSUBCODE07` | CHAR(10) |  |  |  |  |
| 15 | `PRODUCTSUBCODE08` | CHAR(10) |  |  |  |  |
| 16 | `PRODUCTSUBCODE09` | CHAR(10) |  |  |  |  |
| 17 | `PRODUCTSUBCODE10` | CHAR(10) |  |  |  |  |
| 18 | `INDLEVEL` | INTEGER | NOT NULL |  |  |  |
| 19 | `CALCULATEDDATETIME` | TIMESTAMP |  |  |  |  |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `GOODSVALUEINBASECURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 22 | `SELLINGVALUEINBASECURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 23 | `UPTOCOSTLEVELCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 24 | `UPTOCOSTLEVELCODE` | CHAR(3) |  | FK | foreign_key |  |
| 25 | `VALIDITYDATE` | DATE |  |  |  |  |
| 26 | `UPDATEDPRICELISTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 27 | `PERCENTCATEGORY1` | DECIMAL(6,3) |  |  |  |  |
| 28 | `PERCENTCATEGORY2` | DECIMAL(6,3) |  |  |  |  |
| 29 | `PERCENTCATEGORY3` | DECIMAL(6,3) |  |  |  |  |
| 30 | `PERCENTCATEGORY4` | DECIMAL(6,3) |  |  |  |  |
| 31 | `PERCENTCATEGORY5` | DECIMAL(6,3) |  |  |  |  |
| 32 | `PERCENTCATEGORY6` | DECIMAL(6,3) |  |  |  |  |
| 33 | `PERCENTCATEGORY7` | DECIMAL(6,3) |  |  |  |  |
| 34 | `PERCENTCATEGORY8` | DECIMAL(6,3) |  |  |  |  |
| 35 | `PERCENTCATEGORY9` | DECIMAL(6,3) |  |  |  |  |
| 36 | `PERCENTCATEGORY10` | DECIMAL(6,3) |  |  |  |  |
| 37 | `PERCENTCATEGORY11` | DECIMAL(6,3) |  |  |  |  |
| 38 | `PERCENTCATEGORY12` | DECIMAL(6,3) |  |  |  |  |
| 39 | `PERCENTCATEGORY0` | DECIMAL(6,3) |  |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COSTLEVEL_UPTOCOSTLEVEL` | `UPTOCOSTLEVELCOMPANYCODE`, `UPTOCOSTLEVELCODE` | [`COSTLEVEL`](../COSTING/COSTLEVEL.md) | `COMPANYCODE`, `CODE` | RESTRICT | `COSTHEADING.UPTOCOSTLEVELCOMPANYCODE = COSTLEVEL.COMPANYCODE AND COSTHEADING.UPTOCOSTLEVELCODE = COSTLEVEL.CODE` |
| `INTERNALPRICELIST_UPDATEDPRICELIST` | `COMPANYCODE`, `UPDATEDPRICELISTCODE` | [`INTERNALPRICELIST`](../INTERNAL_ORDERS/INTERNALPRICELIST.md) | `COMPANYCODE`, `CODE` | RESTRICT | `COSTHEADING.COMPANYCODE = INTERNALPRICELIST.COMPANYCODE AND COSTHEADING.UPDATEDPRICELISTCODE = INTERNALPRICELIST.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COSTHEADINGUID` (ABSUNIQUEID)
- `CHPRIMRAY` (PRODUCTINDEX, COSTSCOSTGROUPCODE, COSTGROUPCODE, PLANTCODE, COMPANYCODE)

## Starter query

```sql
SELECT t.TABLEINDEX,
       t.COMPANYCODE,
       t.PRODUCTINDEX,
       t.PLANTCODE,
       t.COSTGROUPCODE,
       t.COSTSCOSTGROUPCODE,
       t.AVERAGECOSTINBASECURRENCY,
       t.ITEMTYPECODE,
       t.PRODUCTSUBCODE01,
       t.PRODUCTSUBCODE02,
       t.PRODUCTSUBCODE03,
       t.PRODUCTSUBCODE04
FROM   DB2ADMIN.COSTHEADING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
