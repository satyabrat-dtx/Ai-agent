# DB2ADMIN.WRKFINORDERPARTNERTRANSACTION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 71
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 226244

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `TRANSACTIONNO` | CHAR(20) |  |  |  |  |
| 4 | `GLCODE` | CHAR(25) |  |  |  |  |
| 5 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 6 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 7 | `LEGALNAME1` | VARCHAR(270) |  |  |  |  |
| 8 | `ORIGINBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 9 | `ORIGINFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 10 | `ORIGINDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 11 | `ORIGINSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 12 | `ORIGINCODE` | CHAR(15) |  |  |  |  |
| 13 | `ORIGINLINENUMBER` | DECIMAL(7,0) |  |  |  |  |
| 14 | `ORIGINAMOUNTINCC` | DECIMAL(18,5) |  |  |  |  |
| 15 | `ORIGINAMOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 16 | `ORIGINCLEAREDAMOUNTINCC` | DECIMAL(18,5) |  |  |  |  |
| 17 | `ORGINDOCUMENTCURRENCY` | CHAR(4) |  |  |  |  |
| 18 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 19 | `POSTINGDATE` | DATE |  |  |  |  |
| 20 | `DUEDATE` | DATE |  |  |  |  |
| 21 | `DESTBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 22 | `DESTFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 23 | `DESTDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 24 | `DESTSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 25 | `DESTCODE` | CHAR(15) |  |  |  |  |
| 26 | `DESTLINENUMBER` | DECIMAL(7,0) |  |  |  |  |
| 27 | `DESTAMOUNTINCC` | DECIMAL(18,5) |  |  |  |  |
| 28 | `DESTAMOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 29 | `DESTDOCUMENTCURRENCY` | CHAR(4) |  |  |  |  |
| 30 | `DESTCLEAREDAMOUNTINCC` | DECIMAL(18,5) |  |  |  |  |
| 31 | `DESTPOSTINGDATE` | DATE |  |  |  |  |
| 32 | `DESTEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 33 | `DESTDUEDATE` | DATE |  |  |  |  |
| 34 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 35 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 36 | `MRNNO` | DECIMAL(11,0) |  |  |  |  |
| 37 | `POADVANCEPURORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 38 | `POADVANCEPURCHASEORDERCODE` | CHAR(25) |  |  |  |  |
| 39 | `POADVANCELINE` | INTEGER | NOT NULL |  |  |  |
| 40 | `DOCUMENTDATE` | DATE |  |  |  |  |
| 41 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 42 | `PLANTINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 43 | `PLANTINVOICECODE` | CHAR(15) |  |  |  |  |
| 44 | `COMMERCIALINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 45 | `COMMERCIALINVOICECODE` | CHAR(20) |  |  |  |  |
| 46 | `DIRECTINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 47 | `DIRECTINVOICECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 48 | `DIRECTINVOICECODE` | CHAR(15) |  |  |  |  |
| 49 | `DIRECTINVOICENUMBER` | CHAR(25) |  |  |  |  |
| 50 | `DIRECTINVOICEDATE` | DATE |  |  |  |  |
| 51 | `PURCHASEINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 52 | `PURINVOICEORDPRNCSMSUPTYPE` | CHAR(1) |  |  |  |  |
| 53 | `PURINVOICEORDPRNCSMSUPCODE` | CHAR(8) |  |  |  |  |
| 54 | `PURCHASEINVOICECODE` | CHAR(25) |  |  |  |  |
| 55 | `PURCHASEINVOICEINVOICEDATE` | DATE |  |  |  |  |
| 56 | `EXPENSEINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 57 | `EXPENSEINVOICEORDPRNCSMSUPTE` | CHAR(1) |  |  |  |  |
| 58 | `EXPENSEINVOICEORDPRNCSMSUPCOD` | CHAR(8) |  |  |  |  |
| 59 | `EXPENSEINVOICECODE` | CHAR(25) |  |  |  |  |
| 60 | `EXPENSEINVOICEINVOICEDATE` | DATE |  |  |  |  |
| 61 | `REMAININGAMOUNTINCC` | DECIMAL(18,5) |  |  |  |  |
| 62 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 63 | `PURCHASEORDERCODE` | CHAR(25) |  |  |  |  |
| 64 | `REFERENCENO` | CHAR(100) |  |  |  |  |
| 65 | `SALESORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 66 | `SALESORDERCODE` | CHAR(25) |  |  |  |  |
| 67 | `TDSDEDUCTION` | DECIMAL(18,5) |  |  |  |  |
| 68 | `TDSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 69 | `CLEAREDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 70 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINORDPRNTRANSACTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINENO,
       t.TRANSACTIONNO,
       t.GLCODE,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.LEGALNAME1,
       t.ORIGINBUSINESSUNITCODE,
       t.ORIGINFINANCIALYEARCODE,
       t.ORIGINDOCUMENTTEMPLATECODE,
       t.ORIGINSTATISTICALGROUPCODE
FROM   DB2ADMIN.WRKFINORDERPARTNERTRANSACTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
