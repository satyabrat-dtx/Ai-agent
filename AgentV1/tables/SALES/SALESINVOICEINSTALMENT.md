# DB2ADMIN.SALESINVOICEINSTALMENT

- **Module**: `SALES` (high confidence — table name starts with 'SALES')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPANYCODE`, `PROVISIONALCOUNTERCODE`, `PROVISIONALCODE`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 23499

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PROVISIONALCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PROVISIONALCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 4 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 5 | `PAYMENTMETHODTYPE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `MATURITYATSIGHT` | SMALLINT | NOT NULL |  |  |  |
| 7 | `INSTALMENTVALUEINCMYCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 8 | `INSTALMENTVALUEINDOCCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `INCOMINGAMOUNTDATE` | DATE |  |  |  |  |
| 14 | `INCOMINGAMOUNTINCMYCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 15 | `INCOMINGAMOUNTINDOCCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `SALESINVOICETOTAL_INVOICEINSTALMENT` | `COMPANYCODE`, `PROVISIONALCOUNTERCODE`, `PROVISIONALCODE` | [`SALESINVOICETOTAL`](../SALES/SALESINVOICETOTAL.md) | `COMPANYCODE`, `INVOICEPROVISIONALCOUNTERCODE`, `INVOICEPROVISIONALCODE` | RESTRICT | `SALESINVOICEINSTALMENT.COMPANYCODE = SALESINVOICETOTAL.COMPANYCODE AND SALESINVOICEINSTALMENT.PROVISIONALCOUNTERCODE = SALESINVOICETOTAL.INVOICEPROVISIONALCOUNTERCODE AND SALESINVOICEINSTALMENT.PROVISIONALCODE = SALESINVOICETOTAL.INVOICEPROVISIONALCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESINVOICEINSTALMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PROVISIONALCOUNTERCODE,
       t.PROVISIONALCODE,
       t.LINE,
       t.EXPIRATIONDATE,
       t.PAYMENTMETHODTYPE,
       t.MATURITYATSIGHT,
       t.INSTALMENTVALUEINCMYCURRENCY,
       t.INSTALMENTVALUEINDOCCURRENCY,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.SALESINVOICEINSTALMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
