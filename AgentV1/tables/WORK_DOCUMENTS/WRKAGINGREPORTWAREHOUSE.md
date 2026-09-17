# DB2ADMIN.WRKAGINGREPORTWAREHOUSE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `WAREHOUSEGROUPCODE`, `LINENO`, `PHYSICALWAREHOUSE`, `LOGICALWAREHOUSE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 147159

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `WAREHOUSEGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `LOGICALWAREHOUSE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `PHYSICALWAREHOUSE` | CHAR(8) | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.WAREHOUSEGROUPCODE,
       t.LINENO,
       t.LOGICALWAREHOUSE,
       t.PHYSICALWAREHOUSE
FROM   DB2ADMIN.WRKAGINGREPORTWAREHOUSE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
