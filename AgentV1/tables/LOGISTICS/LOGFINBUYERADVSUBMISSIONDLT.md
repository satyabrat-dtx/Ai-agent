# DB2ADMIN.LOGFINBUYERADVSUBMISSIONDLT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 28
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 202107

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINBUYERADVSUBMISSIONCMYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINBUYERADVSUBMISSIONACODE` | CHAR(5) | NOT NULL |  |  |  |
| 2 | `FINBUYERADVSUBMISSIONCODE` | CHAR(10) | NOT NULL |  |  |  |
| 3 | `SOCODECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 4 | `SOCODECODE` | CHAR(15) |  |  |  |  |
| 5 | `OPCODECUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 6 | `OPCODECUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 7 | `INVOICENODIVISIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 8 | `INVOICENOCODE` | CHAR(20) | NOT NULL |  |  |  |
| 9 | `INVOICEDT` | DATE |  |  |  |  |
| 10 | `INVOICECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 11 | `INVEXCHANGERATE` | DECIMAL(18,5) |  |  |  |  |
| 12 | `INVOICEAMT` | DECIMAL(18,5) |  |  |  |  |
| 13 | `ADJUSTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 14 | `CCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 22 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 23 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 24 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 25 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 26 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 27 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINBUYERADVSUBMISSIONDLT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FINBUYERADVSUBMISSIONCMYCODE,
       t.FINBUYERADVSUBMISSIONACODE,
       t.FINBUYERADVSUBMISSIONCODE,
       t.SOCODECOUNTERCODE,
       t.SOCODECODE,
       t.OPCODECUSTOMERSUPPLIERTYPE,
       t.OPCODECUSTOMERSUPPLIERCODE,
       t.INVOICENODIVISIONCODE,
       t.INVOICENOCODE,
       t.INVOICEDT,
       t.INVOICECURRENCYCODE,
       t.INVEXCHANGERATE
FROM   DB2ADMIN.LOGFINBUYERADVSUBMISSIONDLT t
FETCH FIRST 100 ROWS ONLY;
```
