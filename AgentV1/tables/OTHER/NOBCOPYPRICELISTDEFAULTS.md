# DB2ADMIN.NOBCOPYPRICELISTDEFAULTS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 7145

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TEMPLATEORDERTYPE` | CHAR(1) |  |  |  |  |
| 2 | `TEMPLATEDEFINITIONTYPE` | CHAR(1) |  |  |  |  |
| 3 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 4 | `ORDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 5 | `ORDERLINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 6 | `ASRDEFTEMPLATEORDERTYPE` | CHAR(1) |  |  |  |  |
| 7 | `ASRDEFINITIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 8 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 9 | `ORDPRNGRPSTDORDGRPTYPEORDTYPE` | CHAR(1) |  |  |  |  |
| 10 | `ORDPRNGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 11 | `ORDERPARTNERGROUPCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TEMPLATEORDERTYPE,
       t.TEMPLATEDEFINITIONTYPE,
       t.TEMPLATECODE,
       t.ORDERTEMPLATECODE,
       t.ORDERLINETEMPLATECODE,
       t.ASRDEFTEMPLATEORDERTYPE,
       t.ASRDEFINITIONTEMPLATECODE,
       t.QUALITYLEVELCODE,
       t.ORDPRNGRPSTDORDGRPTYPEORDTYPE,
       t.ORDPRNGRPSTDORDGROUPTYPECODE,
       t.ORDERPARTNERGROUPCODE
FROM   DB2ADMIN.NOBCOPYPRICELISTDEFAULTS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
