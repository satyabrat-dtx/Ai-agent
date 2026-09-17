# DB2ADMIN.TAXTEMPLATEDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `TAXTEMPLATEHEADERCOMPANYCODE`, `TAXTEMPLATEHEADERCODE`, `TAXTMPHEADEREFFECTIVEFROMDATE`, `ITAXCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 125001

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TAXTEMPLATEHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TAXTEMPLATEHEADERCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TAXTMPHEADEREFFECTIVEFROMDATE` | DATE | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ITAXCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `CALCULATIONSEQUENCE` | DECIMAL(2,0) | NOT NULL |  |  |  |
| 5 | `ROUNDOFFTYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `ROUNDOFFAMOUNT` | DECIMAL(10,5) | NOT NULL |  |  |  |
| 7 | `TAXCODETYPE` | INTEGER | NOT NULL |  |  |  |
| 8 | `CALCULATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 9 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 10 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 11 | `SIGN` | INTEGER | NOT NULL |  |  |  |
| 12 | `CALCULATIONBASISCODE` | CHAR(3) |  |  |  |  |
| 13 | `MODVATSETOFF` | INTEGER | NOT NULL |  |  |  |
| 14 | `MODVAT` | INTEGER | NOT NULL |  |  |  |
| 15 | `MODVATCYPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 16 | `MODVATNYPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 17 | `ALLOCATIONBASIS` | INTEGER | NOT NULL |  |  |  |
| 18 | `SOURCEAPPLICABLE` | INTEGER | NOT NULL |  |  |  |
| 19 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 20 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 21 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 22 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 23 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 24 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 25 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 26 | `POSTINFINANCE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `TAXTEMPLATEDETAIL.CURRENCYCODE = CURRENCY.CODE` |
| `TAXTEMPLATEHEADER_TAXTEMPLATEDETAIL` | `TAXTEMPLATEHEADERCOMPANYCODE`, `TAXTEMPLATEHEADERCODE`, `TAXTMPHEADEREFFECTIVEFROMDATE` | [`TAXTEMPLATEHEADER`](../OTHER/TAXTEMPLATEHEADER.md) | `COMPANYCODE`, `CODE`, `EFFECTIVEFROMDATE` | RESTRICT | `TAXTEMPLATEDETAIL.TAXTEMPLATEHEADERCOMPANYCODE = TAXTEMPLATEHEADER.COMPANYCODE AND TAXTEMPLATEDETAIL.TAXTEMPLATEHEADERCODE = TAXTEMPLATEHEADER.CODE AND TAXTEMPLATEDETAIL.TAXTMPHEADEREFFECTIVEFROMDATE = TAXTEMPLATEHEADER.EFFECTIVEFROMDATE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TAXTEMPLATEDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TAXTEMPLATEHEADERCOMPANYCODE,
       t.TAXTEMPLATEHEADERCODE,
       t.TAXTMPHEADEREFFECTIVEFROMDATE,
       t.ITAXCODE,
       t.CALCULATIONSEQUENCE,
       t.ROUNDOFFTYPE,
       t.ROUNDOFFAMOUNT,
       t.TAXCODETYPE,
       t.CALCULATIONTYPE,
       t.VALUE,
       t.CURRENCYCODE,
       t.SIGN
FROM   DB2ADMIN.TAXTEMPLATEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
