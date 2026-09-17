# DB2ADMIN.FINEXPNEGOTIATIONINVOICE

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `LINENO`, `COMPANYCODE`, `NEGOTIATIONCODE`, `INVOICEDIVISIONCODE`, `INVOICECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 176819

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `NEGOTIATIONCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `INVOICEDIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `INVOICECODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `CUSTOMERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 5 | `CUSTOMERCUSTOMERSUPPLIERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 6 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `FCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `INRVALUE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `INVOICEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 10 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 11 | `FINDOCUMENTDATE` | DATE |  |  |  |  |
| 12 | `SHIPMENTDATE` | DATE |  |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 20 | `INVOICEVALUECC` | DECIMAL(18,5) |  |  |  |  |
| 21 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 22 | `RECEIVEDVALUEINFGN` | DECIMAL(18,5) |  |  |  |  |
| 23 | `RECEIVEDVALUEININR` | DECIMAL(18,5) |  |  |  |  |
| 24 | `CLAIMFGN` | DECIMAL(18,5) |  |  |  |  |
| 25 | `BANKCHARGESFGN` | DECIMAL(18,5) |  |  |  |  |
| 26 | `TOTALUSEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 27 | `BALANCEINVVALUE` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `FINEXPNEGOTIATIONINVOICE.CURRENCYCODE = CURRENCY.CODE` |
| `FINEXPNEGOTIATION_NEGOTIATION` | `COMPANYCODE`, `NEGOTIATIONCODE` | [`FINEXPNEGOTIATION`](../FINANCE/FINEXPNEGOTIATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINEXPNEGOTIATIONINVOICE.COMPANYCODE = FINEXPNEGOTIATION.COMPANYCODE AND FINEXPNEGOTIATIONINVOICE.NEGOTIATIONCODE = FINEXPNEGOTIATION.CODE` |
| `ORDERPARTNER_CUSTOMER` | `COMPANYCODE`, `CUSTOMERCUSTOMERSUPPLIERTYPE`, `CUSTOMERCUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `FINEXPNEGOTIATIONINVOICE.COMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND FINEXPNEGOTIATIONINVOICE.CUSTOMERCUSTOMERSUPPLIERTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND FINEXPNEGOTIATIONINVOICE.CUSTOMERCUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINEXPNEGOTIATIONINVOICEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.NEGOTIATIONCODE,
       t.INVOICEDIVISIONCODE,
       t.INVOICECODE,
       t.CUSTOMERCUSTOMERSUPPLIERTYPE,
       t.CUSTOMERCUSTOMERSUPPLIERCODE,
       t.ITEMTYPECODE,
       t.FCVALUE,
       t.INRVALUE,
       t.INVOICEVALUE,
       t.CURRENCYCODE,
       t.FINDOCUMENTDATE
FROM   DB2ADMIN.FINEXPNEGOTIATIONINVOICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
