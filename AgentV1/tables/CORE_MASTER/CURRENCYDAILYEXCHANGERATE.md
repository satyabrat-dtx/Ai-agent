# DB2ADMIN.CURRENCYDAILYEXCHANGERATE

- **Module**: `CORE_MASTER` (high confidence — table name starts with 'CURRENCY')
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `CURRENCYCODE`, `REFERENCEDCURRENCYCODE`, `INITIALDATE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 4424

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CURRENCYCODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `REFERENCEDCURRENCYCODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `INITIALDATE` | DATE | NOT NULL | PK | primary_key |  |
| 3 | `EXCHANGERATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 4 | `PURCHASEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 5 | `SALESEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `VALUATIONEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 11 | `SALESTAXLISTEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `REPORTINGEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_DAILYEXCHANGE` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `CURRENCYDAILYEXCHANGERATE.CURRENCYCODE = CURRENCY.CODE` |
| `CURRENCY_REFERENCEDCURRENCY` | `REFERENCEDCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `CURRENCYDAILYEXCHANGERATE.REFERENCEDCURRENCYCODE = CURRENCY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CURRENCYDAILYEXCHANGERATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CURRENCYCODE,
       t.REFERENCEDCURRENCYCODE,
       t.INITIALDATE,
       t.EXCHANGERATE,
       t.PURCHASEEXCHANGERATE,
       t.SALESEXCHANGERATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.VALUATIONEXCHANGERATE,
       t.SALESTAXLISTEXCHANGERATE
FROM   DB2ADMIN.CURRENCYDAILYEXCHANGERATE t
FETCH FIRST 100 ROWS ONLY;
```
