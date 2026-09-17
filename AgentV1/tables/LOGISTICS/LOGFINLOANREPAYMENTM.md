# DB2ADMIN.LOGFINLOANREPAYMENTM

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 56
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 228374

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL |  |  |  |
| 2 | `FINANCIALYEARCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `FINANCIALYEARCODE` | DECIMAL(4,0) | NOT NULL |  |  |  |
| 4 | `DOCUMENTCODE` | CHAR(3) |  |  |  |  |
| 5 | `LTEUGENGROUPTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `LTYPEUSERGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `LOANTYPECODE` | CHAR(10) | NOT NULL |  |  |  |
| 8 | `CODELOANNO` | CHAR(10) | NOT NULL |  |  |  |
| 9 | `REPAYMENTDATE` | DATE | NOT NULL |  |  |  |
| 10 | `TERMLOANGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `TERMLOANGLCODE` | CHAR(20) |  |  |  |  |
| 12 | `BANKGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 13 | `BANKGLCODE` | CHAR(20) |  |  |  |  |
| 14 | `SLNO` | INTEGER | NOT NULL |  |  |  |
| 15 | `TRANSACTIONDATE` | DATE |  |  |  |  |
| 16 | `BANKREFNO` | CHAR(20) |  |  |  |  |
| 17 | `BANKREFDATE` | DATE |  |  |  |  |
| 18 | `INSTRUMENTTYPE` | CHAR(1) |  |  |  |  |
| 19 | `FAVOUROF` | CHAR(25) |  |  |  |  |
| 20 | `PAYABLEAT` | CHAR(25) |  |  |  |  |
| 21 | `INTERESTDATEA` | DATE |  |  |  |  |
| 22 | `INTERESTDATEM` | DATE |  |  |  |  |
| 23 | `INTERESTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 24 | `INTERESTGLCODE` | CHAR(20) |  |  |  |  |
| 25 | `INTERESTAMTA` | DECIMAL(18,5) |  |  |  |  |
| 26 | `INTERESTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 27 | `TOTALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 28 | `REPAYMENTTOTALAMT` | DECIMAL(18,5) |  |  |  |  |
| 29 | `CONVERSIONRATE` | INTEGER | NOT NULL |  |  |  |
| 30 | `CONVERTEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 31 | `BANKCHARGEGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 32 | `BANKCHARGEGLCODE` | CHAR(20) |  |  |  |  |
| 33 | `BANKCHARGES` | DECIMAL(20,0) |  |  |  |  |
| 34 | `COSTCENTERFINBVSPPCENTERCODE` | CHAR(10) |  |  |  |  |
| 35 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 36 | `POSTINGDATE` | DATE | NOT NULL |  |  |  |
| 37 | `ENDDATE` | DATE |  |  |  |  |
| 38 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 39 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 40 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 41 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 42 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 43 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 44 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 45 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 46 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 47 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 48 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 49 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 50 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 51 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 52 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 53 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 54 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 55 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINLOANREPAYMENTM.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.FINANCIALYEARCOMPANYCODE,
       t.FINANCIALYEARCODE,
       t.DOCUMENTCODE,
       t.LTEUGENGROUPTYPECOMPANYCODE,
       t.LTYPEUSERGENERICGROUPTYPECODE,
       t.LOANTYPECODE,
       t.CODELOANNO,
       t.REPAYMENTDATE,
       t.TERMLOANGLCOMPANYCODE,
       t.TERMLOANGLCODE
FROM   DB2ADMIN.LOGFINLOANREPAYMENTM t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
