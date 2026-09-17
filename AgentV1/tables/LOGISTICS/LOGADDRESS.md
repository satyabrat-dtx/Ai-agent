# DB2ADMIN.LOGADDRESS

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 41
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 50298

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 1 | `ORIGINBUSINESSPARTNERNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 2 | `ORIGINPHYWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 3 | `ORIGINPHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 4 | `CODE` | CHAR(8) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `ORIGINDELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 6 | `ORIGINDELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 7 | `ADDRESSTYPE` | INTEGER | NOT NULL |  |  |  |
| 8 | `ADDRESSEE` | VARCHAR(200) | NOT NULL |  |  |  |
| 9 | `COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 10 | `ADDRESSLINE1` | VARCHAR(150) | NOT NULL |  |  |  |
| 11 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 12 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 13 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 14 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 15 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 16 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 17 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 18 | `TRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 19 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 20 | `ADDRESSFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 21 | `EMAILADDRESS` | VARCHAR(200) |  |  |  |  |
| 22 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 23 | `WORKINGCALENDARCODE` | CHAR(3) |  |  |  |  |
| 24 | `ACKNOWLEDGEMENTREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 25 | `ACKNOWLEDGEMENTTYPE` | CHAR(2) |  |  |  |  |
| 26 | `TAXREGISTRATIONNUMBER` | CHAR(15) |  |  |  |  |
| 27 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 28 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 29 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 30 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 31 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 32 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 33 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 34 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 35 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 36 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 37 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 38 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 39 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 40 | `ADDRESSEE2` | VARCHAR(200) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGADDRESS.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.UNIQUEID,
       t.ORIGINBUSINESSPARTNERNUMBERID,
       t.ORIGINPHYWAREHOUSECOMPANYCODE,
       t.ORIGINPHYSICALWAREHOUSECODE,
       t.CODE,
       t.ORIGINDELIVERYPOINTUNIQUEID,
       t.ORIGINDELIVERYPOINTCODE,
       t.ADDRESSTYPE,
       t.ADDRESSEE,
       t.COUNTRYCODE,
       t.ADDRESSLINE1,
       t.ADDRESSLINE2
FROM   DB2ADMIN.LOGADDRESS t
FETCH FIRST 100 ROWS ONLY;
```
