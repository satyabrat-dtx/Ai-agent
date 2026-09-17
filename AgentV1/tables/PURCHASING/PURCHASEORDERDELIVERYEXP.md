# DB2ADMIN.PURCHASEORDERDELIVERYEXP

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `ENVIRONMENTCODE`, `EXPPURORDLINEPURORDCMYCODE`, `EXPPURORDLINEPURORDCNTCODE`, `EXPPURORDLINEPURORDERCODE`, `EXPPURCHASEORDERLINEORDERLINE`, `EXPPURORDERLINEORDERSUBLINE`, `EXPDELIVERYLINE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 78031

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPPURORDLINEPURORDCMYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPPURORDLINEPURORDCNTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `EXPPURORDLINEPURORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `EXPPURCHASEORDERLINEORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 5 | `EXPPURORDERLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 6 | `EXPDELIVERYLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 7 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 8 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 9 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 12 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASEORDERDELIVERYEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPPURORDLINEPURORDCMYCODE,
       t.EXPPURORDLINEPURORDCNTCODE,
       t.EXPPURORDLINEPURORDERCODE,
       t.EXPPURCHASEORDERLINEORDERLINE,
       t.EXPPURORDERLINEORDERSUBLINE,
       t.EXPDELIVERYLINE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.ABSUNIQUEID,
       t.FATHERABSUNIQUEID
FROM   DB2ADMIN.PURCHASEORDERDELIVERYEXP t
FETCH FIRST 100 ROWS ONLY;
```
