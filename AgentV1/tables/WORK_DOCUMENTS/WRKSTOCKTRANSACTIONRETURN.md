# DB2ADMIN.WRKSTOCKTRANSACTIONRETURN

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 55
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `CREATIONUSER`, `LINENO`, `ITEMTYPECODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 147426

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `ITEMELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 5 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 6 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 8 | `CONTAINERELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 9 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 10 | `BASEPRIMARYUNITCODE` | CHAR(3) |  |  |  |  |
| 11 | `BASEPRIMARYQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 12 | `BASESECONDARYUNITCODE` | CHAR(3) |  |  |  |  |
| 13 | `PRODUCTCODE` | CHAR(140) |  |  |  |  |
| 14 | `PRODUCTDESC` | CHAR(100) |  |  |  |  |
| 15 | `TRANSACTIONDATE` | DATE |  |  |  |  |
| 16 | `BASESECONDARYQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 17 | `PACKAGINGCODE` | CHAR(3) |  |  |  |  |
| 18 | `TRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 19 | `PACKAGINGQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 20 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 21 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 22 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 24 | `PHYSICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 25 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 26 | `WHSZONEPHYWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 27 | `WAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 28 | `WHSLOCWHSZONEPHYWHSCMYCODE` | CHAR(3) |  |  |  |  |
| 29 | `WAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 30 | `DISTRIBUTERNAME` | CHAR(15) |  |  |  |  |
| 31 | `SHADELOT` | CHAR(20) |  |  |  |  |
| 32 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 33 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 34 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 35 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 36 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 37 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 38 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 39 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 40 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 41 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 42 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 43 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 44 | `TRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 45 | `SUPPLIERCODE` | CHAR(20) |  |  |  |  |
| 46 | `STOCKTRANSACTIONTYPE` | CHAR(20) |  |  |  |  |
| 47 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 48 | `FLAGCHECKED` | INTEGER | NOT NULL |  |  |  |
| 49 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 50 | `QUANTITYTOMODIFY` | CHAR(1) |  |  |  |  |
| 51 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 52 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 53 | `TAXTEMPLATEDETAILTEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 54 | `TAXTEMPLATEDETAILCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.LINENO,
       t.ITEMTYPECODE,
       t.ITEMELEMENTCOMPANYCODE,
       t.ITEMELEMENTSUBCODEKEY,
       t.ITEMELEMENTCODE,
       t.CONTAINERITEMTYPECODE,
       t.CONTAINERSUBCODE01,
       t.CONTAINERELEMENTCOMPANYCODE,
       t.CONTAINERELEMENTCODE,
       t.BASEPRIMARYUNITCODE,
       t.BASEPRIMARYQUANTITYUNIT
FROM   DB2ADMIN.WRKSTOCKTRANSACTIONRETURN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
