# DB2ADMIN.WRKDOCUMENTPRINTLINE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 37
- **Primary key**: `CREATIONTIMESTAMP`, `WRKDOCUMENTPRINTLINE`, `SUBLINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 5836

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `WRKDOCUMENTPRINTLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `SUBLINE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 3 | `SALDOCLINESALDOCCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `SALDOCLINESALDOCPRVCNTCODE` | CHAR(8) |  |  |  |  |
| 5 | `SALDOCLINESALDOCPRVCODE` | CHAR(15) |  |  |  |  |
| 6 | `SALESDOCUMENTLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 7 | `SALESDOCUMENTLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 8 | `SALDOCLINECOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 9 | `SUMMARIZEDDESCRIPTION` | CHAR(200) |  |  |  |  |
| 10 | `ORDERITEMUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 11 | `ITEMLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 12 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 13 | `LINEUOMCODE` | CHAR(3) |  |  |  |  |
| 14 | `LINEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 15 | `LINEDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 16 | `CHARQUANTITY` | CHAR(16) |  |  |  |  |
| 17 | `RATE` | DECIMAL(6,3) |  |  |  |  |
| 18 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 19 | `NETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 20 | `DISCOUNTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 21 | `QUALITYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 22 | `STCGROUPLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 23 | `PROJECTLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 24 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 25 | `PHYWAREHOUSELONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 26 | `LGLWAREHOUSELONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 27 | `COSTCENTERLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 28 | `PAYMENTMETHODLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 29 | `PRICELISTLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 30 | `DSCCATEGORYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 31 | `TAXLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 32 | `AGENT1LONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 33 | `AGENT2LONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 34 | `AGENT3LONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 35 | `AGENT4LONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 36 | `AGENT5LONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.WRKDOCUMENTPRINTLINE,
       t.SUBLINE,
       t.SALDOCLINESALDOCCOMPANYCODE,
       t.SALDOCLINESALDOCPRVCNTCODE,
       t.SALDOCLINESALDOCPRVCODE,
       t.SALESDOCUMENTLINEORDERLINE,
       t.SALESDOCUMENTLINEORDERSUBLINE,
       t.SALDOCLINECOMPONENTORDERLINE,
       t.SUMMARIZEDDESCRIPTION,
       t.ORDERITEMUNIQUEID,
       t.ITEMLONGDESCRIPTION
FROM   DB2ADMIN.WRKDOCUMENTPRINTLINE t
FETCH FIRST 100 ROWS ONLY;
```
