# DB2ADMIN.WRKWASHLIST

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 107
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `NUMBERID`, `ITEMTYPECODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`, `LOGICALWAREHOUSECODE`, `LOTCODE`, `CONTAINERITEMTYPECODE`, `CONTAINERSUBCODE01`, `CONTAINERELEMENTSCODE`, `ELEMENTSSUBCODEKEY`, `ELEMENTSCODE`, `PACKAGINGCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 132023

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 5 | `SUBCODE02` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 6 | `SUBCODE03` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE04` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE06` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE07` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE08` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE09` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `SUBCODE10` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 14 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 15 | `LOTCODE` | CHAR(35) | NOT NULL | PK | primary_key |  |
| 16 | `CONTAINERITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 17 | `CONTAINERSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 18 | `CONTAINERELEMENTSCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 19 | `ELEMENTSSUBCODEKEY` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 20 | `ELEMENTSCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 21 | `PACKAGINGCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 22 | `BASEPRIMARYQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 23 | `SETCODENO` | CHAR(12) |  |  |  |  |
| 24 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 25 | `PCS` | INTEGER | NOT NULL |  |  |  |
| 26 | `DPT` | INTEGER | NOT NULL |  |  |  |
| 27 | `DPTSQD` | DECIMAL(6,2) |  |  |  |  |
| 28 | `FOURPTDHLM` | DECIMAL(6,2) |  |  |  |  |
| 29 | `WIDTHGROSS` | DECIMAL(7,2) |  |  |  |  |
| 30 | `UNWASHSHADE` | CHAR(3) |  |  |  |  |
| 31 | `TAPPERGRP` | CHAR(3) |  |  |  |  |
| 32 | `TAPPERNO` | INTEGER | NOT NULL |  |  |  |
| 33 | `WASHINGLISTNO` | CHAR(12) |  |  |  |  |
| 34 | `WASHTYPE` | CHAR(8) |  |  |  |  |
| 35 | `STATUSCODE` | CHAR(3) |  |  |  |  |
| 36 | `L` | DECIMAL(6,2) |  |  |  |  |
| 37 | `A` | DECIMAL(6,2) |  |  |  |  |
| 38 | `B` | DECIMAL(6,2) |  |  |  |  |
| 39 | `DL` | DECIMAL(6,2) |  |  |  |  |
| 40 | `DA` | DECIMAL(6,2) |  |  |  |  |
| 41 | `DB` | DECIMAL(6,2) |  |  |  |  |
| 42 | `DECMCSTD` | DECIMAL(6,2) |  |  |  |  |
| 43 | `TAGNO` | CHAR(4) |  |  |  |  |
| 44 | `INSTOCK` | CHAR(1) |  |  |  |  |
| 45 | `VISUALGROUPING` | CHAR(1) |  |  |  |  |
| 46 | `CUSTOMERNAME` | CHAR(25) |  |  |  |  |
| 47 | `AUDITCLEARANCE` | CHAR(1) |  |  |  |  |
| 48 | `PHYSICALDATACLEARANCE` | CHAR(1) |  |  |  |  |
| 49 | `CSVCLEARANCE` | CHAR(1) |  |  |  |  |
| 50 | `QAVISUALCLEARANCE` | CHAR(1) |  |  |  |  |
| 51 | `CUTTABLESTD` | CHAR(7) |  |  |  |  |
| 52 | `CUTTABLE` | DECIMAL(7,2) |  |  |  |  |
| 53 | `SHNKLENSTD` | CHAR(7) |  |  |  |  |
| 54 | `SHNKLEN` | DECIMAL(7,2) |  |  |  |  |
| 55 | `SHNKWIDSTD` | CHAR(7) |  |  |  |  |
| 56 | `SHNKWID` | DECIMAL(7,2) |  |  |  |  |
| 57 | `SKEWUASTD` | CHAR(7) |  |  |  |  |
| 58 | `SKEWUA` | DECIMAL(7,2) |  |  |  |  |
| 59 | `SKEWUBSTD` | CHAR(7) |  |  |  |  |
| 60 | `SKEWUB` | DECIMAL(7,2) |  |  |  |  |
| 61 | `SKEWWASTD` | CHAR(7) |  |  |  |  |
| 62 | `SKEWWA` | DECIMAL(7,2) |  |  |  |  |
| 63 | `SKEWWBSTD` | CHAR(7) |  |  |  |  |
| 64 | `SKEWWB` | DECIMAL(7,2) |  |  |  |  |
| 65 | `EPISTD` | CHAR(7) |  |  |  |  |
| 66 | `EPI` | DECIMAL(7,2) |  |  |  |  |
| 67 | `PPISTD` | CHAR(7) |  |  |  |  |
| 68 | `PPI` | DECIMAL(7,2) |  |  |  |  |
| 69 | `WOZSSTD` | CHAR(7) |  |  |  |  |
| 70 | `WOZS` | DECIMAL(7,2) |  |  |  |  |
| 71 | `STNESSSTD` | CHAR(7) |  |  |  |  |
| 72 | `STNESS` | DECIMAL(7,2) |  |  |  |  |
| 73 | `OVERALLSTD` | CHAR(7) |  |  |  |  |
| 74 | `OVERALL` | DECIMAL(7,2) |  |  |  |  |
| 75 | `TENSWPSTD` | CHAR(7) |  |  |  |  |
| 76 | `TENSWP` | DECIMAL(7,2) |  |  |  |  |
| 77 | `TENSWFSTD` | CHAR(7) |  |  |  |  |
| 78 | `TENSWF` | DECIMAL(7,2) |  |  |  |  |
| 79 | `TEARWPSTD` | CHAR(7) |  |  |  |  |
| 80 | `TEARWP` | DECIMAL(7,2) |  |  |  |  |
| 81 | `TEARWFSTD` | CHAR(7) |  |  |  |  |
| 82 | `TEARWF` | DECIMAL(7,2) |  |  |  |  |
| 83 | `DRYSTD` | CHAR(7) |  |  |  |  |
| 84 | `DRY` | DECIMAL(7,2) |  |  |  |  |
| 85 | `WETSTD` | CHAR(7) |  |  |  |  |
| 86 | `WET` | DECIMAL(7,2) |  |  |  |  |
| 87 | `STRETCHSTD` | CHAR(7) |  |  |  |  |
| 88 | `STRETCH` | DECIMAL(7,2) |  |  |  |  |
| 89 | `GROWTHSTD` | CHAR(7) |  |  |  |  |
| 90 | `GROWTH` | DECIMAL(7,2) |  |  |  |  |
| 91 | `PHSTD` | CHAR(7) |  |  |  |  |
| 92 | `PH` | DECIMAL(7,2) |  |  |  |  |
| 93 | `ELONGATIONSTD` | CHAR(7) |  |  |  |  |
| 94 | `ELONGATION` | DECIMAL(7,2) |  |  |  |  |
| 95 | `MOVEMENTASTD` | CHAR(7) |  |  |  |  |
| 96 | `MOVEMENTA` | DECIMAL(7,2) |  |  |  |  |
| 97 | `MOVEMENTBSTD` | CHAR(7) |  |  |  |  |
| 98 | `MOVEMENTB` | DECIMAL(7,2) |  |  |  |  |
| 99 | `FABRICAPPSTD` | CHAR(7) |  |  |  |  |
| 100 | `FABRICAPP` | DECIMAL(7,2) |  |  |  |  |
| 101 | `UNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 102 | `FLAGCHECKED` | INTEGER | NOT NULL |  |  |  |
| 103 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 104 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 105 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 106 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.NUMBERID,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.WRKWASHLIST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
