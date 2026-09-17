# DB2ADMIN.SALESINVOICETAX

- **Module**: `SALES` (high confidence — table name starts with 'SALES')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `PROVISIONALCOUNTERCODE`, `PROVISIONALCODE`, `TAXCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 25015

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PROVISIONALCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PROVISIONALCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `TAXCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `RATE` | DECIMAL(6,3) |  |  |  |  |
| 5 | `TAXABLEINCOMEINDOCCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 6 | `TAXABLEINCOMEINCOMPANYCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 7 | `HDRDISCOUNTINDOCUMENTCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 8 | `HEADERDISCOUNTINCMPCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 9 | `TAXVALUEINDOCUMENTCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 10 | `TAXVALUEINCOMPANYCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `SALESINVOICETOTAL_INVOICETAX` | `COMPANYCODE`, `PROVISIONALCOUNTERCODE`, `PROVISIONALCODE` | [`SALESINVOICETOTAL`](../SALES/SALESINVOICETOTAL.md) | `COMPANYCODE`, `INVOICEPROVISIONALCOUNTERCODE`, `INVOICEPROVISIONALCODE` | RESTRICT | `SALESINVOICETAX.COMPANYCODE = SALESINVOICETOTAL.COMPANYCODE AND SALESINVOICETAX.PROVISIONALCOUNTERCODE = SALESINVOICETOTAL.INVOICEPROVISIONALCOUNTERCODE AND SALESINVOICETAX.PROVISIONALCODE = SALESINVOICETOTAL.INVOICEPROVISIONALCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESINVOICETAXUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PROVISIONALCOUNTERCODE,
       t.PROVISIONALCODE,
       t.TAXCODE,
       t.RATE,
       t.TAXABLEINCOMEINDOCCURRENCY,
       t.TAXABLEINCOMEINCOMPANYCURRENCY,
       t.HDRDISCOUNTINDOCUMENTCURRENCY,
       t.HEADERDISCOUNTINCMPCURRENCY,
       t.TAXVALUEINDOCUMENTCURRENCY,
       t.TAXVALUEINCOMPANYCURRENCY,
       t.CREATIONDATETIME
FROM   DB2ADMIN.SALESINVOICETAX t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
