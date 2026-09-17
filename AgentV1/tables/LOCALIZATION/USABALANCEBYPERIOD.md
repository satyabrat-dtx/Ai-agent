# DB2ADMIN.USABALANCEBYPERIOD

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 53
- **Primary key**: `COMPANYCODE`, `WAREHOUSEACCOUNTINGGROUPCODE`, `PERPERIODIZEDCALENDARTYPECODE`, `PERIODPERIODIZEDCALENDARYEAR`, `PERIODCODE`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 88134

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `PERPERIODIZEDCALENDARTYPECODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 3 | `PERIODPERIODIZEDCALENDARYEAR` | DECIMAL(4,0) | NOT NULL | PK | primary_key |  |
| 4 | `PERIODCODE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 5 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 9 | `WAREHOUSEACCOUNTINGGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
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
| 20 | `PHYSICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 21 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 22 | `WHSLOCATIONWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 23 | `WAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 24 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 25 | `LOTCODE` | CHAR(10) |  |  |  |  |
| 26 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 27 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 28 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 29 | `ELEMENTSSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 30 | `ELEMENTSCODE` | CHAR(15) |  |  |  |  |
| 31 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 32 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 33 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 34 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 35 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 36 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 37 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 38 | `DETAILTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 39 | `BASEPRIMARYUNITCODE` | CHAR(3) |  |  |  |  |
| 40 | `BASEPRIMARYQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 41 | `BASESECONDARYUNITCODE` | CHAR(3) |  |  |  |  |
| 42 | `BASESECONDARYQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 43 | `PACKAGINGCODE` | CHAR(3) |  |  |  |  |
| 44 | `PACKAGINGQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 45 | `CLOSINGBASECOST` | DECIMAL(18,5) |  |  |  |  |
| 46 | `ACTUALBASECOST` | DECIMAL(18,5) |  |  |  |  |
| 47 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 48 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 49 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 50 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 51 | `FIKDCLOSINGBASECOST` | DECIMAL(18,5) |  |  |  |  |
| 52 | `FIKDACTUALBASECOST` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `USABALANCEPER02` (PERIODCODE, WAREHOUSEACCOUNTINGGROUPCODE, PERIODPERIODIZEDCALENDARYEAR, PERPERIODIZEDCALENDARTYPECODE, COMPANYCODE)
- `USABALANCEPER03` (COMPANYCODE, PERPERIODIZEDCALENDARTYPECODE, PERIODPERIODIZEDCALENDARYEAR, PERIODCODE, ITEMTYPECODE, DECOSUBCODE01, DECOSUBCODE02, DECOSUBCODE03, DECOSUBCODE04, DECOSUBCODE05, DECOSUBCODE06, DECOSUBCODE07, DECOSUBCODE08, DECOSUBCODE09, DECOSUBCODE10, LOGICALWAREHOUSECODE, PHYSICALWAREHOUSECODE, WHSLOCATIONWAREHOUSEZONECODE, WAREHOUSELOCATIONCODE, QUALITYLEVELCODE, LOTCODE, CONTAINERITEMTYPECODE, CONTAINERSUBCODE01, CONTAINERELEMENTCODE, ELEMENTSSUBCODEKEY, ELEMENTSCODE, CUSTOMERCODE, SUPPLIERCODE, PROJECTCODE, STATISTICALGROUPCODE, STOCKTYPECODE, PACKAGINGCODE)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.NUMBERID,
       t.PERPERIODIZEDCALENDARTYPECODE,
       t.PERIODPERIODIZEDCALENDARYEAR,
       t.PERIODCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.LOGICALWAREHOUSECOMPANYCODE,
       t.LOGICALWAREHOUSECODE,
       t.WAREHOUSEACCOUNTINGGROUPCODE,
       t.DECOSUBCODE01,
       t.DECOSUBCODE02
FROM   DB2ADMIN.USABALANCEBYPERIOD t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
