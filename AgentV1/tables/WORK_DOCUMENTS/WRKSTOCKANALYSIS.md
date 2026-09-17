# DB2ADMIN.WRKSTOCKANALYSIS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 51
- **Primary key**: `COMPANYCODE`, `SERIAL`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 126131

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISION` | CHAR(3) |  |  |  |  |
| 3 | `PLANT` | CHAR(8) |  |  |  |  |
| 4 | `SERIAL` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `ANALYSISTYPE` | CHAR(6) | NOT NULL |  |  |  |
| 6 | `CUSTOMER` | CHAR(8) |  |  |  |  |
| 7 | `FINALCUSTNATN` | CHAR(3) |  |  |  |  |
| 8 | `BUSINESSGROUP` | CHAR(10) |  |  |  |  |
| 9 | `BUSINESSUNIT` | CHAR(10) |  |  |  |  |
| 10 | `WAREHOUSE` | CHAR(8) | NOT NULL |  |  |  |
| 11 | `ITEMTYPE` | CHAR(3) | NOT NULL |  |  |  |
| 12 | `TEMPLATE` | CHAR(4) |  |  |  |  |
| 13 | `CURRENCY` | CHAR(4) | NOT NULL |  |  |  |
| 14 | `LOT` | CHAR(10) |  |  |  |  |
| 15 | `CONTAINER` | CHAR(20) |  |  |  |  |
| 16 | `ELEMENT` | CHAR(15) |  |  |  |  |
| 17 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 18 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `AGEDAYS` | INTEGER | NOT NULL |  |  |  |
| 28 | `PHYSICALWAREHOUSE` | CHAR(8) | NOT NULL |  |  |  |
| 29 | `PRODUCTMAINGRP` | CHAR(30) |  |  |  |  |
| 30 | `PRDMNGRPDESC` | VARCHAR(200) |  |  |  |  |
| 31 | `PRODUCTSUBGRP1` | CHAR(30) |  |  |  |  |
| 32 | `PRDSBGRP1DESC` | VARCHAR(200) |  |  |  |  |
| 33 | `PRODUCTSUBGRP2` | CHAR(30) |  |  |  |  |
| 34 | `PRDSBGRP2DESC` | VARCHAR(200) |  |  |  |  |
| 35 | `PRODUCTSUBGRP3` | CHAR(30) |  |  |  |  |
| 36 | `PRDSBGRP3DESC` | VARCHAR(200) |  |  |  |  |
| 37 | `PRODUCTSUBGRP4` | CHAR(30) |  |  |  |  |
| 38 | `PRDSBGRP4DESC` | VARCHAR(200) |  |  |  |  |
| 39 | `BASEPRIMARYUOM` | CHAR(3) | NOT NULL |  |  |  |
| 40 | `BASESECONDARYUM` | CHAR(3) |  |  |  |  |
| 41 | `PACKAGINGUOM` | CHAR(3) |  |  |  |  |
| 42 | `QUALITYLEVEL` | DECIMAL(2,0) | NOT NULL |  |  |  |
| 43 | `LASTUPDATEDATE` | DATE | NOT NULL |  |  |  |
| 44 | `LASTUPDATETIME` | CHAR(12) | NOT NULL |  |  |  |
| 45 | `DATEUPTO` | DATE | NOT NULL |  |  |  |
| 46 | `CLOSINGQTYBP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 47 | `CLOSINGQTYBS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 48 | `CLOSINGQTYUPM` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 49 | `PROVBSCOST` | DECIMAL(18,5) |  |  |  |  |
| 50 | `CLOSINGAMT` | DECIMAL(18,5) | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.DIVISION,
       t.PLANT,
       t.SERIAL,
       t.ANALYSISTYPE,
       t.CUSTOMER,
       t.FINALCUSTNATN,
       t.BUSINESSGROUP,
       t.BUSINESSUNIT,
       t.WAREHOUSE,
       t.ITEMTYPE
FROM   DB2ADMIN.WRKSTOCKANALYSIS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
