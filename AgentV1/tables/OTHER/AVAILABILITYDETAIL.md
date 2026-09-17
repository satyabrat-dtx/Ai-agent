# DB2ADMIN.AVAILABILITYDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 45
- **Primary key**: `COMPANYCODE`, `IDENTIFIER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 15385

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IDENTIFIER` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `DETAILDATE` | DATE | NOT NULL |  |  |  |
| 3 | `DUEDATE` | DATE |  |  |  |  |
| 4 | `DETAILTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 5 | `STOCKTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL |  |  |  |
| 7 | `ITEMTYPEAFICODE` | CHAR(3) | NOT NULL |  |  |  |
| 8 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 9 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 19 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 20 | `WHSLOCATIONWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 21 | `WAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 22 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 23 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 24 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 25 | `LOTCODE` | CHAR(10) |  |  |  |  |
| 26 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 27 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 28 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 29 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 30 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 31 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 32 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 33 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 34 | `BASEPRIMARYUNITCODE` | CHAR(3) | NOT NULL |  |  |  |
| 35 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 36 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 37 | `BASESECONDARYUNITCODE` | CHAR(3) |  |  |  |  |
| 38 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 39 | `PACKAGINGCODE` | CHAR(3) |  |  |  |  |
| 40 | `PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 41 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 42 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 43 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 44 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IDENTIFIER,
       t.DETAILDATE,
       t.DUEDATE,
       t.DETAILTYPE,
       t.STOCKTYPECODE,
       t.LOGICALWAREHOUSECODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04
FROM   DB2ADMIN.AVAILABILITYDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
