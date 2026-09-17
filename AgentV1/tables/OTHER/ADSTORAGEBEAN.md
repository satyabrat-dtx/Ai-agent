# DB2ADMIN.ADSTORAGEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 24
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 61903

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `NAMEENTITYNAME` | CHAR(50) |  |  |  |  |
| 3 | `NAMENAME` | CHAR(50) |  |  |  |  |
| 4 | `FIELDNAME` | VARCHAR(120) |  |  |  |  |
| 5 | `VALUESTRING` | VARCHAR(250) |  |  |  |  |
| 6 | `VALUEINT` | INTEGER | NOT NULL |  |  |  |
| 7 | `VALUEBOOLEAN` | SMALLINT | NOT NULL |  |  |  |
| 8 | `VALUEDATE` | DATE |  |  |  |  |
| 9 | `VALUEDECIMAL` | DECIMAL(18,5) |  |  |  |  |
| 10 | `VALUELONG` | BIGINT | NOT NULL |  |  |  |
| 11 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 12 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 13 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 14 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 15 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 16 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 17 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 18 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 19 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 20 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 21 | `VALUETIME` | TIME |  |  |  |  |
| 22 | `VALUETIMESTAMP` | TIMESTAMP |  |  |  |  |
| 23 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `ADSTORAGEBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `ADSTORAGEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.NAMEENTITYNAME,
       t.NAMENAME,
       t.FIELDNAME,
       t.VALUESTRING,
       t.VALUEINT,
       t.VALUEBOOLEAN,
       t.VALUEDATE,
       t.VALUEDECIMAL,
       t.VALUELONG,
       t.WSOPERATION
FROM   DB2ADMIN.ADSTORAGEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
