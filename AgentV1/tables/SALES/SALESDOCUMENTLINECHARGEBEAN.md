# DB2ADMIN.SALESDOCUMENTLINECHARGEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 32
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 96279

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 3 | `SEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 4 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `CHARGESSUBCODE01` | CHAR(20) |  |  |  |  |
| 6 | `CHARGETYPE` | CHAR(2) |  |  |  |  |
| 7 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `CHARGECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 9 | `SIGN` | CHAR(2) |  |  |  |  |
| 10 | `CALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 11 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 12 | `CREATIONTYPE` | CHAR(1) |  |  |  |  |
| 13 | `DEFSALCHRDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 14 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 15 | `DOCUMENTLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 16 | `DOCUMENTLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 17 | `DOCUMENTLINECOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 18 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 19 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 20 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 21 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 22 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 23 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 24 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 25 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 26 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 27 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 28 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 29 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 30 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 31 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **SALESDOCUMENTLINE**.`ABSUNIQUEID` (high confidence — name = 'SALESDOCUMENTLINE' + known child suffix 'CHARGE')
  - JOIN predicate: `SALESDOCUMENTLINECHARGEBEAN.FATHERID = SALESDOCUMENTLINE.ABSUNIQUEID`

## Indexes

- `SALDOCUMENTLINECHARGEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.NUMBERID,
       t.SEQUENCE,
       t.ITEMTYPECODE,
       t.CHARGESSUBCODE01,
       t.CHARGETYPE,
       t.VALUE,
       t.CHARGECURRENCYCODE,
       t.SIGN,
       t.CALCULATIONTYPE,
       t.AMOUNTCALCULATIONTYPE
FROM   DB2ADMIN.SALESDOCUMENTLINECHARGEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
