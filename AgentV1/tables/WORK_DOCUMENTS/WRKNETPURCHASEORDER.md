# DB2ADMIN.WRKNETPURCHASEORDER

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 60
- **Primary key**: `LINENO`, `CREATIONTIMESTAMP`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 134259

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `PRODUCTIDENTIFIER` | INTEGER | NOT NULL |  |  |  |
| 4 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 5 | `REPLENCOUNTER` | CHAR(8) |  |  |  |  |
| 6 | `REPLECODE` | CHAR(15) |  |  |  |  |
| 7 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 8 | `UOM` | CHAR(3) |  |  |  |  |
| 9 | `QUANTITY` | DECIMAL(18,5) |  |  |  |  |
| 10 | `POUOM` | CHAR(3) |  |  |  |  |
| 11 | `PRODUCTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 12 | `DISCOUNTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `POQUANTITY` | DECIMAL(18,5) |  |  |  |  |
| 14 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 15 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 16 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 26 | `NETTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 27 | `CALCULATEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 28 | `CURRENCYCODE` | CHAR(5) |  |  |  |  |
| 29 | `DDPAYABLEAT` | CHAR(30) |  |  |  |  |
| 30 | `SCHEMETYPEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 31 | `SCHEMETYPECODE` | CHAR(3) |  |  |  |  |
| 32 | `EXCISEINCLUSIVE` | CHAR(3) |  |  |  |  |
| 33 | `PRIMARYSUBCODE01` | CHAR(20) |  |  |  |  |
| 34 | `PRIMARYSUBCODE02` | CHAR(10) |  |  |  |  |
| 35 | `PRIMARYSUBCODE03` | CHAR(10) |  |  |  |  |
| 36 | `PRIMARYSUBCODE04` | CHAR(10) |  |  |  |  |
| 37 | `PRIMARYSUBCODE05` | CHAR(10) |  |  |  |  |
| 38 | `PRIMARYSUBCODE06` | CHAR(10) |  |  |  |  |
| 39 | `PRIMARYSUBCODE07` | CHAR(10) |  |  |  |  |
| 40 | `PRIMARYSUBCODE08` | CHAR(10) |  |  |  |  |
| 41 | `PRIMARYSUBCODE09` | CHAR(10) |  |  |  |  |
| 42 | `PRIMARYSUBCODE10` | CHAR(10) |  |  |  |  |
| 43 | `DELIVERYDATE` | DATE |  |  |  |  |
| 44 | `PODELIVERYDATE` | DATE |  |  |  |  |
| 45 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 46 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 47 | `PROPOSALDATE` | DATE |  |  |  |  |
| 48 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 49 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 50 | `HEADERCODE` | CHAR(15) |  |  |  |  |
| 51 | `NOTES` | VARCHAR(1000) |  |  |  |  |
| 52 | `DESPLANTCODE` | CHAR(8) |  |  |  |  |
| 53 | `PURCHASEORDERCOUNTER` | CHAR(8) |  |  |  |  |
| 54 | `PURCHASECODE` | CHAR(15) |  |  |  |  |
| 55 | `DIVSIONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 56 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 57 | `COMDEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 58 | `RATE` | DECIMAL(18,5) |  |  |  |  |
| 59 | `PORATE` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.LINENO,
       t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.PRODUCTIDENTIFIER,
       t.DIVISIONCODE,
       t.REPLENCOUNTER,
       t.REPLECODE,
       t.ITEMDESCRIPTION,
       t.UOM,
       t.QUANTITY,
       t.POUOM,
       t.PRODUCTUNIQUEID
FROM   DB2ADMIN.WRKNETPURCHASEORDER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
