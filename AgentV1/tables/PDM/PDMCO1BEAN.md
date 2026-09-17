# DB2ADMIN.PDMCO1BEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PDM` (medium confidence — table name starts with 'PDM')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 25
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 80845

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `CORECTYCODE` | CHAR(3) |  |  |  |  |
| 4 | `COTPREC` | DECIMAL(1,0) |  |  |  |  |
| 5 | `COCITEM` | CHAR(15) |  |  |  |  |
| 6 | `COVERNR` | CHAR(3) |  |  |  |  |
| 7 | `COVERST` | DECIMAL(3,0) |  |  |  |  |
| 8 | `COGRPCO` | CHAR(10) |  |  |  |  |
| 9 | `COCDCOL` | CHAR(10) |  |  |  |  |
| 10 | `COANNUL` | CHAR(1) |  |  |  |  |
| 11 | `COTKGRP` | CHAR(1) |  |  |  |  |
| 12 | `COCMGRP` | CHAR(1) |  |  |  |  |
| 13 | `COERPGR` | CHAR(2) |  |  |  |  |
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
| 24 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `PDMCO1BEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `PDMCO1BEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.CORECTYCODE,
       t.COTPREC,
       t.COCITEM,
       t.COVERNR,
       t.COVERST,
       t.COGRPCO,
       t.COCDCOL,
       t.COANNUL,
       t.COTKGRP
FROM   DB2ADMIN.PDMCO1BEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
