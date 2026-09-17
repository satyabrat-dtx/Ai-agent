# DB2ADMIN.QUOTATION

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 54
- **Primary key**: `COMPANYCODE`, `RFQHEADERRFQHEADERCOUNTERCODE`, `RFQHEADERRFQHEADERCODE`, `RFQHEADERLINENO`, `ORDPRNCUSTOMERSUPPLIERTYPE`, `ORDPRNCUSTOMERSUPPLIERCODE`
- **FK degree**: referenced by 0 constraint(s), references 10 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 109286

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `RFQHEADERRFQHEADERCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `RFQHEADERRFQHEADERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `RFQHEADERLINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 5 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 6 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 9 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `RFQDATE` | DATE |  |  |  |  |
| 19 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 20 | `UOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 21 | `SELECTED` | SMALLINT | NOT NULL |  |  |  |
| 22 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 23 | `PRICEUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 24 | `DELIVERYDATE` | DATE | NOT NULL |  |  |  |
| 25 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 26 | `TERMSOFDELIVERYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 27 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 28 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  | FK | foreign_key |  |
| 29 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 30 | `PAYMENTMETHODCODE` | CHAR(3) |  | FK | foreign_key |  |
| 31 | `QUOTATIONNO` | CHAR(15) |  |  |  |  |
| 32 | `QUOTATIONDATE` | DATE |  |  |  |  |
| 33 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 34 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 35 | `NETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 36 | `ROUNDOFFVALUE` | DECIMAL(18,5) |  |  |  |  |
| 37 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 38 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 39 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 40 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 41 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 42 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 43 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 44 | `VALIDDAYS` | INTEGER | NOT NULL |  |  |  |
| 45 | `QUOTELOCK` | SMALLINT | NOT NULL |  |  |  |
| 46 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 47 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 48 | `ALREADYUSED` | SMALLINT | NOT NULL |  |  |  |
| 49 | `SECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 50 | `PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 51 | `SECONDARYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 52 | `PACKAGINGUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 53 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |

## References (this table → parent) — 10

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `QUOTATION.CURRENCYCODE = CURRENCY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QUOTATION.COMPANYCODE = DIVISION.COMPANYCODE AND QUOTATION.DIVISIONCODE = DIVISION.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QUOTATION.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND QUOTATION.ITEMTYPECODE = ITEMTYPE.CODE` |
| `PAYMENTMETHOD_PAYMENTMETHOD` | `PAYMENTMETHODCOMPANYCODE`, `PAYMENTMETHODCODE` | [`PAYMENTMETHOD`](../CORE_MASTER/PAYMENTMETHOD.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QUOTATION.PAYMENTMETHODCOMPANYCODE = PAYMENTMETHOD.COMPANYCODE AND QUOTATION.PAYMENTMETHODCODE = PAYMENTMETHOD.CODE` |
| `TERMSOFDELIVERY_TERMSOFDELIVERY` | `TERMSOFDELIVERYCOMPANYCODE`, `TERMSOFDELIVERYCODE` | [`TERMSOFDELIVERY`](../CORE_MASTER/TERMSOFDELIVERY.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QUOTATION.TERMSOFDELIVERYCOMPANYCODE = TERMSOFDELIVERY.COMPANYCODE AND QUOTATION.TERMSOFDELIVERYCODE = TERMSOFDELIVERY.CODE` |
| `TERMSOFSHIPPING_TERMSOFSHIPPING` | `TERMSOFSHIPPINGCOMPANYCODE`, `TERMSOFSHIPPINGCODE` | [`TERMSOFSHIPPING`](../CORE_MASTER/TERMSOFSHIPPING.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QUOTATION.TERMSOFSHIPPINGCOMPANYCODE = TERMSOFSHIPPING.COMPANYCODE AND QUOTATION.TERMSOFSHIPPINGCODE = TERMSOFSHIPPING.CODE` |
| `UNITOFMEASURE_PACKAGINGUOM` | `PACKAGINGUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `QUOTATION.PACKAGINGUOMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_PRICEUOM` | `PRICEUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `QUOTATION.PRICEUOMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_SECONDARYUOM` | `SECONDARYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `QUOTATION.SECONDARYUOMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_UOM` | `UOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `QUOTATION.UOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `QUOTATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.RFQHEADERRFQHEADERCOUNTERCODE,
       t.RFQHEADERRFQHEADERCODE,
       t.RFQHEADERLINENO,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04
FROM   DB2ADMIN.QUOTATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
