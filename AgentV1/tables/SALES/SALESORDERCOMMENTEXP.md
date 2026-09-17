# DB2ADMIN.SALESORDERCOMMENTEXP

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `ENVIRONMENTCODE`, `EXPSALESORDERCOMPANYCODE`, `EXPSALESORDERCOUNTERCODE`, `EXPSALESORDERCODE`, `EXPORIGIN`, `EXPCODE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 90486

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPSALESORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPSALESORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `EXPSALESORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `EXPORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `EXPCODE` | CHAR(12) | NOT NULL | PK | primary_key |  |
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

- `SALESORDERCOMMENTEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPSALESORDERCOMPANYCODE,
       t.EXPSALESORDERCOUNTERCODE,
       t.EXPSALESORDERCODE,
       t.EXPORIGIN,
       t.EXPCODE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.ABSUNIQUEID,
       t.FATHERABSUNIQUEID,
       t.EVENTEXPDATETIME
FROM   DB2ADMIN.SALESORDERCOMMENTEXP t
FETCH FIRST 100 ROWS ONLY;
```
