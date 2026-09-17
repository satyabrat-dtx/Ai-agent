# DB2ADMIN.STATISTICALGROUPBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 39
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 74722

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 3 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 4 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 5 | `CODE` | CHAR(6) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 7 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 8 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 9 | `STCTYPESTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `STATISTICALTYPECODE` | CHAR(3) |  |  |  |  |
| 11 | `INITIALDATE` | DATE |  |  |  |  |
| 12 | `FINALDATE` | DATE |  |  |  |  |
| 13 | `DETAILREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 14 | `INITIALORDERDATE` | DATE |  |  |  |  |
| 15 | `FINALORDERDATE` | DATE |  |  |  |  |
| 16 | `INITIALDELIVERYDATE` | DATE |  |  |  |  |
| 17 | `FINALDELIVERYDATE` | DATE |  |  |  |  |
| 18 | `PERIODIZEDCALENDARTYPECODE` | CHAR(10) |  |  |  |  |
| 19 | `PERIODIZEDCALENDARYEAR` | DECIMAL(4,0) |  |  |  |  |
| 20 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 21 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 22 | `PROGRESSSTATUSCODE` | CHAR(3) |  |  |  |  |
| 23 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 24 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 25 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 26 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 27 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 28 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 29 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 30 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 31 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 32 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 33 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 34 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 35 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 36 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 37 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 38 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `STATISTICALGROUPBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `STATISTICALGROUPBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.STCTYPESTANDARDGROUPTYPECODE,
       t.STATISTICALTYPECODE,
       t.INITIALDATE
FROM   DB2ADMIN.STATISTICALGROUPBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
