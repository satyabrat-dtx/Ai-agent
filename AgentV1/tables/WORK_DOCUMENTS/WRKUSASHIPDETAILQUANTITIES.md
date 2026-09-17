# DB2ADMIN.WRKUSASHIPDETAILQUANTITIES

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 48
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 88619

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 3 | `PRINTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 4 | `SALESDOCUMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `SALDOCPROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 6 | `SALESDOCUMENTPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 7 | `SALESDOCUMENTLINEORDERLINE` | DECIMAL(5,0) |  |  |  |  |
| 8 | `SALESDOCUMENTLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 9 | `SALDOCLINECOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 10 | `ALLOCATIONCODE` | CHAR(15) | NOT NULL |  |  |  |
| 11 | `ALLOCATIONLINE` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 12 | `ALLOCATIONCOMPONENTLINE` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 13 | `TRANSACTIONNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 14 | `TRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 15 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 16 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 17 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 18 | `LOTCODE` | CHAR(10) |  |  |  |  |
| 19 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 20 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 21 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 22 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 23 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 24 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 25 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 26 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 27 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 28 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 30 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 31 | `HEIGHTUOMCODE` | CHAR(3) |  |  |  |  |
| 32 | `HEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 33 | `LENGTHUOMCODE` | CHAR(3) |  |  |  |  |
| 34 | `LENGTH` | DECIMAL(15,5) |  |  |  |  |
| 35 | `VOLUMEUOMCODE` | CHAR(3) |  |  |  |  |
| 36 | `VOLUME` | DECIMAL(15,5) |  |  |  |  |
| 37 | `WEIGHTGROSSUOMCODE` | CHAR(3) |  |  |  |  |
| 38 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 39 | `WEIGHTNETUOMCODE` | CHAR(3) |  |  |  |  |
| 40 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 41 | `WEIGHTREALNETUOMCODE` | CHAR(3) |  |  |  |  |
| 42 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 43 | `WIDTHUOMCODE` | CHAR(3) |  |  |  |  |
| 44 | `WIDTH` | DECIMAL(15,5) |  |  |  |  |
| 45 | `ORIGINALCREATIONTIMESTAMP` | BIGINT | NOT NULL |  |  |  |
| 46 | `WORKLINE` | INTEGER | NOT NULL |  |  |  |
| 47 | `WORKSUBLINE` | DECIMAL(5,0) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKUSASHIPDTIDX1` (ORIGINALCREATIONTIMESTAMP, WORKLINE, WORKSUBLINE)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.EXPIRATIONDATE,
       t.PRINTTYPE,
       t.SALESDOCUMENTCOMPANYCODE,
       t.SALDOCPROVISIONALCOUNTERCODE,
       t.SALESDOCUMENTPROVISIONALCODE,
       t.SALESDOCUMENTLINEORDERLINE,
       t.SALESDOCUMENTLINEORDERSUBLINE,
       t.SALDOCLINECOMPONENTORDERLINE,
       t.ALLOCATIONCODE,
       t.ALLOCATIONLINE
FROM   DB2ADMIN.WRKUSASHIPDETAILQUANTITIES t
FETCH FIRST 100 ROWS ONLY;
```
