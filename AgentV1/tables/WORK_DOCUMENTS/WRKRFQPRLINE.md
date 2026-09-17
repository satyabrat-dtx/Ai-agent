# DB2ADMIN.WRKRFQPRLINE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 37
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 109774

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CHOOSER` | SMALLINT | NOT NULL |  |  |  |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 3 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 4 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `COUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 7 | `PRREQUISITIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 8 | `PRCODE` | CHAR(15) |  |  |  |  |
| 9 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 10 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 11 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 12 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 23 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 24 | `PRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 25 | `DELIVERYDATE` | DATE |  |  |  |  |
| 26 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 27 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 28 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 30 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 32 | `REMARK` | VARCHAR(1000) |  |  |  |  |
| 33 | `SECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 34 | `PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 35 | `SECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 36 | `PACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CHOOSER,
       t.DIVISIONCODE,
       t.CREATIONTIMESTAMP,
       t.LINENO,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.PRREQUISITIONTEMPLATECODE,
       t.PRCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01
FROM   DB2ADMIN.WRKRFQPRLINE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
