# DB2ADMIN.ADVLICRECEIVED

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `COMPANYCODE`, `ADVANCELICENSECODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 134560

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ADVANCELICENSECODE` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FILENO` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `ADVANCELICENSENO` | CHAR(15) | NOT NULL |  |  |  |
| 4 | `DEECBOOKNO` | CHAR(15) |  |  |  |  |
| 5 | `EDIREGNO` | CHAR(30) |  |  |  |  |
| 6 | `ALAPPLICATIONDATE` | DATE | NOT NULL |  |  |  |
| 7 | `FILEDATE` | DATE | NOT NULL |  |  |  |
| 8 | `ADVANCELICENSEDATE` | DATE | NOT NULL |  |  |  |
| 9 | `DEECBOOKDATE` | DATE |  |  |  |  |
| 10 | `VALIDITYDATE` | DATE | NOT NULL |  |  |  |
| 11 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 12 | `KEYNO` | DECIMAL(3,2) |  |  |  |  |
| 13 | `BALANCEVALUEFORIMPORT` | DECIMAL(18,5) |  |  |  |  |
| 14 | `CIFVALUEFC` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 15 | `CIFVALUECURRENCYFCCODE` | CHAR(4) |  | FK | foreign_key |  |
| 16 | `CIFVALUEINR` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 17 | `EXCHANGERATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 18 | `FOBVALUEFC` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 19 | `FOBVALUECURRENCYFCCODE` | CHAR(4) |  | FK | foreign_key |  |
| 20 | `FOBVALUEINR` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 21 | `TOTALQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `EXPORTOBLIGATIONIMPOSEDQTY` | DECIMAL(15,5) |  |  |  |  |
| 23 | `EXPORTOBLIGATIONIMPOSEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 24 | `EOVFORIMPORTS1` | DATE |  |  |  |  |
| 25 | `EOVFORIMPORTS2` | DATE |  |  |  |  |
| 26 | `EOVFOREXPORTS1` | DATE |  |  |  |  |
| 27 | `EOVFOREXPORTS2` | DATE |  |  |  |  |
| 28 | `EXPORTPRODUCTDESC` | CHAR(120) |  |  |  |  |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADVANCELICENSE_ADVANCELICENSE` | `COMPANYCODE`, `ADVANCELICENSECODE` | [`ADVANCELICENSE`](../SALES/ADVANCELICENSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ADVLICRECEIVED.COMPANYCODE = ADVANCELICENSE.COMPANYCODE AND ADVLICRECEIVED.ADVANCELICENSECODE = ADVANCELICENSE.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ADVLICRECEIVED.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_CIFVALUECURRENCYFC` | `CIFVALUECURRENCYFCCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `ADVLICRECEIVED.CIFVALUECURRENCYFCCODE = CURRENCY.CODE` |
| `CURRENCY_FOBVALUECURRENCYFC` | `FOBVALUECURRENCYFCCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `ADVLICRECEIVED.FOBVALUECURRENCYFCCODE = CURRENCY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ADVLICRECEIVEDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ADVANCELICENSECODE,
       t.FILENO,
       t.ADVANCELICENSENO,
       t.DEECBOOKNO,
       t.EDIREGNO,
       t.ALAPPLICATIONDATE,
       t.FILEDATE,
       t.ADVANCELICENSEDATE,
       t.DEECBOOKDATE,
       t.VALIDITYDATE,
       t.STATUS
FROM   DB2ADMIN.ADVLICRECEIVED t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
