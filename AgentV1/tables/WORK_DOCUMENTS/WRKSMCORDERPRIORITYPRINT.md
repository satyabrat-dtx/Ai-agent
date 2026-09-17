# DB2ADMIN.WRKSMCORDERPRIORITYPRINT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 131
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 78866

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `COMPANYDECODE` | VARCHAR(100) |  |  |  |  |
| 5 | `COMPANYGROUPCODE` | CHAR(3) |  |  |  |  |
| 6 | `COMPANYGROUPDECODE` | VARCHAR(100) |  |  |  |  |
| 7 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 8 | `LOGICALWAREHOUSEDECODE` | VARCHAR(40) |  |  |  |  |
| 9 | `AVAILABILITYWAREHOUSEGROUPCODE` | CHAR(3) |  |  |  |  |
| 10 | `AVAILABILITYWHGROUPDECODE` | VARCHAR(40) |  |  |  |  |
| 11 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 12 | `PHYSICALWAREHOUSEDECODE` | VARCHAR(40) |  |  |  |  |
| 13 | `DIVISIONCODECODE` | CHAR(3) |  |  |  |  |
| 14 | `DIVISIONDECODE` | VARCHAR(40) |  |  |  |  |
| 15 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 16 | `PLANTDECODE` | VARCHAR(40) |  |  |  |  |
| 17 | `AVAILABILITYFORMULACODE` | CHAR(3) |  |  |  |  |
| 18 | `AVAILABILITYFORMULADECODE` | VARCHAR(40) |  |  |  |  |
| 19 | `ISTANCETYPE` | CHAR(2) |  |  |  |  |
| 20 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 21 | `ISTANCECODE` | CHAR(15) |  |  |  |  |
| 22 | `ISTANCELINE` | DECIMAL(5,0) |  |  |  |  |
| 23 | `ISTANCESUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 24 | `ISTANCELINECOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 25 | `ISTANCESECONDLEVELLINE` | DECIMAL(3,0) |  |  |  |  |
| 26 | `STATUS` | CHAR(2) |  |  |  |  |
| 27 | `DUEDATE` | DATE |  |  |  |  |
| 28 | `PERIODTYPECODE` | CHAR(10) |  |  |  |  |
| 29 | `PERIODTYPEDECODE` | VARCHAR(40) |  |  |  |  |
| 30 | `PERIODYEAR` | DECIMAL(4,0) |  |  |  |  |
| 31 | `PERIODCODE` | DECIMAL(3,0) |  |  |  |  |
| 32 | `PERIODSTARTDATE` | DATE |  |  |  |  |
| 33 | `PERIODENDDATE` | DATE |  |  |  |  |
| 34 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 35 | `ITEMTYPEDECODE` | VARCHAR(40) |  |  |  |  |
| 36 | `DECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 37 | `DECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 38 | `DECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 39 | `DECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 40 | `DECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 41 | `DECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 42 | `DECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 43 | `DECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 44 | `DECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 45 | `DECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 46 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 47 | `ITEMDECODE` | VARCHAR(100) |  |  |  |  |
| 48 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 49 | `QUALITYLEVELDECODE` | VARCHAR(40) |  |  |  |  |
| 50 | `WAREHOUSELOCATIONNATURE` | INTEGER | NOT NULL |  |  |  |
| 51 | `WAREHOUSELOCATIONZONECODE` | CHAR(3) |  |  |  |  |
| 52 | `WAREHOUSELOCATIONZONEDECODE` | VARCHAR(40) |  |  |  |  |
| 53 | `WHSLOCATIONWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 54 | `WAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 55 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 56 | `CONTAINERITEMTYPEDECODE` | VARCHAR(40) |  |  |  |  |
| 57 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 58 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 59 | `LOTCODE` | CHAR(10) |  |  |  |  |
| 60 | `ELEMENTSSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 61 | `ELEMENTSCODE` | CHAR(15) |  |  |  |  |
| 62 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 63 | `PROJECTDECODE` | VARCHAR(40) |  |  |  |  |
| 64 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 65 | `STATISTICALGROUPDECODE` | VARCHAR(40) |  |  |  |  |
| 66 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 67 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 68 | `CUSTOMERDECODE` | VARCHAR(40) |  |  |  |  |
| 69 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 70 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 71 | `SUPPLIERDECODE` | VARCHAR(40) |  |  |  |  |
| 72 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 73 | `STOCKTYPEDECODE` | VARCHAR(40) |  |  |  |  |
| 74 | `BASEPRIMARYUNITCODE` | CHAR(3) |  |  |  |  |
| 75 | `BALANCEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 76 | `BALANCEPRIMARYQTYNODEC` | DECIMAL(15,0) |  |  |  |  |
| 77 | `FUTUREPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 78 | `FUTUREPRIMARYQUANTITYNODEC` | DECIMAL(15,0) |  |  |  |  |
| 79 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 80 | `BASEPRIMARYQUANTITYNODEC` | DECIMAL(15,0) |  |  |  |  |
| 81 | `BASESECONDARYUNITCODE` | CHAR(3) |  |  |  |  |
| 82 | `BALANCESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 83 | `BALANCESECONDARYQTYNODEC` | DECIMAL(15,0) |  |  |  |  |
| 84 | `FUTURESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 85 | `FUTURESECONDARYQUANTITYNODEC` | DECIMAL(15,0) |  |  |  |  |
| 86 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 87 | `BASESECONDARYQUANTITYNODEC` | DECIMAL(15,0) |  |  |  |  |
| 88 | `PACKAGINGUNITCODE` | CHAR(3) |  |  |  |  |
| 89 | `BALANCEPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 90 | `BALANCEPACKAGINGQTYNODEC` | DECIMAL(15,0) |  |  |  |  |
| 91 | `FUTUREPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 92 | `FUTUREPACKAGINGQUANTITYNODEC` | DECIMAL(15,0) |  |  |  |  |
| 93 | `PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 94 | `PACKAGINGQUANTITYNODEC` | DECIMAL(15,0) |  |  |  |  |
| 95 | `SAFETYSTOCK` | DECIMAL(15,5) |  |  |  |  |
| 96 | `SAFETYSTOCKNODEC` | DECIMAL(15,0) |  |  |  |  |
| 97 | `REORDERPOINT` | DECIMAL(15,5) |  |  |  |  |
| 98 | `REORDERPOINTNODEC` | DECIMAL(15,0) |  |  |  |  |
| 99 | `STOCKTYPEQTY1DESC` | VARCHAR(40) |  |  |  |  |
| 100 | `STOCKTYPEQTY1` | DECIMAL(15,5) |  |  |  |  |
| 101 | `STOCKTYPEQTY1NODEC` | DECIMAL(15,0) |  |  |  |  |
| 102 | `STOCKTYPEQTY2DESC` | VARCHAR(40) |  |  |  |  |
| 103 | `STOCKTYPEQTY2` | DECIMAL(15,5) |  |  |  |  |
| 104 | `STOCKTYPEQTY2NODEC` | DECIMAL(15,0) |  |  |  |  |
| 105 | `STOCKTYPEQTY3DESC` | VARCHAR(40) |  |  |  |  |
| 106 | `STOCKTYPEQTY3` | DECIMAL(15,5) |  |  |  |  |
| 107 | `STOCKTYPEQTY3NODEC` | DECIMAL(15,0) |  |  |  |  |
| 108 | `STOCKTYPEQTY4DESC` | VARCHAR(40) |  |  |  |  |
| 109 | `STOCKTYPEQTY4` | DECIMAL(15,5) |  |  |  |  |
| 110 | `STOCKTYPEQTY4NODEC` | DECIMAL(15,0) |  |  |  |  |
| 111 | `STOCKTYPEQTY5DESC` | VARCHAR(40) |  |  |  |  |
| 112 | `STOCKTYPEQTY5` | DECIMAL(15,5) |  |  |  |  |
| 113 | `STOCKTYPEQTY5NODEC` | DECIMAL(15,0) |  |  |  |  |
| 114 | `STOCKTYPEQTY6DESC` | VARCHAR(40) |  |  |  |  |
| 115 | `STOCKTYPEQTY6` | DECIMAL(15,5) |  |  |  |  |
| 116 | `STOCKTYPEQTY6NODEC` | DECIMAL(15,0) |  |  |  |  |
| 117 | `STOCKTYPEQTY7DESC` | VARCHAR(40) |  |  |  |  |
| 118 | `STOCKTYPEQTY7` | DECIMAL(15,5) |  |  |  |  |
| 119 | `STOCKTYPEQTY7NODEC` | DECIMAL(15,0) |  |  |  |  |
| 120 | `STOCKTYPEQTY8DESC` | VARCHAR(40) |  |  |  |  |
| 121 | `STOCKTYPEQTY8` | DECIMAL(15,5) |  |  |  |  |
| 122 | `STOCKTYPEQTY8NODEC` | DECIMAL(15,0) |  |  |  |  |
| 123 | `STOCKTYPEQTY9DESC` | VARCHAR(40) |  |  |  |  |
| 124 | `STOCKTYPEQTY9` | DECIMAL(15,5) |  |  |  |  |
| 125 | `STOCKTYPEQTY9NODEC` | DECIMAL(15,0) |  |  |  |  |
| 126 | `STOCKTYPEQTY10DESC` | VARCHAR(40) |  |  |  |  |
| 127 | `STOCKTYPEQTY10` | DECIMAL(15,5) |  |  |  |  |
| 128 | `STOCKTYPEQTY10NODEC` | DECIMAL(15,0) |  |  |  |  |
| 129 | `RELEASEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 130 | `PRICE` | DECIMAL(18,5) |  |  |  |  |

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
       t.COMPANYDECODE,
       t.COMPANYGROUPCODE,
       t.COMPANYGROUPDECODE,
       t.LOGICALWAREHOUSECODE,
       t.LOGICALWAREHOUSEDECODE,
       t.AVAILABILITYWAREHOUSEGROUPCODE,
       t.AVAILABILITYWHGROUPDECODE,
       t.PHYSICALWAREHOUSECODE
FROM   DB2ADMIN.WRKSMCORDERPRIORITYPRINT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
