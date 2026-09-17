# DB2ADMIN.LOGFINLOANDISBURSEMENT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 45
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 225998

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SLNO` | INTEGER | NOT NULL |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LTEUGENGROUPTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `LTYPEUSERGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `LOANTYPECODE` | CHAR(10) | NOT NULL |  |  |  |
| 5 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 6 | `CODELOANNO` | CHAR(10) | NOT NULL |  |  |  |
| 7 | `DISBURSEMENTDATE` | DATE |  |  |  |  |
| 8 | `DISBURSEMENTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 9 | `CONVERSIONRATE` | DECIMAL(4,0) | NOT NULL |  |  |  |
| 10 | `CONVERTEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 11 | `BANKGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 12 | `BANKGLCODE` | CHAR(20) |  |  |  |  |
| 13 | `REFERENCENO` | CHAR(15) |  |  |  |  |
| 14 | `REFERENCEDATE` | DATE |  |  |  |  |
| 15 | `TERMLOANGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 16 | `TERMLOANGLCODE` | CHAR(20) |  |  |  |  |
| 17 | `INSTRUMENTTYPE` | CHAR(15) |  |  |  |  |
| 18 | `INSTRUMENTNO` | CHAR(15) |  |  |  |  |
| 19 | `INSTRUMENTDATE` | DATE |  |  |  |  |
| 20 | `DRAWNON` | CHAR(20) |  |  |  |  |
| 21 | `BANKCHARGESVALUE` | DECIMAL(18,5) |  |  |  |  |
| 22 | `BANKCHARGESGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `BANKCHARGESGLCODE` | CHAR(20) |  |  |  |  |
| 24 | `COSTCENTERFINBVSPPCENTERCODE` | CHAR(10) |  |  |  |  |
| 25 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 26 | `POSTINGDATE` | DATE |  |  |  |  |
| 27 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 28 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 29 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 30 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 31 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 32 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 33 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 34 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 35 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 36 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 37 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 38 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 39 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 40 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 41 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 42 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 43 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 44 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINLOANDISBURSEMENT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.SLNO,
       t.COMPANYCODE,
       t.LTEUGENGROUPTYPECOMPANYCODE,
       t.LTYPEUSERGENERICGROUPTYPECODE,
       t.LOANTYPECODE,
       t.BUSINESSUNITCODE,
       t.CODELOANNO,
       t.DISBURSEMENTDATE,
       t.DISBURSEMENTAMOUNT,
       t.CONVERSIONRATE,
       t.CONVERTEDVALUE,
       t.BANKGLCOMPANYCODE
FROM   DB2ADMIN.LOGFINLOANDISBURSEMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
