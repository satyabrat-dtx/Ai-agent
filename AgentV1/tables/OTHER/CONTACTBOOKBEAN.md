# DB2ADMIN.CONTACTBOOKBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 41
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 48967

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `CODE` | CHAR(8) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `PERSON` | VARCHAR(200) |  |  |  |  |
| 4 | `ROLEINTHECOMPANY` | VARCHAR(200) |  |  |  |  |
| 5 | `PHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 6 | `FAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 7 | `EMAILADDRESS` | VARCHAR(200) |  |  |  |  |
| 8 | `BOOKLINE01` | VARCHAR(200) |  |  |  |  |
| 9 | `BOOKLINE02` | VARCHAR(200) |  |  |  |  |
| 10 | `BOOKLINE03` | VARCHAR(200) |  |  |  |  |
| 11 | `BOOKLINE04` | VARCHAR(200) |  |  |  |  |
| 12 | `BOOKLINE05` | VARCHAR(200) |  |  |  |  |
| 13 | `DOCUMENTTYPEFORMAIL` | CHAR(90) |  |  |  |  |
| 14 | `ADDRESSTYPE` | INTEGER | NOT NULL |  |  |  |
| 15 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 16 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 17 | `COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 18 | `ADDRESSLINE1` | VARCHAR(150) |  |  |  |  |
| 19 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 20 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 21 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 22 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 23 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 24 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 25 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 26 | `TRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 27 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 28 | `ADDRESSFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 29 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 30 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 31 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 32 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 33 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 34 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 35 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 36 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 37 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 38 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 39 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 40 | `ENTITYNAME` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `CONTACTBOOKBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `CONTACTBOOKBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.CODE,
       t.PERSON,
       t.ROLEINTHECOMPANY,
       t.PHONENUMBER,
       t.FAXNUMBER,
       t.EMAILADDRESS,
       t.BOOKLINE01,
       t.BOOKLINE02,
       t.BOOKLINE03,
       t.BOOKLINE04
FROM   DB2ADMIN.CONTACTBOOKBEAN t
FETCH FIRST 100 ROWS ONLY;
```
