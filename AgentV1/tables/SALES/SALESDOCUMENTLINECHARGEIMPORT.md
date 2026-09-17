# DB2ADMIN.SALESDOCUMENTLINECHARGEIMPORT

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `business_data`
- **Columns**: 32
- **Primary key**: `COMPANYCODE`, `PROVISIONALCODE`, `SALDOCLINEIMPORTORDERLINE`, `SALDOCLINEIMPORTORDERSUBLINE`, `SALDOCLINEIMPCMPORDERLINE`, `IMPORTNUMBERID`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 14963

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
| 7 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 8 | `SEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 9 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `CHARGESSUBCODE01` | CHAR(20) |  |  |  |  |
| 11 | `CHARGETYPE` | CHAR(2) |  |  |  |  |
| 12 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `CHARGECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 14 | `SIGN` | CHAR(2) |  |  |  |  |
| 15 | `CALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 16 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 17 | `CREATIONTYPE` | CHAR(1) |  |  |  |  |
| 18 | `DEFSALCHRDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 19 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 20 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 21 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 22 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 23 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 24 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 25 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 26 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 27 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 28 | `CHARGESCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 30 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 31 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SALESDOCUMENTLINECHARGEIMPORT_LINECHARGEIMPORT` | [`MILSALORDIMPERR`](../SALES/MILSALORDIMPERR.md) | `HEADERIMPORTCC`, `HEADERIMPORTIC`, `LINEIMPORTORDERLINE`, `LINEIMPORTORDERSUBLINE`, `LINEIMPORTCOMPONENTORDERLINE`, `LINECHARGEIMPORTIMPORTNUMBERID` | `MILSALORDIMPERR.HEADERIMPORTCC = SALESDOCUMENTLINECHARGEIMPORT.COMPANYCODE AND MILSALORDIMPERR.HEADERIMPORTIC = SALESDOCUMENTLINECHARGEIMPORT.PROVISIONALCODE AND MILSALORDIMPERR.LINEIMPORTORDERLINE = SALESDOCUMENTLINECHARGEIMPORT.SALDOCLINEIMPORTORDERLINE AND MILSALORDIMPERR.LINEIMPORTORDERSUBLINE = SALESDOCUMENTLINECHARGEIMPORT.SALDOCLINEIMPORTORDERSUBLINE AND MILSALORDIMPERR.LINEIMPORTCOMPONENTORDERLINE = SALESDOCUMENTLINECHARGEIMPORT.SALDOCLINEIMPCMPORDERLINE AND MILSALORDIMPERR.LINECHARGEIMPORTIMPORTNUMBERID = SALESDOCUMENTLINECHARGEIMPORT.IMPORTNUMBERID` |

## Indexes

- `SALDOCLINECHARGEIMPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PROVISIONALCODE,
       t.SALDOCLINEIMPORTORDERLINE,
       t.SALDOCLINEIMPORTORDERSUBLINE,
       t.SALDOCLINEIMPCMPORDERLINE,
       t.IMPORTOPERATION,
       t.IMPORTNUMBERID,
       t.NUMBERID,
       t.SEQUENCE,
       t.ITEMTYPECODE,
       t.CHARGESSUBCODE01,
       t.CHARGETYPE
FROM   DB2ADMIN.SALESDOCUMENTLINECHARGEIMPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
