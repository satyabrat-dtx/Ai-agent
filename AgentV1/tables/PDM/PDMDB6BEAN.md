# DB2ADMIN.PDMDB6BEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PDM` (medium confidence — table name starts with 'PDM')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 25
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 47073

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DSRECT1CODE` | CHAR(3) |  |  |  |  |
| 3 | `DSANNUL` | CHAR(1) |  |  |  |  |
| 4 | `DSSIZFASIZESTYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `DSSIZFACODE` | CHAR(10) |  |  |  |  |
| 6 | `DSQUANT` | DECIMAL(9,5) |  |  |  |  |
| 7 | `DSSIZFISIZESTYPECODE` | CHAR(3) |  |  |  |  |
| 8 | `DSSIZFICODE` | CHAR(10) |  |  |  |  |
| 9 | `DSFLEXC` | CHAR(1) |  |  |  |  |
| 10 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 11 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 12 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 13 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 14 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 15 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 16 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 17 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 18 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 19 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 20 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 21 | `DSLINKEDSIZFASIZESTYPECODE` | CHAR(3) |  |  |  |  |
| 22 | `DSLINKEDSIZFACODE` | CHAR(10) |  |  |  |  |
| 23 | `DSLINKEDSIZFISIZESTYPECODE` | CHAR(3) |  |  |  |  |
| 24 | `DSLINKEDSIZFICODE` | CHAR(10) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `PDMDB6BEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `PDMDB6BEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.DSRECT1CODE,
       t.DSANNUL,
       t.DSSIZFASIZESTYPECODE,
       t.DSSIZFACODE,
       t.DSQUANT,
       t.DSSIZFISIZESTYPECODE,
       t.DSSIZFICODE,
       t.DSFLEXC,
       t.WSOPERATION,
       t.IMPORTSTATUS
FROM   DB2ADMIN.PDMDB6BEAN t
FETCH FIRST 100 ROWS ONLY;
```
