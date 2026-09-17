# DB2ADMIN.LOGBILLOFEXCHANGEDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 24
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 200946

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BILLOFEXCHANGECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `BILLOFEXCHANGEDIVISIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `BILLOFEXCHANGECODE` | CHAR(12) | NOT NULL |  |  |  |
| 3 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 4 | `INVOICETYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `COMMERCIALINVOICECODE` | CHAR(20) |  |  |  |  |
| 6 | `INVOICEDATE` | DATE | NOT NULL |  |  |  |
| 7 | `NETVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 8 | `LCLCNO` | CHAR(35) |  |  |  |  |
| 9 | `LCLCDATE` | DATE |  |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 17 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 18 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 19 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 20 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 21 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 22 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 23 | `CLEAREDVALUE` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGBILLOFEXCHANGE**.`ABSUNIQUEID` (high confidence — name = 'LOGBILLOFEXCHANGE' + known child suffix 'DETAIL')
  - JOIN predicate: `LOGBILLOFEXCHANGEDETAIL.FATHERID = LOGBILLOFEXCHANGE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.BILLOFEXCHANGECOMPANYCODE,
       t.BILLOFEXCHANGEDIVISIONCODE,
       t.BILLOFEXCHANGECODE,
       t.LINENO,
       t.INVOICETYPECODE,
       t.COMMERCIALINVOICECODE,
       t.INVOICEDATE,
       t.NETVALUE,
       t.LCLCNO,
       t.LCLCDATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.LOGBILLOFEXCHANGEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
