# DB2ADMIN.DESIGNEXP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPANYCODE`, `EXPNUMBERID`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 196718

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPNUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 3 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 4 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 5 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 8 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 10 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 11 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 12 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DESIGNEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPANYCODE,
       t.EXPNUMBERID,
       t.OPERATIONTYPE,
       t.STATUS,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUFFIXCODE,
       t.UNIQUEIDPK,
       t.FATHERABSUNIQUEID
FROM   DB2ADMIN.DESIGNEXP t
FETCH FIRST 100 ROWS ONLY;
```
