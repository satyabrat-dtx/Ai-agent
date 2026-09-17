# DB2ADMIN.WRKPRODUCTCOSTHEADING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `UNIQUEID`, `TABLEINDEX`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 8947

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `TABLEINDEX` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `PRODUCTINDEX` | DECIMAL(11,0) |  |  |  |  |
| 4 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 5 | `COSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 6 | `COSTSCOSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 7 | `AVERAGECOSTINBASECURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 8 | `RUNNINGDATE` | DATE |  |  |  |  |
| 9 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `PRODUCTSUBCODE01` | CHAR(20) |  |  |  |  |
| 11 | `PRODUCTSUBCODE02` | CHAR(10) |  |  |  |  |
| 12 | `PRODUCTSUBCODE03` | CHAR(10) |  |  |  |  |
| 13 | `PRODUCTSUBCODE04` | CHAR(10) |  |  |  |  |
| 14 | `PRODUCTSUBCODE05` | CHAR(10) |  |  |  |  |
| 15 | `PRODUCTSUBCODE06` | CHAR(10) |  |  |  |  |
| 16 | `PRODUCTSUBCODE07` | CHAR(10) |  |  |  |  |
| 17 | `PRODUCTSUBCODE08` | CHAR(10) |  |  |  |  |
| 18 | `PRODUCTSUBCODE09` | CHAR(10) |  |  |  |  |
| 19 | `PRODUCTSUBCODE10` | CHAR(10) |  |  |  |  |
| 20 | `INDLEVEL` | INTEGER | NOT NULL |  |  |  |
| 21 | `CALCULATEDDATETIME` | TIMESTAMP |  |  |  |  |
| 22 | `ENDCALCULATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `GOODSVALUEINBASECURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 24 | `SELLINGVALUEINBASECURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 25 | `SUBUNIQUEID` | INTEGER | NOT NULL |  |  |  |
| 26 | `UPTOCOSTLEVELAVGCOST` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.UNIQUEID,
       t.TABLEINDEX,
       t.COMPANYCODE,
       t.PRODUCTINDEX,
       t.PLANTCODE,
       t.COSTGROUPCODE,
       t.COSTSCOSTGROUPCODE,
       t.AVERAGECOSTINBASECURRENCY,
       t.RUNNINGDATE,
       t.ITEMTYPECODE,
       t.PRODUCTSUBCODE01,
       t.PRODUCTSUBCODE02
FROM   DB2ADMIN.WRKPRODUCTCOSTHEADING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
