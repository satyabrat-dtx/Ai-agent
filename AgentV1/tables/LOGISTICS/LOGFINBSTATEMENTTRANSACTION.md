# DB2ADMIN.LOGFINBSTATEMENTTRANSACTION

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 27
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 225391

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL |  |  |  |
| 2 | `BANKGLCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `BANKGLCODE` | CHAR(20) | NOT NULL |  |  |  |
| 4 | `SERIALNO` | CHAR(15) | NOT NULL |  |  |  |
| 5 | `FINMONTH` | INTEGER | NOT NULL |  |  |  |
| 6 | `TRANSACTIONDATE` | DATE |  |  |  |  |
| 7 | `NARRATION` | VARCHAR(255) |  |  |  |  |
| 8 | `CHEQUENO` | CHAR(15) |  |  |  |  |
| 9 | `CREDIT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `DEBIT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `RECONCILATIONTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 12 | `BANKBALANCE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `UTRNO` | VARCHAR(100) |  |  |  |  |
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

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINBSTATEMENTTRANSACTION.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.BANKGLCOMPANYCODE,
       t.BANKGLCODE,
       t.SERIALNO,
       t.FINMONTH,
       t.TRANSACTIONDATE,
       t.NARRATION,
       t.CHEQUENO,
       t.CREDIT,
       t.DEBIT,
       t.RECONCILATIONTRANSACTIONNUMBER
FROM   DB2ADMIN.LOGFINBSTATEMENTTRANSACTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
