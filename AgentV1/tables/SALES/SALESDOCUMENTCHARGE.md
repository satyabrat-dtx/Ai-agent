# DB2ADMIN.SALESDOCUMENTCHARGE

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `SALESDOCUMENTCOMPANYCODE`, `SALDOCPROVISIONALCOUNTERCODE`, `SALESDOCUMENTPROVISIONALCODE`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 11854

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESDOCUMENTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SALDOCPROVISIONALCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SALESDOCUMENTPROVISIONALCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 4 | `SEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `CHARGESSUBCODE01` | CHAR(20) |  |  |  |  |
| 7 | `CHARGETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 9 | `CHARGECURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 10 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 13 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 14 | `DEFSALCHRDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 15 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 16 | `SALESDOCUMENTLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 17 | `SALESDOCUMENTLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 18 | `SALDOCLINECOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 19 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 20 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 21 | `LOGREASONCODE` | CHAR(2) |  | FK | foreign_key |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 28 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 29 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_CHARGECURRENCY` | `CHARGECURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `SALESDOCUMENTCHARGE.CHARGECURRENCYCODE = CURRENCY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESDOCUMENTCHARGE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND SALESDOCUMENTCHARGE.ITEMTYPECODE = ITEMTYPE.CODE` |
| `LOGREASON_LOGREASON` | `SALESDOCUMENTCOMPANYCODE`, `LOGREASONCODE` | [`LOGREASON`](../LOGISTICS/LOGREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESDOCUMENTCHARGE.SALESDOCUMENTCOMPANYCODE = LOGREASON.COMPANYCODE AND SALESDOCUMENTCHARGE.LOGREASONCODE = LOGREASON.CODE` |
| `SALESDOCUMENT_CHARGE` | `SALESDOCUMENTCOMPANYCODE`, `SALDOCPROVISIONALCOUNTERCODE`, `SALESDOCUMENTPROVISIONALCODE` | [`SALESDOCUMENT`](../SALES/SALESDOCUMENT.md) | `COMPANYCODE`, `PROVISIONALCOUNTERCODE`, `PROVISIONALCODE` | RESTRICT | `SALESDOCUMENTCHARGE.SALESDOCUMENTCOMPANYCODE = SALESDOCUMENT.COMPANYCODE AND SALESDOCUMENTCHARGE.SALDOCPROVISIONALCOUNTERCODE = SALESDOCUMENT.PROVISIONALCOUNTERCODE AND SALESDOCUMENTCHARGE.SALESDOCUMENTPROVISIONALCODE = SALESDOCUMENT.PROVISIONALCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESDOCUMENTCHARGEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SALESDOCUMENTCOMPANYCODE,
       t.SALDOCPROVISIONALCOUNTERCODE,
       t.SALESDOCUMENTPROVISIONALCODE,
       t.NUMBERID,
       t.SEQUENCE,
       t.ITEMTYPECODE,
       t.CHARGESSUBCODE01,
       t.CHARGETYPE,
       t.VALUE,
       t.CHARGECURRENCYCODE,
       t.SIGN,
       t.CALCULATIONTYPE
FROM   DB2ADMIN.SALESDOCUMENTCHARGE t
FETCH FIRST 100 ROWS ONLY;
```
