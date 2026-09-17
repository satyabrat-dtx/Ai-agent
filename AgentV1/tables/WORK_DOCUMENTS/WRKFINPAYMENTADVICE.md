# DB2ADMIN.WRKFINPAYMENTADVICE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 66
- **Primary key**: `LINENUMBER`, `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 224237

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 4 | `LINENUMBER` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 5 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 6 | `DOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 7 | `FINANCEMONTHCODE` | INTEGER | NOT NULL |  |  |  |
| 8 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 9 | `DOCUMENTCODE` | CHAR(15) |  |  |  |  |
| 10 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 11 | `GLCODE` | CHAR(20) |  |  |  |  |
| 12 | `CURRENTSTATUS` | CHAR(2) |  |  |  |  |
| 13 | `SLCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 14 | `SLCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 15 | `AMOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 16 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 17 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 18 | `AMOUNTINCC` | DECIMAL(18,5) |  |  |  |  |
| 19 | `COMPANYCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 20 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 21 | `PROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 22 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 23 | `COMMENTS` | VARCHAR(255) |  |  |  |  |
| 24 | `REFERENCETEXT1` | CHAR(50) |  |  |  |  |
| 25 | `REFERENCETEXT2` | CHAR(50) |  |  |  |  |
| 26 | `REFERENCETEXT3` | CHAR(50) |  |  |  |  |
| 27 | `REFERENCETEXT4` | CHAR(50) |  |  |  |  |
| 28 | `REFERENCEAMT1` | DECIMAL(18,5) |  |  |  |  |
| 29 | `REFERENCEAMT2` | DECIMAL(18,5) |  |  |  |  |
| 30 | `REFERENCEAMT3` | DECIMAL(18,5) |  |  |  |  |
| 31 | `REFERENCEAMT4` | DECIMAL(18,5) |  |  |  |  |
| 32 | `REFERENCEAMT5` | DECIMAL(18,5) |  |  |  |  |
| 33 | `HABSVERSIONNUMBER` | BIGINT | NOT NULL |  |  |  |
| 34 | `DOCUMENTDATE` | DATE |  |  |  |  |
| 35 | `POSTINGDATE` | DATE |  |  |  |  |
| 36 | `CHEQUENUMBER` | CHAR(20) |  |  |  |  |
| 37 | `CHEQUEDATE` | DATE |  |  |  |  |
| 38 | `TDSAPPLICABLEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 39 | `TDSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 40 | `BUSINESSUNITDESC` | VARCHAR(200) |  |  |  |  |
| 41 | `PROFITCENTERDESC` | VARCHAR(200) |  |  |  |  |
| 42 | `COSTCENTERDESC` | VARCHAR(200) |  |  |  |  |
| 43 | `GLDESC` | VARCHAR(200) |  |  |  |  |
| 44 | `PLANTINVOICEDATA` | VARCHAR(255) |  |  |  |  |
| 45 | `PURCHASEINVOICEDATE` | DATE |  |  |  |  |
| 46 | `POADVANCEDATA` | VARCHAR(255) |  |  |  |  |
| 47 | `MRNDATA` | VARCHAR(255) |  |  |  |  |
| 48 | `COMMERCIALINVOICEDATA` | CHAR(20) |  |  |  |  |
| 49 | `DOCUMENTTYPECODE` | CHAR(3) |  |  |  |  |
| 50 | `DOCUMENTTYPEDESC` | VARCHAR(200) |  |  |  |  |
| 51 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 52 | `REFFINDOCBUSINESSUNIT` | CHAR(10) |  |  |  |  |
| 53 | `REFFINDOCFINANCIALYEAR` | DECIMAL(4,0) |  |  |  |  |
| 54 | `REFFINDOCDOCUMENTTEMPLATE` | CHAR(3) |  |  |  |  |
| 55 | `REFFINDOCSTATISTICALGROUP` | CHAR(6) |  |  |  |  |
| 56 | `REFFINDOCCODE` | CHAR(15) |  |  |  |  |
| 57 | `REFFINDOCAMOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 58 | `REFFINDOCAMOUNTINCC` | DECIMAL(18,5) |  |  |  |  |
| 59 | `REFFINDOCDOCUMENTCURRENCY` | CHAR(4) |  |  |  |  |
| 60 | `REFFINDOCEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 61 | `PURCHASEINVOICEDATA` | VARCHAR(200) |  |  |  |  |
| 62 | `DIRECTINVOICEDATA` | VARCHAR(200) |  |  |  |  |
| 63 | `EXPENSEINVOICEDATA` | VARCHAR(200) |  |  |  |  |
| 64 | `ADDRESSCODE` | CHAR(8) |  |  |  |  |
| 65 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINPAYMENTADVICEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.LINENO,
       t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.LINENUMBER,
       t.FINANCIALYEARCODE,
       t.DOCUMENTTEMPLATECODE,
       t.FINANCEMONTHCODE,
       t.STATISTICALGROUPCODE,
       t.DOCUMENTCODE,
       t.LINETEMPLATECODE,
       t.GLCODE
FROM   DB2ADMIN.WRKFINPAYMENTADVICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
