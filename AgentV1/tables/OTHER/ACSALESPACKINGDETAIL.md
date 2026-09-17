# DB2ADMIN.ACSALESPACKINGDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `ACSALESPACKINGCOMPANYCODE`, `ACSALESPACKINGCODE`, `CONTAINERITEMTYPECODE`, `CONTAINERSUBCODE01`, `CONTAINERELEMENTCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 42258

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ACSALESPACKINGCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `ACSALESPACKINGCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `CONTAINERITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `CONTAINERSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `CONTAINERELEMENTCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ACSALESPACKINGCOMPANYCODE,
       t.ACSALESPACKINGCODE,
       t.CONTAINERITEMTYPECODE,
       t.CONTAINERSUBCODE01,
       t.CONTAINERELEMENTCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.ACSALESPACKINGDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
