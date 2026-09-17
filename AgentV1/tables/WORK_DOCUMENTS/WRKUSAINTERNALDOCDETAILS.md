# DB2ADMIN.WRKUSAINTERNALDOCDETAILS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 32
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 88567

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 3 | `INTERNALDOCUMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `INTDOCPROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 5 | `INTDOCUMENTPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 6 | `INTERNALDOCUMENTLINEORDERLINE` | DECIMAL(5,0) |  |  |  |  |
| 7 | `INTDOCUMENTLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 8 | `ALLOCATIONCODE` | CHAR(15) | NOT NULL |  |  |  |
| 9 | `ALLOCATIONLINE` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 10 | `ALLOCATIONCOMPONENTLINE` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 11 | `TRANSACTIONNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 12 | `TRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 13 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 14 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 15 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 16 | `LOTCODE` | CHAR(10) |  |  |  |  |
| 17 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 18 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 19 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 20 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 21 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 22 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 23 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 24 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 25 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 28 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `ORIGINALCREATIONTIMESTAMP` | BIGINT | NOT NULL |  |  |  |
| 30 | `WORKLINE` | INTEGER | NOT NULL |  |  |  |
| 31 | `WORKSUBLINE` | DECIMAL(3,0) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.EXPIRATIONDATE,
       t.INTERNALDOCUMENTCOMPANYCODE,
       t.INTDOCPROVISIONALCOUNTERCODE,
       t.INTDOCUMENTPROVISIONALCODE,
       t.INTERNALDOCUMENTLINEORDERLINE,
       t.INTDOCUMENTLINEORDERSUBLINE,
       t.ALLOCATIONCODE,
       t.ALLOCATIONLINE,
       t.ALLOCATIONCOMPONENTLINE,
       t.TRANSACTIONNUMBER
FROM   DB2ADMIN.WRKUSAINTERNALDOCDETAILS t
FETCH FIRST 100 ROWS ONLY;
```
