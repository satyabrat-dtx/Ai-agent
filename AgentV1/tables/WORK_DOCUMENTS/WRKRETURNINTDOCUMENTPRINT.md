# DB2ADMIN.WRKRETURNINTDOCUMENTPRINT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 65
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 19044

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
| 40 | `APPEARANCEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 41 | `TRUCKDRIVERCODE` | CHAR(3) |  |  |  |  |
| 42 | `NUMBERPLATE` | VARCHAR(80) |  |  |  |  |
| 43 | `TRANSPORTSTARTDATE` | DATE |  |  |  |  |
| 44 | `TRANSPORTSTARTTIME` | TIME |  |  |  |  |
| 45 | `NUMBERPARCEL` | DECIMAL(5,0) |  |  |  |  |
| 46 | `VOLUMEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 47 | `VOLUME` | DECIMAL(15,5) |  |  |  |  |
| 48 | `VOLUMEDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 49 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 50 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 51 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 52 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 53 | `WEIGHTDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 54 | `SUMMARIZEDDESCRIPTION` | CHAR(200) |  |  |  |  |
| 55 | `ORDERITEMUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 56 | `ITEMLONGDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 57 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 58 | `LINEUOMCODE` | CHAR(3) |  |  |  |  |
| 59 | `LINEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 60 | `LINEDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 61 | `CHARQUANTITY` | CHAR(16) |  |  |  |  |
| 62 | `QUALITYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 63 | `LGLWAREHOUSELONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 64 | `TRUCKDRIVERCOMPANYCODE` | CHAR(3) |  |  |  |  |

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
FROM   DB2ADMIN.WRKRETURNINTDOCUMENTPRINT t
FETCH FIRST 100 ROWS ONLY;
```
