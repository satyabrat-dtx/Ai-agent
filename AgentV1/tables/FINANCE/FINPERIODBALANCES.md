# DB2ADMIN.FINPERIODBALANCES

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 55
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `INFOTYPECODE`, `FISCALYEAR`, `MARKSHORTFISCALYEAR`, `GLACCOUNTCODE`, `SUBACCOUNTTYPE`, `SUBACCOUNTCUSTOMERSUPPLIERCODE`, `CURRENCYCODE`, `CURRENCYLCCODE`, `SPECIALLEDGERAREA`, `SPECIALLEDGERID`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 99838

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `INFOTYPECODE` | CHAR(2) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `FISCALYEAR` | DECIMAL(4,0) | NOT NULL | PK | primary_key |  |
| 4 | `MARKSHORTFISCALYEAR` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 5 | `GLACCOUNTCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `SUBACCOUNTTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 7 | `SUBACCOUNTCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 8 | `CURRENCYCODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 9 | `CURRENCYLCCODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 10 | `SPECIALLEDGERAREA` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 11 | `SPECIALLEDGERID` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 12 | `DEBITVALUEPERIOD00` | DECIMAL(17,2) |  |  |  |  |
| 13 | `DEBITVALUEPERIOD01` | DECIMAL(17,2) |  |  |  |  |
| 14 | `DEBITVALUEPERIOD02` | DECIMAL(17,2) |  |  |  |  |
| 15 | `DEBITVALUEPERIOD03` | DECIMAL(17,2) |  |  |  |  |
| 16 | `DEBITVALUEPERIOD04` | DECIMAL(17,2) |  |  |  |  |
| 17 | `DEBITVALUEPERIOD05` | DECIMAL(17,2) |  |  |  |  |
| 18 | `DEBITVALUEPERIOD06` | DECIMAL(17,2) |  |  |  |  |
| 19 | `DEBITVALUEPERIOD07` | DECIMAL(17,2) |  |  |  |  |
| 20 | `DEBITVALUEPERIOD08` | DECIMAL(17,2) |  |  |  |  |
| 21 | `DEBITVALUEPERIOD09` | DECIMAL(17,2) |  |  |  |  |
| 22 | `DEBITVALUEPERIOD10` | DECIMAL(17,2) |  |  |  |  |
| 23 | `DEBITVALUEPERIOD11` | DECIMAL(17,2) |  |  |  |  |
| 24 | `DEBITVALUEPERIOD12` | DECIMAL(17,2) |  |  |  |  |
| 25 | `DEBITVALUEPERIOD13` | DECIMAL(17,2) |  |  |  |  |
| 26 | `DEBITVALUEPERIOD14` | DECIMAL(17,2) |  |  |  |  |
| 27 | `DEBITVALUEPERIOD15` | DECIMAL(17,2) |  |  |  |  |
| 28 | `DEBITVALUEPERIOD16` | DECIMAL(17,2) |  |  |  |  |
| 29 | `CREDITVALUEPERIOD00` | DECIMAL(17,2) |  |  |  |  |
| 30 | `CREDITVALUEPERIOD01` | DECIMAL(17,2) |  |  |  |  |
| 31 | `CREDITVALUEPERIOD02` | DECIMAL(17,2) |  |  |  |  |
| 32 | `CREDITVALUEPERIOD03` | DECIMAL(17,2) |  |  |  |  |
| 33 | `CREDITVALUEPERIOD04` | DECIMAL(17,2) |  |  |  |  |
| 34 | `CREDITVALUEPERIOD05` | DECIMAL(17,2) |  |  |  |  |
| 35 | `CREDITVALUEPERIOD06` | DECIMAL(17,2) |  |  |  |  |
| 36 | `CREDITVALUEPERIOD07` | DECIMAL(17,2) |  |  |  |  |
| 37 | `CREDITVALUEPERIOD08` | DECIMAL(17,2) |  |  |  |  |
| 38 | `CREDITVALUEPERIOD09` | DECIMAL(17,2) |  |  |  |  |
| 39 | `CREDITVALUEPERIOD10` | DECIMAL(17,2) |  |  |  |  |
| 40 | `CREDITVALUEPERIOD11` | DECIMAL(17,2) |  |  |  |  |
| 41 | `CREDITVALUEPERIOD12` | DECIMAL(17,2) |  |  |  |  |
| 42 | `CREDITVALUEPERIOD13` | DECIMAL(17,2) |  |  |  |  |
| 43 | `CREDITVALUEPERIOD14` | DECIMAL(17,2) |  |  |  |  |
| 44 | `CREDITVALUEPERIOD15` | DECIMAL(17,2) |  |  |  |  |
| 45 | `CREDITVALUEPERIOD16` | DECIMAL(17,2) |  |  |  |  |
| 46 | `BALANCEYEAR` | DECIMAL(17,2) |  |  |  |  |
| 47 | `BALANCE` | DECIMAL(17,2) |  |  |  |  |
| 48 | `LASTUPDINTERNALVOUNBR` | DECIMAL(15,0) |  |  |  |  |
| 49 | `LASTUPDINTERNALVOULINE` | DECIMAL(5,0) |  |  |  |  |
| 50 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 51 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 52 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 53 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 54 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINPERIODBALANCES.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `FINPERIODBALANCES.CURRENCYCODE = CURRENCY.CODE` |
| `FININFOTYPE_INFOTYPE` | `INFOTYPECODE` | [`FININFOTYPE`](../FINANCE/FININFOTYPE.md) | `CODE` | RESTRICT | `FINPERIODBALANCES.INFOTYPECODE = FININFOTYPE.CODE` |
| `GENERALLEDGERACCOUNT_GLACCOUNT` | `COMPANYCODE`, `GLACCOUNTCODE` | [`GENERALLEDGERACCOUNT`](../FINANCE/GENERALLEDGERACCOUNT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINPERIODBALANCES.COMPANYCODE = GENERALLEDGERACCOUNT.COMPANYCODE AND FINPERIODBALANCES.GLACCOUNTCODE = GENERALLEDGERACCOUNT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINPERIODBALANCESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.INFOTYPECODE,
       t.FISCALYEAR,
       t.MARKSHORTFISCALYEAR,
       t.GLACCOUNTCODE,
       t.SUBACCOUNTTYPE,
       t.SUBACCOUNTCUSTOMERSUPPLIERCODE,
       t.CURRENCYCODE,
       t.CURRENCYLCCODE,
       t.SPECIALLEDGERAREA,
       t.SPECIALLEDGERID
FROM   DB2ADMIN.FINPERIODBALANCES t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
