# DB2ADMIN.WRKGATEENTRYCREATOR

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `CREATIONTIMESTAMP`, `LINENO`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 222207

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `SALESDOCPROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 5 | `SALESDOCPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 6 | `PLANTINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 7 | `PLANTINVOICECODE` | CHAR(15) |  |  |  |  |
| 8 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 9 | `INVOICEDATE` | DATE |  |  |  |  |
| 10 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 11 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 12 | `ORDERPARTNERBRANDCODE` | CHAR(8) |  |  |  |  |
| 13 | `LEGALNAME` | CHAR(100) |  |  |  |  |
| 14 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 15 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 16 | `INTDOCPROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 17 | `INTDOCUMENTPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 18 | `PROVISIONALDOCUMENTDATE` | DATE |  |  |  |  |
| 19 | `GROSSWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 20 | `NETTWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 21 | `TOTALNUMBEROFBALES` | DECIMAL(3,0) |  |  |  |  |
| 22 | `TOTALQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 23 | `HEADERDATA` | BLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINENO,
       t.CHOOSE,
       t.COMPANYCODE,
       t.SALESDOCPROVISIONALCOUNTERCODE,
       t.SALESDOCPROVISIONALCODE,
       t.PLANTINVOICEDIVISIONCODE,
       t.PLANTINVOICECODE,
       t.UOMCODE,
       t.INVOICEDATE,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE
FROM   DB2ADMIN.WRKGATEENTRYCREATOR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
