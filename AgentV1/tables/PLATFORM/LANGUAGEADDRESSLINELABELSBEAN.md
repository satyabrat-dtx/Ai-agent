# DB2ADMIN.LANGUAGEADDRESSLINELABELSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting. Per-language text for a parent row addressed via FATHERID.

- **Module**: `PLATFORM` (medium confidence — table name starts with 'LANGUAGE')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`, `translation`
- **Columns**: 22
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 193560

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 3 | `FIRSTADDRESSLINEDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 4 | `SECONDADDRESSLINEDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 5 | `THIRDADDRESSLINEDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 6 | `FOURTHADDRESSLINEDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 7 | `FIFTHADDRESSLINEDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 8 | `POSTALCODEDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 9 | `TOWNDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 10 | `DISTRICTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 11 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 12 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 13 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 14 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 15 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 16 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 17 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 18 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 19 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 20 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 21 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LANGUAGEADDRESSLINELABELSBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `GUAGEADDRESSLINELABELSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.LANGUAGECODE,
       t.FIRSTADDRESSLINEDESCRIPTION,
       t.SECONDADDRESSLINEDESCRIPTION,
       t.THIRDADDRESSLINEDESCRIPTION,
       t.FOURTHADDRESSLINEDESCRIPTION,
       t.FIFTHADDRESSLINEDESCRIPTION,
       t.POSTALCODEDESCRIPTION,
       t.TOWNDESCRIPTION,
       t.DISTRICTDESCRIPTION,
       t.WSOPERATION
FROM   DB2ADMIN.LANGUAGEADDRESSLINELABELSBEAN t
FETCH FIRST 100 ROWS ONLY;
```
