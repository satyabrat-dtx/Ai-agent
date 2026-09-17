# DB2ADMIN.SALESDOCUMENTCHARGEIMPORT

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `business_data`
- **Columns**: 29
- **Primary key**: `SALESDOCUMENTIMPORTCOMPANYCODE`, `SALDOCIMPIMPPROVISIONALCODE`, `IMPORTNUMBERID`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 9592

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESDOCUMENTIMPORTCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `SALDOCIMPIMPPROVISIONALCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `IMPORTOPERATION` | INTEGER | NOT NULL |  |  |  |
| 3 | `IMPORTNUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 4 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 5 | `SEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `CHARGESSUBCODE01` | CHAR(20) |  |  |  |  |
| 8 | `CHARGETYPE` | CHAR(2) |  |  |  |  |
| 9 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 10 | `CHARGECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 11 | `SIGN` | CHAR(2) |  |  |  |  |
| 12 | `CALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 13 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 14 | `CREATIONTYPE` | CHAR(1) |  |  |  |  |
| 15 | `DEFSALCHRDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 16 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 17 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 18 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 19 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 20 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 21 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 22 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 23 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 24 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 25 | `CHARGESCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 27 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 28 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SALESDOCUMENTCHARGEIMPORT_CHARGEIMPORT` | [`MILSALORDIMPERR`](../SALES/MILSALORDIMPERR.md) | `HEADERIMPORTCC`, `HEADERIMPORTIC`, `CHARGEIMPORTIMPORTNUMBERID` | `MILSALORDIMPERR.HEADERIMPORTCC = SALESDOCUMENTCHARGEIMPORT.SALESDOCUMENTIMPORTCOMPANYCODE AND MILSALORDIMPERR.HEADERIMPORTIC = SALESDOCUMENTCHARGEIMPORT.SALDOCIMPIMPPROVISIONALCODE AND MILSALORDIMPERR.CHARGEIMPORTIMPORTNUMBERID = SALESDOCUMENTCHARGEIMPORT.IMPORTNUMBERID` |

## Indexes

- `SALESDOCUMENTCHARGEIMPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SALESDOCUMENTIMPORTCOMPANYCODE,
       t.SALDOCIMPIMPPROVISIONALCODE,
       t.IMPORTOPERATION,
       t.IMPORTNUMBERID,
       t.NUMBERID,
       t.SEQUENCE,
       t.ITEMTYPECODE,
       t.CHARGESSUBCODE01,
       t.CHARGETYPE,
       t.VALUE,
       t.CHARGECURRENCYCODE,
       t.SIGN
FROM   DB2ADMIN.SALESDOCUMENTCHARGEIMPORT t
FETCH FIRST 100 ROWS ONLY;
```
