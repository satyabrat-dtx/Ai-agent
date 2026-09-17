# DB2ADMIN.SALESDOCUMENTEXP

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPANYCODE`, `EXPPROVISIONALCOUNTERCODE`, `EXPPROVISIONALCODE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 78215

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPPROVISIONALCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `EXPPROVISIONALCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 5 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 6 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 8 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 9 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESDOCUMENTEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPANYCODE,
       t.EXPPROVISIONALCOUNTERCODE,
       t.EXPPROVISIONALCODE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.ABSUNIQUEID,
       t.FATHERABSUNIQUEID,
       t.EVENTEXPDATETIME
FROM   DB2ADMIN.SALESDOCUMENTEXP t
FETCH FIRST 100 ROWS ONLY;
```
