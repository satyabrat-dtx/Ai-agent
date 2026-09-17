# DB2ADMIN.INDTAXDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 39
- **Primary key**: `ABSUNIQUEID`, `COMPANYCODE`, `TAXTEMPLATETEMPLATETYPE`, `TAXTEMPLATECODE`, `SEQUENCENO`, `HEADERALLOCATIONFLAG`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 124177

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 2 | `TAXTEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `ITAXCODE` | CHAR(3) |  |  |  |  |
| 4 | `SEQUENCENO` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 5 | `TAXCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 6 | `FOB` | INTEGER | NOT NULL |  |  |  |
| 7 | `SIGN` | INTEGER | NOT NULL |  |  |  |
| 8 | `CALCULATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 9 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 10 | `CALCULATIONBASISCODE` | CHAR(3) |  |  |  |  |
| 11 | `CALCULATEDVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 12 | `TAXCODETYPE` | INTEGER | NOT NULL |  |  |  |
| 13 | `BASEVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 14 | `ALLOCATIONBASIS` | INTEGER | NOT NULL |  |  |  |
| 15 | `HEADERALLOCATIONFLAG` | INTEGER | NOT NULL | PK | primary_key |  |
| 16 | `ROUNDOFFTYPE` | INTEGER | NOT NULL |  |  |  |
| 17 | `ROUNDOFFAMOUNT` | DECIMAL(10,5) | NOT NULL |  |  |  |
| 18 | `SOURCEAPPLICABLE` | INTEGER | NOT NULL |  |  |  |
| 19 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 20 | `CALCULATEDVALUERTC` | DECIMAL(18,5) |  |  |  |  |
| 21 | `TAXCURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 22 | `CALCULATEDVALUER` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 23 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 24 | `CALCULATEDVALUERCC` | DECIMAL(18,5) |  |  |  |  |
| 25 | `COMPANYCURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 26 | `MODVATCYPERCENTAGE` | DECIMAL(9,5) | NOT NULL |  |  |  |
| 27 | `MODVATCYVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 28 | `MODVATNYPERCENTAGE` | DECIMAL(9,5) | NOT NULL |  |  |  |
| 29 | `MODVATNYVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 30 | `FABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 31 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 32 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 33 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 34 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 35 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 36 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 37 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 38 | `POSTINFINANCE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `INDTAXDETAIL.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_COMPANYCURRENCY` | `COMPANYCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `INDTAXDETAIL.COMPANYCURRENCYCODE = CURRENCY.CODE` |
| `CURRENCY_DOCUMENTCURRENCY` | `DOCUMENTCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `INDTAXDETAIL.DOCUMENTCURRENCYCODE = CURRENCY.CODE` |
| `CURRENCY_TAXCURRENCY` | `TAXCURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `INDTAXDETAIL.TAXCURRENCYCODE = CURRENCY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INDTAXDETAILUID` (ABSUNIQUEID)
- `INDTAXDETAIL1` (COMPANYCODE, FABSUNIQUEID, TAXCODETYPE)
- `INDTAXDETAIL2` (COMPANYCODE, ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TAXTEMPLATETEMPLATETYPE,
       t.TAXTEMPLATECODE,
       t.ITAXCODE,
       t.SEQUENCENO,
       t.TAXCATEGORYCODE,
       t.FOB,
       t.SIGN,
       t.CALCULATIONTYPE,
       t.VALUE,
       t.CALCULATIONBASISCODE,
       t.CALCULATEDVALUE
FROM   DB2ADMIN.INDTAXDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
