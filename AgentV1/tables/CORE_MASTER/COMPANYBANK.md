# DB2ADMIN.COMPANYBANK

- **Module**: `CORE_MASTER` (high confidence — table name starts with 'COMPANY')
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `IDENTIFIER`
- **FK degree**: referenced by 5 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 22088

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IDENTIFIER` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 2 | `BANKCODE` | CHAR(15) |  | FK | foreign_key |  |
| 3 | `BANKBRANCHCODE` | CHAR(6) |  | FK | foreign_key |  |
| 4 | `EXTERNALBANKCODE` | CHAR(15) |  | FK | foreign_key |  |
| 5 | `CINCODE` | CHAR(2) |  |  |  |  |
| 6 | `CURRENTACCOUNTID` | CHAR(30) |  |  |  |  |
| 7 | `BBAN` | CHAR(30) |  |  |  |  |
| 8 | `BIC` | CHAR(11) |  |  |  |  |
| 9 | `IBAN` | CHAR(34) |  |  |  |  |
| 10 | `PRIORITY` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 11 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 12 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `ACCOUNTOWNER` | CHAR(100) |  |  |  |  |
| 14 | `DIRECTDEBIT` | SMALLINT | NOT NULL |  |  |  |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BANKEXTERNAL_EXTERNALBANK` | `COMPANYCODE`, `EXTERNALBANKCODE` | [`BANKEXTERNAL`](../SALES/BANKEXTERNAL.md) | `COMPANYCODE`, `CODE` | RESTRICT | `COMPANYBANK.COMPANYCODE = BANKEXTERNAL.COMPANYCODE AND COMPANYBANK.EXTERNALBANKCODE = BANKEXTERNAL.CODE` |
| `BANK_BANK` | `BANKBANKCOUNTRYCODE`, `BANKCODE`, `BANKBRANCHCODE` | [`BANK`](../CORE_MASTER/BANK.md) | `BANKCOUNTRYCODE`, `CODE`, `BRANCHCODE` | RESTRICT | `COMPANYBANK.BANKBANKCOUNTRYCODE = BANK.BANKCOUNTRYCODE AND COMPANYBANK.BANKCODE = BANK.CODE AND COMPANYBANK.BANKBRANCHCODE = BANK.BRANCHCODE` |
| `COMPANY_BANK` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `COMPANYBANK.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `COMPANYBANK.CURRENCYCODE = CURRENCY.CODE` |

## Referenced by (child → this table) — 5

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `COMPANYBANK_COMPANYBANK` | [`FINCOMPANYBANK`](../FINANCE/FINCOMPANYBANK.md) | `COMPANYCODE`, `COMPANYBANKIDENTIFIER` | `FINCOMPANYBANK.COMPANYCODE = COMPANYBANK.COMPANYCODE AND FINCOMPANYBANK.COMPANYBANKIDENTIFIER = COMPANYBANK.IDENTIFIER` |
| `COMPANYBANK_LCBENEFICIARYID` | [`BILLOFEXCHANGE`](../FINANCE/BILLOFEXCHANGE.md) | `COMPANYCODE`, `LCBENEFICIARYIDIDENTIFIER` | `BILLOFEXCHANGE.COMPANYCODE = COMPANYBANK.COMPANYCODE AND BILLOFEXCHANGE.LCBENEFICIARYIDIDENTIFIER = COMPANYBANK.IDENTIFIER` |
| `COMPANYBANK_LCADVISORYBANKID` | [`LCDETAILPUR`](../FINANCE/LCDETAILPUR.md) | `COMPANYCODE`, `LCADVISORYBANKIDIDENTIFIER` | `LCDETAILPUR.COMPANYCODE = COMPANYBANK.COMPANYCODE AND LCDETAILPUR.LCADVISORYBANKIDIDENTIFIER = COMPANYBANK.IDENTIFIER` |
| `COMPANYBANK_LCDRAFTBANKID` | [`LCDETAILPUR`](../FINANCE/LCDETAILPUR.md) | `COMPANYCODE`, `LCDRAFTBANKIDIDENTIFIER` | `LCDETAILPUR.COMPANYCODE = COMPANYBANK.COMPANYCODE AND LCDETAILPUR.LCDRAFTBANKIDIDENTIFIER = COMPANYBANK.IDENTIFIER` |
| `COMPANYBANK_BANKID` | [`BANKVSGLMAPPING`](../OTHER/BANKVSGLMAPPING.md) | `COMPANYCODE`, `BANKIDIDENTIFIER` | `BANKVSGLMAPPING.COMPANYCODE = COMPANYBANK.COMPANYCODE AND BANKVSGLMAPPING.BANKIDIDENTIFIER = COMPANYBANK.IDENTIFIER` |

## Indexes

- `COMPANYBANKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IDENTIFIER,
       t.BANKCODE,
       t.BANKBRANCHCODE,
       t.EXTERNALBANKCODE,
       t.CINCODE,
       t.CURRENTACCOUNTID,
       t.BBAN,
       t.BIC,
       t.IBAN,
       t.PRIORITY,
       t.CURRENCYCODE
FROM   DB2ADMIN.COMPANYBANK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
