# DB2ADMIN.WRKYARNDASHBOARD

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 83
- **Primary key**: `VIEWTYPE`, `VIEWSUBTYPE`, `COMPANYCODE`, `COUNTERCODE`, `CODE`, `STEPNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 132170

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `VIEWTYPE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 1 | `VIEWSUBTYPE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `STEPNUMBER` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 7 | `SUBUNITCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `SUBUNITCODE` | CHAR(8) |  |  |  |  |
| 9 | `UNITNAME` | VARCHAR(200) |  |  |  |  |
| 10 | `OLDUNIT` | VARCHAR(200) |  |  |  |  |
| 11 | `MIXINGLINENOCODE` | CHAR(8) |  |  |  |  |
| 12 | `SALESORDERDATE` | DATE |  |  |  |  |
| 13 | `SEGMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 14 | `SEGMENTCODE` | CHAR(6) |  |  |  |  |
| 15 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 16 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 17 | `CUSTOMERNAME` | VARCHAR(200) |  |  |  |  |
| 18 | `DESTINATION` | CHAR(100) |  |  |  |  |
| 19 | `PRDGRPUSGENGRPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `PRDGRPUSGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 21 | `PRODUCTGROUPCODE` | CHAR(10) |  |  |  |  |
| 22 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 24 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 25 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `PRODUCTCODE` | CHAR(120) |  |  |  |  |
| 35 | `ACTUALCOUNT` | CHAR(30) |  |  |  |  |
| 36 | `SALESORDERQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 37 | `DEMANDDATE` | DATE |  |  |  |  |
| 38 | `DEMANDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 39 | `POCREATIONDATE` | TIMESTAMP |  |  |  |  |
| 40 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 41 | `STEPPROGRESSQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 42 | `PRODUCEDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 43 | `QUANTITYINSTOCK` | DECIMAL(15,5) |  |  |  |  |
| 44 | `SINGLEYARNSTARTDATE` | DATE |  |  |  |  |
| 45 | `SINGLEYARNFINISHDATE` | DATE |  |  |  |  |
| 46 | `DOUBLEYARNSTARTDATE` | DATE |  |  |  |  |
| 47 | `DOUBLEYARNFINISHDATE` | DATE |  |  |  |  |
| 48 | `REFERENCELOTNO` | CHAR(35) |  |  |  |  |
| 49 | `LOTNO` | CHAR(35) |  |  |  |  |
| 50 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 51 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 52 | `PRICEBASISCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 53 | `PRICEBASISCODE` | CHAR(3) |  |  |  |  |
| 54 | `PACKAGE` | CHAR(1) |  |  |  |  |
| 55 | `CONEANGLE` | CHAR(20) |  |  |  |  |
| 56 | `PACKINGTYPE` | CHAR(1) |  |  |  |  |
| 57 | `SUBPACKINGTYPE` | CHAR(1) |  |  |  |  |
| 58 | `STUFFINGDETAIL` | CHAR(20) |  |  |  |  |
| 59 | `PACKINGREMARKS` | CHAR(50) |  |  |  |  |
| 60 | `CONEITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 61 | `CONEITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 62 | `CONESUBCODE01` | CHAR(20) |  |  |  |  |
| 63 | `CONESUBCODE02` | CHAR(10) |  |  |  |  |
| 64 | `CONESUBCODE03` | CHAR(10) |  |  |  |  |
| 65 | `CONESUBCODE04` | CHAR(10) |  |  |  |  |
| 66 | `CONESUBCODE05` | CHAR(10) |  |  |  |  |
| 67 | `CONESUBCODE06` | CHAR(10) |  |  |  |  |
| 68 | `CONESUBCODE07` | CHAR(10) |  |  |  |  |
| 69 | `CONESUBCODE08` | CHAR(10) |  |  |  |  |
| 70 | `CONESUBCODE09` | CHAR(10) |  |  |  |  |
| 71 | `CONESUBCODE10` | CHAR(10) |  |  |  |  |
| 72 | `HASATTACHMENT` | SMALLINT | NOT NULL |  |  |  |
| 73 | `COMMENT1` | CHAR(50) |  |  |  |  |
| 74 | `COMMENT2` | CHAR(50) |  |  |  |  |
| 75 | `COMMENT3` | CHAR(50) |  |  |  |  |
| 76 | `COMMENT4` | CHAR(50) |  |  |  |  |
| 77 | `COMMENT5` | CHAR(50) |  |  |  |  |
| 78 | `COMMISSION` | DECIMAL(18,5) |  |  |  |  |
| 79 | `DOMESTICFREIGHT` | CHAR(20) |  |  |  |  |
| 80 | `LCTENURE` | VARCHAR(80) |  |  |  |  |
| 81 | `OCEANFREIGHT` | CHAR(20) |  |  |  |  |
| 82 | `WARNING` | CHAR(100) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.VIEWTYPE,
       t.VIEWSUBTYPE,
       t.COMPANYCODE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.STEPNUMBER,
       t.SUBUNITCOMPANYCODE,
       t.SUBUNITCODE,
       t.UNITNAME,
       t.OLDUNIT,
       t.MIXINGLINENOCODE
FROM   DB2ADMIN.WRKYARNDASHBOARD t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
