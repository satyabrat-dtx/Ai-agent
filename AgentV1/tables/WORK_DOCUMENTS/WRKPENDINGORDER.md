# DB2ADMIN.WRKPENDINGORDER

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 65
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `SERIAL`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 125731

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
| 7 | `CUSTNATN` | CHAR(3) |  |  |  |  |
| 8 | `FINALCUSTOMER` | CHAR(8) |  |  |  |  |
| 9 | `FINALCUSTNATN` | CHAR(3) |  |  |  |  |
| 10 | `BUSINESSGROUP` | CHAR(10) |  |  |  |  |
| 11 | `BUSINESSUNIT` | CHAR(10) |  |  |  |  |
| 12 | `WAREHOUSE` | CHAR(8) |  |  |  |  |
| 13 | `ITEMTYPE` | CHAR(3) | NOT NULL |  |  |  |
| 14 | `TEMPLATE` | CHAR(4) | NOT NULL |  |  |  |
| 15 | `COMPANYCURRENCY` | CHAR(4) | NOT NULL |  |  |  |
| 16 | `DOCUMENTCURRENCY` | CHAR(4) | NOT NULL |  |  |  |
| 17 | `EXCHANGERATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 18 | `RATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 19 | `UNITPRICE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 20 | `DELIVERYTERM` | CHAR(3) | NOT NULL |  |  |  |
| 21 | `PAYMENTTERM` | CHAR(3) | NOT NULL |  |  |  |
| 22 | `SALESGRPTYP` | CHAR(20) | NOT NULL |  |  |  |
| 23 | `DELIVERYPERIOD` | CHAR(8) | NOT NULL |  |  |  |
| 24 | `DELAYDAYS` | INTEGER | NOT NULL |  |  |  |
| 25 | `MANAGER` | CHAR(10) |  |  |  |  |
| 26 | `MANAGERNAME` | CHAR(100) |  |  |  |  |
| 27 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 28 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `ARTICLE` | CHAR(140) | NOT NULL |  |  |  |
| 38 | `PRODUCTMAINGRP` | CHAR(30) |  |  |  |  |
| 39 | `PRDMNGRPDESC` | VARCHAR(200) |  |  |  |  |
| 40 | `PRODUCTSUBGRP1` | CHAR(30) |  |  |  |  |
| 41 | `PRDSBGRP1DESC` | VARCHAR(200) |  |  |  |  |
| 42 | `PRODUCTSUBGRP2` | CHAR(30) |  |  |  |  |
| 43 | `PRDSBGRP2DESC` | VARCHAR(200) |  |  |  |  |
| 44 | `PRODUCTSUBGRP3` | CHAR(30) |  |  |  |  |
| 45 | `PRDSBGRP3DESC` | VARCHAR(200) |  |  |  |  |
| 46 | `PRODUCTSUBGRP4` | CHAR(30) |  |  |  |  |
| 47 | `PRDSBGRP4DESC` | VARCHAR(200) |  |  |  |  |
| 48 | `BASEPRIMARYUOM` | CHAR(3) | NOT NULL |  |  |  |
| 49 | `USERPRIMARYUOM` | CHAR(3) |  |  |  |  |
| 50 | `USERSECONDARYUM` | CHAR(3) |  |  |  |  |
| 51 | `BASESECONDARYUM` | CHAR(3) |  |  |  |  |
| 52 | `PACKAGINGUOM` | CHAR(3) |  |  |  |  |
| 53 | `QUALITYLEVEL` | DECIMAL(2,0) | NOT NULL |  |  |  |
| 54 | `MAINKEY` | VARCHAR(200) | NOT NULL |  |  |  |
| 55 | `ORDERDATE` | DATE |  |  |  |  |
| 56 | `LASTUPDATEDATE` | DATE | NOT NULL |  |  |  |
| 57 | `LASTUPDATETIME` | CHAR(12) | NOT NULL |  |  |  |
| 58 | `DATEUPTO` | DATE | NOT NULL |  |  |  |
| 59 | `TODAYQTYBP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 60 | `TODAYQTYUP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 61 | `TODAYQTYBS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 62 | `TODAYQTYUS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 63 | `TODAYQTYUPK` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 64 | `TODAYAMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |

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
       t.CUSTNATN,
       t.FINALCUSTOMER,
       t.FINALCUSTNATN,
       t.BUSINESSGROUP,
       t.BUSINESSUNIT
FROM   DB2ADMIN.WRKPENDINGORDER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
