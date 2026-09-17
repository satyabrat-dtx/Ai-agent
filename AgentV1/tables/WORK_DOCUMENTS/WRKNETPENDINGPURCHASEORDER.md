# DB2ADMIN.WRKNETPENDINGPURCHASEORDER

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 32
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 239991

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 5 | `SUPPLIERNAME` | VARCHAR(270) |  |  |  |  |
| 6 | `ORDERDATE` | DATE |  |  |  |  |
| 7 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
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
| 18 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 19 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 20 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `CANCELLEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `DELIVERYDATE` | DATE |  |  |  |  |
| 23 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 24 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 25 | `POLINEUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `GROSSVALUEEXT` | DECIMAL(18,5) |  |  |  |  |
| 27 | `DIVISIONDESC` | VARCHAR(200) |  |  |  |  |
| 28 | `DELIVERYPURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 29 | `DELIVERYPURCHASEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 30 | `DELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 31 | `POLINEITEMDESC` | VARCHAR(200) |  |  |  |  |

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
       t.SUPPLIERCODE,
       t.SUPPLIERNAME,
       t.ORDERDATE,
       t.CURRENCYCODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04
FROM   DB2ADMIN.WRKNETPENDINGPURCHASEORDER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
