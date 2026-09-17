# DB2ADMIN.SALESINVOICECOMMISSION

- **Module**: `SALES` (high confidence — table name starts with 'SALES')
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `PROVISIONALCOUNTERCODE`, `PROVISIONALCODE`, `LINEORDERLINE`, `LINEORDERSUBLINE`, `LINECOMPONENTORDERLINE`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 785

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PROVISIONALCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PROVISIONALCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINEORDERLINE` | DECIMAL(7,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `LINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `LINECOMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `SEQUENCE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 7 | `AGENTCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `COMMISSIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `COMMISSIONVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 10 | `COMMISSIONSIGN` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `CMSVALUEINDOCUMENTCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 12 | `CMSVALUEINCOMPANYCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 13 | `TAXABLEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `AGENT_AGENT` | `COMPANYCODE`, `AGENTCODE` | [`AGENT`](../CORE_MASTER/AGENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESINVOICECOMMISSION.COMPANYCODE = AGENT.COMPANYCODE AND SALESINVOICECOMMISSION.AGENTCODE = AGENT.CODE` |
| `SALESDOCUMENTLINE_LINE` | `COMPANYCODE`, `PROVISIONALCOUNTERCODE`, `PROVISIONALCODE`, `LINEORDERLINE`, `LINEORDERSUBLINE`, `LINECOMPONENTORDERLINE` | [`SALESDOCUMENTLINE`](../SALES/SALESDOCUMENTLINE.md) | `SALESDOCUMENTCOMPANYCODE`, `SALDOCPROVISIONALCOUNTERCODE`, `SALESDOCUMENTPROVISIONALCODE`, `ORDERLINE`, `ORDERSUBLINE`, `COMPONENTORDERLINE` | RESTRICT | `SALESINVOICECOMMISSION.COMPANYCODE = SALESDOCUMENTLINE.SALESDOCUMENTCOMPANYCODE AND SALESINVOICECOMMISSION.PROVISIONALCOUNTERCODE = SALESDOCUMENTLINE.SALDOCPROVISIONALCOUNTERCODE AND SALESINVOICECOMMISSION.PROVISIONALCODE = SALESDOCUMENTLINE.SALESDOCUMENTPROVISIONALCODE AND SALESINVOICECOMMISSION.LINEORDERLINE = SALESDOCUMENTLINE.ORDERLINE AND SALESINVOICECOMMISSION.LINEORDERSUBLINE = SALESDOCUMENTLINE.ORDERSUBLINE AND SALESINVOICECOMMISSION.LINECOMPONENTORDERLINE = SALESDOCUMENTLINE.COMPONENTORDERLINE` |
| `SALESINVOICETOTAL_COMMISSION` | `COMPANYCODE`, `PROVISIONALCOUNTERCODE`, `PROVISIONALCODE` | [`SALESINVOICETOTAL`](../SALES/SALESINVOICETOTAL.md) | `COMPANYCODE`, `INVOICEPROVISIONALCOUNTERCODE`, `INVOICEPROVISIONALCODE` | RESTRICT | `SALESINVOICECOMMISSION.COMPANYCODE = SALESINVOICETOTAL.COMPANYCODE AND SALESINVOICECOMMISSION.PROVISIONALCOUNTERCODE = SALESINVOICETOTAL.INVOICEPROVISIONALCOUNTERCODE AND SALESINVOICECOMMISSION.PROVISIONALCODE = SALESINVOICETOTAL.INVOICEPROVISIONALCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESINVOICECOMMISSIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PROVISIONALCOUNTERCODE,
       t.PROVISIONALCODE,
       t.LINEORDERLINE,
       t.LINEORDERSUBLINE,
       t.LINECOMPONENTORDERLINE,
       t.SEQUENCE,
       t.AGENTCODE,
       t.COMMISSIONTYPE,
       t.COMMISSIONVALUE,
       t.COMMISSIONSIGN,
       t.CMSVALUEINDOCUMENTCURRENCY
FROM   DB2ADMIN.SALESINVOICECOMMISSION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
