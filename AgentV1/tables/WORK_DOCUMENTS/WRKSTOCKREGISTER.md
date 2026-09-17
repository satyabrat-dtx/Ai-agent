# DB2ADMIN.WRKSTOCKREGISTER

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 47
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 147305

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 5 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 8 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 18 | `UOM` | CHAR(3) |  |  |  |  |
| 19 | `OPENINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 20 | `CLOSINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `RECEIVEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 22 | `OPENINGVALUE` | DECIMAL(18,5) |  |  |  |  |
| 23 | `ISSUEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 24 | `CLOSINGVALUE` | DECIMAL(18,5) |  |  |  |  |
| 25 | `ISSUEDQTY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `RECEIVEDQTY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 28 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 29 | `ITEMLONGDESC` | VARCHAR(200) |  |  |  |  |
| 30 | `DIVISIONLONGDESC` | VARCHAR(200) |  |  |  |  |
| 31 | `COSTUNITVALUE` | DECIMAL(18,5) |  |  |  |  |
| 32 | `WAREHOUSEGROUPCODE` | CHAR(3) |  |  |  |  |
| 33 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 34 | `WAREHOUSEGROUPLONGDES` | VARCHAR(200) |  |  |  |  |
| 35 | `TRANSACTIONISSUEDQTY` | DECIMAL(15,5) |  |  |  |  |
| 36 | `TRANSACTIONRECEIVEDQTY` | DECIMAL(15,5) |  |  |  |  |
| 37 | `TRANSACTIONISSUEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 38 | `TRANSACTIONRECEIVEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 39 | `RECIPTFROMSUPPILERVALUE` | DECIMAL(18,5) |  |  |  |  |
| 40 | `RECIPTFROMSUPPILERQTY` | DECIMAL(15,5) |  |  |  |  |
| 41 | `ENTRYFORIDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 42 | `ENTRYFORIDQTY` | DECIMAL(15,5) |  |  |  |  |
| 43 | `ISSUEFORIDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 44 | `ISSUEFORIDQTY` | DECIMAL(15,5) |  |  |  |  |
| 45 | `ISSUEFORPRODUCTIONVALUE` | DECIMAL(18,5) |  |  |  |  |
| 46 | `ISSUEFORPRODUCTIONQTY` | DECIMAL(15,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.EXPIRATIONDATE,
       t.COMPANYCODE,
       t.LOGICALWAREHOUSECODE,
       t.PHYSICALWAREHOUSECODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05
FROM   DB2ADMIN.WRKSTOCKREGISTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
