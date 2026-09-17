# DB2ADMIN.SALESRELEASELINEEXP

- **Module**: `SALES` (high confidence — table name starts with 'SALES')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPANYCODE`, `EXPCODE`, `EXPLINE`, `EXPSUBLINE`, `EXPCOMPONENTRELEASELINE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 78450

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `EXPLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 4 | `EXPSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 5 | `EXPCOMPONENTRELEASELINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 6 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 7 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 8 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 10 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 11 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESRELEASELINEEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPANYCODE,
       t.EXPCODE,
       t.EXPLINE,
       t.EXPSUBLINE,
       t.EXPCOMPONENTRELEASELINE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.ABSUNIQUEID,
       t.FATHERABSUNIQUEID,
       t.EVENTEXPDATETIME
FROM   DB2ADMIN.SALESRELEASELINEEXP t
FETCH FIRST 100 ROWS ONLY;
```
