# DB2ADMIN.WRKCUSTOMINVOICE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 59
- **Primary key**: `LINENO`, `COMPANYCODE`, `DIVISIONCODE`, `CUSTOMINVOICECODE`, `INVOICELINENO`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 144645

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 3 | `CUSTOMINVOICECODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `INVOICELINENO` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 5 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 6 | `PONO` | CHAR(120) |  |  |  |  |
| 7 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(20) |  |  | generic_classification_code |  |
| 9 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SIZESDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 11 | `PRODUCTAD` | DECIMAL(15,5) |  |  |  |  |
| 12 | `PCSINDOZENS` | DECIMAL(15,5) |  |  |  |  |
| 13 | `SCHEMETYPECODE` | CHAR(3) |  |  |  |  |
| 14 | `PRODUCTGROUPCODE` | CHAR(3) |  |  |  |  |
| 15 | `DEPBSRNO` | CHAR(20) |  |  |  |  |
| 16 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 17 | `EXCHANGERATEOFCONTRACT` | DECIMAL(28,15) |  |  |  |  |
| 18 | `SHIPPINGMARK` | VARCHAR(960) |  |  |  |  |
| 19 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 20 | `COMPANYCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 21 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `AMOUNT` | DECIMAL(15,5) |  |  |  |  |
| 23 | `PMVVALUE` | DECIMAL(15,5) |  |  |  |  |
| 24 | `TOTALQUANT` | DECIMAL(15,5) |  |  |  |  |
| 25 | `TOTALYARDS` | DECIMAL(15,5) |  |  |  |  |
| 26 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 28 | `PRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 29 | `SECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `BASEPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 31 | `BASEPRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 32 | `BASESECODARYUMCODE` | CHAR(3) |  |  |  |  |
| 33 | `SECODARYUMCODE` | CHAR(3) |  |  |  |  |
| 34 | `BASESECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 35 | `PACKINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 36 | `PACKINGUMCODE` | CHAR(3) |  |  |  |  |
| 37 | `RATE` | DECIMAL(18,5) |  |  |  |  |
| 38 | `TOTALNUMBEROFBALES` | INTEGER | NOT NULL |  |  |  |
| 39 | `ITEMDESCRIPTION` | VARCHAR(250) |  |  |  |  |
| 40 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 41 | `WIDTH` | DECIMAL(18,5) |  |  |  |  |
| 42 | `GROSSWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 43 | `NETTWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 44 | `SEARCHDESCRIPTION` | VARCHAR(200) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 45 | `PRODUCTDESCRIPTION` | VARCHAR(250) |  |  |  |  |
| 46 | `TOTALVALUE` | DECIMAL(18,5) |  |  |  |  |
| 47 | `LESSFREIGHT` | DECIMAL(18,5) |  |  |  |  |
| 48 | `LESSINSURANCE` | DECIMAL(18,5) |  |  |  |  |
| 49 | `LESSDISCOUNT` | DECIMAL(18,5) |  |  |  |  |
| 50 | `TOTALFOBVALUE` | DECIMAL(18,5) |  |  |  |  |
| 51 | `FOBVALUEINRS` | DECIMAL(18,5) |  |  |  |  |
| 52 | `PMVAMNTINRS` | DECIMAL(18,5) |  |  |  |  |
| 53 | `LESSDISCOUNTINCC` | DECIMAL(18,5) |  |  |  |  |
| 54 | `LESSFREIGHTINCC` | DECIMAL(18,5) |  |  |  |  |
| 55 | `LESSINSURANCEINCC` | DECIMAL(18,5) |  |  |  |  |
| 56 | `LESSUPCHARGE` | DECIMAL(18,5) |  |  |  |  |
| 57 | `LESSUPCHARGEINCC` | DECIMAL(18,5) |  |  |  |  |
| 58 | `LOTNO` | VARCHAR(200) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.LINENO,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CUSTOMINVOICECODE,
       t.INVOICELINENO,
       t.CREATIONTIMESTAMP,
       t.PONO,
       t.SUBCODE01,
       t.SUBCODE05,
       t.SUBCODE04,
       t.SIZESDESCRIPTION,
       t.PRODUCTAD
FROM   DB2ADMIN.WRKCUSTOMINVOICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
