# DB2ADMIN.ORDERCONTACTPEOPLE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `UNIQUEID`, `REPORTTYPE`, `PERSONTYPE`, `PERSONUNIQUEID`, `PERSONCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 26142

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `REPORTTYPE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `PERSONTYPE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 3 | `PERSONUNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 4 | `PERSONCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ORDERCONTACTPEOPLEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.REPORTTYPE,
       t.PERSONTYPE,
       t.PERSONUNIQUEID,
       t.PERSONCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ORDERCONTACTPEOPLE t
FETCH FIRST 100 ROWS ONLY;
```
