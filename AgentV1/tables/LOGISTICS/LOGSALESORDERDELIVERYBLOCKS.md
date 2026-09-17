# DB2ADMIN.LOGSALESORDERDELIVERYBLOCKS

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 36
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 55262

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `ORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `COMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 6 | `SALESORDERDELIVERYDELIVERYLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 7 | `BLOCKSORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 8 | `BLOCKSCODE` | CHAR(3) | NOT NULL |  |  |  |
| 9 | `BLOCKDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 10 | `APPLICATIONDOCUMENTTYPE` | CHAR(3) | NOT NULL |  |  |  |
| 11 | `APPLICATIONDOCUMENTACTIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 12 | `APPLYONCREATE` | SMALLINT | NOT NULL |  |  |  |
| 13 | `APPLYONUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 14 | `APPLYONDELETE` | SMALLINT | NOT NULL |  |  |  |
| 15 | `UNBLOCKINGSEQUENCE` | DECIMAL(2,0) |  |  |  |  |
| 16 | `UNBLOCKINGTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 17 | `UNBLOCKINGUSER` | CHAR(50) |  |  |  |  |
| 18 | `UNBLOCKINGDATE` | DATE |  |  |  |  |
| 19 | `UNBLOCKINGTIME` | TIME |  |  |  |  |
| 20 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 21 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 22 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 23 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 24 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 25 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 26 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 27 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 28 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 29 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 30 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 31 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 32 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 33 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 34 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 35 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGSALESORDERDELIVERY**.`ABSUNIQUEID` (high confidence — name = 'LOGSALESORDERDELIVERY' + known child suffix 'BLOCKS')
  - JOIN predicate: `LOGSALESORDERDELIVERYBLOCKS.FATHERID = LOGSALESORDERDELIVERY.ABSUNIQUEID`

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCODE,
       t.ORDERCODE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.COMPONENTORDERLINE,
       t.SALESORDERDELIVERYDELIVERYLINE,
       t.BLOCKSORDERTYPE,
       t.BLOCKSCODE,
       t.BLOCKDESCRIPTION,
       t.APPLICATIONDOCUMENTTYPE,
       t.APPLICATIONDOCUMENTACTIONCODE
FROM   DB2ADMIN.LOGSALESORDERDELIVERYBLOCKS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
