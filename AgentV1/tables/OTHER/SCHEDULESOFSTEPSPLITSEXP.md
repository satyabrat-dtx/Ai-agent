# DB2ADMIN.SCHEDULESOFSTEPSPLITSEXP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPANYCODE`, `EXPCOUNTERCODE`, `EXPCODE`, `EXPSTEPNUMBER`, `EXPSUBSTEP`, `EXPREPROCESS`, `EXPHIGHLEVELSCHEDULE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 86345

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `EXPCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `EXPSTEPNUMBER` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 5 | `EXPSUBSTEP` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `EXPREPROCESS` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `EXPHIGHLEVELSCHEDULE` | SMALLINT | NOT NULL | PK | primary_key |  |
| 8 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 9 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 10 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 13 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SCHEDULESOFSTEPSPLITSEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPANYCODE,
       t.EXPCOUNTERCODE,
       t.EXPCODE,
       t.EXPSTEPNUMBER,
       t.EXPSUBSTEP,
       t.EXPREPROCESS,
       t.EXPHIGHLEVELSCHEDULE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.ABSUNIQUEID
FROM   DB2ADMIN.SCHEDULESOFSTEPSPLITSEXP t
FETCH FIRST 100 ROWS ONLY;
```
