# DB2ADMIN.WRKCUTSHIPRATIO

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 74
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `SERIAL`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 125489

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISION` | CHAR(3) |  |  |  |  |
| 3 | `PLANT` | CHAR(8) |  |  |  |  |
| 4 | `SERIAL` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `ANALYSISTYPE` | CHAR(6) | NOT NULL |  |  |  |
| 6 | `SALESORDERTYPE` | CHAR(25) | NOT NULL |  |  |  |
| 7 | `CUSTOMER` | CHAR(8) |  |  |  |  |
| 8 | `CUSTNATN` | CHAR(3) |  |  |  |  |
| 9 | `FINALCUSTOMER` | CHAR(8) |  |  |  |  |
| 10 | `FINALCUSTNATN` | CHAR(3) |  |  |  |  |
| 11 | `BUSINESSGROUP` | CHAR(10) |  |  |  |  |
| 12 | `BUSINESSUNIT` | CHAR(10) |  |  |  |  |
| 13 | `ARTICLE` | CHAR(140) | NOT NULL |  |  |  |
| 14 | `DESTINATION` | CHAR(50) |  |  |  |  |
| 15 | `WAREHOUSE` | CHAR(8) |  |  |  |  |
| 16 | `ITEMTYPE` | CHAR(3) | NOT NULL |  |  |  |
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
| 27 | `COMPANYCURRENCY` | CHAR(4) | NOT NULL |  |  |  |
| 28 | `DOCUMENTCURRENCY` | CHAR(4) | NOT NULL |  |  |  |
| 29 | `EXCHANGERATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 30 | `RATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 31 | `SALESGROUPTYPE` | CHAR(20) |  |  |  |  |
| 32 | `PRODUCTMAINGRP` | CHAR(30) |  |  |  |  |
| 33 | `PRDMNGRPDESC` | VARCHAR(200) |  |  |  |  |
| 34 | `PRODUCTSUBGRP1` | CHAR(30) |  |  |  |  |
| 35 | `PRDSBGRP1DESC` | VARCHAR(200) |  |  |  |  |
| 36 | `PRODUCTSUBGRP2` | CHAR(30) |  |  |  |  |
| 37 | `PRDSBGRP2DESC` | VARCHAR(200) |  |  |  |  |
| 38 | `PRODUCTSUBGRP3` | CHAR(30) |  |  |  |  |
| 39 | `PRDSBGRP3DESC` | VARCHAR(200) |  |  |  |  |
| 40 | `PRODUCTSUBGRP4` | CHAR(30) |  |  |  |  |
| 41 | `PRDSBGRP4DESC` | VARCHAR(200) |  |  |  |  |
| 42 | `USERPRIMARYUM` | CHAR(3) |  |  |  |  |
| 43 | `BASEPRIMARYUM` | CHAR(3) | NOT NULL |  |  |  |
| 44 | `USERSECONDARYUM` | CHAR(3) |  |  |  |  |
| 45 | `BASESECONDARYUM` | CHAR(3) |  |  |  |  |
| 46 | `USERPACKAGINGUM` | CHAR(3) |  |  |  |  |
| 47 | `QUALITYLEVEL` | DECIMAL(2,0) | NOT NULL |  |  |  |
| 48 | `DELIVERYPERIOD` | CHAR(8) | NOT NULL |  |  |  |
| 49 | `LASTUPDATEDATE` | DATE | NOT NULL |  |  |  |
| 50 | `LASTUPDATETIME` | CHAR(12) | NOT NULL |  |  |  |
| 51 | `DATAUPTO` | DATE |  |  |  |  |
| 52 | `TOLERANCE` | INTEGER | NOT NULL |  |  |  |
| 53 | `CUTTINGQTY` | CHAR(3) |  |  |  |  |
| 54 | `ORDERQTYUP` | DECIMAL(15,5) |  |  |  |  |
| 55 | `ORDERQTYBP` | DECIMAL(15,5) |  |  |  |  |
| 56 | `ORDERQTYUS` | DECIMAL(15,5) |  |  |  |  |
| 57 | `ORDERQTYBS` | DECIMAL(15,5) |  |  |  |  |
| 58 | `ORDERQTYUPK` | DECIMAL(15,5) |  |  |  |  |
| 59 | `ORDERQTYUPWT` | DECIMAL(15,5) |  |  |  |  |
| 60 | `ORDERQTYBPWT` | DECIMAL(15,5) |  |  |  |  |
| 61 | `ORDERQTYUSWT` | DECIMAL(15,5) |  |  |  |  |
| 62 | `ORDERQTYBSWT` | DECIMAL(15,5) |  |  |  |  |
| 63 | `ORDERQTYUPKWT` | DECIMAL(15,5) |  |  |  |  |
| 64 | `SHIPQTYUP` | DECIMAL(15,5) |  |  |  |  |
| 65 | `SHIPQTYBP` | DECIMAL(15,5) |  |  |  |  |
| 66 | `SHIPQTYUS` | DECIMAL(15,5) |  |  |  |  |
| 67 | `SHIPQTYBS` | DECIMAL(15,5) |  |  |  |  |
| 68 | `SHIPQTYUPK` | DECIMAL(15,5) |  |  |  |  |
| 69 | `CUTQTYUP` | DECIMAL(15,5) |  |  |  |  |
| 70 | `CUTQTYBP` | DECIMAL(15,5) |  |  |  |  |
| 71 | `CUTQTYUS` | DECIMAL(15,5) |  |  |  |  |
| 72 | `CUTQTYBS` | DECIMAL(15,5) |  |  |  |  |
| 73 | `CUTQTYPK` | DECIMAL(15,5) |  |  |  |  |

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
       t.SALESORDERTYPE,
       t.CUSTOMER,
       t.CUSTNATN,
       t.FINALCUSTOMER,
       t.FINALCUSTNATN,
       t.BUSINESSGROUP
FROM   DB2ADMIN.WRKCUTSHIPRATIO t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
