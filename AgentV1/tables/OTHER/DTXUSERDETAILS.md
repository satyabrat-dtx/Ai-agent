# DB2ADMIN.DTXUSERDETAILS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `USERID`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 238617

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `USERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `FAILSCOUNT` | INTEGER | NOT NULL |  |  |  |
| 2 | `PASSWORD` | VARCHAR(100) | NOT NULL |  |  |  |
| 3 | `IDENTIFIER` | CHAR(20) |  |  |  |  |
| 4 | `SUSPENDED` | SMALLINT | NOT NULL |  |  |  |
| 5 | `DATEPASSSTART` | DATE | NOT NULL |  |  |  |
| 6 | `PASSEXPIRED` | SMALLINT | NOT NULL |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `DTXUSERDETAILS_HISTORY` | [`DTXUSERDETAILSHISTORY`](../OTHER/DTXUSERDETAILSHISTORY.md) | `DTXUSERDETAILSUSERID` | `DTXUSERDETAILSHISTORY.DTXUSERDETAILSUSERID = DTXUSERDETAILS.USERID` |

## Indexes

- `DTXUSERDETAILSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.USERID,
       t.FAILSCOUNT,
       t.PASSWORD,
       t.IDENTIFIER,
       t.SUSPENDED,
       t.DATEPASSSTART,
       t.PASSEXPIRED,
       t.ABSUNIQUEID
FROM   DB2ADMIN.DTXUSERDETAILS t
FETCH FIRST 100 ROWS ONLY;
```
