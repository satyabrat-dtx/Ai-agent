# DB2ADMIN.INITIALSROLEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 33
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 199314

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `ROLESTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `ROLECODE` | CHAR(3) |  |  |  |  |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 9 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 10 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 18 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 21 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 22 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 23 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 24 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 25 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 26 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 27 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 28 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 29 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 30 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 31 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 32 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `INITIALSROLEBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `INITIALSROLEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.ROLESTANDARDGROUPTYPECODE,
       t.ROLECODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.OWNINGCOMPANYCODE,
       t.TRANSLATEDLONGDESCRIPTION,
       t.TRANSLATEDLANGUAGECODE,
       t.TRANSLATEDSHORTDESCRIPTION,
       t.CREATIONDATETIME
FROM   DB2ADMIN.INITIALSROLEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
