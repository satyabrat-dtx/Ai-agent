# DB2ADMIN.PURCHASERETURNDOCUMENTEXP

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPANYCODE`, `EXPCODE`, `EXPLINE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 117044

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `EXPLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
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

- `PURCHASERETURNDOCUMENTEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPANYCODE,
       t.EXPCODE,
       t.EXPLINE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.FATHERABSUNIQUEID,
       t.EVENTEXPDATETIME,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PURCHASERETURNDOCUMENTEXP t
FETCH FIRST 100 ROWS ONLY;
```
