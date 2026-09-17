# DB2ADMIN.WRKLOCKCOSTSFROMACCOUNTING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `COMPANYCODE`, `ELEMENTITEMTYPECODE`, `ELEMENTSUBCODE01`, `PERIODYEAR`, `PERIODCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 238395

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ELEMENTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `ELEMENTITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `ELEMENTSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `PERIODYEAR` | DECIMAL(4,0) | NOT NULL | PK | primary_key |  |
| 5 | `PERIODCODE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 6 | `ROWISLOCKED` | SMALLINT | NOT NULL |  |  |  |
| 7 | `LOCKEDTIME` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ELEMENTCOMPANYCODE,
       t.ELEMENTITEMTYPECODE,
       t.ELEMENTSUBCODE01,
       t.PERIODYEAR,
       t.PERIODCODE,
       t.ROWISLOCKED,
       t.LOCKEDTIME
FROM   DB2ADMIN.WRKLOCKCOSTSFROMACCOUNTING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
