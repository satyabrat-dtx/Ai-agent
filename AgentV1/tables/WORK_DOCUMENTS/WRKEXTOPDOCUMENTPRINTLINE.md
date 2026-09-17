# DB2ADMIN.WRKEXTOPDOCUMENTPRINTLINE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `CREATIONTIMESTAMP`, `WRKEXTOPDOCUMENTPRINTLINE`, `SUBLINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 30804

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `WRKEXTOPDOCUMENTPRINTLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `SUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 3 | `EXTOPDOCLINEEXTOPDOCCMYCODE` | CHAR(3) |  |  |  |  |
| 4 | `EXTOPDOCLINEEXTOPDOCPROVCNTCOD` | CHAR(8) |  |  |  |  |
| 5 | `EXTOPDOCLINEEXTOPDOCPRVCODE` | CHAR(15) |  |  |  |  |
| 6 | `EXTOPDOCUMENTLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 7 | `SUMMARIZEDDESCRIPTION` | CHAR(200) |  |  |  |  |
| 8 | `ORDERITEMUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 9 | `ITEMLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 10 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 11 | `LINEUOMCODE` | CHAR(3) |  |  |  |  |
| 12 | `LINEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 13 | `LINEDECIMALNUMBER` | INTEGER | NOT NULL |  |  |  |
| 14 | `CHARQUANTITY` | CHAR(16) |  |  |  |  |
| 15 | `DESTINATIONPHYWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 16 | `DESTINATIONPHYWHSLONGDES` | VARCHAR(200) |  |  |  |  |
| 17 | `DESTINATIONWHSLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 18 | `STCGROUPLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 19 | `PROJECTLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 20 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 21 | `PHYWAREHOUSELONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 22 | `LGLWAREHOUSELONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 23 | `COSTCENTERLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.WRKEXTOPDOCUMENTPRINTLINE,
       t.SUBLINE,
       t.EXTOPDOCLINEEXTOPDOCCMYCODE,
       t.EXTOPDOCLINEEXTOPDOCPROVCNTCOD,
       t.EXTOPDOCLINEEXTOPDOCPRVCODE,
       t.EXTOPDOCUMENTLINEORDERLINE,
       t.SUMMARIZEDDESCRIPTION,
       t.ORDERITEMUNIQUEID,
       t.ITEMLONGDESCRIPTION,
       t.ITEMCODE,
       t.LINEUOMCODE
FROM   DB2ADMIN.WRKEXTOPDOCUMENTPRINTLINE t
FETCH FIRST 100 ROWS ONLY;
```
