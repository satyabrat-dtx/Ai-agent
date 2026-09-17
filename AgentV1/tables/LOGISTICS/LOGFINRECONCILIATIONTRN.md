# DB2ADMIN.LOGFINRECONCILIATIONTRN

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 32
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 223870

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TRANSACTIONNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 2 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 3 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL |  |  |  |
| 4 | `BANKGLCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `BANKGLCODE` | CHAR(20) | NOT NULL |  |  |  |
| 6 | `FINMONTHFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 7 | `FINMONTHBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 8 | `FINMONTHCODE` | INTEGER | NOT NULL |  |  |  |
| 9 | `FDLFINDOCUMENTBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 10 | `FDLFINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 11 | `FDLFINDOCDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 12 | `FDLFINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 13 | `FDLFINDOCUMENTCODE` | CHAR(15) |  |  |  |  |
| 14 | `FDLLINENUMBER` | DECIMAL(7,0) |  |  |  |  |
| 15 | `FBSTATETRANBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 16 | `FBSTATETRANBANKGLCODE` | CHAR(20) |  |  |  |  |
| 17 | `FBSTATETRANSERIALNO` | CHAR(15) |  |  |  |  |
| 18 | `REMARKS` | VARCHAR(100) |  |  |  |  |
| 19 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 20 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 21 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 22 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 23 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 24 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 25 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 26 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 27 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 28 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 29 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 30 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 31 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINRECONCILIATIONTRN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TRANSACTIONNUMBER,
       t.LINENO,
       t.BUSINESSUNITCODE,
       t.BANKGLCOMPANYCODE,
       t.BANKGLCODE,
       t.FINMONTHFINANCIALYEARCODE,
       t.FINMONTHBUSINESSUNITCODE,
       t.FINMONTHCODE,
       t.FDLFINDOCUMENTBUSINESSUNITCODE,
       t.FDLFINDOCFINANCIALYEARCODE,
       t.FDLFINDOCDOCUMENTTEMPLATECODE
FROM   DB2ADMIN.LOGFINRECONCILIATIONTRN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
