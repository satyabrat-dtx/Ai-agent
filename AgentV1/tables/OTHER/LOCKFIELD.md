# DB2ADMIN.LOCKFIELD

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `UNIQUEID`, `ENTITYNAME`, `FIELDNAME`, `ACTIVITYCODE`, `SEQNO`, `PARENTUNIQUEID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 212838

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `ENTITYNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 2 | `FIELDNAME` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 3 | `ACTIVITYCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `SEQNO` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 5 | `ISATTRIBUTE` | SMALLINT | NOT NULL |  |  |  |
| 6 | `ITEMSTLINKPOSITION` | INTEGER | NOT NULL |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 8 | `PARENTUNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LOCKFIELDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.ENTITYNAME,
       t.FIELDNAME,
       t.ACTIVITYCODE,
       t.SEQNO,
       t.ISATTRIBUTE,
       t.ITEMSTLINKPOSITION,
       t.ABSUNIQUEID,
       t.PARENTUNIQUEID
FROM   DB2ADMIN.LOCKFIELD t
FETCH FIRST 100 ROWS ONLY;
```
