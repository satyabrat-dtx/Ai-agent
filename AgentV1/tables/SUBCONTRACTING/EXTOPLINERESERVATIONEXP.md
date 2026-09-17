# DB2ADMIN.EXTOPLINERESERVATIONEXP

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOP')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `ENVIRONMENTCODE`, `EXPEXTOPLINECOMPANYCODE`, `EXPEXTOPLINECOUNTERCODE`, `EXPEXTOPLINECODE`, `EXPEXTOPLINEORDERLINE`, `EXPRESERVATIONORDERCOUNTERCODE`, `EXPRESERVATIONORDERCODE`, `EXPRESERVATIONRESERVATIONLINE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 237959

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPEXTOPLINECOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPEXTOPLINECOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `EXPEXTOPLINECODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `EXPEXTOPLINEORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 5 | `EXPRESERVATIONORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 6 | `EXPRESERVATIONORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 7 | `EXPRESERVATIONRESERVATIONLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 8 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 9 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 10 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 11 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 12 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EXTOPLINERESERVATIONEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPEXTOPLINECOMPANYCODE,
       t.EXPEXTOPLINECOUNTERCODE,
       t.EXPEXTOPLINECODE,
       t.EXPEXTOPLINEORDERLINE,
       t.EXPRESERVATIONORDERCOUNTERCODE,
       t.EXPRESERVATIONORDERCODE,
       t.EXPRESERVATIONRESERVATIONLINE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.FATHERABSUNIQUEID
FROM   DB2ADMIN.EXTOPLINERESERVATIONEXP t
FETCH FIRST 100 ROWS ONLY;
```
