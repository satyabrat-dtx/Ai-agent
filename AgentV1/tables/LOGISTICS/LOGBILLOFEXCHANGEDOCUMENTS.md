# DB2ADMIN.LOGBILLOFEXCHANGEDOCUMENTS

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 30
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 200991

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BILLOFEXCHANGECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `BILLOFEXCHANGEDIVISIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `BILLOFEXCHANGECODE` | CHAR(12) | NOT NULL |  |  |  |
| 3 | `LINENO` | DECIMAL(8,0) | NOT NULL |  |  |  |
| 4 | `DRAFT` | CHAR(15) |  |  |  |  |
| 5 | `BLAWB` | CHAR(15) |  |  |  |  |
| 6 | `INVOICE` | CHAR(15) |  |  |  |  |
| 7 | `INSURCERTIFICATE` | CHAR(15) |  |  |  |  |
| 8 | `CERTORG` | CHAR(15) |  |  |  |  |
| 9 | `CUSTOMSINV` | CHAR(15) |  |  |  |  |
| 10 | `NOOFCARTONS` | INTEGER | NOT NULL |  |  |  |
| 11 | `PACKINGLIST` | CHAR(15) |  |  |  |  |
| 12 | `INSREPT` | CHAR(15) |  |  |  |  |
| 13 | `GSPCERT` | CHAR(15) |  |  |  |  |
| 14 | `OTHERDOCS` | CHAR(120) |  |  |  |  |
| 15 | `BENCERT` | CHAR(15) |  |  |  |  |
| 16 | `NOOFPCS` | INTEGER | NOT NULL |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 24 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 25 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 26 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 27 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 28 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 29 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGBILLOFEXCHANGE**.`ABSUNIQUEID` (medium confidence — name = 'LOGBILLOFEXCHANGE' + recurring fragment 'DOCUMENTS' (seen in 5 tables))
  - JOIN predicate: `LOGBILLOFEXCHANGEDOCUMENTS.FATHERID = LOGBILLOFEXCHANGE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.BILLOFEXCHANGECOMPANYCODE,
       t.BILLOFEXCHANGEDIVISIONCODE,
       t.BILLOFEXCHANGECODE,
       t.LINENO,
       t.DRAFT,
       t.BLAWB,
       t.INVOICE,
       t.INSURCERTIFICATE,
       t.CERTORG,
       t.CUSTOMSINV,
       t.NOOFCARTONS,
       t.PACKINGLIST
FROM   DB2ADMIN.LOGBILLOFEXCHANGEDOCUMENTS t
FETCH FIRST 100 ROWS ONLY;
```
