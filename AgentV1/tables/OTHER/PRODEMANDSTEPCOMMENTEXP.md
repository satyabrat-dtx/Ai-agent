# DB2ADMIN.PRODEMANDSTEPCOMMENTEXP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `ENVIRONMENTCODE`, `EXPPRODEMANDSTEPPDCOMPANYCODE`, `EXPPRODEMANDSTEPPDCOUNTERCODE`, `EXPPRODUCTIONDEMANDSTEPPDCODE`, `EXPPRODEMANDSTEPSTEPNUMBER`, `EXPORIGIN`, `EXPCODE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 117134

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPPRODEMANDSTEPPDCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPPRODEMANDSTEPPDCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `EXPPRODUCTIONDEMANDSTEPPDCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `EXPPRODEMANDSTEPSTEPNUMBER` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 5 | `EXPORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `EXPCODE` | CHAR(12) | NOT NULL | PK | primary_key |  |
| 7 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 8 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 9 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 10 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 11 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRODEMANDSTEPCOMMENTEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPPRODEMANDSTEPPDCOMPANYCODE,
       t.EXPPRODEMANDSTEPPDCOUNTERCODE,
       t.EXPPRODUCTIONDEMANDSTEPPDCODE,
       t.EXPPRODEMANDSTEPSTEPNUMBER,
       t.EXPORIGIN,
       t.EXPCODE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.FATHERABSUNIQUEID,
       t.EVENTEXPDATETIME
FROM   DB2ADMIN.PRODEMANDSTEPCOMMENTEXP t
FETCH FIRST 100 ROWS ONLY;
```
