# DB2ADMIN.LOGEMPLOYEEPREFIX

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 25
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 222751

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `CATEGORYICSTABLECODE` | CHAR(4) | NOT NULL |  |  |  |
| 3 | `CATEGORYCODE` | CHAR(6) | NOT NULL |  |  |  |
| 4 | `CODE` | CHAR(3) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `FLAG` | INTEGER | NOT NULL |  |  |  |
| 6 | `STARTINGNO` | DECIMAL(6,0) |  |  |  |  |
| 7 | `CURRENTNO` | DECIMAL(6,0) |  |  |  |  |
| 8 | `PADDINGREQUIRED` | INTEGER | NOT NULL |  |  |  |
| 9 | `NOOFZEROSPADDED` | INTEGER | NOT NULL |  |  |  |
| 10 | `LOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 11 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
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

- `FATHERID` → **LOGEMPLOYEE**.`ABSUNIQUEID` (medium confidence — name = 'LOGEMPLOYEE' + recurring fragment 'PREFIX' (seen in 5 tables))
  - JOIN predicate: `LOGEMPLOYEEPREFIX.FATHERID = LOGEMPLOYEE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CATEGORYICSTABLECODE,
       t.CATEGORYCODE,
       t.CODE,
       t.FLAG,
       t.STARTINGNO,
       t.CURRENTNO,
       t.PADDINGREQUIRED,
       t.NOOFZEROSPADDED,
       t.LOGMANAGEMENT,
       t.TERMSOFLOGCODE
FROM   DB2ADMIN.LOGEMPLOYEEPREFIX t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
