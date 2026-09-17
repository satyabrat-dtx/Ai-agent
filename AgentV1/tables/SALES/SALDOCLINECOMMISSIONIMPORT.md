# DB2ADMIN.SALDOCLINECOMMISSIONIMPORT

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 29
- **Primary key**: `COMPANYCODE`, `PROVISIONALCODE`, `SALDOCLINEIMPORTORDERLINE`, `SALDOCLINEIMPORTORDERSUBLINE`, `SALDOCLINEIMPCMPORDERLINE`, `AGENTCODE`, `IMPORTNUMBERID`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 4525

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PROVISIONALCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `SALDOCLINEIMPORTORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 3 | `SALDOCLINEIMPORTORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 4 | `SALDOCLINEIMPCMPORDERLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 5 | `IMPORTOPERATION` | INTEGER | NOT NULL |  |  |  |
| 6 | `AGENTCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 7 | `IMPORTNUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 8 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 9 | `SEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 10 | `COMMISSIONTYPE` | CHAR(2) |  |  |  |  |
| 11 | `COMMISSIONVALUE` | DECIMAL(18,5) |  |  |  |  |
| 12 | `COMMISSIONCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 13 | `COMMISSIONSIGN` | CHAR(2) |  |  |  |  |
| 14 | `CALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 15 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 16 | `COMMISSIONCREATIONTYPE` | CHAR(1) |  |  |  |  |
| 17 | `DEFSALCMSDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 18 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 19 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 20 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 21 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 27 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 28 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SALDOCLINECOMMISSIONIMPORT_LINECOMMISSIONIMPORT` | [`MILSALORDIMPERR`](../SALES/MILSALORDIMPERR.md) | `HEADERIMPORTCC`, `HEADERIMPORTIC`, `LINEIMPORTORDERLINE`, `LINEIMPORTORDERSUBLINE`, `LINEIMPORTCOMPONENTORDERLINE`, `LINECOMMISSIONIMPORTAGENTCODE`, `LINECMSIMPORTIMPORTNUMBERID` | `MILSALORDIMPERR.HEADERIMPORTCC = SALDOCLINECOMMISSIONIMPORT.COMPANYCODE AND MILSALORDIMPERR.HEADERIMPORTIC = SALDOCLINECOMMISSIONIMPORT.PROVISIONALCODE AND MILSALORDIMPERR.LINEIMPORTORDERLINE = SALDOCLINECOMMISSIONIMPORT.SALDOCLINEIMPORTORDERLINE AND MILSALORDIMPERR.LINEIMPORTORDERSUBLINE = SALDOCLINECOMMISSIONIMPORT.SALDOCLINEIMPORTORDERSUBLINE AND MILSALORDIMPERR.LINEIMPORTCOMPONENTORDERLINE = SALDOCLINECOMMISSIONIMPORT.SALDOCLINEIMPCMPORDERLINE AND MILSALORDIMPERR.LINECOMMISSIONIMPORTAGENTCODE = SALDOCLINECOMMISSIONIMPORT.AGENTCODE AND MILSALORDIMPERR.LINECMSIMPORTIMPORTNUMBERID = SALDOCLINECOMMISSIONIMPORT.IMPORTNUMBERID` |

## Indexes

- `SALDOCLINECMSIMPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PROVISIONALCODE,
       t.SALDOCLINEIMPORTORDERLINE,
       t.SALDOCLINEIMPORTORDERSUBLINE,
       t.SALDOCLINEIMPCMPORDERLINE,
       t.IMPORTOPERATION,
       t.AGENTCODE,
       t.IMPORTNUMBERID,
       t.NUMBERID,
       t.SEQUENCE,
       t.COMMISSIONTYPE,
       t.COMMISSIONVALUE
FROM   DB2ADMIN.SALDOCLINECOMMISSIONIMPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
