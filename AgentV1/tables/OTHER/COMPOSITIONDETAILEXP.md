# DB2ADMIN.COMPOSITIONDETAILEXP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPOSITIONCOMPANYCODE`, `EXPCOMPOSITIONCODE`, `EXPSUBCOMPOSITION`, `EXPTOUSE`, `EXPSEQUENCE`, `EXPCOMPONENTCODE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 76210

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPOSITIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPCOMPOSITIONCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 3 | `EXPSUBCOMPOSITION` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 4 | `EXPTOUSE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 5 | `EXPSEQUENCE` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `EXPCOMPONENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
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

- `COMPOSITIONDETAILEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPOSITIONCOMPANYCODE,
       t.EXPCOMPOSITIONCODE,
       t.EXPSUBCOMPOSITION,
       t.EXPTOUSE,
       t.EXPSEQUENCE,
       t.EXPCOMPONENTCODE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.ABSUNIQUEID,
       t.FATHERABSUNIQUEID
FROM   DB2ADMIN.COMPOSITIONDETAILEXP t
FETCH FIRST 100 ROWS ONLY;
```
