# DB2ADMIN.SALESORDERLINEEXP

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `ENVIRONMENTCODE`, `EXPSALESORDERCOMPANYCODE`, `EXPSALESORDERCOUNTERCODE`, `EXPSALESORDERCODE`, `EXPORDERLINE`, `EXPORDERSUBLINE`, `EXPCOMPONENTORDERLINE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 78401

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPSALESORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPSALESORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `EXPSALESORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `EXPORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 5 | `EXPORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 6 | `EXPCOMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
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

- `SALESORDERLINEEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPSALESORDERCOMPANYCODE,
       t.EXPSALESORDERCOUNTERCODE,
       t.EXPSALESORDERCODE,
       t.EXPORDERLINE,
       t.EXPORDERSUBLINE,
       t.EXPCOMPONENTORDERLINE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.ABSUNIQUEID,
       t.FATHERABSUNIQUEID
FROM   DB2ADMIN.SALESORDERLINEEXP t
FETCH FIRST 100 ROWS ONLY;
```
