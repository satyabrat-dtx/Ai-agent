# DB2ADMIN.NOWDESCRIPTIONCHANGE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `ENTITYNAME`, `FULLENTITYNAME`, `ENTITYKEY`, `CHECKCODE`, `GROUPTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 106631

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENTITYNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `FULLENTITYNAME` | CHAR(70) | NOT NULL | PK | primary_key |  |
| 2 | `ENTITYKEY` | CHAR(140) | NOT NULL | PK | primary_key |  |
| 3 | `CHECKCODE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 4 | `GROUPTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ENTITYNAME,
       t.FULLENTITYNAME,
       t.ENTITYKEY,
       t.CHECKCODE,
       t.GROUPTYPECODE
FROM   DB2ADMIN.NOWDESCRIPTIONCHANGE t
FETCH FIRST 100 ROWS ONLY;
```
