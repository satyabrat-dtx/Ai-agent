# DB2ADMIN.LOGSTATUSRULEPOLICY

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 29
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 194603

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `STATUSCODE` | CHAR(8) | NOT NULL |  |  |  |
| 3 | `LINENR` | INTEGER | NOT NULL |  |  |  |
| 4 | `STATUSRULECOMBINATIONSUBLINE` | INTEGER | NOT NULL |  |  |  |
| 5 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 6 | `STATUSPOLICYCODECODE` | CHAR(8) | NOT NULL |  |  |  |
| 7 | `QUANTITYFROM` | DECIMAL(15,5) |  |  |  |  |
| 8 | `QUANTITYTO` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 9 | `QUANTITYCALCRULECODE` | CHAR(20) |  |  |  |  |
| 10 | `TEMPLATELIST` | VARCHAR(2000) |  |  |  |  |
| 11 | `TEMPLATERULE` | INTEGER | NOT NULL |  |  |  |
| 12 | `ALLOWCHANGE` | SMALLINT | NOT NULL |  |  |  |
| 13 | `NOTIFICATIONMESSAGEMESSAGECODE` | CHAR(8) |  |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 22 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 23 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 24 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 25 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 26 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 27 | `DIVISIONLIST` | VARCHAR(2000) |  |  |  |  |
| 28 | `DIVISIONRULE` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGSTATUSRULEPOLICY.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.STATUSCODE,
       t.LINENR,
       t.STATUSRULECOMBINATIONSUBLINE,
       t.SEQUENCE,
       t.STATUSPOLICYCODECODE,
       t.QUANTITYFROM,
       t.QUANTITYTO,
       t.QUANTITYCALCRULECODE,
       t.TEMPLATELIST,
       t.TEMPLATERULE
FROM   DB2ADMIN.LOGSTATUSRULEPOLICY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
