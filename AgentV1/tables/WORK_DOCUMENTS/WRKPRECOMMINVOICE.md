# DB2ADMIN.WRKPRECOMMINVOICE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 43
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `DIVISIONCODE`, `INVOICETYPECODE`, `BUYERSPOREFNO`, `RATE`, `ITEMTYPECODE`, `STYLENO`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 145406

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 3 | `INVOICETYPECODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `BUYERSPOREFNO` | CHAR(100) | NOT NULL | PK | primary_key |  |
| 5 | `RATE` | DECIMAL(18,5) | NOT NULL | PK | primary_key |  |
| 6 | `STYLENO` | CHAR(100) | NOT NULL | PK | primary_key |  |
| 7 | `ITEMDESP` | VARCHAR(200) |  |  |  |  |
| 8 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 9 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 10 | `DESPOFGOODS` | VARCHAR(200) |  |  |  |  |
| 11 | `QUANTITY` | DECIMAL(18,5) |  |  |  |  |
| 12 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `HSCODE` | CHAR(100) |  |  |  |  |
| 14 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 15 | `PRODUCTGRPDESP` | VARCHAR(200) |  |  |  |  |
| 16 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 17 | `ALLBUYERREF` | VARCHAR(1000) |  |  |  |  |
| 18 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 19 | `SIONDRAWBACKS` | VARCHAR(1000) |  |  |  |  |
| 20 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 21 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 22 | `ALLSTYLEREF` | VARCHAR(1000) |  |  |  |  |
| 23 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 24 | `QTYCURRENCYDESP` | VARCHAR(80) |  |  |  |  |
| 25 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 26 | `RATEDESP` | VARCHAR(80) |  |  |  |  |
| 27 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 28 | `AMTDESP` | VARCHAR(80) |  |  |  |  |
| 29 | `FIRMADDRESS` | VARCHAR(200) |  |  |  |  |
| 30 | `SHIPPINGMARK` | VARCHAR(1000) |  |  |  |  |
| 31 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 32 | `HANGERAMOUT` | DECIMAL(9,2) |  |  |  |  |
| 33 | `HANGERPRICE` | DECIMAL(5,2) |  |  |  |  |
| 34 | `HANGERQTY` | INTEGER | NOT NULL |  |  |  |
| 35 | `REMARK01` | CHAR(50) |  |  |  |  |
| 36 | `REMARK02` | CHAR(50) |  |  |  |  |
| 37 | `REMARK03` | CHAR(50) |  |  |  |  |
| 38 | `REMARK04` | CHAR(50) |  |  |  |  |
| 39 | `REMARK05` | CHAR(50) |  |  |  |  |
| 40 | `TEXTFORPRINTING` | CHAR(50) |  |  |  |  |
| 41 | `DRAWBACKS` | VARCHAR(1000) |  |  |  |  |
| 42 | `FINALSUMCOMMERCIALINVOICE` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.INVOICETYPECODE,
       t.BUYERSPOREFNO,
       t.RATE,
       t.STYLENO,
       t.ITEMDESP,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.DESPOFGOODS,
       t.QUANTITY
FROM   DB2ADMIN.WRKPRECOMMINVOICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
