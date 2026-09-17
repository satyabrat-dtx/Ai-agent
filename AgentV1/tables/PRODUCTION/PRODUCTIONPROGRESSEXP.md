# DB2ADMIN.PRODUCTIONPROGRESSEXP

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPANYCODE`, `EXPPROGRESSNUMBER`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 83085

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPPROGRESSNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 4 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 5 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 7 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 8 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRODUCTIONPROGRESSEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPANYCODE,
       t.EXPPROGRESSNUMBER,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.ABSUNIQUEID,
       t.FATHERABSUNIQUEID,
       t.EVENTEXPDATETIME
FROM   DB2ADMIN.PRODUCTIONPROGRESSEXP t
FETCH FIRST 100 ROWS ONLY;
```
