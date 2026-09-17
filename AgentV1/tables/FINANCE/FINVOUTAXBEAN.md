# DB2ADMIN.FINVOUTAXBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 30
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 99314

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT |  |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `TAXCODECODE` | CHAR(5) |  |  |  |  |
| 3 | `TAXTYPE` | CHAR(1) |  |  |  |  |
| 4 | `TAXPERCENTAGE` | DECIMAL(6,3) |  |  |  |  |
| 5 | `AMOUNTASSESSMENT` | DECIMAL(17,2) |  |  |  |  |
| 6 | `BALANCENET` | DECIMAL(17,2) |  |  |  |  |
| 7 | `DEBITCREDITINDICATOR` | CHAR(1) |  |  |  |  |
| 8 | `TAXAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 9 | `BALANCETAX` | DECIMAL(17,2) |  |  |  |  |
| 10 | `ACCOUNTTAXCODE` | CHAR(10) |  |  |  |  |
| 11 | `ACCOUNTTAXREVERSECHARGECODE` | CHAR(10) |  |  |  |  |
| 12 | `TAXNUMBER` | CHAR(20) |  |  |  |  |
| 13 | `SALESTAXIDENTIFICATION` | CHAR(20) |  |  |  |  |
| 14 | `DATETAXDECLARATION` | DATE |  |  |  |  |
| 15 | `AMOUNTASSESSMENTCURRENCY1` | DECIMAL(17,2) |  |  |  |  |
| 16 | `TAXAMOUNTCURRENCY1` | DECIMAL(17,2) |  |  |  |  |
| 17 | `ACCOUNTSIDEFIRSTPOSTING` | CHAR(1) |  |  |  |  |
| 18 | `ACCOUNTSIDETAXPOSTING` | CHAR(1) |  |  |  |  |
| 19 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 20 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 21 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 22 | `IMPCREATIONUSER` | CHAR(25) |  |  |  |  |
| 23 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 24 | `IMPLASTUPDATEUSER` | CHAR(25) |  |  |  |  |
| 25 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 26 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 27 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 28 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 29 | `IMPOPERATIONUSER` | CHAR(25) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `FINVOUTAXBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.TAXCODECODE,
       t.TAXTYPE,
       t.TAXPERCENTAGE,
       t.AMOUNTASSESSMENT,
       t.BALANCENET,
       t.DEBITCREDITINDICATOR,
       t.TAXAMOUNT,
       t.BALANCETAX,
       t.ACCOUNTTAXCODE,
       t.ACCOUNTTAXREVERSECHARGECODE
FROM   DB2ADMIN.FINVOUTAXBEAN t
FETCH FIRST 100 ROWS ONLY;
```
