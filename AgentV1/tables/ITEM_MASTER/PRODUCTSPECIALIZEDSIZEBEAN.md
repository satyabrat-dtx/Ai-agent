# DB2ADMIN.PRODUCTSPECIALIZEDSIZEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'PRODUCT')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 33
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 44928

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `SIZETYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `SIZETYPEMATRIXROWCODE` | CHAR(3) |  |  |  |  |
| 4 | `MADEINCODE` | CHAR(3) |  |  |  |  |
| 5 | `WASHSYMBOL01CODE` | CHAR(10) |  |  |  |  |
| 6 | `WASHSYMBOL02CODE` | CHAR(10) |  |  |  |  |
| 7 | `WASHSYMBOL03CODE` | CHAR(10) |  |  |  |  |
| 8 | `WASHSYMBOL04CODE` | CHAR(10) |  |  |  |  |
| 9 | `WASHSYMBOL05CODE` | CHAR(10) |  |  |  |  |
| 10 | `WASHSYMBOL06CODE` | CHAR(10) |  |  |  |  |
| 11 | `VALUESCOMBINATIONS` | INTEGER | NOT NULL |  |  |  |
| 12 | `ALLOWEDFORMATRIX` | SMALLINT | NOT NULL |  |  |  |
| 13 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 14 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 15 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 16 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 17 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 18 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 19 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 20 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 22 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 23 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 24 | `SIZEDISTRIBUTIONCODE` | CHAR(30) |  |  |  |  |
| 25 | `SIZEDISTRIBUTIONMATRIXROWCODE` | CHAR(30) |  |  |  |  |
| 26 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 27 | `WASHSYMBOLLABELCODE` | CHAR(10) |  |  |  |  |
| 28 | `WASHFINALLABEL` | VARCHAR(500) |  |  |  |  |
| 29 | `STANDARDMINUTEVALUE` | DECIMAL(10,5) |  |  |  |  |
| 30 | `NUMBEROFOPERATORS` | INTEGER | NOT NULL |  |  |  |
| 31 | `STEPREPETITIONNUMBER` | DECIMAL(17,6) |  |  |  |  |
| 32 | `SMVISFORLASTSTEP` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `PRODUCTSPECIALIZEDSIZEBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `PRODUCTSPECIALIZEDSIZEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.SIZETYPECODE,
       t.SIZETYPEMATRIXROWCODE,
       t.MADEINCODE,
       t.WASHSYMBOL01CODE,
       t.WASHSYMBOL02CODE,
       t.WASHSYMBOL03CODE,
       t.WASHSYMBOL04CODE,
       t.WASHSYMBOL05CODE,
       t.WASHSYMBOL06CODE,
       t.VALUESCOMBINATIONS
FROM   DB2ADMIN.PRODUCTSPECIALIZEDSIZEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
