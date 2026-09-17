# DB2ADMIN.SALESORDERLINECOMMENTEXP

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `ENVIRONMENTCODE`, `EXPSALORDLINESALORDCMYCODE`, `EXPSALORDLINESALORDCNTCODE`, `EXPSALORDERLINESALESORDERCODE`, `EXPSALESORDERLINEORDERLINE`, `EXPSALESORDERLINEORDERSUBLINE`, `EXPSALORDLINECMPORDERLINE`, `EXPORIGIN`, `EXPCODE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 90533

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
| 7 | `EXPORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 8 | `EXPCODE` | CHAR(12) | NOT NULL | PK | primary_key |  |
| 9 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 10 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 11 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 14 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESORDERLINECOMMENTEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPSALORDLINESALORDCMYCODE,
       t.EXPSALORDLINESALORDCNTCODE,
       t.EXPSALORDERLINESALESORDERCODE,
       t.EXPSALESORDERLINEORDERLINE,
       t.EXPSALESORDERLINEORDERSUBLINE,
       t.EXPSALORDLINECMPORDERLINE,
       t.EXPORIGIN,
       t.EXPCODE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK
FROM   DB2ADMIN.SALESORDERLINECOMMENTEXP t
FETCH FIRST 100 ROWS ONLY;
```
