# DB2ADMIN.WRKPRODUCTIONANALYSIS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 67
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `SERIAL`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 125867

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISION` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `PLANT` | CHAR(8) |  |  |  |  |
| 4 | `SERIAL` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `ANALYSISTYPE` | CHAR(6) | NOT NULL |  |  |  |
| 6 | `CUSTOMER` | CHAR(8) | NOT NULL |  |  |  |
| 7 | `BUSINESSGROUP` | CHAR(10) |  |  |  |  |
| 8 | `BUSINESSUNIT` | CHAR(10) |  |  |  |  |
| 9 | `WAREHOUSE` | CHAR(8) |  |  |  |  |
| 10 | `ITEMTYPE` | CHAR(3) | NOT NULL |  |  |  |
| 11 | `TEMPLATE` | CHAR(4) | NOT NULL |  |  |  |
| 12 | `WORKCENTERGROUP` | CHAR(3) | NOT NULL |  |  |  |
| 13 | `WORKCENTER` | CHAR(8) |  |  |  |  |
| 14 | `FLAG` | CHAR(1) |  |  |  |  |
| 15 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 16 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `PRODUCTMAINGRP` | CHAR(30) |  |  |  |  |
| 26 | `PRDMNGRPDESC` | VARCHAR(200) |  |  |  |  |
| 27 | `PRODUCTSUBGRP1` | CHAR(30) |  |  |  |  |
| 28 | `PRDSBGRP1DESC` | VARCHAR(200) |  |  |  |  |
| 29 | `PRODUCTSUBGRP2` | CHAR(30) |  |  |  |  |
| 30 | `PRDSBGRP2DESC` | VARCHAR(200) |  |  |  |  |
| 31 | `PRODUCTSUBGRP3` | CHAR(30) |  |  |  |  |
| 32 | `PRDSBGRP3DESC` | VARCHAR(200) |  |  |  |  |
| 33 | `PRODUCTSUBGRP4` | CHAR(30) |  |  |  |  |
| 34 | `PRDSBGRP4DESC` | VARCHAR(200) |  |  |  |  |
| 35 | `BASEPRIMARYUOM` | CHAR(3) | NOT NULL |  |  |  |
| 36 | `USERPRIMARYUOM` | CHAR(3) |  |  |  |  |
| 37 | `USERSECONDARYUM` | CHAR(3) |  |  |  |  |
| 38 | `BASESECONDARYUM` | CHAR(3) |  |  |  |  |
| 39 | `PACKAGINGUOM` | CHAR(3) |  |  |  |  |
| 40 | `QUALITYLEVEL` | DECIMAL(2,0) | NOT NULL |  |  |  |
| 41 | `MONTHLYTGT` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 42 | `NOOFDAYS` | INTEGER | NOT NULL |  |  |  |
| 43 | `TODAYTARGETQTYBP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 44 | `TODAYTARGETQTYUP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 45 | `TODAYTARGETQTYBS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 46 | `TODAYTARGETQTYUS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 47 | `TODAYTARGETQTYUPK` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 48 | `TODAYACTUALQTYUPK` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 49 | `TODAYACTUALQTYUS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 50 | `TODAYACTUALQTYBS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 51 | `TODAYACTUALQTYUP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 52 | `TODAYACTUALQTYBP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 53 | `UPTODATETARGETQTYUP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 54 | `UPTODATETARGETQTYBS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 55 | `UPTODATETARGETQTYUS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 56 | `UPTODATETARGETQTYUPK` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 57 | `UPTODATETARGETQTYBP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 58 | `UPTODATEACTUALQTYUP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 59 | `UPTODATEACTUALQTYBS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 60 | `UPTODATEACTUALQTYUS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 61 | `UPTODATEACTUALQTYUPK` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 62 | `UPTODATEACTUALQTYBP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 63 | `LASTUPDATEDATE` | DATE | NOT NULL |  |  |  |
| 64 | `PARTIALENDDATE` | DATE | NOT NULL |  |  |  |
| 65 | `LASTUPDATETIME` | CHAR(12) | NOT NULL |  |  |  |
| 66 | `DATEUPTO` | DATE | NOT NULL |  |  |  |

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
       t.BUSINESSGROUP,
       t.BUSINESSUNIT,
       t.WAREHOUSE,
       t.ITEMTYPE,
       t.TEMPLATE
FROM   DB2ADMIN.WRKPRODUCTIONANALYSIS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
