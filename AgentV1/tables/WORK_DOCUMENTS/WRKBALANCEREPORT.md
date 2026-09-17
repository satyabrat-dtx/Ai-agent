# DB2ADMIN.WRKBALANCEREPORT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 40
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `CREATIONUSER`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 147189

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `STEP` | CHAR(1) | NOT NULL |  |  |  |
| 3 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 4 | `BALANCEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 5 | `RECEIPTQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 6 | `ISSUEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 7 | `ITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 8 | `CONTAINERELEMENTCODE` | CHAR(30) |  |  |  |  |
| 9 | `DECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 10 | `ITEMTYPEFROMCODE` | CHAR(3) | NOT NULL |  |  |  |
| 11 | `DECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 12 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 13 | `ITEMTYPETOCODE` | CHAR(3) |  |  |  |  |
| 14 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 15 | `DECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 16 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 17 | `DECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 18 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 19 | `DECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 20 | `TRANSACTIONDATE` | DATE |  |  |  |  |
| 21 | `REPORTOPTION` | INTEGER | NOT NULL |  |  |  |
| 22 | `UOMCODE` | CHAR(5) |  |  |  |  |
| 23 | `PRODUCTDESCRIPTION` | CHAR(120) |  |  |  |  |
| 24 | `DECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 25 | `DECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 26 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 27 | `DECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 28 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 29 | `DECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 30 | `DECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 31 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 32 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 33 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 34 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 35 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 36 | `OPENVALUE` | DECIMAL(18,5) |  |  |  |  |
| 37 | `RECEIPTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 38 | `ISSUEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 39 | `CUSTOMERNAME` | CHAR(100) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.USERPRIMARYQUANTITY,
       t.COMPANYCODE,
       t.STEP,
       t.CREATIONTIMESTAMP,
       t.BALANCEQUANTITY,
       t.RECEIPTQUANTITY,
       t.ISSUEQUANTITY,
       t.ITEMTYPECODE,
       t.CONTAINERELEMENTCODE,
       t.DECOSUBCODE01,
       t.ITEMTYPEFROMCODE,
       t.DECOSUBCODE02
FROM   DB2ADMIN.WRKBALANCEREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
