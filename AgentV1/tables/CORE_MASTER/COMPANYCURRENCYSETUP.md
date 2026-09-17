# DB2ADMIN.COMPANYCURRENCYSETUP

- **Module**: `CORE_MASTER` (high confidence — table name starts with 'COMPANY')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `COMPANYCODE`, `CURRENCYCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 42361

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CURRENCYCODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CUSTOMDECIMALSFORUNITPRICES` | SMALLINT | NOT NULL |  |  |  |
| 3 | `NUMBEROFDECFORUNITPRICES` | INTEGER | NOT NULL |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_CURRENCYSETUP` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `COMPANYCURRENCYSETUP.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `COMPANYCURRENCYSETUP.CURRENCYCODE = CURRENCY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COMPANYCURRENCYSETUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CURRENCYCODE,
       t.CUSTOMDECIMALSFORUNITPRICES,
       t.NUMBEROFDECFORUNITPRICES,
       t.ABSUNIQUEID
FROM   DB2ADMIN.COMPANYCURRENCYSETUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
