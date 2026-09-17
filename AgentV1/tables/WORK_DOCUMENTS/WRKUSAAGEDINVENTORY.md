# DB2ADMIN.WRKUSAAGEDINVENTORY

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 91
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 88455

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 3 | `WHSACCOUNTINGGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `WAREHOUSEACCOUNTINGGROUPCODE` | CHAR(3) |  |  |  |  |
| 5 | `PERPERIODIZEDCALENDARTYPECODE` | CHAR(10) |  |  |  |  |
| 6 | `PERIODPERIODIZEDCALENDARYEAR` | DECIMAL(4,0) |  |  |  |  |
| 7 | `PERIODCODE` | DECIMAL(3,0) |  |  |  |  |
| 8 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 9 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 12 | `DECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 13 | `DECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 14 | `DECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 15 | `DECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 16 | `DECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 17 | `DECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 18 | `DECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 19 | `DECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 20 | `DECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 21 | `DECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 22 | `PHYSICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 24 | `WHSLOCWHSZONEPHYWHSCMYCODE` | CHAR(3) |  |  |  |  |
| 25 | `WHSLOCATIONWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 26 | `WAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 27 | `QUALITYLVLITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 28 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 29 | `LOTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 30 | `LOTCODE` | CHAR(10) |  |  |  |  |
| 31 | `CONTAINERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 32 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 33 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 34 | `CONTAINERELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 35 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 36 | `ELEMENTSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 37 | `ELEMENTSSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 38 | `ELEMENTSCODE` | CHAR(15) |  |  |  |  |
| 39 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 40 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 41 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 42 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 43 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 44 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 45 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 46 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 47 | `BASEPRIMARYUNITCODE` | CHAR(3) |  |  |  |  |
| 48 | `BASEPRIMARYQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 49 | `BASESECONDARYUNITCODE` | CHAR(3) |  |  |  |  |
| 50 | `BASESECONDARYQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 51 | `PACKAGINGCODE` | CHAR(3) |  |  |  |  |
| 52 | `PACKAGINGQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 53 | `CLOSINGBASECOST` | DECIMAL(18,5) |  |  |  |  |
| 54 | `ACTUALBASECOST` | DECIMAL(18,5) |  |  |  |  |
| 55 | `CATEGORYLEVEL` | INTEGER | NOT NULL |  |  |  |
| 56 | `CAT0PRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 57 | `CAT0SECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 58 | `CAT0PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 59 | `CAT1PRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 60 | `CAT1SECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 61 | `CAT1PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 62 | `CAT2PRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 63 | `CAT2SECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 64 | `CAT2PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 65 | `CAT3PRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 66 | `CAT3SECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 67 | `CAT3PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 68 | `CAT4PRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 69 | `CAT4SECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 70 | `CAT4PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 71 | `CAT5PRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 72 | `CAT5SECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 73 | `CAT5PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 74 | `NEXTPERPERIODIZEDCALENDARYEAR` | DECIMAL(4,0) |  |  |  |  |
| 75 | `NEXTPERIODCODE` | DECIMAL(3,0) |  |  |  |  |
| 76 | `CAT6PRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 77 | `CAT6SECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 78 | `CAT6PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 79 | `CAT7PRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 80 | `CAT7SECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 81 | `CAT7PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 82 | `CAT8PRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 83 | `CAT8SECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 84 | `CAT8PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 85 | `CAT9PRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 86 | `CAT9SECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 87 | `CAT9PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 88 | `CAT10PRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 89 | `CAT10SECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 90 | `CAT10PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.NUMBERID,
       t.WHSACCOUNTINGGROUPCOMPANYCODE,
       t.WAREHOUSEACCOUNTINGGROUPCODE,
       t.PERPERIODIZEDCALENDARTYPECODE,
       t.PERIODPERIODIZEDCALENDARYEAR,
       t.PERIODCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.LOGICALWAREHOUSECOMPANYCODE,
       t.LOGICALWAREHOUSECODE
FROM   DB2ADMIN.WRKUSAAGEDINVENTORY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
