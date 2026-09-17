# DB2ADMIN.LOGFINOPENDOCUMENTSTRN

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 36
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 225439

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSVERSIONNUMBER` | BIGINT | NOT NULL |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `TRANSACTIONNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `TRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 4 | `TRANSACTIONDATE` | DATE | NOT NULL |  |  |  |
| 5 | `ORIGINBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 6 | `ORIGINFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 7 | `ORIGINDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 8 | `ORIGINSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 9 | `ORIGINCODE` | CHAR(15) |  |  |  |  |
| 10 | `ORIGINLINENUMBER` | DECIMAL(7,0) |  |  |  |  |
| 11 | `ORIGINTYPE` | INTEGER | NOT NULL |  |  |  |
| 12 | `ORIGINDUEDATE` | DATE |  |  |  |  |
| 13 | `DESTBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 14 | `DESTFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 15 | `DESTDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 16 | `DESTSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 17 | `DESTCODE` | CHAR(15) |  |  |  |  |
| 18 | `DESTLINENUMBER` | DECIMAL(7,0) |  |  |  |  |
| 19 | `DESTINATIONDUEDATE` | DATE |  |  |  |  |
| 20 | `CLEAREDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 21 | `CLEAREDAMOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 22 | `CLEAREDBYCC` | SMALLINT | NOT NULL |  |  |  |
| 23 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 24 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 25 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 26 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 27 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 28 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 30 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 31 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 32 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 33 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 34 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 35 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINOPENDOCUMENTSTRN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.ABSVERSIONNUMBER,
       t.COMPANYCODE,
       t.TRANSACTIONNUMBER,
       t.TRANSACTIONDETAILNUMBER,
       t.TRANSACTIONDATE,
       t.ORIGINBUSINESSUNITCODE,
       t.ORIGINFINANCIALYEARCODE,
       t.ORIGINDOCUMENTTEMPLATECODE,
       t.ORIGINSTATISTICALGROUPCODE,
       t.ORIGINCODE,
       t.ORIGINLINENUMBER,
       t.ORIGINTYPE
FROM   DB2ADMIN.LOGFINOPENDOCUMENTSTRN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
