# DB2ADMIN.LOGFINRECONCILEOPENENTRY

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 29
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 228182

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL |  |  |  |
| 2 | `BANKGLCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `BANKGLCODE` | CHAR(20) | NOT NULL |  |  |  |
| 4 | `FDLFINDOCFINANCIALYEARCODE` | DECIMAL(4,0) | NOT NULL |  |  |  |
| 5 | `FDLFINDOCDOCUMENTTEMPLATECODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `FDLFINDOCSTATISTICALGROUPCODE` | CHAR(6) | NOT NULL |  |  |  |
| 7 | `FDLFINDOCUMENTCODE` | CHAR(15) | NOT NULL |  |  |  |
| 8 | `FDLLINENUMBER` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 9 | `RECONCILETRANNO` | CHAR(15) |  |  |  |  |
| 10 | `POSTINGDATE` | DATE |  |  |  |  |
| 11 | `CHEQUENO` | CHAR(20) |  |  |  |  |
| 12 | `UTRNO` | CHAR(50) |  |  |  |  |
| 13 | `NARRATION` | VARCHAR(255) |  |  |  |  |
| 14 | `CREDIT` | DECIMAL(18,5) |  |  |  |  |
| 15 | `DEBIT` | DECIMAL(18,5) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 23 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 24 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 25 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 26 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 27 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 28 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINRECONCILEOPENENTRY.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.BANKGLCOMPANYCODE,
       t.BANKGLCODE,
       t.FDLFINDOCFINANCIALYEARCODE,
       t.FDLFINDOCDOCUMENTTEMPLATECODE,
       t.FDLFINDOCSTATISTICALGROUPCODE,
       t.FDLFINDOCUMENTCODE,
       t.FDLLINENUMBER,
       t.RECONCILETRANNO,
       t.POSTINGDATE,
       t.CHEQUENO
FROM   DB2ADMIN.LOGFINRECONCILEOPENENTRY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
