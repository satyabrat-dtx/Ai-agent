# DB2ADMIN.FINOPENITEMCLEARING

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 41
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `CLEARINGNUMBER`, `INTERNALVOUCHERCODE`, `VOUCHERLINE`, `SUBLINE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 99763

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `CLEARINGNUMBER` | DECIMAL(15,0) | NOT NULL | PK | primary_key |  |
| 3 | `INTERNALVOUCHERCODE` | DECIMAL(15,0) | NOT NULL | PK | primary_key |  |
| 4 | `VOUCHERLINE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 5 | `SUBLINE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 6 | `GLACCOUNTCODE` | CHAR(10) |  | FK | foreign_key |  |
| 7 | `SUBACCOUNTTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 8 | `SUBACCOUNTCUSTOMERSUPPLIERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 9 | `ACCOUNTASSOCIATE` | CHAR(10) |  |  |  |  |
| 10 | `VALUATIONBASE` | DATE |  |  |  |  |
| 11 | `CLEARINGCOUNT` | INTEGER | NOT NULL |  |  |  |
| 12 | `CLEARINGVOUCHERNUMBER` | CHAR(20) |  |  |  |  |
| 13 | `CLEARINGDATE` | DATE |  |  |  |  |
| 14 | `CLEARINGPERIOD` | INTEGER | NOT NULL |  |  |  |
| 15 | `CLEARINGYEAR` | DECIMAL(4,0) | NOT NULL |  |  |  |
| 16 | `CLEARINGMARKSHORTFISCALYEAR` | CHAR(1) |  |  |  |  |
| 17 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 18 | `BALANCEAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 19 | `BALANCEAMOUNTCURRENCY1` | DECIMAL(17,2) |  |  |  |  |
| 20 | `BALANCEDISCOUNT` | DECIMAL(17,2) |  |  |  |  |
| 21 | `BALANCEDISCOUNTCURRENCY1` | DECIMAL(17,2) |  |  |  |  |
| 22 | `EXCHANGERATEDIFFERENCE` | DECIMAL(17,2) |  |  |  |  |
| 23 | `EXCHANGEDIFFERENCECURRENCY1` | DECIMAL(17,2) |  |  |  |  |
| 24 | `BALANCEOTHERDISCOUNT` | DECIMAL(17,2) |  |  |  |  |
| 25 | `BALANCEOTHERDISCOUNTCURR1` | DECIMAL(17,2) |  |  |  |  |
| 26 | `DEBITCREDITINDICATOROI` | CHAR(1) |  |  |  |  |
| 27 | `OPENITEMAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 28 | `OPENITEMAMOUNTCURRENCY1` | DECIMAL(17,2) |  |  |  |  |
| 29 | `CLEARINGTEXTKEYSTDTABLECODE` | CHAR(5) |  | FK | foreign_key |  |
| 30 | `CLEARINGTEXTKEYCODE` | CHAR(10) |  | FK | foreign_key |  |
| 31 | `CLEARINGTEXT` | CHAR(50) |  |  |  |  |
| 32 | `CLEARINGTEXTLONG` | VARCHAR(140) |  |  |  |  |
| 33 | `VOUCHERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 34 | `VOUCHERTYPECLEARING` | CHAR(1) |  |  |  |  |
| 35 | `MARKMULTICURRENCYCLEARING` | SMALLINT | NOT NULL |  |  |  |
| 36 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 37 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 38 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 39 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 40 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINOPENITEMCLEARING.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `FINOPENITEMCLEARING.CURRENCYCODE = CURRENCY.CODE` |
| `GENERALLEDGERACCOUNT_GLACCOUNT` | `COMPANYCODE`, `GLACCOUNTCODE` | [`GENERALLEDGERACCOUNT`](../FINANCE/GENERALLEDGERACCOUNT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINOPENITEMCLEARING.COMPANYCODE = GENERALLEDGERACCOUNT.COMPANYCODE AND FINOPENITEMCLEARING.GLACCOUNTCODE = GENERALLEDGERACCOUNT.CODE` |
| `ORDERPARTNER_SUBACCOUNT` | `COMPANYCODE`, `SUBACCOUNTTYPE`, `SUBACCOUNTCUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `FINOPENITEMCLEARING.COMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND FINOPENITEMCLEARING.SUBACCOUNTTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND FINOPENITEMCLEARING.SUBACCOUNTCUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |
| `STANDARDTABLERECORDS_CLEARINGTEXTKEY` | `COMPANYCODE`, `CLEARINGTEXTKEYSTDTABLECODE`, `CLEARINGTEXTKEYCODE` | [`STANDARDTABLERECORDS`](../FINANCE/STANDARDTABLERECORDS.md) | `STANDARDTABLECOMPANYCODE`, `STANDARDTABLECODE`, `CODE` | RESTRICT | `FINOPENITEMCLEARING.COMPANYCODE = STANDARDTABLERECORDS.STANDARDTABLECOMPANYCODE AND FINOPENITEMCLEARING.CLEARINGTEXTKEYSTDTABLECODE = STANDARDTABLERECORDS.STANDARDTABLECODE AND FINOPENITEMCLEARING.CLEARINGTEXTKEYCODE = STANDARDTABLERECORDS.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINOPENITEMCLEARINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CLEARINGNUMBER,
       t.INTERNALVOUCHERCODE,
       t.VOUCHERLINE,
       t.SUBLINE,
       t.GLACCOUNTCODE,
       t.SUBACCOUNTTYPE,
       t.SUBACCOUNTCUSTOMERSUPPLIERCODE,
       t.ACCOUNTASSOCIATE,
       t.VALUATIONBASE,
       t.CLEARINGCOUNT
FROM   DB2ADMIN.FINOPENITEMCLEARING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
