# DB2ADMIN.RECIPEEXP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPANYCODE`, `EXPNUMBERID`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 86259

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPNUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 3 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 4 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 5 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 7 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 8 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |
| 9 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 10 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 11 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 12 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RECIPEEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPANYCODE,
       t.EXPNUMBERID,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.ABSUNIQUEID,
       t.FATHERABSUNIQUEID,
       t.EVENTEXPDATETIME,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01
FROM   DB2ADMIN.RECIPEEXP t
FETCH FIRST 100 ROWS ONLY;
```
