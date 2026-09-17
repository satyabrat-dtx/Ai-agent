# DB2ADMIN.LOGFINLOANCAPITALSR

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 39
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 226653

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `LTEUGENGROUPTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `LTYPEUSERGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `LOANTYPECODE` | CHAR(10) | NOT NULL |  |  |  |
| 4 | `CODELOANNO` | CHAR(10) | NOT NULL |  |  |  |
| 5 | `SLNO` | INTEGER | NOT NULL |  |  |  |
| 6 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 7 | `DOCUMENTDATE` | DATE |  |  |  |  |
| 8 | `POSTINGDATE` | DATE |  |  |  |  |
| 9 | `DOCUMENTTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `BANKGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `BANKGLCODE` | CHAR(20) |  |  |  |  |
| 12 | `CAPSUBSIDYGLACCCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 13 | `CAPITALSUBSIDYGLACCOUNTCODE` | CHAR(20) |  |  |  |  |
| 14 | `BANKREFERENCENO` | CHAR(12) |  |  |  |  |
| 15 | `BANKADVISEDATE` | DATE |  |  |  |  |
| 16 | `SUBSIDYAMOUNTCALCULATED` | DECIMAL(18,5) |  |  |  |  |
| 17 | `SUBSIDYAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 18 | `COSTCENTERFINBVSPPCENTERCODE` | CHAR(10) |  |  |  |  |
| 19 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 20 | `REMARKS` | CHAR(50) |  |  |  |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 26 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 27 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 28 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 29 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 30 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 31 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 32 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 33 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 34 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 35 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 36 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 37 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 38 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINLOANCAPITALSR.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.LTEUGENGROUPTYPECOMPANYCODE,
       t.LTYPEUSERGENERICGROUPTYPECODE,
       t.LOANTYPECODE,
       t.CODELOANNO,
       t.SLNO,
       t.BUSINESSUNITCODE,
       t.DOCUMENTDATE,
       t.POSTINGDATE,
       t.DOCUMENTTYPECODE,
       t.BANKGLCOMPANYCODE,
       t.BANKGLCODE
FROM   DB2ADMIN.LOGFINLOANCAPITALSR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
