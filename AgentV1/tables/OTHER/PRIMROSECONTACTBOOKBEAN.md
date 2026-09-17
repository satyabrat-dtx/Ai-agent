# DB2ADMIN.PRIMROSECONTACTBOOKBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 46
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 49410

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `UNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 3 | `CODE` | CHAR(8) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `PERSON` | VARCHAR(200) |  |  |  |  |
| 5 | `ROLEINTHECOMPANY` | VARCHAR(200) |  |  |  |  |
| 6 | `PHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 7 | `FAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 8 | `EMAILADDRESS` | VARCHAR(200) |  |  |  |  |
| 9 | `BOOKLINE01` | VARCHAR(200) |  |  |  |  |
| 10 | `BOOKLINE02` | VARCHAR(200) |  |  |  |  |
| 11 | `BOOKLINE03` | VARCHAR(200) |  |  |  |  |
| 12 | `BOOKLINE04` | VARCHAR(200) |  |  |  |  |
| 13 | `BOOKLINE05` | VARCHAR(200) |  |  |  |  |
| 14 | `DOCUMENTTYPEFORMAIL` | CHAR(90) |  |  |  |  |
| 15 | `ADDRESSTYPE` | INTEGER | NOT NULL |  |  |  |
| 16 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 17 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 18 | `COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 19 | `ADDRESSLINE1` | VARCHAR(150) |  |  |  |  |
| 20 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 21 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 22 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 23 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 24 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 25 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 26 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 27 | `TRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 28 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 29 | `ADDRESSFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 30 | `ANRNOLIB` | CHAR(60) |  |  |  |  |
| 31 | `ADDRESSPRIMROSEANANUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 32 | `ANICD` | DECIMAL(7,0) |  |  |  |  |
| 33 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 34 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 35 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 36 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 37 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 38 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 39 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 40 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 41 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 42 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 43 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 44 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 45 | `ENTITYNAME` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `PRIMROSECONTACTBOOKBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `PRIMROSECONTACTBOOKBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.UNIQUEID,
       t.CODE,
       t.PERSON,
       t.ROLEINTHECOMPANY,
       t.PHONENUMBER,
       t.FAXNUMBER,
       t.EMAILADDRESS,
       t.BOOKLINE01,
       t.BOOKLINE02,
       t.BOOKLINE03
FROM   DB2ADMIN.PRIMROSECONTACTBOOKBEAN t
FETCH FIRST 100 ROWS ONLY;
```
