# DB2ADMIN.WRKBILLOFEXCHANGEINVOICE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 240270

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 5 | `BILLOFEXCHANGECODE` | CHAR(12) | NOT NULL |  |  |  |
| 6 | `COMINVOICENO` | CHAR(20) |  |  |  |  |
| 7 | `INVTYPECODE` | CHAR(3) |  |  |  |  |
| 8 | `INVOICEDATE` | DATE |  |  |  |  |
| 9 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `USERPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 11 | `USERUOMCODE` | CHAR(3) |  |  |  |  |
| 12 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `TARIFFLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 14 | `SUBCODE01` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |

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
       t.BILLOFEXCHANGECODE,
       t.COMINVOICENO,
       t.INVTYPECODE,
       t.INVOICEDATE,
       t.ITEMTYPECODE,
       t.USERPRIMARYQTY,
       t.USERUOMCODE
FROM   DB2ADMIN.WRKBILLOFEXCHANGEINVOICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
