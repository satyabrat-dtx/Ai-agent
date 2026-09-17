# DB2ADMIN.WRKSALESPRICELISTPRINT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 10616

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 3 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `SALPRCLISTDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 5 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 6 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 7 | `PRICELISTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 8 | `PRICELISTTYPE` | CHAR(2) |  |  |  |  |
| 9 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 10 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 11 | `DISCOUNTCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 12 | `DISCOUNTDESCRIPTION` | VARCHAR(120) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.SALPRCLISTDEFINITIONNUMBERID,
       t.ORDERTYPE,
       t.PRICELISTCODE,
       t.PRICELISTDESCRIPTION,
       t.PRICELISTTYPE,
       t.CURRENCYCODE,
       t.EXCHANGERATE,
       t.DISCOUNTCATEGORYCODE
FROM   DB2ADMIN.WRKSALESPRICELISTPRINT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
