# DB2ADMIN.SALESDOCUMENTDISCOUNTIMPORT

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `SALESDOCUMENTIMPORTCOMPANYCODE`, `SALDOCIMPIMPPROVISIONALCODE`, `IMPORTNUMBERID`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 13681

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESDOCUMENTIMPORTCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `SALDOCIMPIMPPROVISIONALCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `IMPORTOPERATION` | INTEGER | NOT NULL |  |  |  |
| 3 | `IMPORTNUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 4 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 5 | `SEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 6 | `DISCOUNTTYPE` | CHAR(2) |  |  |  |  |
| 7 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `DISCOUNTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 9 | `SIGN` | CHAR(2) |  |  |  |  |
| 10 | `TAXAPPLICATIONTYPE` | CHAR(2) |  |  |  |  |
| 11 | `CALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 12 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 13 | `EXCLUDEDINCMSCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 14 | `EXCLUDEDINCOMMISSIONRETRIEVING` | SMALLINT | NOT NULL |  |  |  |
| 15 | `CREATIONTYPE` | CHAR(1) |  |  |  |  |
| 16 | `DEFSALDSCDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 17 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 18 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 19 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 20 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 26 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 27 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SALESDOCUMENTDISCOUNTIMPORT_DISCOUNTIMPORT` | [`MILSALORDIMPERR`](../SALES/MILSALORDIMPERR.md) | `HEADERIMPORTCC`, `HEADERIMPORTIC`, `DISCOUNTIMPORTIMPORTNUMBERID` | `MILSALORDIMPERR.HEADERIMPORTCC = SALESDOCUMENTDISCOUNTIMPORT.SALESDOCUMENTIMPORTCOMPANYCODE AND MILSALORDIMPERR.HEADERIMPORTIC = SALESDOCUMENTDISCOUNTIMPORT.SALDOCIMPIMPPROVISIONALCODE AND MILSALORDIMPERR.DISCOUNTIMPORTIMPORTNUMBERID = SALESDOCUMENTDISCOUNTIMPORT.IMPORTNUMBERID` |

## Indexes

- `SALDOCUMENTDISCOUNTIMPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SALESDOCUMENTIMPORTCOMPANYCODE,
       t.SALDOCIMPIMPPROVISIONALCODE,
       t.IMPORTOPERATION,
       t.IMPORTNUMBERID,
       t.NUMBERID,
       t.SEQUENCE,
       t.DISCOUNTTYPE,
       t.VALUE,
       t.DISCOUNTCURRENCYCODE,
       t.SIGN,
       t.TAXAPPLICATIONTYPE,
       t.CALCULATIONTYPE
FROM   DB2ADMIN.SALESDOCUMENTDISCOUNTIMPORT t
FETCH FIRST 100 ROWS ONLY;
```
