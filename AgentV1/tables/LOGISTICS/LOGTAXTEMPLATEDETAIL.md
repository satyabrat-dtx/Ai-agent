# DB2ADMIN.LOGTAXTEMPLATEDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 33
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 220781

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TAXTEMPLATEHEADERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `TAXTEMPLATEHEADERCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `TAXTMPHEADEREFFECTIVEFROMDATE` | DATE | NOT NULL |  |  |  |
| 3 | `ITAXCODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `CALCULATIONSEQUENCE` | DECIMAL(2,0) | NOT NULL |  |  |  |
| 5 | `ROUNDOFFTYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `ROUNDOFFAMOUNT` | DECIMAL(10,5) | NOT NULL |  |  |  |
| 7 | `TAXCODETYPE` | INTEGER | NOT NULL |  |  |  |
| 8 | `CALCULATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 9 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 10 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 11 | `SIGN` | INTEGER | NOT NULL |  |  |  |
| 12 | `CALCULATIONBASISCODE` | CHAR(3) |  |  |  |  |
| 13 | `MODVATSETOFF` | INTEGER | NOT NULL |  |  |  |
| 14 | `MODVAT` | INTEGER | NOT NULL |  |  |  |
| 15 | `MODVATCYPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 16 | `MODVATNYPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 17 | `ALLOCATIONBASIS` | INTEGER | NOT NULL |  |  |  |
| 18 | `SOURCEAPPLICABLE` | INTEGER | NOT NULL |  |  |  |
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
| 32 | `POSTINFINANCE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGTAXTEMPLATEDETAIL.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.TAXTEMPLATEHEADERCOMPANYCODE,
       t.TAXTEMPLATEHEADERCODE,
       t.TAXTMPHEADEREFFECTIVEFROMDATE,
       t.ITAXCODE,
       t.CALCULATIONSEQUENCE,
       t.ROUNDOFFTYPE,
       t.ROUNDOFFAMOUNT,
       t.TAXCODETYPE,
       t.CALCULATIONTYPE,
       t.VALUE,
       t.CURRENCYCODE,
       t.SIGN
FROM   DB2ADMIN.LOGTAXTEMPLATEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
