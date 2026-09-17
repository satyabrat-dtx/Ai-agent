# DB2ADMIN.ORDERPARTNEREXP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `ENVIRONMENTCODE`, `EXPCUSTOMERSUPPLIERCOMPANYCODE`, `EXPCUSTOMERSUPPLIERTYPE`, `EXPCUSTOMERSUPPLIERCODE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 77537

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCUSTOMERSUPPLIERCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPCUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 3 | `EXPCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 5 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 6 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 8 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 9 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ORDERPARTNEREXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCUSTOMERSUPPLIERCOMPANYCODE,
       t.EXPCUSTOMERSUPPLIERTYPE,
       t.EXPCUSTOMERSUPPLIERCODE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.ABSUNIQUEID,
       t.FATHERABSUNIQUEID,
       t.EVENTEXPDATETIME
FROM   DB2ADMIN.ORDERPARTNEREXP t
FETCH FIRST 100 ROWS ONLY;
```
