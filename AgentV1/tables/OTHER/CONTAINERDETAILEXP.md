# DB2ADMIN.CONTAINERDETAILEXP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `ENVIRONMENTCODE`, `EXPCONTAINERCOMPANYCODE`, `EXPCONTAINERITEMTYPECODE`, `EXPCONTAINERSUBCODE01`, `EXPLINE`, `EXPSUBLINE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 76259

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCONTAINERCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPCONTAINERITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `EXPCONTAINERSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `EXPLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `EXPSUBLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 7 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 8 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 9 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 10 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CONTAINERDETAILEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCONTAINERCOMPANYCODE,
       t.EXPCONTAINERITEMTYPECODE,
       t.EXPCONTAINERSUBCODE01,
       t.EXPLINE,
       t.EXPSUBLINE,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.FATHERABSUNIQUEID,
       t.EVENTEXPDATETIME,
       t.ABSUNIQUEID
FROM   DB2ADMIN.CONTAINERDETAILEXP t
FETCH FIRST 100 ROWS ONLY;
```
