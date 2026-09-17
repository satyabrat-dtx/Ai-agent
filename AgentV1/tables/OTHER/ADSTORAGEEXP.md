# DB2ADMIN.ADSTORAGEEXP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `ENVIRONMENTCODE`, `EXPUNIQUEID`, `EXPNAMEENTITYNAME`, `EXPNAMENAME`, `EXPFIELDNAME`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 76000

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPUNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `EXPNAMEENTITYNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `EXPNAMENAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 4 | `EXPFIELDNAME` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 5 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 7 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 9 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 10 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ADSTORAGEEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPUNIQUEID,
       t.EXPNAMEENTITYNAME,
       t.EXPNAMENAME,
       t.EXPFIELDNAME,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.ABSUNIQUEID,
       t.FATHERABSUNIQUEID,
       t.EVENTEXPDATETIME
FROM   DB2ADMIN.ADSTORAGEEXP t
FETCH FIRST 100 ROWS ONLY;
```
