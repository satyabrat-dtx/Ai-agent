# DB2ADMIN.WRKSALESANALYSIS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 71
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `SERIAL`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 126039

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISION` | CHAR(3) |  |  |  |  |
| 3 | `PLANT` | CHAR(8) |  |  |  |  |
| 4 | `SERIAL` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `ANALYSISTYPE` | CHAR(6) | NOT NULL |  |  |  |
| 6 | `SALESORDER` | CHAR(25) | NOT NULL |  |  |  |
| 7 | `CUSTOMER` | CHAR(8) |  |  |  |  |
| 8 | `CUSTNATN` | CHAR(3) |  |  |  |  |
| 9 | `FINALCUSTOMER` | CHAR(8) |  |  |  |  |
| 10 | `FINALCUSTNATN` | CHAR(3) |  |  |  |  |
| 11 | `BUSINESSGROUP` | CHAR(10) |  |  |  |  |
| 12 | `BUSINESSUNIT` | CHAR(10) |  |  |  |  |
| 13 | `WAREHOUSE` | CHAR(8) | NOT NULL |  |  |  |
| 14 | `ITEMTYPE` | CHAR(3) | NOT NULL |  |  |  |
| 15 | `TEMPLATE` | CHAR(4) |  |  |  |  |
| 16 | `COMPANYCURRENCY` | CHAR(4) | NOT NULL |  |  |  |
| 17 | `DOCUMENTCURRENCY` | CHAR(4) | NOT NULL |  |  |  |
| 18 | `EXCHANGERATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 19 | `RATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 20 | `UNITPRICE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 21 | `DELIVERYTERM` | CHAR(3) | NOT NULL |  |  |  |
| 22 | `PAYMENTTERM` | CHAR(3) | NOT NULL |  |  |  |
| 23 | `INVOICETYPE` | CHAR(3) | NOT NULL |  |  |  |
| 24 | `TYPEOFINV` | CHAR(20) | NOT NULL |  |  |  |
| 25 | `DELIVERYPERIOD` | CHAR(8) | NOT NULL |  |  |  |
| 26 | `MANAGER` | CHAR(10) | NOT NULL |  |  |  |
| 27 | `MANAGERNAME` | CHAR(100) |  |  |  |  |
| 28 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 29 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `ARTICLE` | CHAR(140) | NOT NULL |  |  |  |
| 39 | `DELAYDAYS` | INTEGER | NOT NULL |  |  |  |
| 40 | `PRODUCTMAINGRP` | CHAR(30) |  |  |  |  |
| 41 | `PRDMNGRPDESC` | VARCHAR(200) |  |  |  |  |
| 42 | `PRODUCTSUBGRP1` | CHAR(30) |  |  |  |  |
| 43 | `PRDSBGRP1DESC` | VARCHAR(200) |  |  |  |  |
| 44 | `PRODUCTSUBGRP2` | CHAR(30) |  |  |  |  |
| 45 | `PRDSBGRP2DESC` | VARCHAR(200) |  |  |  |  |
| 46 | `PRODUCTSUBGRP3` | CHAR(30) |  |  |  |  |
| 47 | `PRDSBGRP3DESC` | VARCHAR(200) |  |  |  |  |
| 48 | `PRODUCTSUBGRP4` | CHAR(30) |  |  |  |  |
| 49 | `PRDSBGRP4DESC` | VARCHAR(200) |  |  |  |  |
| 50 | `BASEPRIMARYUOM` | CHAR(3) | NOT NULL |  |  |  |
| 51 | `USERPRIMARYUOM` | CHAR(3) |  |  |  |  |
| 52 | `USERSECONDARYUM` | CHAR(3) |  |  |  |  |
| 53 | `BASESECONDARYUM` | CHAR(3) |  |  |  |  |
| 54 | `PACKAGINGUOM` | CHAR(3) |  |  |  |  |
| 55 | `QUALITYLEVEL` | DECIMAL(2,0) | NOT NULL |  |  |  |
| 56 | `LASTUPDATEDATE` | DATE | NOT NULL |  |  |  |
| 57 | `LASTUPDATETIME` | CHAR(12) | NOT NULL |  |  |  |
| 58 | `DATEUPTO` | DATE | NOT NULL |  |  |  |
| 59 | `TODAYQTYBP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 60 | `TODAYQTYUP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 61 | `TODAYQTYBS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 62 | `TODAYQTYUS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 63 | `TODAYQTYUPK` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 64 | `TODAYAMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 65 | `UPTODATEQTYBP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 66 | `UPTODATEQTYUP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 67 | `UPTODATEQTYBS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 68 | `UPTODATEQTYUS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 69 | `UPTODATEQTYUPK` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 70 | `UPTODATEAMT` | DECIMAL(18,5) | NOT NULL |  |  |  |

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
       t.SALESORDER,
       t.CUSTOMER,
       t.CUSTNATN,
       t.FINALCUSTOMER,
       t.FINALCUSTNATN,
       t.BUSINESSGROUP
FROM   DB2ADMIN.WRKSALESANALYSIS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
