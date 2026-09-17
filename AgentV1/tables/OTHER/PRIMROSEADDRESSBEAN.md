# DB2ADMIN.PRIMROSEADDRESSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 62
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 43401

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `UNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 2 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 3 | `ORIGINBUSINESSPARTNERNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 4 | `ORIGINPHYWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `ORIGINPHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 6 | `CODE` | CHAR(8) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 7 | `ORIGINDELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 8 | `ORIGINDELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 9 | `ADDRESSTYPE` | INTEGER | NOT NULL |  |  |  |
| 10 | `ADDRESSEE` | VARCHAR(200) |  |  |  |  |
| 11 | `COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 12 | `ADDRESSLINE1` | VARCHAR(150) |  |  |  |  |
| 13 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 14 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 15 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 16 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 17 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 18 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 19 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 20 | `TRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 21 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 22 | `ADDRESSFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 23 | `EMAILADDRESS` | VARCHAR(200) |  |  |  |  |
| 24 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 25 | `WORKINGCALENDARCODE` | CHAR(3) |  |  |  |  |
| 26 | `ACKNOWLEDGEMENTREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 27 | `ACKNOWLEDGEMENTTYPE` | CHAR(2) |  |  |  |  |
| 28 | `TAXREGISTRATIONNUMBER` | CHAR(15) |  |  |  |  |
| 29 | `CALLEDFROM` | INTEGER | NOT NULL |  |  |  |
| 30 | `ANIRASO2` | CHAR(35) |  |  |  |  |
| 31 | `DISTRICTPCODE` | CHAR(5) |  |  |  |  |
| 32 | `ANITELEX` | CHAR(20) |  |  |  |  |
| 33 | `ANICOEDI` | CHAR(20) |  |  |  |  |
| 34 | `ANINOTEL` | CHAR(60) |  |  |  |  |
| 35 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 36 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 37 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 38 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 39 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 40 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 41 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 42 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 43 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 44 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 45 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 46 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 47 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 48 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 49 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 50 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 51 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 52 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 53 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 54 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 55 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 56 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 57 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 58 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 59 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 60 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 61 | `ADDRESSEE2` | VARCHAR(200) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `PRIMROSEADDRESSBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `PRIMROSEADDRESSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.UNIQUEID,
       t.IMPORTAUTOCOUNTER,
       t.ORIGINBUSINESSPARTNERNUMBERID,
       t.ORIGINPHYWAREHOUSECOMPANYCODE,
       t.ORIGINPHYSICALWAREHOUSECODE,
       t.CODE,
       t.ORIGINDELIVERYPOINTUNIQUEID,
       t.ORIGINDELIVERYPOINTCODE,
       t.ADDRESSTYPE,
       t.ADDRESSEE,
       t.COUNTRYCODE
FROM   DB2ADMIN.PRIMROSEADDRESSBEAN t
FETCH FIRST 100 ROWS ONLY;
```
