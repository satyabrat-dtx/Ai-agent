# DB2ADMIN.WRKBILLOFEXCHANGE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 46
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 240204

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 5 | `DIVISIONNAME` | VARCHAR(200) |  |  |  |  |
| 6 | `BILLOFEXCHANGECODE` | CHAR(12) | NOT NULL |  |  |  |
| 7 | `BILLOFEXCHANGEDATE` | DATE | NOT NULL |  |  |  |
| 8 | `BILLOFEXCHANGEDAYSAFTER` | VARCHAR(100) |  |  |  |  |
| 9 | `BILLOFEXCHANGEPAYTOORDER` | VARCHAR(100) |  |  |  |  |
| 10 | `BIOFEXCHNAGEINVCURRENCYCODE` | CHAR(12) |  |  |  |  |
| 11 | `AWBNOCODE` | CHAR(20) |  |  |  |  |
| 12 | `AWBDATE` | DATE |  |  |  |  |
| 13 | `AMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 14 | `COMINVOICENO` | CHAR(20) |  |  |  |  |
| 15 | `INVTYPECODE` | CHAR(3) |  |  |  |  |
| 16 | `INVOICECURRENCYCODE` | CHAR(3) |  |  |  |  |
| 17 | `INVOICEDATE` | DATE |  |  |  |  |
| 18 | `LCLCNO` | CHAR(35) |  |  |  |  |
| 19 | `LCLCDATE` | DATE |  |  |  |  |
| 20 | `LCBENEFICIARYBANKBANKCNYCODE` | VARCHAR(200) |  |  |  |  |
| 21 | `LCBENEFICIARYBANKBRANCHCODE` | VARCHAR(200) |  |  |  |  |
| 22 | `LCBENEFICIARYBANKCODE` | VARCHAR(200) |  |  |  |  |
| 23 | `LCBADDRESSLINE1` | VARCHAR(200) |  |  |  |  |
| 24 | `LCBADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 25 | `LCBADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 26 | `LCBADDRESSLINE4` | VARCHAR(200) |  |  |  |  |
| 27 | `LCBADDRESSLINE5` | VARCHAR(200) |  |  |  |  |
| 28 | `LCBPOSTALCODE` | CHAR(20) |  |  |  |  |
| 29 | `LCBTOWN` | VARCHAR(200) |  |  |  |  |
| 30 | `LCBDISTRICT` | VARCHAR(200) |  |  |  |  |
| 31 | `LCBBANKNAME` | VARCHAR(200) |  |  |  |  |
| 32 | `LCBBANKCOUNTRY` | VARCHAR(200) |  |  |  |  |
| 33 | `LCOPENINGBANKBANKCOUNTRYCODE` | VARCHAR(200) |  |  |  |  |
| 34 | `LCOPENINGBANKBRANCHCODE` | VARCHAR(200) |  |  |  |  |
| 35 | `LCOPENINGBANKCODE` | VARCHAR(200) |  |  |  |  |
| 36 | `LCOADDRESSLINE1` | VARCHAR(200) |  |  |  |  |
| 37 | `LCOADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 38 | `LCOADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 39 | `LCOADDRESSLINE4` | VARCHAR(200) |  |  |  |  |
| 40 | `LCOADDRESSLINE5` | VARCHAR(200) |  |  |  |  |
| 41 | `LCOPOSTALCODE` | CHAR(20) |  |  |  |  |
| 42 | `LCOTOWN` | VARCHAR(200) |  |  |  |  |
| 43 | `LCODISTRICT` | VARCHAR(200) |  |  |  |  |
| 44 | `LCOBANKNAME` | VARCHAR(200) |  |  |  |  |
| 45 | `LCOBANKCOUNTRY` | VARCHAR(200) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.DIVISIONNAME,
       t.BILLOFEXCHANGECODE,
       t.BILLOFEXCHANGEDATE,
       t.BILLOFEXCHANGEDAYSAFTER,
       t.BILLOFEXCHANGEPAYTOORDER,
       t.BIOFEXCHNAGEINVCURRENCYCODE,
       t.AWBNOCODE
FROM   DB2ADMIN.WRKBILLOFEXCHANGE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
