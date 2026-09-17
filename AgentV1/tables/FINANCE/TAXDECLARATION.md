# DB2ADMIN.TAXDECLARATION

- **Module**: `FINANCE` (low confidence — FK neighbourhood: 1 of 1 related tables are FINANCE)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `TAXRETURNCODE`, `COUNTRYCODE`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 103179

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TAXRETURNCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `COUNTRYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `UIDNUMBER` | CHAR(50) |  |  |  |  |
| 3 | `VATNUMBER` | CHAR(50) |  |  |  |  |
| 4 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 5 | `RATE` | CHAR(3) |  |  |  |  |
| 6 | `PERIOD` | CHAR(1) |  |  |  |  |
| 7 | `FINANCEOFFICE` | CHAR(30) |  |  |  |  |
| 8 | `POSTING` | SMALLINT | NOT NULL |  |  |  |
| 9 | `VATREPORT` | CHAR(30) |  |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COUNTRY_COUNTRY` | `COUNTRYCODE` | [`COUNTRY`](../CORE_MASTER/COUNTRY.md) | `CODE` | RESTRICT | `TAXDECLARATION.COUNTRYCODE = COUNTRY.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `TAXDECLARATION.CURRENCYCODE = CURRENCY.CODE` |
| `TAXRETURN_TAXRETURN` | `TAXRETURNCODE` | [`TAXRETURN`](../FINANCE/TAXRETURN.md) | `CODE` | RESTRICT | `TAXDECLARATION.TAXRETURNCODE = TAXRETURN.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TAXDECLARATION_TAXBOOKING` | [`TAXBOOKING`](../FINANCE/TAXBOOKING.md) | `TAXDECLARATIONTAXRETURNCODE`, `TAXDECLARATIONCOUNTRYCODE` | `TAXBOOKING.TAXDECLARATIONTAXRETURNCODE = TAXDECLARATION.TAXRETURNCODE AND TAXBOOKING.TAXDECLARATIONCOUNTRYCODE = TAXDECLARATION.COUNTRYCODE` |

## Indexes

- `TAXDECLARATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TAXRETURNCODE,
       t.COUNTRYCODE,
       t.UIDNUMBER,
       t.VATNUMBER,
       t.CURRENCYCODE,
       t.RATE,
       t.PERIOD,
       t.FINANCEOFFICE,
       t.POSTING,
       t.VATREPORT,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.TAXDECLARATION t
FETCH FIRST 100 ROWS ONLY;
```
