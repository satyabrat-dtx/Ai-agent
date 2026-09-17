# DB2ADMIN.WRKCOMMERCIALINVOICEMATRIX

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `LINENO`, `COMPANYCODE`, `DIVISIONCODE`, `COMMERCIALINVOICECODE`, `INVOICELINENO`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 144488

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 3 | `COMMERCIALINVOICECODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `INVOICELINENO` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 5 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 6 | `SHIPPINGMARK` | VARCHAR(960) |  |  |  |  |
| 7 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `COLORCODE` | CHAR(10) |  |  |  |  |
| 10 | `SIZECODE` | CHAR(10) |  |  |  |  |
| 11 | `AMOUNT` | DECIMAL(15,5) |  |  |  |  |
| 12 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 13 | `TOTALQUANT` | DECIMAL(15,5) |  |  |  |  |
| 14 | `TOTALYARDS` | DECIMAL(15,5) |  |  |  |  |
| 15 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 16 | `RATE` | DECIMAL(18,5) |  |  |  |  |
| 17 | `PRODUCTDESCRIPTION` | VARCHAR(960) |  |  |  |  |
| 18 | `INVOICEDESCRIPTION` | VARCHAR(960) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.LINENO,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.COMMERCIALINVOICECODE,
       t.INVOICELINENO,
       t.CREATIONTIMESTAMP,
       t.SHIPPINGMARK,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.COLORCODE,
       t.SIZECODE,
       t.AMOUNT
FROM   DB2ADMIN.WRKCOMMERCIALINVOICEMATRIX t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
