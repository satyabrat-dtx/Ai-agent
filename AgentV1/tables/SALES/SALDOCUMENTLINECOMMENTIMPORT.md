# DB2ADMIN.SALDOCUMENTLINECOMMENTIMPORT

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `IMPORTPROVISIONALCODE`, `SALDOCLINEIMPORTORDERLINE`, `SALDOCLINEIMPORTORDERSUBLINE`, `SALDOCLINEIMPCMPORDERLINE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 11038

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTPROVISIONALCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `SALDOCLINEIMPORTORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 3 | `SALDOCLINEIMPORTORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 4 | `SALDOCLINEIMPCMPORDERLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 5 | `IMPORTOPERATION` | INTEGER | NOT NULL |  |  |  |
| 6 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 7 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 8 | `COMMENTTEXT` | LONG VARCHAR |  |  |  |  |
| 9 | `COMMENTTYPE` | CHAR(2) |  |  |  |  |
| 10 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SALDOCUMENTLINECOMMENTIMPORT_LINECOMMENTIMPORT` | [`MILSALORDIMPERR`](../SALES/MILSALORDIMPERR.md) | `HEADERIMPORTCC`, `HEADERIMPORTIC`, `LINEIMPORTORDERLINE`, `LINEIMPORTORDERSUBLINE`, `LINEIMPORTCOMPONENTORDERLINE`, `LINECOMMENTIMPORTCODE` | `MILSALORDIMPERR.HEADERIMPORTCC = SALDOCUMENTLINECOMMENTIMPORT.COMPANYCODE AND MILSALORDIMPERR.HEADERIMPORTIC = SALDOCUMENTLINECOMMENTIMPORT.IMPORTPROVISIONALCODE AND MILSALORDIMPERR.LINEIMPORTORDERLINE = SALDOCUMENTLINECOMMENTIMPORT.SALDOCLINEIMPORTORDERLINE AND MILSALORDIMPERR.LINEIMPORTORDERSUBLINE = SALDOCUMENTLINECOMMENTIMPORT.SALDOCLINEIMPORTORDERSUBLINE AND MILSALORDIMPERR.LINEIMPORTCOMPONENTORDERLINE = SALDOCUMENTLINECOMMENTIMPORT.SALDOCLINEIMPCMPORDERLINE AND MILSALORDIMPERR.LINECOMMENTIMPORTCODE = SALDOCUMENTLINECOMMENTIMPORT.CODE` |

## Indexes

- `SALDOCLINECOMMENTIMPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTPROVISIONALCODE,
       t.SALDOCLINEIMPORTORDERLINE,
       t.SALDOCLINEIMPORTORDERSUBLINE,
       t.SALDOCLINEIMPCMPORDERLINE,
       t.IMPORTOPERATION,
       t.REPORTTYPE,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED,
       t.CREATIONDATETIME
FROM   DB2ADMIN.SALDOCUMENTLINECOMMENTIMPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
