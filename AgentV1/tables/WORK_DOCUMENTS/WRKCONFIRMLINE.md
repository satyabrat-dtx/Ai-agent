# DB2ADMIN.WRKCONFIRMLINE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 36
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`, `SALORDLINESALORDERCOMPANYCODE`, `SALORDLINESALORDERCOUNTERCODE`, `SALESORDERLINESALESORDERCODE`, `SALESORDERLINEORDERLINE`, `SALESORDERLINEORDERSUBLINE`, `SALORDLINECOMPONENTORDERLINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 10483

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `SALORDLINESALORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `SALORDLINESALORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `SALESORDERLINESALESORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 6 | `SALESORDERLINEORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 7 | `SALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 8 | `SALORDLINECOMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 9 | `REMAINEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 10 | `REMAINEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 11 | `REMAINEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 12 | `CONFIRMEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 13 | `CONFIRMEDUSERSECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 14 | `CONFIRMEDUSERPACKAGINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 15 | `PRIMARYQUANTITYDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 16 | `SECONDARYQTYDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 17 | `PACKAGINGQTYDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 18 | `VALUEDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 19 | `QUALITYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 20 | `PAYMENTMETHODLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 21 | `STCGROUPLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 22 | `PROJECTLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 23 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 24 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 34 | `ITEMLONGDESCRIPTION` | CHAR(200) |  |  |  |  |
| 35 | `ORDERITEMUNIQUEID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.SALORDLINESALORDERCOMPANYCODE,
       t.SALORDLINESALORDERCOUNTERCODE,
       t.SALESORDERLINESALESORDERCODE,
       t.SALESORDERLINEORDERLINE,
       t.SALESORDERLINEORDERSUBLINE,
       t.SALORDLINECOMPONENTORDERLINE,
       t.REMAINEDUSERPRIMARYQUANTITY,
       t.REMAINEDUSERSECONDARYQUANTITY,
       t.REMAINEDUSERPACKAGINGQUANTITY
FROM   DB2ADMIN.WRKCONFIRMLINE t
FETCH FIRST 100 ROWS ONLY;
```
