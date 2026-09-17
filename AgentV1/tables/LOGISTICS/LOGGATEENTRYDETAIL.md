# DB2ADMIN.LOGGATEENTRYDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 18
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 217204

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `GATEENTRYCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `GATEENTRYMAINGATEENTRYSRNO` | CHAR(20) | NOT NULL |  |  |  |
| 2 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 3 | `MATERIALNAME` | VARCHAR(200) |  |  |  |  |
| 4 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 5 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 6 | `PLANTINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 7 | `PLANTINVOICECODE` | CHAR(15) |  |  |  |  |
| 8 | `INTDOCPROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 9 | `INTDOCUMENTPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 10 | `TOTALQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 13 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 14 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 15 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 16 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 17 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGGATEENTRY**.`ABSUNIQUEID` (high confidence — name = 'LOGGATEENTRY' + known child suffix 'DETAIL')
  - JOIN predicate: `LOGGATEENTRYDETAIL.FATHERID = LOGGATEENTRY.ABSUNIQUEID`

## Starter query

```sql
SELECT t.GATEENTRYCOMPANYCODE,
       t.GATEENTRYMAINGATEENTRYSRNO,
       t.LINENO,
       t.MATERIALNAME,
       t.QUANTITY,
       t.UOMCODE,
       t.PLANTINVOICEDIVISIONCODE,
       t.PLANTINVOICECODE,
       t.INTDOCPROVISIONALCOUNTERCODE,
       t.INTDOCUMENTPROVISIONALCODE,
       t.TOTALQUANTITY,
       t.ABSUNIQUEID
FROM   DB2ADMIN.LOGGATEENTRYDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
