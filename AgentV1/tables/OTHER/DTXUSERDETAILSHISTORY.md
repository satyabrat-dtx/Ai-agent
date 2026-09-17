# DB2ADMIN.DTXUSERDETAILSHISTORY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `DTXUSERDETAILSUSERID`, `VALIDFROM`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 238654

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DTXUSERDETAILSUSERID` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `VALIDFROM` | TIMESTAMP | NOT NULL | PK | primary_key | Inclusive start of a validity period. |
| 2 | `PASSWORD` | VARCHAR(100) | NOT NULL |  |  |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DTXUSERDETAILS_HISTORY` | `DTXUSERDETAILSUSERID` | [`DTXUSERDETAILS`](../OTHER/DTXUSERDETAILS.md) | `USERID` | RESTRICT | `DTXUSERDETAILSHISTORY.DTXUSERDETAILSUSERID = DTXUSERDETAILS.USERID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DTXUSERDETAILSHISTORYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DTXUSERDETAILSUSERID,
       t.VALIDFROM,
       t.PASSWORD,
       t.ABSUNIQUEID
FROM   DB2ADMIN.DTXUSERDETAILSHISTORY t
FETCH FIRST 100 ROWS ONLY;
```
