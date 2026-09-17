# DB2ADMIN.WRKBOMCOMPONENTCOLOR

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 34
- **Primary key**: `WRKBOMCMPWRKBIOFMATCMYCODE`, `WRKBOMCMPWRKBIOFMATCRTISTAMP`, `WRKBOMCMPWRKBIOFMATPRDITCODE`, `WRKBOMCMPWRKBIOFMATSUBCODE01`, `WRKBOMCMPWRKBIOFMATSUBCODE02`, `WRKBOMCMPWRKBIOFMATSUBCODE03`, `WRKBOMCMPWRKBIOFMATSUBCODE04`, `WRKBOMCMPWRKBIOFMATSUBCODE05`, `WRKBOMCMPWRKBIOFMATSUBCODE06`, `WRKBOMCMPWRKBIOFMATSUBCODE07`, `WRKBOMCMPWRKBIOFMATSUBCODE08`, `WRKBOMCMPWRKBIOFMATSUBCODE09`, `WRKBOMCMPWRKBIOFMATSUBCODE10`, `WRKBOMCOMPONENTLINENO`, `WRKBOMCMPCOMPITEMTYPECODE`, `WRKBOMCOMPONENTITEMTYPEAFICODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 127727

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WRKBOMCMPWRKBIOFMATCMYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `WRKBOMCMPWRKBIOFMATCRTISTAMP` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `WRKBOMCMPWRKBIOFMATPRDITCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `WRKBOMCMPWRKBIOFMATSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `WRKBOMCMPWRKBIOFMATSUBCODE02` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 5 | `WRKBOMCMPWRKBIOFMATSUBCODE03` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 6 | `WRKBOMCMPWRKBIOFMATSUBCODE04` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 7 | `WRKBOMCMPWRKBIOFMATSUBCODE05` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 8 | `WRKBOMCMPWRKBIOFMATSUBCODE06` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 9 | `WRKBOMCMPWRKBIOFMATSUBCODE07` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 10 | `WRKBOMCMPWRKBIOFMATSUBCODE08` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 11 | `WRKBOMCMPWRKBIOFMATSUBCODE09` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 12 | `WRKBOMCMPWRKBIOFMATSUBCODE10` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 13 | `WRKBOMCOMPONENTLINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 14 | `WRKBOMCMPCOMPITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 15 | `WRKBOMCOMPONENTITEMTYPEAFICODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 16 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 17 | `CODE1` | CHAR(10) |  |  |  |  |
| 18 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 19 | `SUBCODE02` | CHAR(20) |  |  | generic_classification_code |  |
| 20 | `SUBCODE03` | CHAR(20) |  |  | generic_classification_code |  |
| 21 | `SUBCODE04` | CHAR(20) |  |  | generic_classification_code |  |
| 22 | `SUBCODE05` | CHAR(20) |  |  | generic_classification_code |  |
| 23 | `SUBCODE06` | CHAR(20) |  |  | generic_classification_code |  |
| 24 | `SUBCODE07` | CHAR(20) |  |  | generic_classification_code |  |
| 25 | `SUBCODE08` | CHAR(20) |  |  | generic_classification_code |  |
| 26 | `SUBCODE09` | CHAR(20) |  |  | generic_classification_code |  |
| 27 | `USERGENERICGROUPTYPECODE` | CHAR(10) |  |  |  |  |
| 28 | `SUBCODE10` | CHAR(20) |  |  | generic_classification_code |  |
| 29 | `COMPCOLORCODE` | CHAR(10) |  |  |  |  |
| 30 | `SKIPBOM` | SMALLINT | NOT NULL |  |  |  |
| 31 | `CONSUMPTION` | DECIMAL(9,5) |  |  |  |  |
| 32 | `WASTAGE` | DECIMAL(11,2) |  |  |  |  |
| 33 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKBOMCOMPONENTCOLORUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.WRKBOMCMPWRKBIOFMATCMYCODE,
       t.WRKBOMCMPWRKBIOFMATCRTISTAMP,
       t.WRKBOMCMPWRKBIOFMATPRDITCODE,
       t.WRKBOMCMPWRKBIOFMATSUBCODE01,
       t.WRKBOMCMPWRKBIOFMATSUBCODE02,
       t.WRKBOMCMPWRKBIOFMATSUBCODE03,
       t.WRKBOMCMPWRKBIOFMATSUBCODE04,
       t.WRKBOMCMPWRKBIOFMATSUBCODE05,
       t.WRKBOMCMPWRKBIOFMATSUBCODE06,
       t.WRKBOMCMPWRKBIOFMATSUBCODE07,
       t.WRKBOMCMPWRKBIOFMATSUBCODE08,
       t.WRKBOMCMPWRKBIOFMATSUBCODE09
FROM   DB2ADMIN.WRKBOMCOMPONENTCOLOR t
FETCH FIRST 100 ROWS ONLY;
```
