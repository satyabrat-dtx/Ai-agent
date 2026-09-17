# DB2ADMIN.BPBALANCEANALYSISREPORT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 42
- **Primary key**: `REPORT`, `PROGRESSIVE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 13097

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `REPORT` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `PROGRESSIVE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 5 | `ITEMDESCRIPTION` | CHAR(20) |  |  |  |  |
| 6 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 7 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 8 | `STATISTICALGROUPCODE` | CHAR(3) |  |  |  |  |
| 9 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 10 | `DECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 11 | `DECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 12 | `DECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 13 | `DECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 14 | `DECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 15 | `DECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 16 | `DECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 17 | `DECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 18 | `DECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 19 | `DECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 20 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 21 | `WHSLOCATIONWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 22 | `WAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 23 | `LOTCODE` | CHAR(10) |  |  |  |  |
| 24 | `MINIMUMQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `MAXIMUMQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 27 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 28 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 29 | `ELEMENTSSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 30 | `ELEMENTSCODE` | CHAR(15) |  |  |  |  |
| 31 | `ENTRYDOCUMENTDATE` | DATE |  |  |  |  |
| 32 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 33 | `STOCKTYPEDESCRIPTION` | CHAR(20) |  |  |  |  |
| 34 | `ANALYSISUOMCODE` | CHAR(3) |  |  |  |  |
| 35 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 36 | `BASEPRIMARYUNITCODE` | CHAR(3) |  |  |  |  |
| 37 | `BASEPRIMARYQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 38 | `BASESECONDARYUNITCODE` | CHAR(3) |  |  |  |  |
| 39 | `BASESECONDARYQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 40 | `PACKAGINGCODE` | CHAR(3) |  |  |  |  |
| 41 | `PACKAGINGQUANTITYUNIT` | DECIMAL(15,0) |  |  |  |  |

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
       t.ITEMCODE,
       t.ITEMDESCRIPTION,
       t.PHYSICALWAREHOUSECODE,
       t.PROJECTCODE,
       t.STATISTICALGROUPCODE,
       t.LOGICALWAREHOUSECODE,
       t.DECOSUBCODE01,
       t.DECOSUBCODE02
FROM   DB2ADMIN.BPBALANCEANALYSISREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
