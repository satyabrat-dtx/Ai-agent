# DB2ADMIN.WRKWASTEGENERATION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 58
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `SERIAL`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 126203

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `ANALYSISTYPE` | CHAR(6) | NOT NULL |  |  |  |
| 3 | `SERIAL` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `BUSINESSGROUP` | CHAR(10) |  |  |  |  |
| 5 | `BUSINESSUNIT` | CHAR(10) |  |  |  |  |
| 6 | `DIVISION` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `PLANT` | CHAR(8) |  |  |  |  |
| 8 | `GROUPID` | CHAR(3) |  |  |  |  |
| 9 | `TRANSACTIONTEMPLATE` | CHAR(4) | NOT NULL |  |  |  |
| 10 | `WAREHOUSE` | CHAR(8) |  |  |  |  |
| 11 | `WORKCENTERGROUP` | CHAR(3) | NOT NULL |  |  |  |
| 12 | `WORKCENTER` | CHAR(8) |  |  |  |  |
| 13 | `FLAG` | CHAR(1) |  |  |  |  |
| 14 | `ITEMTYPE` | CHAR(3) | NOT NULL |  |  |  |
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
| 25 | `QUALITYLEVEL` | DECIMAL(2,0) | NOT NULL |  |  |  |
| 26 | `PRODUCTMAINGRP` | CHAR(30) |  |  |  |  |
| 27 | `PRDMNGRPDESC` | VARCHAR(200) |  |  |  |  |
| 28 | `PRODUCTSUBGRP1` | CHAR(30) |  |  |  |  |
| 29 | `PRDSBGRP1DESC` | VARCHAR(200) |  |  |  |  |
| 30 | `PRODUCTSUBGRP2` | CHAR(30) |  |  |  |  |
| 31 | `PRDSBGRP2DESC` | VARCHAR(200) |  |  |  |  |
| 32 | `PRODUCTSUBGRP3` | CHAR(30) |  |  |  |  |
| 33 | `PRDSBGRP3DESC` | VARCHAR(200) |  |  |  |  |
| 34 | `PRODUCTSUBGRP4` | CHAR(30) |  |  |  |  |
| 35 | `PRDSBGRP4DESC` | VARCHAR(200) |  |  |  |  |
| 36 | `USERPRIMARYUM` | CHAR(3) |  |  |  |  |
| 37 | `BASEPRIMARYUM` | CHAR(3) | NOT NULL |  |  |  |
| 38 | `USERSECONDARYUM` | CHAR(3) |  |  |  |  |
| 39 | `BASESECONDARYUM` | CHAR(3) |  |  |  |  |
| 40 | `USERPACKAGINGUM` | CHAR(3) |  |  |  |  |
| 41 | `CUSTOMER` | CHAR(8) | NOT NULL |  |  |  |
| 42 | `MONTHLYTGT` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 43 | `NOOFDAYS` | INTEGER | NOT NULL |  |  |  |
| 44 | `TODAYACTUALQTYUP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 45 | `TODAYACTUALQTYBP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 46 | `TODAYACTUALQTYUS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 47 | `TODAYACTUALQTYBS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 48 | `TODAYACTUALQTYUPK` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 49 | `UPTODATEACTUALQUANTITYUP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 50 | `UPTODATEACTUALQTYBP` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 51 | `UPTODATEACTUALQTYUS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 52 | `UPTODATEACTUALQTYBS` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 53 | `UPTODATEACTUALQTYPK` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 54 | `PARTIALENDDATE` | DATE | NOT NULL |  |  |  |
| 55 | `LASTUPDATEDATE` | DATE | NOT NULL |  |  |  |
| 56 | `LASTUPDATETIME` | CHAR(12) | NOT NULL |  |  |  |
| 57 | `DATAUPTO` | DATE |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.ANALYSISTYPE,
       t.SERIAL,
       t.BUSINESSGROUP,
       t.BUSINESSUNIT,
       t.DIVISION,
       t.PLANT,
       t.GROUPID,
       t.TRANSACTIONTEMPLATE,
       t.WAREHOUSE,
       t.WORKCENTERGROUP
FROM   DB2ADMIN.WRKWASTEGENERATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
