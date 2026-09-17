# DB2ADMIN.ABSACTIVELOCK

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `LOCKTYPE`, `JNDINAME`, `ENTITYKEY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 70239

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LOCKTYPE` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `JNDINAME` | CHAR(100) | NOT NULL | PK | primary_key |  |
| 2 | `ENTITYKEY` | VARCHAR(250) | NOT NULL | PK | primary_key |  |
| 3 | `USERID` | CHAR(50) |  |  |  |  |
| 4 | `IPADDRESS` | CHAR(20) |  |  |  |  |
| 5 | `HTMLSESSIONID` | VARCHAR(250) | NOT NULL |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSACTIVELOCKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.LOCKTYPE,
       t.JNDINAME,
       t.ENTITYKEY,
       t.USERID,
       t.IPADDRESS,
       t.HTMLSESSIONID,
       t.CREATIONDATETIME,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSACTIVELOCK t
FETCH FIRST 100 ROWS ONLY;
```
