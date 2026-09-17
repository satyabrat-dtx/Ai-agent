# DB2ADMIN.BUSINESSPARTNEREXP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `ENVIRONMENTCODE`, `EXPNUMBERID`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 76132

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPNUMBERID` | DECIMAL(8,0) | NOT NULL | PK | primary_key |  |
| 2 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 3 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 4 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 6 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 7 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BUSINESSPARTNEREXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPNUMBERID,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.ABSUNIQUEID,
       t.FATHERABSUNIQUEID,
       t.EVENTEXPDATETIME
FROM   DB2ADMIN.BUSINESSPARTNEREXP t
FETCH FIRST 100 ROWS ONLY;
```
