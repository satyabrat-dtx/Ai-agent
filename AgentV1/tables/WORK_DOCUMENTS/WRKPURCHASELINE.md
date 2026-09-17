# DB2ADMIN.WRKPURCHASELINE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 35
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`, `PURORDLINEPURORDERCOMPANYCODE`, `PURORDLINEPURORDERCOUNTERCODE`, `PURORDERLINEPURCHASEORDERCODE`, `PURCHASEORDERLINEORDERLINE`, `PURCHASEORDERLINEORDERSUBLINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 19793

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `PURORDLINEPURORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `PURORDLINEPURORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `PURORDERLINEPURCHASEORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 6 | `PURCHASEORDERLINEORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 7 | `PURCHASEORDERLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 8 | `REMAINEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 9 | `REMAINEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 10 | `REMAINEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 11 | `CONFIRMEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 12 | `CONFIRMEDUSERSECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 13 | `CONFIRMEDUSERPACKAGINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 14 | `PRIMARYQUANTITYDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 15 | `SECONDARYQTYDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 16 | `PACKAGINGQTYDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 17 | `VALUEDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 18 | `QUALITYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 19 | `PAYMENTMETHODLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 20 | `STCGROUPLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 21 | `PROJECTLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 22 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 23 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 33 | `ITEMLONGDESCRIPTION` | CHAR(200) |  |  |  |  |
| 34 | `ORDERITEMUNIQUEID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.PURORDLINEPURORDERCOMPANYCODE,
       t.PURORDLINEPURORDERCOUNTERCODE,
       t.PURORDERLINEPURCHASEORDERCODE,
       t.PURCHASEORDERLINEORDERLINE,
       t.PURCHASEORDERLINEORDERSUBLINE,
       t.REMAINEDUSERPRIMARYQUANTITY,
       t.REMAINEDUSERSECONDARYQUANTITY,
       t.REMAINEDUSERPACKAGINGQUANTITY,
       t.CONFIRMEDUSERPRIMARYQUANTITY
FROM   DB2ADMIN.WRKPURCHASELINE t
FETCH FIRST 100 ROWS ONLY;
```
