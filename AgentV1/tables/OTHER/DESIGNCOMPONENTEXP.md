# DB2ADMIN.DESIGNCOMPONENTEXP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `ENVIRONMENTCODE`, `EXPDESIGNCOMPANYCODE`, `EXPDESIGNNUMBERID`, `EXPVARIANTCODE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 196675

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPDESIGNCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPDESIGNNUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 3 | `EXPVARIANTCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 5 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 6 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 7 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 8 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DESIGNCOMPONENTEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPDESIGNCOMPANYCODE,
       t.EXPDESIGNNUMBERID,
       t.EXPVARIANTCODE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.FATHERABSUNIQUEID,
       t.EVENTEXPDATETIME,
       t.ABSUNIQUEID
FROM   DB2ADMIN.DESIGNCOMPONENTEXP t
FETCH FIRST 100 ROWS ONLY;
```
