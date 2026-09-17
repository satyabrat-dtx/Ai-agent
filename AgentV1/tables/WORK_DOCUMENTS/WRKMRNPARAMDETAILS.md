# DB2ADMIN.WRKMRNPARAMDETAILS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `CREATIONSTAMPTIME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 181922

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONSTAMPTIME` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `MRNPREFIXCODE` | CHAR(3) |  |  |  |  |
| 4 | `MRNDATE` | DATE |  |  |  |  |
| 5 | `MAINGATEENTRYDATE` | DATE |  |  |  |  |
| 6 | `MAINGATEENTRYSRNO` | CHAR(15) |  |  |  |  |
| 7 | `WEIGHTATINVOICEGROSS` | DECIMAL(18,5) |  |  |  |  |
| 8 | `WEIGHTATMILLWAREHOUSEGROSS` | DECIMAL(18,5) |  |  |  |  |
| 9 | `INVOICENO` | CHAR(25) |  |  |  |  |
| 10 | `INVOICEDATE` | DATE |  |  |  |  |
| 11 | `CHALLANNO` | CHAR(25) |  |  |  |  |
| 12 | `CHALLANDATE` | DATE |  |  |  |  |
| 13 | `INITIALEXTOPHEADERCODE` | CHAR(15) |  |  |  |  |
| 14 | `INITIALEXTOPHEADERCOUNTERCODE` | CHAR(15) |  |  |  |  |
| 15 | `INITIALEXTOPLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 16 | `PROCESSNAME` | CHAR(100) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONSTAMPTIME,
       t.DIVISIONCODE,
       t.MRNPREFIXCODE,
       t.MRNDATE,
       t.MAINGATEENTRYDATE,
       t.MAINGATEENTRYSRNO,
       t.WEIGHTATINVOICEGROSS,
       t.WEIGHTATMILLWAREHOUSEGROSS,
       t.INVOICENO,
       t.INVOICEDATE,
       t.CHALLANNO
FROM   DB2ADMIN.WRKMRNPARAMDETAILS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
