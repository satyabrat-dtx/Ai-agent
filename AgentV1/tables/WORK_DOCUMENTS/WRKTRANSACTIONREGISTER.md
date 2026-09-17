# DB2ADMIN.WRKTRANSACTIONREGISTER

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `SERIALNO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 147514

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `SERIALNO` | BIGINT | NOT NULL | PK | primary_key |  |
| 3 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 4 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `TRANSACTIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 6 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 7 | `PRODUCTCODE` | CHAR(140) |  |  |  |  |
| 8 | `PRODUCTDESC` | CHAR(100) |  |  |  |  |
| 9 | `FROMDATE` | DATE | NOT NULL |  |  | Inclusive start of a validity period. |
| 10 | `TRANSACTIONTIME` | TIME | NOT NULL |  |  |  |
| 11 | `TODATE` | DATE | NOT NULL |  |  | End of a validity period. |
| 12 | `SHIFTS` | CHAR(23) |  |  |  |  |
| 13 | `LONGDESCRIPTION` | CHAR(100) |  |  | description | Long human-readable label. |
| 14 | `SUMMARYDETAIL` | INTEGER | NOT NULL |  |  |  |
| 15 | `TRANSACTIONDATE` | DATE | NOT NULL |  |  |  |
| 16 | `VALUATION` | CHAR(1) |  |  |  |  |
| 17 | `TRANSACTIONNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 18 | `TRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 19 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 20 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 21 | `CONTAINERSUBCODE1` | CHAR(20) |  |  |  |  |
| 22 | `PROVISIONALBASECOST` | DECIMAL(18,5) |  |  |  |  |
| 23 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 24 | `DEFINITIVETRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 25 | `LOTCODE` | CHAR(10) |  |  |  |  |
| 26 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.SERIALNO,
       t.WAREHOUSECODE,
       t.ITEMTYPECODE,
       t.TRANSACTIONTYPE,
       t.TEMPLATECODE,
       t.PRODUCTCODE,
       t.PRODUCTDESC,
       t.FROMDATE,
       t.TRANSACTIONTIME,
       t.TODATE
FROM   DB2ADMIN.WRKTRANSACTIONREGISTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
