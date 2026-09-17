# DB2ADMIN.SALESORDERDELIVERYEXP

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `ENVIRONMENTCODE`, `EXPSALORDLINESALORDCMYCODE`, `EXPSALORDLINESALORDCNTCODE`, `EXPSALORDERLINESALESORDERCODE`, `EXPSALESORDERLINEORDERLINE`, `EXPSALESORDERLINEORDERSUBLINE`, `EXPSALORDLINECMPORDERLINE`, `EXPDELIVERYLINE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 78307

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPSALORDLINESALORDCMYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPSALORDLINESALORDCNTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `EXPSALORDERLINESALESORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `EXPSALESORDERLINEORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 5 | `EXPSALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 6 | `EXPSALORDLINECMPORDERLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 7 | `EXPDELIVERYLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
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

- `SALESORDERDELIVERYEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPSALORDLINESALORDCMYCODE,
       t.EXPSALORDLINESALORDCNTCODE,
       t.EXPSALORDERLINESALESORDERCODE,
       t.EXPSALESORDERLINEORDERLINE,
       t.EXPSALESORDERLINEORDERSUBLINE,
       t.EXPSALORDLINECMPORDERLINE,
       t.EXPDELIVERYLINE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.ABSUNIQUEID
FROM   DB2ADMIN.SALESORDERDELIVERYEXP t
FETCH FIRST 100 ROWS ONLY;
```
