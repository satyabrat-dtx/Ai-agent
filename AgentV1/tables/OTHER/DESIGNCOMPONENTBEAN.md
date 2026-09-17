# DB2ADMIN.DESIGNCOMPONENTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 46
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 71851

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DESIGNITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `DESIGNSUBCODE01` | CHAR(20) |  |  |  |  |
| 4 | `DESIGNSUBCODE02` | CHAR(10) |  |  |  |  |
| 5 | `DESIGNSUBCODE03` | CHAR(10) |  |  |  |  |
| 6 | `DESIGNSUBCODE04` | CHAR(10) |  |  |  |  |
| 7 | `DESIGNSUBCODE05` | CHAR(10) |  |  |  |  |
| 8 | `DESIGNSUBCODE06` | CHAR(10) |  |  |  |  |
| 9 | `DESIGNSUBCODE07` | CHAR(10) |  |  |  |  |
| 10 | `DESIGNSUBCODE08` | CHAR(10) |  |  |  |  |
| 11 | `DESIGNSUBCODE09` | CHAR(10) |  |  |  |  |
| 12 | `DESIGNSUBCODE10` | CHAR(10) |  |  |  |  |
| 13 | `DESIGNSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 14 | `VARIANTCODE` | CHAR(20) |  |  |  |  |
| 15 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 16 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 17 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 18 | `IMAGENAME` | CHAR(50) |  |  |  |  |
| 19 | `IMAGEPATH` | CHAR(30) |  |  |  |  |
| 20 | `IMAGEVIEW` | CHAR(80) |  |  |  |  |
| 21 | `INITIALDATE` | DATE |  |  |  |  |
| 22 | `FINALDATE` | DATE |  |  |  |  |
| 23 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 24 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 25 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 26 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 27 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 28 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 29 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 30 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 31 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 32 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 33 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 34 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 35 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 36 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 37 | `PREVIOUSDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 38 | `DESCRIPTIONCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 39 | `PREVIOUSSHORTDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 40 | `SHORTDESCRIPTIONCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 41 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 42 | `SEARCHDESCRIPTIONCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 43 | `PREVIOUSSEARCHDESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 44 | `DSNCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 45 | `DSNNUMBERID` | DECIMAL(11,0) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **DESIGN**.`ABSUNIQUEID` (medium confidence — name = 'DESIGN' + recurring fragment 'COMPONENT' (seen in 11 tables))
  - JOIN predicate: `DESIGNCOMPONENTBEAN.FATHERID = DESIGN.ABSUNIQUEID`

## Indexes

- `DESIGNCOMPONENTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.DESIGNITEMTYPECODE,
       t.DESIGNSUBCODE01,
       t.DESIGNSUBCODE02,
       t.DESIGNSUBCODE03,
       t.DESIGNSUBCODE04,
       t.DESIGNSUBCODE05,
       t.DESIGNSUBCODE06,
       t.DESIGNSUBCODE07,
       t.DESIGNSUBCODE08,
       t.DESIGNSUBCODE09
FROM   DB2ADMIN.DESIGNCOMPONENTBEAN t
FETCH FIRST 100 ROWS ONLY;
```
