# DB2ADMIN.WRKPURCHASEANALYSIS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 63
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `SERIAL`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 125955

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISION` | CHAR(3) |  |  |  |  |
| 3 | `PLANT` | CHAR(8) |  |  |  |  |
| 4 | `SERIAL` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `ANALYSISTYPE` | CHAR(6) | NOT NULL |  |  |  |
| 6 | `PURCHASEORDER` | CHAR(25) | NOT NULL |  |  |  |
| 7 | `CUSTOMER` | CHAR(8) |  |  |  |  |
| 8 | `CUSTNATN` | CHAR(3) |  |  |  |  |
| 9 | `FINALCUSTOMER` | CHAR(8) |  |  |  |  |
| 10 | `FINALCUSTNATN` | CHAR(3) |  |  |  |  |
| 11 | `BUSINESSGROUP` | CHAR(10) |  |  |  |  |
| 12 | `BUSINESSUNIT` | CHAR(10) |  |  |  |  |
| 13 | `WAREHOUSE` | CHAR(8) | NOT NULL |  |  |  |
| 14 | `ITEMTYPE` | CHAR(3) | NOT NULL |  |  |  |
| 15 | `TEMPLATE` | CHAR(4) |  |  |  |  |
| 16 | `TRANSACTIONNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 17 | `COMPANYCURRENCY` | CHAR(4) | NOT NULL |  |  |  |
| 18 | `DOCUMENTCURRENCY` | CHAR(4) | NOT NULL |  |  |  |
| 19 | `EXCHANGERATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 20 | `RATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 21 | `UNITPRICE` | DECIMAL(28,15) |  |  |  |  |
| 22 | `DELIVERYTERM` | CHAR(3) | NOT NULL |  |  |  |
| 23 | `PAYMENTTERM` | CHAR(3) | NOT NULL |  |  |  |
| 24 | `MANAGER` | CHAR(10) | NOT NULL |  |  |  |
| 25 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 26 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `ARTICLE` | VARCHAR(1000) | NOT NULL |  |  |  |
| 36 | `MAINKEY` | VARCHAR(1000) |  |  |  |  |
| 37 | `PURCHASEGRPTYPE` | CHAR(3) | NOT NULL |  |  |  |
| 38 | `DELAYDAYS` | INTEGER | NOT NULL |  |  |  |
| 39 | `PRODUCTMAINGRP` | CHAR(30) |  |  |  |  |
| 40 | `PRDMNGRPDESC` | VARCHAR(200) |  |  |  |  |
| 41 | `PRODUCTSUBGRP1` | CHAR(30) |  |  |  |  |
| 42 | `PRDSBGRP1DESC` | VARCHAR(200) |  |  |  |  |
| 43 | `PRODUCTSUBGRP2` | CHAR(30) |  |  |  |  |
| 44 | `PRDSBGRP2DESC` | VARCHAR(200) |  |  |  |  |
| 45 | `PRODUCTSUBGRP3` | CHAR(30) |  |  |  |  |
| 46 | `PRDSBGRP3DESC` | VARCHAR(200) |  |  |  |  |
| 47 | `PRODUCTSUBGRP4` | CHAR(30) |  |  |  |  |
| 48 | `PRDSBGRP4DESC` | VARCHAR(200) |  |  |  |  |
| 49 | `BASEPRIMARYUOM` | CHAR(3) | NOT NULL |  |  |  |
| 50 | `USERPRIMARYUOM` | CHAR(3) |  |  |  |  |
| 51 | `USERSECONDARYUM` | CHAR(3) |  |  |  |  |
| 52 | `BASESECONDARYUM` | CHAR(3) |  |  |  |  |
| 53 | `PACKAGINGUOM` | CHAR(3) |  |  |  |  |
| 54 | `LASTUPDATEDATE` | DATE | NOT NULL |  |  |  |
| 55 | `LASTUPDATETIME` | CHAR(12) | NOT NULL |  |  |  |
| 56 | `DATEUPTO` | DATE | NOT NULL |  |  |  |
| 57 | `TODAYQTYBP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 58 | `TODAYQTYUP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 59 | `TODAYQTYBS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 60 | `TODAYQTYUS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 61 | `TODAYQTYUPK` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 62 | `TODAYAMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |

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
       t.PURCHASEORDER,
       t.CUSTOMER,
       t.CUSTNATN,
       t.FINALCUSTOMER,
       t.FINALCUSTNATN,
       t.BUSINESSGROUP
FROM   DB2ADMIN.WRKPURCHASEANALYSIS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
