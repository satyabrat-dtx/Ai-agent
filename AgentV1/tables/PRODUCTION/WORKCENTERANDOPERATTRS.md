# DB2ADMIN.WORKCENTERANDOPERATTRS

- **Module**: `PRODUCTION` (high confidence — table name starts with 'WORKCENTER')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPANYCODE`, `EXPWORKCENTERCODE`, `EXPOPERATIONCODE`, `EXPCODE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 78737

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPWORKCENTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `EXPOPERATIONCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `EXPCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 5 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 6 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 7 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 9 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 10 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WORKCENTERANDOPERATTRSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPANYCODE,
       t.EXPWORKCENTERCODE,
       t.EXPOPERATIONCODE,
       t.EXPCODE,
       t.UNIQUEIDPK,
       t.OPERATIONTYPE,
       t.STATUS,
       t.ABSUNIQUEID,
       t.FATHERABSUNIQUEID,
       t.EVENTEXPDATETIME
FROM   DB2ADMIN.WORKCENTERANDOPERATTRS t
FETCH FIRST 100 ROWS ONLY;
```
