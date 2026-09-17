# DB2ADMIN.WRKEXPNEGOTIATIONINVOICE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 177696

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 4 | `INVOICENUMBERDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 5 | `INVOICENUMBERCODE` | CHAR(20) |  |  |  |  |
| 6 | `CSMCODECUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 7 | `CSMCODECUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 8 | `ITEMTYPE` | CHAR(3) |  |  |  |  |
| 9 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 10 | `INVOICEDATE` | DATE |  |  |  |  |
| 11 | `INVOICEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 12 | `CURRENCY` | CHAR(4) |  |  |  |  |
| 13 | `CURRENTADJUSTMENT` | DECIMAL(18,5) |  |  |  |  |
| 14 | `FINDOCUMENTDATE` | DATE |  |  |  |  |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 16 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 17 | `CURRENTADJUSTMENTINDC` | DECIMAL(18,5) |  |  |  |  |
| 18 | `RECEIVEDVALUEINFGN` | DECIMAL(18,5) |  |  |  |  |
| 19 | `RECEIVEDVALUEININR` | DECIMAL(18,5) |  |  |  |  |
| 20 | `CLAIMFGN` | DECIMAL(18,5) |  |  |  |  |
| 21 | `BANKCHARGESFGN` | DECIMAL(18,5) |  |  |  |  |
| 22 | `TOTALUSEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 23 | `BALANCEINVVALUE` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKEXPNEGOTIATIONINVOICEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINENO,
       t.COMPANYCODE,
       t.CHOOSE,
       t.INVOICENUMBERDIVISIONCODE,
       t.INVOICENUMBERCODE,
       t.CSMCODECUSTOMERSUPPLIERTYPE,
       t.CSMCODECUSTOMERSUPPLIERCODE,
       t.ITEMTYPE,
       t.VALUE,
       t.INVOICEDATE,
       t.INVOICEVALUE
FROM   DB2ADMIN.WRKEXPNEGOTIATIONINVOICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
