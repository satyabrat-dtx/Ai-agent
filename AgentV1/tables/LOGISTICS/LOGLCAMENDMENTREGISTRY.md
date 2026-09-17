# DB2ADMIN.LOGLCAMENDMENTREGISTRY

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 30
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 221753

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LCDETAILCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `LCDETAILLCNO` | CHAR(35) | NOT NULL |  |  |  |
| 2 | `LCDETAILLCDATE` | DATE | NOT NULL |  |  |  |
| 3 | `LCAMENDMENTNO` | DECIMAL(2,0) | NOT NULL |  |  |  |
| 4 | `LCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 5 | `AMENDMENTDATE` | DATE |  |  |  |  |
| 6 | `AMEDNMENTQUANTITY` | DECIMAL(18,5) |  |  |  |  |
| 7 | `AMENDMENTAMT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `AMENDMENTGROSSAMT` | DECIMAL(18,5) |  |  |  |  |
| 9 | `NETQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 10 | `NETAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `TOTALGROSSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 12 | `EXTENDEDSHIPMENTDATE` | DATE |  |  |  |  |
| 13 | `EXTENDEDEXPIRYDATE` | DATE |  |  |  |  |
| 14 | `UGGUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 15 | `UGGCODE` | CHAR(10) |  |  |  |  |
| 16 | `REMARKS` | VARCHAR(100) |  |  |  |  |
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

- `FATHERID` → **LOGLCAMENDMENT**.`ABSUNIQUEID` (medium confidence — name = 'LOGLCAMENDMENT' + recurring fragment 'REGISTRY' (seen in 4 tables))
  - JOIN predicate: `LOGLCAMENDMENTREGISTRY.FATHERID = LOGLCAMENDMENT.ABSUNIQUEID`

## Starter query

```sql
SELECT t.LCDETAILCOMPANYCODE,
       t.LCDETAILLCNO,
       t.LCDETAILLCDATE,
       t.LCAMENDMENTNO,
       t.LCVALUE,
       t.AMENDMENTDATE,
       t.AMEDNMENTQUANTITY,
       t.AMENDMENTAMT,
       t.AMENDMENTGROSSAMT,
       t.NETQUANTITY,
       t.NETAMOUNT,
       t.TOTALGROSSAMOUNT
FROM   DB2ADMIN.LOGLCAMENDMENTREGISTRY t
FETCH FIRST 100 ROWS ONLY;
```
