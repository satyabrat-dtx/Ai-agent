# DB2ADMIN.SALESORDERCOMMISSIONBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 28
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 60208

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `AGENTCODE` | CHAR(3) |  |  |  |  |
| 3 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 4 | `SEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 5 | `COMMISSIONTYPE` | CHAR(2) |  |  |  |  |
| 6 | `COMMISSIONVALUE` | DECIMAL(18,5) |  |  |  |  |
| 7 | `COMMISSIONCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 8 | `COMMISSIONSIGN` | CHAR(2) |  |  |  |  |
| 9 | `CALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 10 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 11 | `COMMISSIONCREATIONTYPE` | CHAR(1) |  |  |  |  |
| 12 | `DEFSALCMSDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 13 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 14 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 15 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 16 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 17 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 18 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 19 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 20 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 21 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 22 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 23 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 24 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 25 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 26 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 27 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **SALESORDER**.`ABSUNIQUEID` (medium confidence — name = 'SALESORDER' + recurring fragment 'COMMISSION' (seen in 11 tables))
  - JOIN predicate: `SALESORDERCOMMISSIONBEAN.FATHERID = SALESORDER.ABSUNIQUEID`

## Indexes

- `SALESORDERCOMMISSIONBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.AGENTCODE,
       t.NUMBERID,
       t.SEQUENCE,
       t.COMMISSIONTYPE,
       t.COMMISSIONVALUE,
       t.COMMISSIONCURRENCYCODE,
       t.COMMISSIONSIGN,
       t.CALCULATIONTYPE,
       t.AMOUNTCALCULATIONTYPE,
       t.COMMISSIONCREATIONTYPE
FROM   DB2ADMIN.SALESORDERCOMMISSIONBEAN t
FETCH FIRST 100 ROWS ONLY;
```
