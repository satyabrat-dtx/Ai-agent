# DB2ADMIN.WRKBRCPRINT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 144177

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 3 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 4 | `COMMERCIALCODE` | CHAR(20) |  |  |  |  |
| 5 | `CUSTOMCODE` | VARCHAR(250) |  |  |  |  |
| 6 | `EXPORTSHIPPINGCODES` | VARCHAR(250) |  |  |  |  |
| 7 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `DISCOUNTAMT` | DECIMAL(18,5) |  |  |  |  |
| 9 | `FREIGHTAMT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `INSURANCEAMT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `COMMISIONAMT` | DECIMAL(18,5) |  |  |  |  |
| 12 | `BILLLOADINGCODE` | VARCHAR(250) |  |  |  |  |
| 13 | `BILLLOADINGDATE` | DATE |  |  |  |  |
| 14 | `CUSTOMINVOICEDATE` | DATE |  |  |  |  |
| 15 | `EXPSHIPPINGDATE` | DATE |  |  |  |  |
| 16 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 17 | `GROSSWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 18 | `COMMPER` | DECIMAL(9,5) |  |  |  |  |
| 19 | `BRCREALIZATIONDATE` | DATE |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.LINENO,
       t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.DIVISIONCODE,
       t.COMMERCIALCODE,
       t.CUSTOMCODE,
       t.EXPORTSHIPPINGCODES,
       t.AMOUNT,
       t.DISCOUNTAMT,
       t.FREIGHTAMT,
       t.INSURANCEAMT,
       t.COMMISIONAMT
FROM   DB2ADMIN.WRKBRCPRINT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
