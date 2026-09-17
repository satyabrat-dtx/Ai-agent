# DB2ADMIN.WRKFINTAXREGISTERPRINT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 85
- **Primary key**: `CREATIONTIME`, `LINENO`, `DETAILLINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 178620

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIME` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `DETAILLINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `ITAXCODE1` | CHAR(3) |  |  |  |  |
| 5 | `BASICVALUE1` | DECIMAL(18,5) |  |  |  |  |
| 6 | `PERCENTAGE1` | DECIMAL(9,5) |  |  |  |  |
| 7 | `PERCENTAGEVALUE1` | DECIMAL(18,5) |  |  |  |  |
| 8 | `ITAXCODE2` | CHAR(3) |  |  |  |  |
| 9 | `BASICVALUE2` | DECIMAL(18,5) |  |  |  |  |
| 10 | `PERCENTAGE2` | DECIMAL(9,5) |  |  |  |  |
| 11 | `PERCENTAGEVALUE2` | DECIMAL(18,5) |  |  |  |  |
| 12 | `ITAXCODE3` | CHAR(3) |  |  |  |  |
| 13 | `BASICVALUE3` | DECIMAL(18,5) |  |  |  |  |
| 14 | `PERCENTAGE3` | DECIMAL(9,5) |  |  |  |  |
| 15 | `PERCENTAGEVALUE3` | DECIMAL(18,5) |  |  |  |  |
| 16 | `ITAXCODE4` | CHAR(3) |  |  |  |  |
| 17 | `BASICVALUE4` | DECIMAL(18,5) |  |  |  |  |
| 18 | `PERCENTAGE4` | DECIMAL(9,5) |  |  |  |  |
| 19 | `PERCENTAGEVALUE4` | DECIMAL(18,5) |  |  |  |  |
| 20 | `ITAXCODE5` | CHAR(3) |  |  |  |  |
| 21 | `BASICVALUE5` | DECIMAL(18,5) |  |  |  |  |
| 22 | `PERCENTAGE5` | DECIMAL(9,5) |  |  |  |  |
| 23 | `PERCENTAGEVALUE5` | DECIMAL(18,5) |  |  |  |  |
| 24 | `ITAXCODE6` | CHAR(3) |  |  |  |  |
| 25 | `BASICVALUE6` | DECIMAL(18,5) |  |  |  |  |
| 26 | `PERCENTAGE6` | DECIMAL(9,5) |  |  |  |  |
| 27 | `PERCENTAGEVALUE6` | DECIMAL(18,5) |  |  |  |  |
| 28 | `ITAXCODE7` | CHAR(3) |  |  |  |  |
| 29 | `BASICVALUE7` | DECIMAL(18,5) |  |  |  |  |
| 30 | `PERCENTAGE7` | DECIMAL(9,5) |  |  |  |  |
| 31 | `PERCENTAGEVALUE7` | DECIMAL(18,5) |  |  |  |  |
| 32 | `ITAXCODE8` | CHAR(3) |  |  |  |  |
| 33 | `BASICVALUE8` | DECIMAL(18,5) |  |  |  |  |
| 34 | `PERCENTAGE8` | DECIMAL(9,5) |  |  |  |  |
| 35 | `PERCENTAGEVALUE8` | DECIMAL(18,5) |  |  |  |  |
| 36 | `ITAXCODE9` | CHAR(3) |  |  |  |  |
| 37 | `BASICVALUE9` | DECIMAL(18,5) |  |  |  |  |
| 38 | `PERCENTAGE9` | DECIMAL(9,5) |  |  |  |  |
| 39 | `PERCENTAGEVALUE9` | DECIMAL(18,5) |  |  |  |  |
| 40 | `ITAXCODE10` | CHAR(3) |  |  |  |  |
| 41 | `BASICVALUE10` | DECIMAL(18,5) |  |  |  |  |
| 42 | `PERCENTAGE10` | DECIMAL(9,5) |  |  |  |  |
| 43 | `PERCENTAGEVALUE10` | DECIMAL(18,5) |  |  |  |  |
| 44 | `ITAXCODE11` | CHAR(3) |  |  |  |  |
| 45 | `BASICVALUE11` | DECIMAL(18,5) |  |  |  |  |
| 46 | `PERCENTAGE11` | DECIMAL(9,5) |  |  |  |  |
| 47 | `PERCENTAGEVALUE11` | DECIMAL(18,5) |  |  |  |  |
| 48 | `ITAXCODE12` | CHAR(3) |  |  |  |  |
| 49 | `BASICVALUE12` | DECIMAL(18,5) |  |  |  |  |
| 50 | `PERCENTAGE12` | DECIMAL(9,5) |  |  |  |  |
| 51 | `PERCENTAGEVALUE12` | DECIMAL(18,5) |  |  |  |  |
| 52 | `ITAXCODE13` | CHAR(3) |  |  |  |  |
| 53 | `BASICVALUE13` | DECIMAL(18,5) |  |  |  |  |
| 54 | `PERCENTAGE13` | DECIMAL(9,5) |  |  |  |  |
| 55 | `PERCENTAGEVALUE13` | DECIMAL(18,5) |  |  |  |  |
| 56 | `ITAXCODE14` | CHAR(3) |  |  |  |  |
| 57 | `BASICVALUE14` | DECIMAL(18,5) |  |  |  |  |
| 58 | `PERCENTAGE14` | DECIMAL(9,5) |  |  |  |  |
| 59 | `PERCENTAGEVALUE14` | DECIMAL(18,5) |  |  |  |  |
| 60 | `ITAXCODE15` | CHAR(3) |  |  |  |  |
| 61 | `BASICVALUE15` | DECIMAL(18,5) |  |  |  |  |
| 62 | `PERCENTAGE15` | DECIMAL(9,5) |  |  |  |  |
| 63 | `PERCENTAGEVALUE15` | DECIMAL(18,5) |  |  |  |  |
| 64 | `ITAXCODE16` | CHAR(3) |  |  |  |  |
| 65 | `BASICVALUE16` | DECIMAL(18,5) |  |  |  |  |
| 66 | `PERCENTAGE16` | DECIMAL(9,5) |  |  |  |  |
| 67 | `PERCENTAGEVALUE16` | DECIMAL(18,5) |  |  |  |  |
| 68 | `ITAXCODE17` | CHAR(3) |  |  |  |  |
| 69 | `BASICVALUE17` | DECIMAL(18,5) |  |  |  |  |
| 70 | `PERCENTAGE17` | DECIMAL(9,5) |  |  |  |  |
| 71 | `PERCENTAGEVALUE17` | DECIMAL(18,5) |  |  |  |  |
| 72 | `ITAXCODE18` | CHAR(3) |  |  |  |  |
| 73 | `BASICVALUE18` | DECIMAL(18,5) |  |  |  |  |
| 74 | `PERCENTAGE18` | DECIMAL(9,5) |  |  |  |  |
| 75 | `PERCENTAGEVALUE18` | DECIMAL(18,5) |  |  |  |  |
| 76 | `ITAXCODE19` | CHAR(3) |  |  |  |  |
| 77 | `BASICVALUE19` | DECIMAL(18,5) |  |  |  |  |
| 78 | `PERCENTAGE19` | DECIMAL(9,5) |  |  |  |  |
| 79 | `PERCENTAGEVALUE19` | DECIMAL(18,5) |  |  |  |  |
| 80 | `ITAXCODE20` | CHAR(3) |  |  |  |  |
| 81 | `BASICVALUE20` | DECIMAL(18,5) |  |  |  |  |
| 82 | `PERCENTAGE20` | DECIMAL(9,5) |  |  |  |  |
| 83 | `PERCENTAGEVALUE20` | DECIMAL(18,5) |  |  |  |  |
| 84 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINTAXREGISTERPRINTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIME,
       t.LINENO,
       t.DETAILLINENO,
       t.CODE,
       t.ITAXCODE1,
       t.BASICVALUE1,
       t.PERCENTAGE1,
       t.PERCENTAGEVALUE1,
       t.ITAXCODE2,
       t.BASICVALUE2,
       t.PERCENTAGE2,
       t.PERCENTAGEVALUE2
FROM   DB2ADMIN.WRKFINTAXREGISTERPRINT t
FETCH FIRST 100 ROWS ONLY;
```
