# DB2ADMIN.LOGFINPOADVANCEPROPOSALLINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 24
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 230883

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINPOADVANCEPROPOSALCMYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINPOADVANCEPROPOSALCODE` | CHAR(15) | NOT NULL |  |  |  |
| 2 | `POADVPURCHASEORDERCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 3 | `POADVPURCHASEORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 4 | `POADVLINENO` | INTEGER | NOT NULL |  |  |  |
| 5 | `FDBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 6 | `FDFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 7 | `FDDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 8 | `FDSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 9 | `FDCODE` | CHAR(15) |  |  |  |  |
| 10 | `ADVANCEPAYMENT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 18 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 19 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 20 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 21 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 22 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 23 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGFINPOADVANCEPROPOSAL**.`ABSUNIQUEID` (high confidence — name = 'LOGFINPOADVANCEPROPOSAL' + known child suffix 'LINE')
  - JOIN predicate: `LOGFINPOADVANCEPROPOSALLINE.FATHERID = LOGFINPOADVANCEPROPOSAL.ABSUNIQUEID`

## Starter query

```sql
SELECT t.FINPOADVANCEPROPOSALCMYCODE,
       t.FINPOADVANCEPROPOSALCODE,
       t.POADVPURCHASEORDERCOUNTERCODE,
       t.POADVPURCHASEORDERCODE,
       t.POADVLINENO,
       t.FDBUSINESSUNITCODE,
       t.FDFINANCIALYEARCODE,
       t.FDDOCUMENTTEMPLATECODE,
       t.FDSTATISTICALGROUPCODE,
       t.FDCODE,
       t.ADVANCEPAYMENT,
       t.CREATIONDATETIME
FROM   DB2ADMIN.LOGFINPOADVANCEPROPOSALLINE t
FETCH FIRST 100 ROWS ONLY;
```
