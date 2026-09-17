# DB2ADMIN.COSTHEADINGBYDATE

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 40
- **Primary key**: `COMPANYCODE`, `PRODUCTINDEX`, `PLANTCODE`, `COSTGROUPCODE`, `COSTSCOSTGROUPCODE`, `VALIDITYDATE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 238060

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PRODUCTINDEX` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `PLANTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `COSTGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `COSTSCOSTGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `VALIDITYDATE` | DATE | NOT NULL | PK | primary_key |  |
| 6 | `AVERAGECOSTINBASECURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 7 | `GOODSVALUEINBASECURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 8 | `SELLINGVALUEINBASECURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 9 | `VALIDTODATE` | DATE |  |  |  |  |
| 10 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 11 | `PRODUCTSUBCODE01` | CHAR(20) |  |  |  |  |
| 12 | `PRODUCTSUBCODE02` | CHAR(10) |  |  |  |  |
| 13 | `PRODUCTSUBCODE03` | CHAR(10) |  |  |  |  |
| 14 | `PRODUCTSUBCODE04` | CHAR(10) |  |  |  |  |
| 15 | `PRODUCTSUBCODE05` | CHAR(10) |  |  |  |  |
| 16 | `PRODUCTSUBCODE06` | CHAR(10) |  |  |  |  |
| 17 | `PRODUCTSUBCODE07` | CHAR(10) |  |  |  |  |
| 18 | `PRODUCTSUBCODE08` | CHAR(10) |  |  |  |  |
| 19 | `PRODUCTSUBCODE09` | CHAR(10) |  |  |  |  |
| 20 | `PRODUCTSUBCODE10` | CHAR(10) |  |  |  |  |
| 21 | `INDLEVEL` | INTEGER | NOT NULL |  |  |  |
| 22 | `CALCULATEDDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `UPTOCOSTLEVELCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 24 | `UPTOCOSTLEVELCODE` | CHAR(3) |  | FK | foreign_key |  |
| 25 | `UPDATEDPRICELISTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 26 | `PERCENTCATEGORY1` | DECIMAL(6,3) |  |  |  |  |
| 27 | `PERCENTCATEGORY2` | DECIMAL(6,3) |  |  |  |  |
| 28 | `PERCENTCATEGORY3` | DECIMAL(6,3) |  |  |  |  |
| 29 | `PERCENTCATEGORY4` | DECIMAL(6,3) |  |  |  |  |
| 30 | `PERCENTCATEGORY5` | DECIMAL(6,3) |  |  |  |  |
| 31 | `PERCENTCATEGORY6` | DECIMAL(6,3) |  |  |  |  |
| 32 | `PERCENTCATEGORY7` | DECIMAL(6,3) |  |  |  |  |
| 33 | `PERCENTCATEGORY8` | DECIMAL(6,3) |  |  |  |  |
| 34 | `PERCENTCATEGORY9` | DECIMAL(6,3) |  |  |  |  |
| 35 | `PERCENTCATEGORY10` | DECIMAL(6,3) |  |  |  |  |
| 36 | `PERCENTCATEGORY11` | DECIMAL(6,3) |  |  |  |  |
| 37 | `PERCENTCATEGORY12` | DECIMAL(6,3) |  |  |  |  |
| 38 | `PERCENTCATEGORY0` | DECIMAL(6,3) |  |  |  |  |
| 39 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COSTLEVEL_UPTOCOSTLEVEL` | `UPTOCOSTLEVELCOMPANYCODE`, `UPTOCOSTLEVELCODE` | [`COSTLEVEL`](../COSTING/COSTLEVEL.md) | `COMPANYCODE`, `CODE` | RESTRICT | `COSTHEADINGBYDATE.UPTOCOSTLEVELCOMPANYCODE = COSTLEVEL.COMPANYCODE AND COSTHEADINGBYDATE.UPTOCOSTLEVELCODE = COSTLEVEL.CODE` |
| `INTERNALPRICELIST_UPDATEDPRICELIST` | `COMPANYCODE`, `UPDATEDPRICELISTCODE` | [`INTERNALPRICELIST`](../INTERNAL_ORDERS/INTERNALPRICELIST.md) | `COMPANYCODE`, `CODE` | RESTRICT | `COSTHEADINGBYDATE.COMPANYCODE = INTERNALPRICELIST.COMPANYCODE AND COSTHEADINGBYDATE.UPDATEDPRICELISTCODE = INTERNALPRICELIST.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COSTHEADINGBYDATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PRODUCTINDEX,
       t.PLANTCODE,
       t.COSTGROUPCODE,
       t.COSTSCOSTGROUPCODE,
       t.VALIDITYDATE,
       t.AVERAGECOSTINBASECURRENCY,
       t.GOODSVALUEINBASECURRENCY,
       t.SELLINGVALUEINBASECURRENCY,
       t.VALIDTODATE,
       t.ITEMTYPECODE,
       t.PRODUCTSUBCODE01
FROM   DB2ADMIN.COSTHEADINGBYDATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
