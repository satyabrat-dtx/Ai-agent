# DB2ADMIN.INDTAXTOTAL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `ABSUNIQUEID`, `SEQUENCENO`, `ITAXCODE`, `SOURCEAPPLICABLE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 124318

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SEQUENCENO` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 2 | `ITAXCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `TAXCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 4 | `FOB` | INTEGER | NOT NULL |  |  |  |
| 5 | `SOURCEAPPLICABLE` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `CALCULATEDVALUERTC` | DECIMAL(18,5) |  |  |  |  |
| 7 | `CALCULATEDVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 8 | `CALCULATEDVALUERCC` | DECIMAL(18,5) |  |  |  |  |
| 9 | `TAXCURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 10 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 11 | `COMPANYCURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 12 | `MODVATCYVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 13 | `MODVATNYVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `INDTAXTOTAL.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_COMPANYCURRENCY` | `COMPANYCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `INDTAXTOTAL.COMPANYCURRENCYCODE = CURRENCY.CODE` |
| `CURRENCY_DOCUMENTCURRENCY` | `DOCUMENTCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `INDTAXTOTAL.DOCUMENTCURRENCYCODE = CURRENCY.CODE` |
| `CURRENCY_TAXCURRENCY` | `TAXCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `INDTAXTOTAL.TAXCURRENCYCODE = CURRENCY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INDTAXTOTALUID` (ABSUNIQUEID)
- `INDTAXTOTAL1` (ABSUNIQUEID, COMPANYCODE)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SEQUENCENO,
       t.ITAXCODE,
       t.TAXCATEGORYCODE,
       t.FOB,
       t.SOURCEAPPLICABLE,
       t.CALCULATEDVALUERTC,
       t.CALCULATEDVALUE,
       t.CALCULATEDVALUERCC,
       t.TAXCURRENCYCODE,
       t.DOCUMENTCURRENCYCODE,
       t.COMPANYCURRENCYCODE
FROM   DB2ADMIN.INDTAXTOTAL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
