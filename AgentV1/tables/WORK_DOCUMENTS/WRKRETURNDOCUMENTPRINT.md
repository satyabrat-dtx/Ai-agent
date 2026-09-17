# DB2ADMIN.WRKRETURNDOCUMENTPRINT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 68
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 25621

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `PROVISIONALCODE` | INTEGER | NOT NULL |  |  |  |
| 4 | `RETURNDOCUMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `RETURNDOCUMENTCODE` | CHAR(15) |  |  |  |  |
| 6 | `RETURNDOCUMENTLINE` | DECIMAL(7,0) |  |  |  |  |
| 7 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 8 | `CHOICEDELIVERYPOINT` | CHAR(2) |  |  |  |  |
| 9 | `DELIVERYPOINTLEGALNAME1` | VARCHAR(200) |  |  |  |  |
| 10 | `DELIVERYPOINTLEGALNAME2` | VARCHAR(200) |  |  |  |  |
| 11 | `DELIVERYPOINTADDRESSLINE1` | VARCHAR(200) |  |  |  |  |
| 12 | `DELIVERYPOINTADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 13 | `DELIVERYPOINTADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 14 | `DELIVERYPOINTPOSTALCODE` | CHAR(20) |  |  |  |  |
| 15 | `DELIVERYPOINTTOWN` | VARCHAR(200) |  |  |  |  |
| 16 | `DELIVERYPOINTDISTRICT` | VARCHAR(200) |  |  |  |  |
| 17 | `DELIVERYPOINTCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 18 | `DELIVERYCNYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 19 | `CHOICEDOCUMENTADDRESS` | CHAR(2) |  |  |  |  |
| 20 | `DOCUMENTADDRESSLEGALNAME1` | VARCHAR(200) |  |  |  |  |
| 21 | `DOCUMENTADDRESSLEGALNAME2` | VARCHAR(200) |  |  |  |  |
| 22 | `DOCUMENTADDRESSADDRESSLINE1` | VARCHAR(200) |  |  |  |  |
| 23 | `DOCUMENTADDRESSADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 24 | `DOCUMENTADDRESSADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 25 | `DOCUMENTADDRESSPOSTALCODE` | CHAR(20) |  |  |  |  |
| 26 | `DOCUMENTADDRESSTOWN` | VARCHAR(200) |  |  |  |  |
| 27 | `DOCUMENTADDRESSDISTRICT` | VARCHAR(200) |  |  |  |  |
| 28 | `DOCUMENTADDRESSCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 29 | `DOCADDRESSCNYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 30 | `DOCUMENTADDRESSFISCALCODE` | CHAR(16) |  |  |  |  |
| 31 | `CHOICESHIPPINGADDRESS` | CHAR(2) |  |  |  |  |
| 32 | `COMPANYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 33 | `DIVISIONLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 34 | `TERMSOFDLVLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 35 | `TERMSOFSHPLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 36 | `TRANSPORTREASONDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 37 | `FIRSTCARRIERLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 38 | `SECONDCARRIERLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 39 | `THIRDCARRIERLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 40 | `CURRENCYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 41 | `PRICELISTLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 42 | `TAXLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 43 | `APPEARANCEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 44 | `TRUCKDRIVERCODE` | CHAR(3) |  |  |  |  |
| 45 | `NUMBERPLATE` | VARCHAR(80) |  |  |  |  |
| 46 | `TRANSPORTSTARTDATE` | DATE |  |  |  |  |
| 47 | `TRANSPORTSTARTTIME` | TIME |  |  |  |  |
| 48 | `NUMBERPARCEL` | DECIMAL(5,0) |  |  |  |  |
| 49 | `VOLUMEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 50 | `VOLUME` | DECIMAL(15,5) |  |  |  |  |
| 51 | `VOLUMEDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 52 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 53 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 54 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 55 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 56 | `WEIGHTDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 57 | `SUMMARIZEDDESCRIPTION` | CHAR(200) |  |  |  |  |
| 58 | `ORDERITEMUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 59 | `ITEMLONGDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 60 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 61 | `LINEUOMCODE` | CHAR(3) |  |  |  |  |
| 62 | `LINEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 63 | `LINEDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 64 | `CHARQUANTITY` | CHAR(16) |  |  |  |  |
| 65 | `QUALITYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 66 | `LGLWAREHOUSELONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 67 | `TRUCKDRIVERCOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.PROVISIONALCODE,
       t.RETURNDOCUMENTCOMPANYCODE,
       t.RETURNDOCUMENTCODE,
       t.RETURNDOCUMENTLINE,
       t.LANGUAGECODE,
       t.CHOICEDELIVERYPOINT,
       t.DELIVERYPOINTLEGALNAME1,
       t.DELIVERYPOINTLEGALNAME2,
       t.DELIVERYPOINTADDRESSLINE1
FROM   DB2ADMIN.WRKRETURNDOCUMENTPRINT t
FETCH FIRST 100 ROWS ONLY;
```
