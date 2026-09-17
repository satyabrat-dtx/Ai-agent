# DB2ADMIN.SCHEDULESDOWNLOADPROGRESS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `ENVIRONMENTCODE`, `COMPANYCODE`, `PROGRESSNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 47227

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ENVIRONMENTCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `PROGRESSNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `PROGRESSTEMPLATECODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `ORIGINALENDDATE` | DATE |  |  |  |  |
| 5 | `EVERDOWNLOADED` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ENVIRONMENTCODE,
       t.PROGRESSNUMBER,
       t.PROGRESSTEMPLATECODE,
       t.ORIGINALENDDATE,
       t.EVERDOWNLOADED
FROM   DB2ADMIN.SCHEDULESDOWNLOADPROGRESS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
