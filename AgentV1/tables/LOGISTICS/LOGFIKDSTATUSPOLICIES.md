# DB2ADMIN.LOGFIKDSTATUSPOLICIES

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 22
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 190343

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `STATUSCODE` | CHAR(8) | NOT NULL |  |  |  |
| 5 | `STATUSRULELINENR` | INTEGER | NOT NULL |  |  |  |
| 6 | `SUBLINE` | INTEGER | NOT NULL |  |  |  |
| 7 | `ENABLED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `ISRULEPRIMARYKEY` | SMALLINT | NOT NULL |  |  |  |
| 9 | `FORCEDSTATUS` | SMALLINT | NOT NULL |  |  |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 12 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 13 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 14 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 15 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 16 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 17 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 18 | `AUTOMATIC` | SMALLINT | NOT NULL |  |  |  |
| 19 | `NOSTATUSMANAGED` | INTEGER | NOT NULL |  |  |  |
| 20 | `ISCONFIGROW` | SMALLINT | NOT NULL |  |  |  |
| 21 | `BATCHLOCK` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFIKDSTATUSPOLICIES.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.UNIQUEID,
       t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.STATUSCODE,
       t.STATUSRULELINENR,
       t.SUBLINE,
       t.ENABLED,
       t.ISRULEPRIMARYKEY,
       t.FORCEDSTATUS,
       t.ABSUNIQUEID,
       t.LOGTIMESTAMP
FROM   DB2ADMIN.LOGFIKDSTATUSPOLICIES t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
