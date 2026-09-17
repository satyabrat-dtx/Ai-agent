# DB2ADMIN.SCDC_MAIL_SET_LIST

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `MSL_IDENTIFIER`, `MSL_WORKSTATION`, `MSL_MAIL_GROUP_NAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189554

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MSL_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `MSL_WORKSTATION` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 2 | `MSL_MAIL_GROUP_NAME` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `MSL_USER_ID` | VARCHAR(120) |  |  |  |  |
| 4 | `MSL_PASSWORD` | VARCHAR(50) |  |  |  |  |
| 5 | `MSL_RECIPIENT` | VARCHAR(2000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.MSL_IDENTIFIER,
       t.MSL_WORKSTATION,
       t.MSL_MAIL_GROUP_NAME,
       t.MSL_USER_ID,
       t.MSL_PASSWORD,
       t.MSL_RECIPIENT
FROM   DB2ADMIN.SCDC_MAIL_SET_LIST t
FETCH FIRST 100 ROWS ONLY;
```
