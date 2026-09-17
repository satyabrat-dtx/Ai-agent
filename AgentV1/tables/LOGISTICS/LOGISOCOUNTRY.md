# DB2ADMIN.LOGISOCOUNTRY

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 37
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 102651

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(2) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(100) |  |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `ISO3A` | CHAR(3) |  |  |  |  |
| 5 | `ISO3N` | DECIMAL(3,0) |  |  |  |  |
| 6 | `EUMEMBER` | SMALLINT | NOT NULL |  |  |  |
| 7 | `EUROMEMBER` | SMALLINT | NOT NULL |  |  |  |
| 8 | `IBANMEMBER` | SMALLINT | NOT NULL |  |  |  |
| 9 | `SEPAMEMBER` | SMALLINT | NOT NULL |  |  |  |
| 10 | `IBANCHECKRULE` | CHAR(1) |  |  |  |  |
| 11 | `BICCHECKRULE` | CHAR(1) |  |  |  |  |
| 12 | `CLEARINGCHECKRULE` | CHAR(1) |  |  |  |  |
| 13 | `VALIDATEIBAN` | SMALLINT | NOT NULL |  |  |  |
| 14 | `VALIDATEBIC` | SMALLINT | NOT NULL |  |  |  |
| 15 | `VALIDATEBANKMASTER` | SMALLINT | NOT NULL |  |  |  |
| 16 | `IBANCOUNTRYMATCH` | SMALLINT | NOT NULL |  |  |  |
| 17 | `BICCOUNTRYMATCH` | SMALLINT | NOT NULL |  |  |  |
| 18 | `IBANISOOVERRIDECODE` | CHAR(2) |  |  |  |  |
| 19 | `BICISOOVERRIDECODE` | CHAR(2) |  |  |  |  |
| 20 | `ACCOUNTVALIDATIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 21 | `CLEARINGVALIDATIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 22 | `BICVALIDATIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 23 | `BANKDETAILVALIDATIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 24 | `LENGTHOFCLEARING` | INTEGER | NOT NULL |  |  |  |
| 25 | `LENGTHOFACCOUNT` | INTEGER | NOT NULL |  |  |  |
| 26 | `STARTOFACCOUNT` | INTEGER | NOT NULL |  |  |  |
| 27 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 28 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 29 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 30 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 31 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 32 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 33 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 34 | `LOGUSER` | CHAR(25) |  |  | audit | User responsible for the audited change (change-log table). |
| 35 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 36 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGISOCOUNTRY.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ISO3A,
       t.ISO3N,
       t.EUMEMBER,
       t.EUROMEMBER,
       t.IBANMEMBER,
       t.SEPAMEMBER,
       t.IBANCHECKRULE,
       t.BICCHECKRULE
FROM   DB2ADMIN.LOGISOCOUNTRY t
FETCH FIRST 100 ROWS ONLY;
```
