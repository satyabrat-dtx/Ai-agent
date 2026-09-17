# DB2ADMIN.ALLOCATIONEXP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPANYCODE`, `EXPCODE`, `EXPLINENUMBER`, `EXPCOMPONENTLINENUMBER`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 76045

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `EXPLINENUMBER` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 4 | `EXPCOMPONENTLINENUMBER` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
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

- `ALLOCATIONEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPANYCODE,
       t.EXPCODE,
       t.EXPLINENUMBER,
       t.EXPCOMPONENTLINENUMBER,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.ABSUNIQUEID,
       t.FATHERABSUNIQUEID,
       t.EVENTEXPDATETIME
FROM   DB2ADMIN.ALLOCATIONEXP t
FETCH FIRST 100 ROWS ONLY;
```
