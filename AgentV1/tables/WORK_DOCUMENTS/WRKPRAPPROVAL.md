# DB2ADMIN.WRKPRAPPROVAL

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `COMPANYCODE`, `REQUISITIONTEMPLATECODE`, `CODE`, `CREATIONUSER`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 130061

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `REQUISITIONTEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 4 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 5 | `UMCODE` | CHAR(3) |  |  |  |  |
| 6 | `STOCKQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 7 | `AVGCONQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 8 | `PENDINGPRQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 9 | `PENDINGPOQUANTITY` | DECIMAL(15,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.REQUISITIONTEMPLATECODE,
       t.CODE,
       t.CREATIONUSER,
       t.CREATIONTIMESTAMP,
       t.UMCODE,
       t.STOCKQUANTITY,
       t.AVGCONQUANTITY,
       t.PENDINGPRQUANTITY,
       t.PENDINGPOQUANTITY
FROM   DB2ADMIN.WRKPRAPPROVAL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
