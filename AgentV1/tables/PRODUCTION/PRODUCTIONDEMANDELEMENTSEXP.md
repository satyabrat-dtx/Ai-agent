# DB2ADMIN.PRODUCTIONDEMANDELEMENTSEXP

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPANYCODE`, `EXPDEMANDCOUNTERCODE`, `EXPDEMANDCODE`, `EXPITEMTYPEAFICODE`, `EXPELEMENTSUBCODEKEY`, `EXPELEMENTCODE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 109043

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPDEMANDCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `EXPDEMANDCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `EXPITEMTYPEAFICODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `EXPELEMENTSUBCODEKEY` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 6 | `EXPELEMENTCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
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

- `PRODEMANDELEMENTSEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPANYCODE,
       t.EXPDEMANDCOUNTERCODE,
       t.EXPDEMANDCODE,
       t.EXPITEMTYPEAFICODE,
       t.EXPELEMENTSUBCODEKEY,
       t.EXPELEMENTCODE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.FATHERABSUNIQUEID,
       t.EVENTEXPDATETIME
FROM   DB2ADMIN.PRODUCTIONDEMANDELEMENTSEXP t
FETCH FIRST 100 ROWS ONLY;
```
