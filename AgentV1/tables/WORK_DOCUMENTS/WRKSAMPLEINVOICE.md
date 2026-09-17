# DB2ADMIN.WRKSAMPLEINVOICE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `LINENO`, `COMPANYCODE`, `DIVISIONCODE`, `PLANTINVOICECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 146242

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 3 | `PLANTINVOICECODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `AMOUNT` | DECIMAL(15,5) |  |  |  |  |
| 5 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 6 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 7 | `RATE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `PRODUCTDESCRIPTION` | VARCHAR(250) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.LINENO,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.PLANTINVOICECODE,
       t.AMOUNT,
       t.QUANTITY,
       t.UOMCODE,
       t.RATE,
       t.PRODUCTDESCRIPTION
FROM   DB2ADMIN.WRKSAMPLEINVOICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
