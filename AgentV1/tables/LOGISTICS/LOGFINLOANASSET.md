# DB2ADMIN.LOGFINLOANASSET

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 25
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 229228

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINLOANMASTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINLMLTEUGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `FINLOANMASTERLOANTYPECODE` | CHAR(10) | NOT NULL |  |  |  |
| 3 | `FINLOANMASTERLOANNO` | CHAR(10) | NOT NULL |  |  |  |
| 4 | `SLNO` | INTEGER | NOT NULL |  |  |  |
| 5 | `ASSETNAME` | CHAR(30) |  |  |  |  |
| 6 | `QUANTITY` | DECIMAL(4,0) |  |  |  |  |
| 7 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 8 | `DISBURSEMENT` | DECIMAL(18,5) |  |  |  |  |
| 9 | `DISBURSEMENTDATE` | DATE |  |  |  |  |
| 10 | `INTERESTSUBSIDY` | DECIMAL(3,0) |  |  |  |  |
| 11 | `CAPITALSUBSIDY` | DECIMAL(3,0) |  |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 19 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 20 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 21 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 22 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 23 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 24 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINLOANASSET.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FINLOANMASTERCOMPANYCODE,
       t.FINLMLTEUGENERICGROUPTYPECODE,
       t.FINLOANMASTERLOANTYPECODE,
       t.FINLOANMASTERLOANNO,
       t.SLNO,
       t.ASSETNAME,
       t.QUANTITY,
       t.COST,
       t.DISBURSEMENT,
       t.DISBURSEMENTDATE,
       t.INTERESTSUBSIDY,
       t.CAPITALSUBSIDY
FROM   DB2ADMIN.LOGFINLOANASSET t
FETCH FIRST 100 ROWS ONLY;
```
