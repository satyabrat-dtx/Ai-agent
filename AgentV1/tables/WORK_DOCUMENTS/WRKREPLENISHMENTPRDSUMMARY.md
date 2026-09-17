# DB2ADMIN.WRKREPLENISHMENTPRDSUMMARY

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `CREATIONTIMESTAMP`, `ITEMTYPEAFICODE`, `COMPANYCODE`, `SERIALNO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 130094

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `ITEMTYPEAFICODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 3 | `SUBCODE02` | CHAR(20) |  |  | generic_classification_code |  |
| 4 | `SUBCODE03` | CHAR(20) |  |  | generic_classification_code |  |
| 5 | `SUBCODE04` | CHAR(20) |  |  | generic_classification_code |  |
| 6 | `SUBCODE05` | CHAR(20) |  |  | generic_classification_code |  |
| 7 | `SUBCODE06` | CHAR(20) |  |  | generic_classification_code |  |
| 8 | `SUBCODE07` | CHAR(20) |  |  | generic_classification_code |  |
| 9 | `SUBCODE08` | CHAR(20) |  |  | generic_classification_code |  |
| 10 | `SUBCODE09` | CHAR(20) |  |  | generic_classification_code |  |
| 11 | `SUBCODE10` | CHAR(20) |  |  | generic_classification_code |  |
| 12 | `ORDERBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 13 | `ORDERBASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 14 | `ORDERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 15 | `ORDERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 16 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 17 | `PRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 18 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 19 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 20 | `UNITPRICE` | DECIMAL(18,5) |  |  |  |  |
| 21 | `SERIALNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 22 | `ITEMTYPECODE` | CHAR(120) |  |  |  |  |
| 23 | `SUMMARIZEDDESCRIPTION` | CHAR(100) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08,
       t.SUBCODE09,
       t.SUBCODE10
FROM   DB2ADMIN.WRKREPLENISHMENTPRDSUMMARY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
