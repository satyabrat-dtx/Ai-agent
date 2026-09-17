# DB2ADMIN.LOCKLINKEDOBJECT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `UNIQUEID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 194910

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `LOCKCOMPO` | SMALLINT | NOT NULL |  |  |  |
| 2 | `LOCKFLOW` | SMALLINT | NOT NULL |  |  |  |
| 3 | `LOCKBASELIST` | SMALLINT | NOT NULL |  |  |  |
| 4 | `LOCKQA` | SMALLINT | NOT NULL |  |  |  |
| 5 | `LOCKATTRIBUTEKEY2` | SMALLINT | NOT NULL |  |  |  |
| 6 | `LOCKATTRIBUTEKEY3` | SMALLINT | NOT NULL |  |  |  |
| 7 | `LOCKATTRIBUTEKEY4` | SMALLINT | NOT NULL |  |  |  |
| 8 | `LOCKATTRIBUTEKEY5` | SMALLINT | NOT NULL |  |  |  |
| 9 | `LOCKATTRIBUTEKEY6` | SMALLINT | NOT NULL |  |  |  |
| 10 | `LOCKATTRIBUTEKEY7` | SMALLINT | NOT NULL |  |  |  |
| 11 | `LOCKATTRIBUTEKEY8` | SMALLINT | NOT NULL |  |  |  |
| 12 | `LOCKATTRIBUTEKEY9` | SMALLINT | NOT NULL |  |  |  |
| 13 | `LOCKATTRIBUTEKEY10` | SMALLINT | NOT NULL |  |  |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 15 | `LOCKAPPROVALREQUESTROWS` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LOCKLINKEDOBJECTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.LOCKCOMPO,
       t.LOCKFLOW,
       t.LOCKBASELIST,
       t.LOCKQA,
       t.LOCKATTRIBUTEKEY2,
       t.LOCKATTRIBUTEKEY3,
       t.LOCKATTRIBUTEKEY4,
       t.LOCKATTRIBUTEKEY5,
       t.LOCKATTRIBUTEKEY6,
       t.LOCKATTRIBUTEKEY7,
       t.LOCKATTRIBUTEKEY8
FROM   DB2ADMIN.LOCKLINKEDOBJECT t
FETCH FIRST 100 ROWS ONLY;
```
