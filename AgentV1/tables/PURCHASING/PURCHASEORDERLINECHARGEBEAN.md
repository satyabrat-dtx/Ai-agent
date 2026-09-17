# DB2ADMIN.PURCHASEORDERLINECHARGEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 27
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 59761

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
| 13 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 14 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 15 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 16 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 17 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 18 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 19 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 20 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 22 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 24 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 25 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 26 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **PURCHASEORDERLINE**.`ABSUNIQUEID` (high confidence — name = 'PURCHASEORDERLINE' + known child suffix 'CHARGE')
  - JOIN predicate: `PURCHASEORDERLINECHARGEBEAN.FATHERID = PURCHASEORDERLINE.ABSUNIQUEID`

## Indexes

- `PURORDERLINECHARGEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

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
FROM   DB2ADMIN.PURCHASEORDERLINECHARGEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
