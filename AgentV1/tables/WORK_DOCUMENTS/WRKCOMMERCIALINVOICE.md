# DB2ADMIN.WRKCOMMERCIALINVOICE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 57
- **Primary key**: `LINENO`, `COMPANYCODE`, `DIVISIONCODE`, `COMMERCIALINVOICECODE`, `INVOICELINENO`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 144407

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 3 | `COMMERCIALINVOICECODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `INVOICELINENO` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 5 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 6 | `PONO` | CHAR(120) |  |  |  |  |
| 7 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 8 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE05` | CHAR(20) |  |  | generic_classification_code |  |
| 10 | `PRODUCTAD` | DECIMAL(15,5) |  |  |  |  |
| 11 | `PCSINDOZENS` | DECIMAL(15,5) |  |  |  |  |
| 12 | `SCHEMETYPECODE` | CHAR(3) |  |  |  |  |
| 13 | `PRODUCTGROUPCODE` | CHAR(3) |  |  |  |  |
| 14 | `DEPBSRNO` | CHAR(20) |  |  |  |  |
| 15 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 16 | `EXCHANGERATEOFCONTRACT` | DECIMAL(28,15) |  |  |  |  |
| 17 | `SHIPPINGMARK` | VARCHAR(960) |  |  |  |  |
| 18 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 19 | `COMPANYCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 20 | `AMOUNT` | DECIMAL(15,5) |  |  |  |  |
| 21 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `TOTALQUANT` | DECIMAL(15,5) |  |  |  |  |
| 23 | `TOTALYARDS` | DECIMAL(15,5) |  |  |  |  |
| 24 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 26 | `PRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 27 | `SECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 28 | `BASEPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `BASEPRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 30 | `BASESECODARYUMCODE` | CHAR(3) |  |  |  |  |
| 31 | `SECODARYUMCODE` | CHAR(3) |  |  |  |  |
| 32 | `BASESECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 33 | `PACKINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 34 | `PACKINGUMCODE` | CHAR(3) |  |  |  |  |
| 35 | `RATE` | DECIMAL(18,5) |  |  |  |  |
| 36 | `TOTALNUMBEROFBALES` | INTEGER | NOT NULL |  |  |  |
| 37 | `GROSSWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 38 | `NETTWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 39 | `SEARCHDESCRIPTION` | VARCHAR(200) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 40 | `PRODUCTDESCRIPTION` | VARCHAR(960) |  |  |  |  |
| 41 | `INVOICEDESCRIPTION` | VARCHAR(960) |  |  |  |  |
| 42 | `CUSTOMINVOICES` | CHAR(120) |  |  |  |  |
| 43 | `FOBVALUEINRS` | DECIMAL(18,5) |  |  |  |  |
| 44 | `LESSDISCOUNT` | DECIMAL(18,5) |  |  |  |  |
| 45 | `LESSDISCOUNTINCC` | DECIMAL(18,5) |  |  |  |  |
| 46 | `LESSFREIGHT` | DECIMAL(18,5) |  |  |  |  |
| 47 | `LESSFREIGHTINCC` | DECIMAL(18,5) |  |  |  |  |
| 48 | `LESSINSURANCE` | DECIMAL(18,5) |  |  |  |  |
| 49 | `LESSINSURANCEINCC` | DECIMAL(18,5) |  |  |  |  |
| 50 | `PMVAMNTINRS` | DECIMAL(18,5) |  |  |  |  |
| 51 | `TOTALFOBVALUE` | DECIMAL(18,5) |  |  |  |  |
| 52 | `TOTALVALUE` | DECIMAL(18,5) |  |  |  |  |
| 53 | `LESSUPCHARGE` | DECIMAL(18,5) |  |  |  |  |
| 54 | `LESSUPCHARGEINCC` | DECIMAL(18,5) |  |  |  |  |
| 55 | `POLICYDETAILS` | VARCHAR(200) |  |  |  |  |
| 56 | `GRDETAILS` | VARCHAR(200) |  |  |  |  |

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
       t.PONO,
       t.SUBCODE01,
       t.SUBCODE04,
       t.SUBCODE05,
       t.PRODUCTAD,
       t.PCSINDOZENS
FROM   DB2ADMIN.WRKCOMMERCIALINVOICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
