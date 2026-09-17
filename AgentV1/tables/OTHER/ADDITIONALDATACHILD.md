# DB2ADMIN.ADDITIONALDATACHILD

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `ADDITIONALDATAGROUPCOMPANYCODE`, `ADDITIONALDATAGROUPCODE`, `ADDITIONALDATAGROUPENTITYNAME`, `LABELLABEL`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 29148

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ADDITIONALDATAGROUPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `ADDITIONALDATAGROUPCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `ADDITIONALDATAGROUPENTITYNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `LABELLABEL` | CHAR(50) | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ADDITIONALDATAGROUPCOMPANYCODE,
       t.ADDITIONALDATAGROUPCODE,
       t.ADDITIONALDATAGROUPENTITYNAME,
       t.LABELLABEL
FROM   DB2ADMIN.ADDITIONALDATACHILD t
FETCH FIRST 100 ROWS ONLY;
```
