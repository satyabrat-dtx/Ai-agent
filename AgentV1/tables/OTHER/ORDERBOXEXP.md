# DB2ADMIN.ORDERBOXEXP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPANYCODE`, `EXPORDERTYPE`, `EXPORDERCOUNTERCODE`, `EXPORDERCODE`, `EXPITEMTYPECODE`, `EXPCONTAINERSUBCODE01`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 77488

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPORDERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 3 | `EXPORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `EXPORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 5 | `EXPITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `EXPCONTAINERSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
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

- `ORDERBOXEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPANYCODE,
       t.EXPORDERTYPE,
       t.EXPORDERCOUNTERCODE,
       t.EXPORDERCODE,
       t.EXPITEMTYPECODE,
       t.EXPCONTAINERSUBCODE01,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.ABSUNIQUEID,
       t.FATHERABSUNIQUEID
FROM   DB2ADMIN.ORDERBOXEXP t
FETCH FIRST 100 ROWS ONLY;
```
