# DB2ADMIN.WRKINTERNALLINE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 33
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`, `INTORDLINEINTORDERCOMPANYCODE`, `INTORDLINEINTORDERCOUNTERCODE`, `INTORDERLINEINTERNALORDERCODE`, `INTERNALORDERLINEORDERLINE`, `INTERNALORDERLINEORDERSUBLINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 21885

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `INTORDLINEINTORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `INTORDLINEINTORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `INTORDERLINEINTERNALORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 6 | `INTERNALORDERLINEORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 7 | `INTERNALORDERLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 8 | `REMAINEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 9 | `REMAINEDUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 10 | `REMAINEDUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 11 | `CONFIRMEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 12 | `CONFIRMEDUSERSECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 13 | `CONFIRMEDUSERPACKAGINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 14 | `PRIMARYQUANTITYDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 15 | `SECONDARYQTYDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 16 | `PACKAGINGQTYDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 17 | `QUALITYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 18 | `STCGROUPLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 19 | `PROJECTLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 20 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 21 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 31 | `ITEMLONGDESCRIPTION` | CHAR(200) |  |  |  |  |
| 32 | `ORDERITEMUNIQUEID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.INTORDLINEINTORDERCOMPANYCODE,
       t.INTORDLINEINTORDERCOUNTERCODE,
       t.INTORDERLINEINTERNALORDERCODE,
       t.INTERNALORDERLINEORDERLINE,
       t.INTERNALORDERLINEORDERSUBLINE,
       t.REMAINEDUSERPRIMARYQUANTITY,
       t.REMAINEDUSERSECONDARYQUANTITY,
       t.REMAINEDUSERPACKAGINGQUANTITY,
       t.CONFIRMEDUSERPRIMARYQUANTITY
FROM   DB2ADMIN.WRKINTERNALLINE t
FETCH FIRST 100 ROWS ONLY;
```
