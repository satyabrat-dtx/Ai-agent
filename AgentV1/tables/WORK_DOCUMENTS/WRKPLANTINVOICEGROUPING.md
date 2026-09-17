# DB2ADMIN.WRKPLANTINVOICEGROUPING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 44
- **Primary key**: `CREATIONTIMESTAMP`, `CREATIONUSER`, `LINE`, `INVOICETYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 145167

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `INVOICETYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `SUBCODE1` | CHAR(20) |  |  |  |  |
| 6 | `SUBCODE2` | CHAR(10) |  |  |  |  |
| 7 | `SUBCODE3` | CHAR(10) |  |  |  |  |
| 8 | `SUBCODE4` | CHAR(10) |  |  |  |  |
| 9 | `SUBCODE5` | CHAR(10) |  |  |  |  |
| 10 | `SUBCODE6` | CHAR(10) |  |  |  |  |
| 11 | `SUBCODE7` | CHAR(10) |  |  |  |  |
| 12 | `SUBCODE8` | CHAR(10) |  |  |  |  |
| 13 | `SUBCODE9` | CHAR(10) |  |  |  |  |
| 14 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 16 | `PRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 17 | `BASEPRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 18 | `SECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 19 | `SECODARYUMCODE` | CHAR(3) |  |  |  |  |
| 20 | `BASEPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `BASESECODARYUMCODE` | CHAR(3) |  |  |  |  |
| 22 | `PACKINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 23 | `BASESECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `PACKINGUMCODE` | CHAR(3) |  |  |  |  |
| 25 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 26 | `ORDERPRICE` | DECIMAL(18,5) |  |  |  |  |
| 27 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 28 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 29 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 30 | `INPUTCAPITAL` | INTEGER | NOT NULL |  |  |  |
| 31 | `WAREHOUSECODE` | CHAR(10) |  |  |  |  |
| 32 | `TRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 33 | `TRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 34 | `SOLINEABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 35 | `ORDERCOUNTERCODE` | CHAR(10) |  |  |  |  |
| 36 | `ORDERCODE` | CHAR(20) |  |  |  |  |
| 37 | `ORDERLINE` | DECIMAL(10,0) |  |  |  |  |
| 38 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 39 | `ORDERCOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 40 | `ARTICLERATE1` | DECIMAL(18,5) |  |  |  |  |
| 41 | `ARTICLERATE2` | DECIMAL(18,5) |  |  |  |  |
| 42 | `ARTICLERATE3` | DECIMAL(18,5) |  |  |  |  |
| 43 | `VALUE` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.INVOICETYPECODE,
       t.ITEMTYPECODE,
       t.SUBCODE1,
       t.SUBCODE2,
       t.SUBCODE3,
       t.SUBCODE4,
       t.SUBCODE5,
       t.SUBCODE6,
       t.SUBCODE7
FROM   DB2ADMIN.WRKPLANTINVOICEGROUPING t
FETCH FIRST 100 ROWS ONLY;
```
