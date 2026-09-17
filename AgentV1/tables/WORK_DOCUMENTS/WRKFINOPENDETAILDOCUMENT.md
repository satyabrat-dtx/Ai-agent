# DB2ADMIN.WRKFINOPENDETAILDOCUMENT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 67
- **Primary key**: `COMPANYCODE`, `LINENO`, `BUSINESSUNITCODE`, `BUSINESSUNITCODE1`, `FINANCIALYEARCODE`, `DOCUMENTTEMPLATECODE`, `DOCUMENTCODE`, `LINENUMBER`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 203863

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 3 | `BUSINESSUNITCODE1` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 4 | `FINANCIALYEARCODE` | DECIMAL(4,0) | NOT NULL | PK | primary_key |  |
| 5 | `DOCUMENTTEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `DOCUMENTCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 7 | `POSTINGDATE` | DATE |  |  |  |  |
| 8 | `LINENUMBER` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 9 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 10 | `DOCUMENTDATE` | DATE |  |  |  |  |
| 11 | `CREDITLINE` | SMALLINT | NOT NULL |  |  |  |
| 12 | `GLCODE` | CHAR(20) |  |  |  |  |
| 13 | `DUEDATE` | DATE |  |  |  |  |
| 14 | `GLDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 15 | `AMOUNTINCC` | DECIMAL(18,5) |  |  |  |  |
| 16 | `AMOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 17 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 18 | `COMPANYCURRENCYCODE` | CHAR(10) |  |  |  |  |
| 19 | `DOCUMENTCURRENCYCODE` | CHAR(10) |  |  |  |  |
| 20 | `SLCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 21 | `CUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 22 | `SLCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 23 | `CUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 24 | `ORDERPARTNERCODE` | CHAR(8) |  |  |  |  |
| 25 | `SLCUSTOMERSUPPLIERDESC` | VARCHAR(270) |  |  |  |  |
| 26 | `CUSTOMERSUPPLIERDESC` | VARCHAR(270) |  |  |  |  |
| 27 | `ORDERPARTNERDESC` | VARCHAR(270) |  |  |  |  |
| 28 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 29 | `CHEQUENUMBER` | CHAR(20) |  |  |  |  |
| 30 | `CHEQUEDATE` | DATE |  |  |  |  |
| 31 | `COMMERCIALINVOICECODE` | CHAR(20) |  |  |  |  |
| 32 | `COMMERCIALINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 33 | `PLANTINVOICECODE` | CHAR(20) |  |  |  |  |
| 34 | `PLANTINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 35 | `CLEAREDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 36 | `POADVANCEPURORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 37 | `POADVANCEPURCHASEORDERCODE` | CHAR(20) |  |  |  |  |
| 38 | `POADVANCELINENO` | INTEGER | NOT NULL |  |  |  |
| 39 | `MRNDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 40 | `MRNCODE` | DECIMAL(11,0) |  |  |  |  |
| 41 | `MRNMRNPREFIXCODE` | CHAR(3) |  |  |  |  |
| 42 | `PURCHASEINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 43 | `PURCHASEINVOICECODE` | CHAR(25) |  |  |  |  |
| 44 | `PURCHASEINVOICEINVOICEDATE` | DATE |  |  |  |  |
| 45 | `CUSTOMERREFNO` | CHAR(20) |  |  |  |  |
| 46 | `CUSTOMERREFNODATE` | DATE |  |  |  |  |
| 47 | `DIRECTINVOICEDIVCODE` | CHAR(3) |  |  |  |  |
| 48 | `DIRECTINVOICECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 49 | `DIRECTINVOICECODE` | CHAR(15) |  |  |  |  |
| 50 | `DOCUMENTTYPECODE` | CHAR(3) |  |  |  |  |
| 51 | `DAYSDIFF` | INTEGER | NOT NULL |  |  |  |
| 52 | `REFERENCETEXT1` | CHAR(100) |  |  |  |  |
| 53 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 54 | `INVOICENO` | CHAR(25) |  |  |  |  |
| 55 | `INVOICEDATE` | DATE |  |  |  |  |
| 56 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 57 | `EXPENSEINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 58 | `EXPENSEINVOICEORDPRNCSMSUPTE` | CHAR(1) |  |  |  |  |
| 59 | `EXPENSEINVOICEORDPRNCSMSUPCOD` | CHAR(8) |  |  |  |  |
| 60 | `EXPENSEINVOICECODE` | CHAR(25) |  |  |  |  |
| 61 | `EXPENSEINVOICEINVOICEDATE` | DATE |  |  |  |  |
| 62 | `DOCTEMPDESC` | CHAR(200) |  |  |  |  |
| 63 | `OUTSTANDBYDC` | DECIMAL(18,5) |  |  |  |  |
| 64 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 65 | `COSTCENTERDESC` | CHAR(200) |  |  |  |  |
| 66 | `PROFITCENTERCODE` | CHAR(10) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINOPENDETAILDOCUMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.LINENO,
       t.BUSINESSUNITCODE,
       t.BUSINESSUNITCODE1,
       t.FINANCIALYEARCODE,
       t.DOCUMENTTEMPLATECODE,
       t.DOCUMENTCODE,
       t.POSTINGDATE,
       t.LINENUMBER,
       t.CREATIONTIMESTAMP,
       t.DOCUMENTDATE,
       t.CREDITLINE
FROM   DB2ADMIN.WRKFINOPENDETAILDOCUMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
