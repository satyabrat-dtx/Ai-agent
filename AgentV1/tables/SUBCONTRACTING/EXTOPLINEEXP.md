# DB2ADMIN.EXTOPLINEEXP

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOP')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPANYCODE`, `EXPCOUNTERCODE`, `EXPCODE`, `EXPORDERLINE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 91700

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `EXPCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `EXPORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 5 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 7 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 9 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 10 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EXTOPLINEEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPANYCODE,
       t.EXPCOUNTERCODE,
       t.EXPCODE,
       t.EXPORDERLINE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.ABSUNIQUEID,
       t.FATHERABSUNIQUEID,
       t.EVENTEXPDATETIME
FROM   DB2ADMIN.EXTOPLINEEXP t
FETCH FIRST 100 ROWS ONLY;
```
