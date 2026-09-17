# DB2ADMIN.BALANCEANALYSISREPORT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 47
- **Primary key**: `REPORT`, `PROGRESSIVE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 1404

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `REPORT` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `PROGRESSIVE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `DECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 5 | `DECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 6 | `DECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 7 | `DECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 8 | `DECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 9 | `DECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 10 | `DECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 11 | `DECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 12 | `DECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 13 | `DECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 14 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 15 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 16 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 17 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 18 | `STATISTICALGROUPCODE` | CHAR(3) |  |  |  |  |
| 19 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 20 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 21 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 22 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 23 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 24 | `BALANCEDATE` | DATE |  |  |  |  |
| 25 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 26 | `WHSLOCATIONWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 27 | `WAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 28 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 29 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 30 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 31 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 32 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 33 | `ELEMENTSSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 34 | `ELEMENTSCODE` | CHAR(15) |  |  |  |  |
| 35 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 36 | `STOCKTYPEDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 37 | `ANALYSISUOMCODE` | CHAR(3) |  |  |  |  |
| 38 | `QUANTITYDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 39 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 40 | `BASEPRIMARYUNITCODE` | CHAR(3) |  |  |  |  |
| 41 | `BASEPRIMARYQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 42 | `BASESECONDARYUNITCODE` | CHAR(3) |  |  |  |  |
| 43 | `BASESECONDARYQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 44 | `PACKAGINGCODE` | CHAR(3) |  |  |  |  |
| 45 | `PACKAGINGQUANTITYUNIT` | DECIMAL(15,0) |  |  |  |  |
| 46 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.REPORT,
       t.PROGRESSIVE,
       t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.DECOSUBCODE01,
       t.DECOSUBCODE02,
       t.DECOSUBCODE03,
       t.DECOSUBCODE04,
       t.DECOSUBCODE05,
       t.DECOSUBCODE06,
       t.DECOSUBCODE07,
       t.DECOSUBCODE08
FROM   DB2ADMIN.BALANCEANALYSISREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
