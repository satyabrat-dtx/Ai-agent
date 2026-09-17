# DB2ADMIN.SALDOCLINEDISCOUNTIMPORT

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 31
- **Primary key**: `COMPANYCODE`, `PROVISIONALCODE`, `SALDOCLINEIMPORTORDERLINE`, `SALDOCLINEIMPORTORDERSUBLINE`, `SALDOCLINEIMPCMPORDERLINE`, `IMPORTNUMBERID`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 26390

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PROVISIONALCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `SALDOCLINEIMPORTORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 3 | `SALDOCLINEIMPORTORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 4 | `SALDOCLINEIMPCMPORDERLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 5 | `IMPORTOPERATION` | INTEGER | NOT NULL |  |  |  |
| 6 | `IMPORTNUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 7 | `SEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 8 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 9 | `DISCOUNTTYPE` | CHAR(2) |  |  |  |  |
| 10 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 11 | `DISCOUNTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 12 | `SIGN` | CHAR(2) |  |  |  |  |
| 13 | `TAXAPPLICATIONTYPE` | CHAR(2) |  |  |  |  |
| 14 | `CALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 15 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 16 | `EXCLUDEDINCMSCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 17 | `EXCLUDEDINCOMMISSIONRETRIEVING` | SMALLINT | NOT NULL |  |  |  |
| 18 | `CREATIONTYPE` | CHAR(1) |  |  |  |  |
| 19 | `DEFSALDSCDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 20 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 21 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 22 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 23 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 24 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 25 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 26 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 27 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 28 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 29 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 30 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SALDOCLINEDISCOUNTIMPORT_LINEDISCOUNTIMPORT` | [`MILSALORDIMPERR`](../SALES/MILSALORDIMPERR.md) | `HEADERIMPORTCC`, `HEADERIMPORTIC`, `LINEIMPORTORDERLINE`, `LINEIMPORTORDERSUBLINE`, `LINEIMPORTCOMPONENTORDERLINE`, `LINEDSCIMPORTIMPORTNUMBERID` | `MILSALORDIMPERR.HEADERIMPORTCC = SALDOCLINEDISCOUNTIMPORT.COMPANYCODE AND MILSALORDIMPERR.HEADERIMPORTIC = SALDOCLINEDISCOUNTIMPORT.PROVISIONALCODE AND MILSALORDIMPERR.LINEIMPORTORDERLINE = SALDOCLINEDISCOUNTIMPORT.SALDOCLINEIMPORTORDERLINE AND MILSALORDIMPERR.LINEIMPORTORDERSUBLINE = SALDOCLINEDISCOUNTIMPORT.SALDOCLINEIMPORTORDERSUBLINE AND MILSALORDIMPERR.LINEIMPORTCOMPONENTORDERLINE = SALDOCLINEDISCOUNTIMPORT.SALDOCLINEIMPCMPORDERLINE AND MILSALORDIMPERR.LINEDSCIMPORTIMPORTNUMBERID = SALDOCLINEDISCOUNTIMPORT.IMPORTNUMBERID` |

## Indexes

- `SALDOCLINEDISCOUNTIMPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PROVISIONALCODE,
       t.SALDOCLINEIMPORTORDERLINE,
       t.SALDOCLINEIMPORTORDERSUBLINE,
       t.SALDOCLINEIMPCMPORDERLINE,
       t.IMPORTOPERATION,
       t.IMPORTNUMBERID,
       t.SEQUENCE,
       t.NUMBERID,
       t.DISCOUNTTYPE,
       t.VALUE,
       t.DISCOUNTCURRENCYCODE
FROM   DB2ADMIN.SALDOCLINEDISCOUNTIMPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
