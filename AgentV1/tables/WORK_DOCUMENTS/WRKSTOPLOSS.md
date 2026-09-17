# DB2ADMIN.WRKSTOPLOSS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 39
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 131799

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `WRKCENTER` | CHAR(15) |  |  |  |  |
| 4 | `RESOURCENO` | CHAR(6) |  |  |  |  |
| 5 | `LOOMRPM` | INTEGER | NOT NULL |  |  |  |
| 6 | `GRANDPRIQUANTITY` | DECIMAL(18,5) |  |  |  |  |
| 7 | `GRANDTOTALRPM` | DECIMAL(18,5) |  |  |  |  |
| 8 | `PRMQTY1` | DECIMAL(18,5) |  |  |  |  |
| 9 | `PRMQTY2` | DECIMAL(18,5) |  |  |  |  |
| 10 | `PRMQTY3` | DECIMAL(18,5) |  |  |  |  |
| 11 | `PRMQTY4` | DECIMAL(18,5) |  |  |  |  |
| 12 | `PRMQTY5` | DECIMAL(18,5) |  |  |  |  |
| 13 | `PRMQTY6` | DECIMAL(18,5) |  |  |  |  |
| 14 | `PRMQTY7` | DECIMAL(18,5) |  |  |  |  |
| 15 | `PRMQTY8` | DECIMAL(18,5) |  |  |  |  |
| 16 | `PRMQTY9` | DECIMAL(18,5) |  |  |  |  |
| 17 | `PRMQTY10` | DECIMAL(18,5) |  |  |  |  |
| 18 | `PRMQTY11` | DECIMAL(18,5) |  |  |  |  |
| 19 | `PRMQTY12` | DECIMAL(18,5) |  |  |  |  |
| 20 | `PRMQTY13` | DECIMAL(18,5) |  |  |  |  |
| 21 | `PRMQTY14` | DECIMAL(18,5) |  |  |  |  |
| 22 | `PRMQTY15` | DECIMAL(18,5) |  |  |  |  |
| 23 | `PRMQTY16` | DECIMAL(18,5) |  |  |  |  |
| 24 | `PRMQTY17` | DECIMAL(18,5) |  |  |  |  |
| 25 | `PRMQTY18` | DECIMAL(18,5) |  |  |  |  |
| 26 | `PRMQTY19` | DECIMAL(18,5) |  |  |  |  |
| 27 | `PRMQTY20` | DECIMAL(18,5) |  |  |  |  |
| 28 | `PRMQTY21` | DECIMAL(18,5) |  |  |  |  |
| 29 | `PRMQTY22` | DECIMAL(18,5) |  |  |  |  |
| 30 | `PRMQTY23` | DECIMAL(18,5) |  |  |  |  |
| 31 | `PRMQTY24` | DECIMAL(18,5) |  |  |  |  |
| 32 | `PRMQTY25` | DECIMAL(18,5) |  |  |  |  |
| 33 | `PRMQTY26` | DECIMAL(18,5) |  |  |  |  |
| 34 | `PRMQTY27` | DECIMAL(18,5) |  |  |  |  |
| 35 | `PRMQTY28` | DECIMAL(18,5) |  |  |  |  |
| 36 | `PRMQTY29` | DECIMAL(18,5) |  |  |  |  |
| 37 | `PRMQTY30` | DECIMAL(18,5) |  |  |  |  |
| 38 | `PRMQTY31` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.WRKCENTER,
       t.RESOURCENO,
       t.LOOMRPM,
       t.GRANDPRIQUANTITY,
       t.GRANDTOTALRPM,
       t.PRMQTY1,
       t.PRMQTY2,
       t.PRMQTY3,
       t.PRMQTY4
FROM   DB2ADMIN.WRKSTOPLOSS t
FETCH FIRST 100 ROWS ONLY;
```
