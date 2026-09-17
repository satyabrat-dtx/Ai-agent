# DB2ADMIN.LOGINTORDERDELIVERYBLOCKS

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 35
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 52102

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `ORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `INTORDERDELIVERYDELIVERYLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 6 | `BLOCKSORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 7 | `BLOCKSCODE` | CHAR(3) | NOT NULL |  |  |  |
| 8 | `BLOCKDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 9 | `APPLICATIONDOCUMENTTYPE` | CHAR(3) | NOT NULL |  |  |  |
| 10 | `APPLICATIONDOCUMENTACTIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 11 | `APPLYONCREATE` | SMALLINT | NOT NULL |  |  |  |
| 12 | `APPLYONUPDATE` | SMALLINT | NOT NULL |  |  |  |
| 13 | `APPLYONDELETE` | SMALLINT | NOT NULL |  |  |  |
| 14 | `UNBLOCKINGSEQUENCE` | DECIMAL(2,0) |  |  |  |  |
| 15 | `UNBLOCKINGTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 16 | `UNBLOCKINGUSER` | CHAR(50) |  |  |  |  |
| 17 | `UNBLOCKINGDATE` | DATE |  |  |  |  |
| 18 | `UNBLOCKINGTIME` | TIME |  |  |  |  |
| 19 | `CREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 20 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 21 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 27 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 28 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 29 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 30 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 31 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 32 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 33 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 34 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGINTORDERDELIVERYBLOCKS.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCODE,
       t.ORDERCODE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.INTORDERDELIVERYDELIVERYLINE,
       t.BLOCKSORDERTYPE,
       t.BLOCKSCODE,
       t.BLOCKDESCRIPTION,
       t.APPLICATIONDOCUMENTTYPE,
       t.APPLICATIONDOCUMENTACTIONCODE,
       t.APPLYONCREATE
FROM   DB2ADMIN.LOGINTORDERDELIVERYBLOCKS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
