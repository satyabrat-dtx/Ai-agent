# DB2ADMIN.LOGFINLOANINTERESTSUBSIDY

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 41
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 230108

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `LTEUGENGROUPTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `LTYPEUSERGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `LOANTYPECODE` | CHAR(10) | NOT NULL |  |  |  |
| 4 | `CODELOANNO` | CHAR(10) | NOT NULL |  |  |  |
| 5 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 6 | `DOCUMENTDATE` | DATE |  |  |  |  |
| 7 | `POSTINGDATE` | DATE |  |  |  |  |
| 8 | `INTERESTDATEA` | DATE |  |  |  |  |
| 9 | `INTERESTDATEM` | DATE |  |  |  |  |
| 10 | `CALCULATEDINTERESTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `SUBSIDYAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 12 | `SUBSIDYRECDAMT` | DECIMAL(18,5) |  |  |  |  |
| 13 | `BANKGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 14 | `BANKGLCODE` | CHAR(20) |  |  |  |  |
| 15 | `SLNO` | INTEGER | NOT NULL |  |  |  |
| 16 | `SUBSIDYGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 17 | `SUBSIDYGLCODE` | CHAR(20) |  |  |  |  |
| 18 | `BANKADVICENO` | CHAR(12) |  |  |  |  |
| 19 | `BANKADVICEDATE` | DATE |  |  |  |  |
| 20 | `COSTCENTERFINBVSPPCENTERCODE` | CHAR(10) |  |  |  |  |
| 21 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 22 | `REMARKS` | VARCHAR(500) |  |  |  |  |
| 23 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 24 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 25 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 26 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 27 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 28 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 29 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 30 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 31 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 32 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 33 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 34 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 35 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 36 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 37 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 38 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 39 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 40 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGFINLOANINTEREST**.`ABSUNIQUEID` (medium confidence — name = 'LOGFINLOANINTEREST' + recurring fragment 'SUBSIDY' (seen in 3 tables))
  - JOIN predicate: `LOGFINLOANINTERESTSUBSIDY.FATHERID = LOGFINLOANINTEREST.ABSUNIQUEID`

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.LTEUGENGROUPTYPECOMPANYCODE,
       t.LTYPEUSERGENERICGROUPTYPECODE,
       t.LOANTYPECODE,
       t.CODELOANNO,
       t.BUSINESSUNITCODE,
       t.DOCUMENTDATE,
       t.POSTINGDATE,
       t.INTERESTDATEA,
       t.INTERESTDATEM,
       t.CALCULATEDINTERESTAMOUNT,
       t.SUBSIDYAMOUNT
FROM   DB2ADMIN.LOGFINLOANINTERESTSUBSIDY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
