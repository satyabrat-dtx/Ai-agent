# DB2ADMIN.PLANLISTQUEUE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `TABLEINDEX`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 42668

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TABLEINDEX` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `SALSALORDLINESALORDCNTCODE` | CHAR(8) |  |  |  |  |
| 3 | `SALSALORDERLINESALESORDERCODE` | CHAR(15) |  |  |  |  |
| 4 | `SALESSALESORDERLINEORDERLINE` | DECIMAL(5,0) |  |  |  |  |
| 5 | `SALSALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 6 | `SALSALORDLINECMPORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 7 | `SALESDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 8 | `PRODUCTIONCODE` | CHAR(15) |  |  |  |  |
| 9 | `EXPLOSIONFAMILYCODE` | BIGINT | NOT NULL |  |  |  |
| 10 | `FORCED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `USERAPPROVALISNEEDED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `USERAPPROVEAFTERCOPY` | SMALLINT | NOT NULL |  |  |  |
| 13 | `HIGHPRIORITY` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.TABLEINDEX,
       t.COMPANYCODE,
       t.SALSALORDLINESALORDCNTCODE,
       t.SALSALORDERLINESALESORDERCODE,
       t.SALESSALESORDERLINEORDERLINE,
       t.SALSALESORDERLINEORDERSUBLINE,
       t.SALSALORDLINECMPORDERLINE,
       t.SALESDELIVERYLINE,
       t.PRODUCTIONCODE,
       t.EXPLOSIONFAMILYCODE,
       t.FORCED,
       t.USERAPPROVALISNEEDED
FROM   DB2ADMIN.PLANLISTQUEUE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
