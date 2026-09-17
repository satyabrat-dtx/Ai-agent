# DB2ADMIN.LOGBUSINESSPARTNER

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 59
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 50360

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `NUMBERID` | DECIMAL(8,0) | NOT NULL |  |  |  |
| 1 | `ORIGININFORMATIONTYPECODE` | CHAR(3) |  |  |  |  |
| 2 | `ENDDATE` | DATE |  |  |  |  |
| 3 | `SUBSTITUTEBPNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 4 | `LEGALNAME1` | VARCHAR(270) | NOT NULL |  |  |  |
| 5 | `LEGALNAME2` | VARCHAR(200) |  |  |  |  |
| 6 | `SHORTNAME` | VARCHAR(80) |  |  |  |  |
| 7 | `SEARCHNAME` | VARCHAR(120) |  |  |  |  |
| 8 | `GROUPBPNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 9 | `SUNDRY` | SMALLINT | NOT NULL |  |  |  |
| 10 | `FISCALTYPECODE` | CHAR(2) |  |  |  |  |
| 11 | `FISCALCODE` | CHAR(16) |  |  |  |  |
| 12 | `TAXREGISTRATIONNUMBER` | CHAR(15) |  |  |  |  |
| 13 | `COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 14 | `ADDRESSLINE1` | VARCHAR(150) | NOT NULL |  |  |  |
| 15 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 16 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 17 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 18 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 19 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 20 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 21 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 22 | `TRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 23 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 24 | `ADDRESSFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 25 | `PERSON` | VARCHAR(200) |  |  |  |  |
| 26 | `ROLEINTHECOMPANY` | VARCHAR(200) |  |  |  |  |
| 27 | `PHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 28 | `FAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 29 | `EMAILADDRESS` | VARCHAR(200) |  |  |  |  |
| 30 | `BOOKLINE01` | VARCHAR(200) |  |  |  |  |
| 31 | `BOOKLINE02` | VARCHAR(200) |  |  |  |  |
| 32 | `BOOKLINE03` | VARCHAR(200) |  |  |  |  |
| 33 | `BOOKLINE04` | VARCHAR(200) |  |  |  |  |
| 34 | `BOOKLINE05` | VARCHAR(200) |  |  |  |  |
| 35 | `DOCUMENTTYPEFORMAIL` | CHAR(90) |  |  |  |  |
| 36 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 37 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 38 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 39 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 40 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 41 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 42 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 43 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 44 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 45 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 46 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 47 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 48 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 49 | `FISCALREPRESENTATIVENUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 50 | `FISCALREPRESENTATIVEUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 51 | `PERMESTABLISHMENTCODE` | CHAR(8) |  |  |  |  |
| 52 | `GENDER` | CHAR(1) |  |  |  |  |
| 53 | `DATEOFBIRTH` | DATE |  |  |  |  |
| 54 | `COUNTRYOFBIRTHCODE` | CHAR(3) |  |  |  |  |
| 55 | `DISTRICTOFBIRTH` | VARCHAR(200) |  |  |  |  |
| 56 | `PLACEOFBIRTH` | VARCHAR(200) |  |  |  |  |
| 57 | `NATIONALITY` | CHAR(20) |  |  |  |  |
| 58 | `EORICODE` | CHAR(17) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGBUSINESSPARTNER.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.NUMBERID,
       t.ORIGININFORMATIONTYPECODE,
       t.ENDDATE,
       t.SUBSTITUTEBPNUMBERID,
       t.LEGALNAME1,
       t.LEGALNAME2,
       t.SHORTNAME,
       t.SEARCHNAME,
       t.GROUPBPNUMBERID,
       t.SUNDRY,
       t.FISCALTYPECODE,
       t.FISCALCODE
FROM   DB2ADMIN.LOGBUSINESSPARTNER t
FETCH FIRST 100 ROWS ONLY;
```
