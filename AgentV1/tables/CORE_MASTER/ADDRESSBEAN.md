# DB2ADMIN.ADDRESSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `CORE_MASTER` (high confidence — table name starts with 'ADDRESS')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 46
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 43198

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `ORIGINBUSINESSPARTNERNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 3 | `ORIGINPHYWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `ORIGINPHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 5 | `CODE` | CHAR(8) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `ORIGINDELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 7 | `ORIGINDELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 8 | `ADDRESSTYPE` | INTEGER | NOT NULL |  |  |  |
| 9 | `ADDRESSEE` | VARCHAR(200) |  |  |  |  |
| 10 | `COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 11 | `ADDRESSLINE1` | VARCHAR(150) |  |  |  |  |
| 12 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 13 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 14 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 15 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 16 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 17 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 18 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 19 | `TRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 20 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 21 | `ADDRESSFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 22 | `EMAILADDRESS` | VARCHAR(200) |  |  |  |  |
| 23 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 24 | `WORKINGCALENDARCODE` | CHAR(3) |  |  |  |  |
| 25 | `ACKNOWLEDGEMENTREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 26 | `ACKNOWLEDGEMENTTYPE` | CHAR(2) |  |  |  |  |
| 27 | `TAXREGISTRATIONNUMBER` | CHAR(15) |  |  |  |  |
| 28 | `CALLEDFROM` | INTEGER | NOT NULL |  |  |  |
| 29 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 30 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 31 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 32 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 33 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 34 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 35 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 36 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 37 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 38 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 39 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 40 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 41 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 42 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 43 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 44 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 45 | `ADDRESSEE2` | VARCHAR(200) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `ADDRESSBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `ADDRESSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.ORIGINBUSINESSPARTNERNUMBERID,
       t.ORIGINPHYWAREHOUSECOMPANYCODE,
       t.ORIGINPHYSICALWAREHOUSECODE,
       t.CODE,
       t.ORIGINDELIVERYPOINTUNIQUEID,
       t.ORIGINDELIVERYPOINTCODE,
       t.ADDRESSTYPE,
       t.ADDRESSEE,
       t.COUNTRYCODE,
       t.ADDRESSLINE1
FROM   DB2ADMIN.ADDRESSBEAN t
FETCH FIRST 100 ROWS ONLY;
```
