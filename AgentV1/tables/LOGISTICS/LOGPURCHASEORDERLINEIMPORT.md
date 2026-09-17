# DB2ADMIN.LOGPURCHASEORDERLINEIMPORT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`
- **Columns**: 62
- **Primary key**: `PURCHASEORDERIMPORTCOMPANYCODE`, `PURORDIMPORTIMPORTPRVCODE`, `ORDERLINE`, `ORDERSUBLINE`, `LOGTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 7731

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PURCHASEORDERIMPORTCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `PURORDIMPORTIMPORTPRVCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 3 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 4 | `ORDERLINE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 5 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 6 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 7 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 8 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 9 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `EXTERNALITEM` | CHAR(30) |  |  |  |  |
| 19 | `ITEMDESCRIPTION` | CHAR(50) |  |  |  |  |
| 20 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 21 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 23 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 25 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `BUYERCODE` | CHAR(25) |  |  |  |  |
| 27 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 28 | `LINESTATUS` | CHAR(2) |  |  |  |  |
| 29 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 30 | `STATISTICALGROUPCODE` | CHAR(3) |  |  |  |  |
| 31 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 32 | `LINEGROUP` | CHAR(3) |  |  |  |  |
| 33 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 34 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 35 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 36 | `DELIVERYDESCRIPTION` | CHAR(50) |  |  |  |  |
| 37 | `SHIPPINGDESCRIPTION` | CHAR(50) |  |  |  |  |
| 38 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 39 | `LEFTOVERLOSS` | SMALLINT | NOT NULL |  |  |  |
| 40 | `JOINEDPURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 41 | `JOINEDORDERLINE` | DECIMAL(5,0) |  |  |  |  |
| 42 | `JOINEDORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 43 | `SENDTOSUPPLIER` | SMALLINT | NOT NULL |  |  |  |
| 44 | `ENTRYEXCHANGERATE` | DECIMAL(15,7) |  |  |  |  |
| 45 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 46 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 47 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 48 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 49 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 50 | `PRICETYPE` | CHAR(2) |  |  |  |  |
| 51 | `PRICESIGN` | CHAR(2) |  |  |  |  |
| 52 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 53 | `NETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 54 | `UPDATEVALUE` | SMALLINT | NOT NULL |  |  |  |
| 55 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 56 | `FREEGIFTTAXDEBIT` | SMALLINT | NOT NULL |  |  |  |
| 57 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 58 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 59 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 60 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 61 | `LOGUSER` | CHAR(25) |  |  | audit | User responsible for the audited change (change-log table). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PURCHASEORDERIMPORTCOMPANYCODE,
       t.PURORDIMPORTIMPORTPRVCODE,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.LINETEMPLATECODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04
FROM   DB2ADMIN.LOGPURCHASEORDERLINEIMPORT t
FETCH FIRST 100 ROWS ONLY;
```
