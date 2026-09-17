# DB2ADMIN.LOGVATDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 25
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 103516

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `VATCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `VATCODE` | CHAR(5) | NOT NULL |  |  |  |
| 2 | `VALIDFROM` | DATE | NOT NULL |  |  | Inclusive start of a validity period. |
| 3 | `PERCENTAGERATE` | DECIMAL(6,3) |  |  |  |  |
| 4 | `CALCULATIONMETHOD` | CHAR(1) | NOT NULL |  |  |  |
| 5 | `ACCOUNTPURCHASETAXCODE` | CHAR(10) |  |  |  |  |
| 6 | `ACCOUNTSALESTAXCODE` | CHAR(10) |  |  |  |  |
| 7 | `DISCOUNTACCOUNTCASHCODE` | CHAR(10) |  |  |  |  |
| 8 | `DISCOUNTACCOUNTOTHERCODE` | CHAR(10) |  |  |  |  |
| 9 | `NUMBERVAT` | CHAR(5) |  |  |  |  |
| 10 | `TAXNOWCODE` | CHAR(3) |  |  |  |  |
| 11 | `NONDEDUCTIBLEINPUTTAX` | SMALLINT | NOT NULL |  |  |  |
| 12 | `NONDEDUCTIBLEPERCENT` | DECIMAL(6,3) |  |  |  |  |
| 13 | `NONDEDUCTIBLETAXACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 14 | `EXPENSEACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 20 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 21 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 22 | `LOGUSER` | CHAR(25) |  |  | audit | User responsible for the audited change (change-log table). |
| 23 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 24 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGVAT**.`ABSUNIQUEID` (high confidence — name = 'LOGVAT' + known child suffix 'DETAIL')
  - JOIN predicate: `LOGVATDETAIL.FATHERID = LOGVAT.ABSUNIQUEID`

## Starter query

```sql
SELECT t.VATCOMPANYCODE,
       t.VATCODE,
       t.VALIDFROM,
       t.PERCENTAGERATE,
       t.CALCULATIONMETHOD,
       t.ACCOUNTPURCHASETAXCODE,
       t.ACCOUNTSALESTAXCODE,
       t.DISCOUNTACCOUNTCASHCODE,
       t.DISCOUNTACCOUNTOTHERCODE,
       t.NUMBERVAT,
       t.TAXNOWCODE,
       t.NONDEDUCTIBLEINPUTTAX
FROM   DB2ADMIN.LOGVATDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
