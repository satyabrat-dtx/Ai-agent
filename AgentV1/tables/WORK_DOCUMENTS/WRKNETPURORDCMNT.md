# DB2ADMIN.WRKNETPURORDCMNT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `CREATIONTIMESTAMP`, `LINENOCOM`, `COMPANYCODE`, `COUNTERCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 240145

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINENOCOM` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `DESCRIPTION` | LONG VARCHAR |  |  | description |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINENOCOM,
       t.DESCRIPTION,
       t.COMPANYCODE,
       t.COUNTERCODE,
       t.CODE
FROM   DB2ADMIN.WRKNETPURORDCMNT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
