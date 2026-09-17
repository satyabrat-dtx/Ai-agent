# DB2ADMIN.WRKINTERNALDOCUMENTPRINTLINE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `CREATIONTIMESTAMP`, `WRKINTERNALDOCUMENTPRINTLINE`, `SUBLINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 61377

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `WRKINTERNALDOCUMENTPRINTLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `SUBLINE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 3 | `INTDOCLINEINTDOCCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `INTDOCLINEINTDOCPRVCNTCODE` | CHAR(8) |  |  |  |  |
| 5 | `INTDOCLINEINTDOCPRVCODE` | CHAR(15) |  |  |  |  |
| 6 | `INTERNALDOCUMENTLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 7 | `INTDOCUMENTLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 8 | `RECEIVINGSTOCKTYPELONGDES` | VARCHAR(200) |  |  |  |  |
| 9 | `SUMMARIZEDDESCRIPTION` | CHAR(200) |  |  |  |  |
| 10 | `ORDERITEMUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 11 | `ITEMLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 12 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 13 | `LINEUOMCODE` | CHAR(3) |  |  |  |  |
| 14 | `LINEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 15 | `LINEDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 16 | `CHARQUANTITY` | CHAR(16) |  |  |  |  |
| 17 | `QUALITYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 18 | `DESTINATIONPHYWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 19 | `DESTINATIONPHYWHSLONGDES` | VARCHAR(200) |  |  |  |  |
| 20 | `DESTINATIONWHSLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 21 | `STCGROUPLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 22 | `PROJECTLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 23 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 24 | `PHYWAREHOUSELONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 25 | `LGLWAREHOUSELONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 26 | `COSTCENTERLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.WRKINTERNALDOCUMENTPRINTLINE,
       t.SUBLINE,
       t.INTDOCLINEINTDOCCOMPANYCODE,
       t.INTDOCLINEINTDOCPRVCNTCODE,
       t.INTDOCLINEINTDOCPRVCODE,
       t.INTERNALDOCUMENTLINEORDERLINE,
       t.INTDOCUMENTLINEORDERSUBLINE,
       t.RECEIVINGSTOCKTYPELONGDES,
       t.SUMMARIZEDDESCRIPTION,
       t.ORDERITEMUNIQUEID,
       t.ITEMLONGDESCRIPTION
FROM   DB2ADMIN.WRKINTERNALDOCUMENTPRINTLINE t
FETCH FIRST 100 ROWS ONLY;
```
