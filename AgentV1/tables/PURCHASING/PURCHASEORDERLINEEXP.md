# DB2ADMIN.PURCHASEORDERLINEEXP

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `ENVIRONMENTCODE`, `EXPPURCHASEORDERCOMPANYCODE`, `EXPPURCHASEORDERCOUNTERCODE`, `EXPPURCHASEORDERCODE`, `EXPORDERLINE`, `EXPORDERSUBLINE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 78123

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPPURCHASEORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPPURCHASEORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `EXPPURCHASEORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `EXPORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 5 | `EXPORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
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

- `PURCHASEORDERLINEEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPPURCHASEORDERCOMPANYCODE,
       t.EXPPURCHASEORDERCOUNTERCODE,
       t.EXPPURCHASEORDERCODE,
       t.EXPORDERLINE,
       t.EXPORDERSUBLINE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.ABSUNIQUEID,
       t.FATHERABSUNIQUEID,
       t.EVENTEXPDATETIME
FROM   DB2ADMIN.PURCHASEORDERLINEEXP t
FETCH FIRST 100 ROWS ONLY;
```
