# DB2ADMIN.QASTANDARDDETAILBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 38
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 85960

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT |  |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `STEP` | INTEGER | NOT NULL |  |  |  |
| 3 | `CODECODE` | CHAR(6) |  |  |  |  |
| 4 | `TESTCODEDESC` | VARCHAR(40) |  |  |  |  |
| 5 | `STDVALUE1` | CHAR(25) |  |  |  |  |
| 6 | `STDVALUE2` | INTEGER | NOT NULL |  |  |  |
| 7 | `STDVALUE3` | DECIMAL(18,5) |  |  |  |  |
| 8 | `STANDARDVALUE` | CHAR(50) |  |  |  |  |
| 9 | `STDUMCODE` | CHAR(3) |  |  |  |  |
| 10 | `STDMINIMUM1` | CHAR(25) |  |  |  |  |
| 11 | `STDMINIMUM2` | INTEGER | NOT NULL |  |  |  |
| 12 | `STDMINIMUM3` | DECIMAL(18,5) |  |  |  |  |
| 13 | `STANDARDMINIMUM` | CHAR(50) |  |  |  |  |
| 14 | `STDMINUMCODE` | CHAR(3) |  |  |  |  |
| 15 | `STDMAXIMUM1` | CHAR(25) |  |  |  |  |
| 16 | `STDMAXIMUM2` | INTEGER | NOT NULL |  |  |  |
| 17 | `STDMAXIMUM3` | DECIMAL(18,5) |  |  |  |  |
| 18 | `STANDARDMAXIMUM` | CHAR(50) |  |  |  |  |
| 19 | `STDMAXUMCODE` | CHAR(3) |  |  |  |  |
| 20 | `REMARK1` | CHAR(50) |  |  |  |  |
| 21 | `REMARK2` | CHAR(50) |  |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 26 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 27 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 28 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 29 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 30 | `IMPCREATIONUSER` | CHAR(25) |  |  |  |  |
| 31 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 32 | `IMPLASTUPDATEUSER` | CHAR(25) |  |  |  |  |
| 33 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 34 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 35 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 36 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 37 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `QASTANDARDDETAILBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.STEP,
       t.CODECODE,
       t.TESTCODEDESC,
       t.STDVALUE1,
       t.STDVALUE2,
       t.STDVALUE3,
       t.STANDARDVALUE,
       t.STDUMCODE,
       t.STDMINIMUM1,
       t.STDMINIMUM2
FROM   DB2ADMIN.QASTANDARDDETAILBEAN t
FETCH FIRST 100 ROWS ONLY;
```
