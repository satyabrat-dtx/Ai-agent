# DB2ADMIN.SALESINVOICEDISCOUNT

- **Module**: `SALES` (high confidence — table name starts with 'SALES')
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `COMPANYCODE`, `PROVISIONALCOUNTERCODE`, `PROVISIONALCODE`, `LINEORDERLINE`, `LINEORDERSUBLINE`, `LINECOMPONENTORDERLINE`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 7432

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
| 7 | `TYPE` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `DISCOUNTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 10 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `PAYMENTDISCOUNT` | SMALLINT | NOT NULL |  |  |  |
| 12 | `DISCOUNTGROUPCODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `TAXAPPLICATIONTYPE` | CHAR(2) |  |  |  |  |
| 14 | `DSCVALUEINDOCUMENTCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 15 | `DISCOUNTVALUEINCOMPANYCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `CALCULATIONTYPE` | CHAR(2) |  |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DISCOUNTGROUP_DISCOUNTGROUP` | `COMPANYCODE`, `DISCOUNTGROUPCODE` | [`DISCOUNTGROUP`](../SALES/DISCOUNTGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESINVOICEDISCOUNT.COMPANYCODE = DISCOUNTGROUP.COMPANYCODE AND SALESINVOICEDISCOUNT.DISCOUNTGROUPCODE = DISCOUNTGROUP.CODE` |
| `SALESDOCUMENTLINE_LINE` | `COMPANYCODE`, `PROVISIONALCOUNTERCODE`, `PROVISIONALCODE`, `LINEORDERLINE`, `LINEORDERSUBLINE`, `LINECOMPONENTORDERLINE` | [`SALESDOCUMENTLINE`](../SALES/SALESDOCUMENTLINE.md) | `SALESDOCUMENTCOMPANYCODE`, `SALDOCPROVISIONALCOUNTERCODE`, `SALESDOCUMENTPROVISIONALCODE`, `ORDERLINE`, `ORDERSUBLINE`, `COMPONENTORDERLINE` | RESTRICT | `SALESINVOICEDISCOUNT.COMPANYCODE = SALESDOCUMENTLINE.SALESDOCUMENTCOMPANYCODE AND SALESINVOICEDISCOUNT.PROVISIONALCOUNTERCODE = SALESDOCUMENTLINE.SALDOCPROVISIONALCOUNTERCODE AND SALESINVOICEDISCOUNT.PROVISIONALCODE = SALESDOCUMENTLINE.SALESDOCUMENTPROVISIONALCODE AND SALESINVOICEDISCOUNT.LINEORDERLINE = SALESDOCUMENTLINE.ORDERLINE AND SALESINVOICEDISCOUNT.LINEORDERSUBLINE = SALESDOCUMENTLINE.ORDERSUBLINE AND SALESINVOICEDISCOUNT.LINECOMPONENTORDERLINE = SALESDOCUMENTLINE.COMPONENTORDERLINE` |
| `SALESINVOICETOTAL_DISCOUNT` | `COMPANYCODE`, `PROVISIONALCOUNTERCODE`, `PROVISIONALCODE` | [`SALESINVOICETOTAL`](../SALES/SALESINVOICETOTAL.md) | `COMPANYCODE`, `INVOICEPROVISIONALCOUNTERCODE`, `INVOICEPROVISIONALCODE` | RESTRICT | `SALESINVOICEDISCOUNT.COMPANYCODE = SALESINVOICETOTAL.COMPANYCODE AND SALESINVOICEDISCOUNT.PROVISIONALCOUNTERCODE = SALESINVOICETOTAL.INVOICEPROVISIONALCOUNTERCODE AND SALESINVOICEDISCOUNT.PROVISIONALCODE = SALESINVOICETOTAL.INVOICEPROVISIONALCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESINVOICEDISCOUNTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PROVISIONALCOUNTERCODE,
       t.PROVISIONALCODE,
       t.LINEORDERLINE,
       t.LINEORDERSUBLINE,
       t.LINECOMPONENTORDERLINE,
       t.SEQUENCE,
       t.TYPE,
       t.DISCOUNTTYPE,
       t.VALUE,
       t.SIGN,
       t.PAYMENTDISCOUNT
FROM   DB2ADMIN.SALESINVOICEDISCOUNT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
