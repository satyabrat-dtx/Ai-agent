# DB2ADMIN.COMPOSITIONDETAILBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 26
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 46633

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `SUBCOMPOSITION` | CHAR(2) |  |  |  |  |
| 3 | `TOUSE` | CHAR(2) |  |  |  |  |
| 4 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 5 | `COMPONENTCODE` | CHAR(10) |  |  |  |  |
| 6 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 7 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 8 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 9 | `COMPONENTPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 10 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
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
| 21 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 22 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 23 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 24 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 25 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **COMPOSITION**.`ABSUNIQUEID` (high confidence — name = 'COMPOSITION' + known child suffix 'DETAIL')
  - JOIN predicate: `COMPOSITIONDETAILBEAN.FATHERID = COMPOSITION.ABSUNIQUEID`

## Indexes

- `COMPOSITIONDETAILBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.SUBCOMPOSITION,
       t.TOUSE,
       t.SEQUENCE,
       t.COMPONENTCODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.COMPONENTPERCENTAGE,
       t.OWNINGCOMPANYCODE,
       t.WSOPERATION
FROM   DB2ADMIN.COMPOSITIONDETAILBEAN t
FETCH FIRST 100 ROWS ONLY;
```
