# DB2ADMIN.WRKFINOPENITEMCLEARING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 69
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `CLEARINGNUMBER`, `INTERNALVOUCHERCODE`, `VOUCHERLINE`, `SUBLINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 100381

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `CLEARINGNUMBER` | DECIMAL(15,0) | NOT NULL | PK | primary_key |  |
| 3 | `INTERNALVOUCHERCODE` | DECIMAL(15,0) | NOT NULL | PK | primary_key |  |
| 4 | `VOUCHERLINE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 5 | `SUBLINE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 6 | `GLACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 7 | `SUBACCOUNTTYPE` | CHAR(1) |  |  |  |  |
| 8 | `SUBACCOUNTCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 9 | `ACCOUNTASSOCIATE` | CHAR(10) |  |  |  |  |
| 10 | `VALUATIONBASE` | DATE |  |  |  |  |
| 11 | `CLEARINGDATE` | DATE |  |  |  |  |
| 12 | `CLEARINGPERIOD` | INTEGER | NOT NULL |  |  |  |
| 13 | `CLEARINGYEAR` | DECIMAL(4,0) | NOT NULL |  |  |  |
| 14 | `CLEARINGMARKSHORTFISCALYEAR` | CHAR(1) |  |  |  |  |
| 15 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 16 | `BALANCEAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 17 | `BALANCEAMOUNTCURRENCY1` | DECIMAL(17,2) |  |  |  |  |
| 18 | `BALANCEDISCOUNT` | DECIMAL(17,2) |  |  |  |  |
| 19 | `BALANCEDISCOUNTCURRENCY1` | DECIMAL(17,2) |  |  |  |  |
| 20 | `EXCHANGERATEDIFFERENCE` | DECIMAL(17,2) |  |  |  |  |
| 21 | `EXCHANGEDIFFERENCECURRENCY1` | DECIMAL(17,2) |  |  |  |  |
| 22 | `BALANCEOTHERDISCOUNT` | DECIMAL(17,2) |  |  |  |  |
| 23 | `BALANCEOTHERDISCOUNTCURR1` | DECIMAL(17,2) |  |  |  |  |
| 24 | `DEBITCREDITINDICATOROI` | CHAR(1) |  |  |  |  |
| 25 | `OPENITEMAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 26 | `OPENITEMAMOUNTCURRENCY1` | DECIMAL(17,2) |  |  |  |  |
| 27 | `CLEARINGTEXTKEYSTDTABLECODE` | CHAR(5) |  |  |  |  |
| 28 | `CLEARINGTEXTKEYCODE` | CHAR(10) |  |  |  |  |
| 29 | `CLEARINGTEXT` | CHAR(50) |  |  |  |  |
| 30 | `CLEARINGTEXTLONG` | VARCHAR(140) |  |  |  |  |
| 31 | `VOUCHERTYPECLEARING` | CHAR(1) |  |  |  |  |
| 32 | `MARKMULTICURRENCYCLEARING` | SMALLINT | NOT NULL |  |  |  |
| 33 | `MARKPOSTVOUCHER` | SMALLINT | NOT NULL |  |  |  |
| 34 | `ACCOUNTAREA` | CHAR(1) |  |  |  |  |
| 35 | `DEDUCTIONLEVEL` | CHAR(1) |  |  |  |  |
| 36 | `DEDUCTIONTYPECODE` | CHAR(3) |  |  |  |  |
| 37 | `DEDUCTIONGLACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 38 | `DEDUCTIONTAXCODE` | CHAR(5) |  |  |  |  |
| 39 | `DDNNOTEKEYSTANDARDTABLECODE` | CHAR(5) |  |  |  |  |
| 40 | `DEDUCTIONNOTEKEYCODE` | CHAR(10) |  |  |  |  |
| 41 | `DEDUCTIONNOTE` | CHAR(50) |  |  |  |  |
| 42 | `DEDUCTIONDEBITCREDIT` | CHAR(1) |  |  |  |  |
| 43 | `DEDUCTIONAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 44 | `DEDUCTIONAMOUNTCURRENCY1` | DECIMAL(17,2) |  |  |  |  |
| 45 | `DEDUCTIONLEVEL2` | CHAR(1) |  |  |  |  |
| 46 | `DEDUCTIONTYPE2CODE` | CHAR(3) |  |  |  |  |
| 47 | `DEDUCTIONGLACCOUNT2CODE` | CHAR(10) |  |  |  |  |
| 48 | `DEDUCTIONTAX2CODE` | CHAR(5) |  |  |  |  |
| 49 | `DDNNOTEKEY2STANDARDTABLECODE` | CHAR(5) |  |  |  |  |
| 50 | `DEDUCTIONNOTEKEY2CODE` | CHAR(10) |  |  |  |  |
| 51 | `DEDUCTIONNOTE2` | CHAR(50) |  |  |  |  |
| 52 | `DEDUCTIONDEBITCREDIT2` | CHAR(1) |  |  |  |  |
| 53 | `DEDUCTIONAMOUNT2` | DECIMAL(17,2) |  |  |  |  |
| 54 | `DEDUCTIONAMOUNTCURRENCY12` | DECIMAL(17,2) |  |  |  |  |
| 55 | `DEDUCTIONLEVEL3` | CHAR(1) |  |  |  |  |
| 56 | `DEDUCTIONTYPE3CODE` | CHAR(3) |  |  |  |  |
| 57 | `DEDUCTIONGLACCOUNT3CODE` | CHAR(10) |  |  |  |  |
| 58 | `DEDUCTIONTAX3CODE` | CHAR(5) |  |  |  |  |
| 59 | `DDNNOTEKEY3STANDARDTABLECODE` | CHAR(5) |  |  |  |  |
| 60 | `DEDUCTIONNOTEKEY3CODE` | CHAR(10) |  |  |  |  |
| 61 | `DEDUCTIONNOTE3` | CHAR(50) |  |  |  |  |
| 62 | `DEDUCTIONDEBITCREDIT3` | CHAR(1) |  |  |  |  |
| 63 | `DEDUCTIONAMOUNT3` | DECIMAL(17,2) |  |  |  |  |
| 64 | `DEDUCTIONAMOUNTCURRENCY13` | DECIMAL(17,2) |  |  |  |  |
| 65 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 66 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 67 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 68 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

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
       t.CLEARINGDATE
FROM   DB2ADMIN.WRKFINOPENITEMCLEARING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
