# DB2ADMIN.WRKSALESORDERLINE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 52
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `CODE`, `PAGENUMBER`, `ROWNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 146089

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `PAGENUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `ROWNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `ROWDESCRIPTION` | CHAR(50) |  |  |  |  |
| 6 | `COLUMNNUMBER` | INTEGER | NOT NULL |  |  |  |
| 7 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 8 | `UNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 9 | `NAMEENTITYNAME` | CHAR(50) |  |  |  |  |
| 10 | `NAMENAME` | CHAR(50) |  |  |  |  |
| 11 | `FIELDNAME` | CHAR(50) |  |  |  |  |
| 12 | `DATATYPE` | INTEGER | NOT NULL |  |  |  |
| 13 | `VALUESTRING` | CHAR(50) |  |  |  |  |
| 14 | `VALUEINT` | INTEGER | NOT NULL |  |  |  |
| 15 | `VALUEBOOLEAN` | SMALLINT | NOT NULL |  |  |  |
| 16 | `VALUEDATE` | DATE |  |  |  |  |
| 17 | `VALUEDECIMAL` | DECIMAL(18,5) |  |  |  |  |
| 18 | `VALUELONG` | BIGINT | NOT NULL |  |  |  |
| 19 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 20 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 21 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 22 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 23 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `BASEPRIMARYUNITCODE` | CHAR(3) |  |  |  |  |
| 26 | `USERPRIMARYUNITCODE` | CHAR(3) |  |  |  |  |
| 27 | `COLUMNVALUE1` | CHAR(50) |  |  |  |  |
| 28 | `COLUMNVALUE2` | CHAR(50) |  |  |  |  |
| 29 | `COLUMNVALUE3` | CHAR(50) |  |  |  |  |
| 30 | `COLUMNVALUE4` | CHAR(50) |  |  |  |  |
| 31 | `COLUMNVALUE5` | CHAR(50) |  |  |  |  |
| 32 | `ADDRESS1` | VARCHAR(200) |  |  |  |  |
| 33 | `ADDRESS2` | VARCHAR(200) |  |  |  |  |
| 34 | `CUSTOMERNAME` | CHAR(100) |  |  |  |  |
| 35 | `COMPANYDESC` | VARCHAR(200) |  |  |  |  |
| 36 | `QTYTOLERANCE` | CHAR(25) |  |  |  |  |
| 37 | `COUNTRYCENTRE` | CHAR(50) |  |  |  |  |
| 38 | `FOLLOWHO` | CHAR(25) |  |  |  |  |
| 39 | `FOLLOWAO` | CHAR(25) |  |  |  |  |
| 40 | `CUSTOMERPODATE` | CHAR(50) |  |  |  |  |
| 41 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 42 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 43 | `SALESORDDATE` | DATE |  |  |  |  |
| 44 | `ITEMTYPE` | CHAR(3) |  |  |  |  |
| 45 | `PRODUCTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 46 | `SPLCOMMENT` | CHAR(100) |  |  |  |  |
| 47 | `SOCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 48 | `OVERALLINS` | CHAR(100) |  |  |  |  |
| 49 | `DEVELOPMENTSO` | DATE |  |  |  |  |
| 50 | `SOINVOICETYPE` | CHAR(20) |  |  |  |  |
| 51 | `TYPEPROJECTION` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.CODE,
       t.PAGENUMBER,
       t.ROWNUMBER,
       t.ROWDESCRIPTION,
       t.COLUMNNUMBER,
       t.ORDERLINE,
       t.UNIQUEID,
       t.NAMEENTITYNAME,
       t.NAMENAME,
       t.FIELDNAME
FROM   DB2ADMIN.WRKSALESORDERLINE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
