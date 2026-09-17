# DB2ADMIN.WRKRELEASEPRINTLINE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 36
- **Primary key**: `CREATIONTIMESTAMP`, `WRKRELEASEPRINTLINE`, `SUBLINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 31513

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `WRKRELEASEPRINTLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `SUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 3 | `SALESRELEASELINECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `SALESRELEASELINECODE` | CHAR(15) |  |  |  |  |
| 5 | `SALESRELEASELINELINE` | DECIMAL(7,0) |  |  |  |  |
| 6 | `SALESRELEASELINESUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 7 | `SALRELEASELINECMPRELEASELINE` | DECIMAL(3,0) |  |  |  |  |
| 8 | `SUMMARIZEDDESCRIPTION` | CHAR(200) |  |  |  |  |
| 9 | `ORDERITEMUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 10 | `ITEMLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 11 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 12 | `LINEUOMCODE` | CHAR(3) |  |  |  |  |
| 13 | `LINEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 14 | `LINEDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 15 | `CHARQUANTITY` | CHAR(16) |  |  |  |  |
| 16 | `RATE` | DECIMAL(6,3) |  |  |  |  |
| 17 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 18 | `NETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 19 | `DISCOUNTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 20 | `QUALITYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 21 | `STCGROUPLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 22 | `PROJECTLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 23 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 24 | `PHYWAREHOUSELONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 25 | `LGLWAREHOUSELONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 26 | `COSTCENTERLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 27 | `PAYMENTMETHODLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 28 | `PRICELISTLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 29 | `DSCCATEGORYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 30 | `TAXLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 31 | `AGENT1LONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 32 | `AGENT2LONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 33 | `AGENT3LONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 34 | `AGENT4LONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 35 | `AGENT5LONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.WRKRELEASEPRINTLINE,
       t.SUBLINE,
       t.SALESRELEASELINECOMPANYCODE,
       t.SALESRELEASELINECODE,
       t.SALESRELEASELINELINE,
       t.SALESRELEASELINESUBLINE,
       t.SALRELEASELINECMPRELEASELINE,
       t.SUMMARIZEDDESCRIPTION,
       t.ORDERITEMUNIQUEID,
       t.ITEMLONGDESCRIPTION,
       t.ITEMCODE
FROM   DB2ADMIN.WRKRELEASEPRINTLINE t
FETCH FIRST 100 ROWS ONLY;
```
