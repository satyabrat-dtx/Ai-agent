# DB2ADMIN.BOMANALYSISEXPLOSIONREPORT

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'BOM')
- **Roles**: `business_data`
- **Columns**: 77
- **Primary key**: `REPORT`, `PROGRESSIVE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 2379

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `REPORT` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `PROGRESSIVE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `INDLEVEL` | INTEGER | NOT NULL |  |  |  |
| 3 | `OWNEDCOMPONENT` | CHAR(2) | NOT NULL |  |  |  |
| 4 | `BILLOFMATERIALCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `BILLOFMATERIALNUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 6 | `BILLOFMATERIALITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `BILLOFMATERIALSUBCODE01` | CHAR(20) | NOT NULL |  |  |  |
| 8 | `BILLOFMATERIALSUBCODE02` | CHAR(10) |  |  |  |  |
| 9 | `BILLOFMATERIALSUBCODE03` | CHAR(10) |  |  |  |  |
| 10 | `BILLOFMATERIALSUBCODE04` | CHAR(10) |  |  |  |  |
| 11 | `BILLOFMATERIALSUBCODE05` | CHAR(10) |  |  |  |  |
| 12 | `BILLOFMATERIALSUBCODE06` | CHAR(10) |  |  |  |  |
| 13 | `BILLOFMATERIALSUBCODE07` | CHAR(10) |  |  |  |  |
| 14 | `BILLOFMATERIALSUBCODE08` | CHAR(10) |  |  |  |  |
| 15 | `BILLOFMATERIALSUBCODE09` | CHAR(10) |  |  |  |  |
| 16 | `BILLOFMATERIALSUBCODE10` | CHAR(10) |  |  |  |  |
| 17 | `BILLOFMATERIALSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 18 | `SEQUENCE` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 19 | `SUBSEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 20 | `COMPONENTINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 21 | `REFBOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 22 | `BOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 23 | `BOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 24 | `BOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 25 | `BOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 26 | `BOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 27 | `BOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 28 | `BOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 29 | `BOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 30 | `BOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 31 | `BOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 32 | `REFBOMSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 33 | `REFBOMSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 34 | `REFBOMSUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 35 | `REFBOMSTATUS` | CHAR(2) |  |  |  |  |
| 36 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 37 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 38 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 39 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 40 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 41 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 42 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 43 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 44 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 45 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 46 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 47 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 48 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 49 | `CALCULATEQTYCODE` | CHAR(20) |  |  |  |  |
| 50 | `ASSEMBLYUOMCODE` | CHAR(3) |  |  |  |  |
| 51 | `COMPONENTUOMCODE` | CHAR(3) |  |  |  |  |
| 52 | `QUANTITYPER` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 53 | `COMPONENTQTY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 54 | `AVAILABLEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 55 | `DELTAQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 56 | `ASSEMBLYQTYADJPRC` | DECIMAL(5,2) |  |  |  |  |
| 57 | `ASSEMBLYFIXLEADTIMEADJ` | DECIMAL(10,5) |  |  |  |  |
| 58 | `ASSEMBLYVARLEADTIMEADJ` | DECIMAL(10,5) |  |  |  |  |
| 59 | `SUBCONTRACTORSUPPLYTYPE` | CHAR(2) |  |  |  |  |
| 60 | `CUSTOMERSUPPLYTYPE` | CHAR(2) |  |  |  |  |
| 61 | `PRODUCTIONRESERVATIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 62 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 63 | `RESERVATIONWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 64 | `REFERENCEITEM` | CHAR(2) |  |  |  |  |
| 65 | `WASTETYPE1` | CHAR(2) |  |  |  |  |
| 66 | `WASTE1` | DECIMAL(11,2) |  |  |  |  |
| 67 | `WASTETYPE2` | CHAR(2) |  |  |  |  |
| 68 | `WASTE2` | DECIMAL(11,2) |  |  |  |  |
| 69 | `CONFIGURATIONRULE` | CHAR(3) |  |  |  |  |
| 70 | `INITIALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 71 | `FINALENGINEERINGCHANGE` | DECIMAL(11,0) |  |  |  |  |
| 72 | `INITIALDATE` | DATE |  |  |  |  |
| 73 | `FINALDATE` | DATE |  |  |  |  |
| 74 | `BILLOFMATITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 75 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 76 | `RESERVATIONWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.REPORT,
       t.PROGRESSIVE,
       t.INDLEVEL,
       t.OWNEDCOMPONENT,
       t.BILLOFMATERIALCOMPANYCODE,
       t.BILLOFMATERIALNUMBERID,
       t.BILLOFMATERIALITEMTYPECODE,
       t.BILLOFMATERIALSUBCODE01,
       t.BILLOFMATERIALSUBCODE02,
       t.BILLOFMATERIALSUBCODE03,
       t.BILLOFMATERIALSUBCODE04,
       t.BILLOFMATERIALSUBCODE05
FROM   DB2ADMIN.BOMANALYSISEXPLOSIONREPORT t
FETCH FIRST 100 ROWS ONLY;
```
