# DB2ADMIN.LOGFINPACKINGCREDIT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 61
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 203630

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 2 | `LETTERNO` | CHAR(5) | NOT NULL |  |  |  |
| 3 | `BANKCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `BANKCODE` | CHAR(20) |  |  |  |  |
| 5 | `PACKINGDATE` | DATE |  |  |  |  |
| 6 | `ADJFORTHISBILL` | DECIMAL(18,5) |  |  |  |  |
| 7 | `LOANREQUISITIONAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `LOANINTERESTRATE` | DECIMAL(6,3) | NOT NULL |  |  |  |
| 9 | `SUBVENSION` | DECIMAL(6,3) |  |  |  |  |
| 10 | `NETINTERESTRATE` | DECIMAL(6,3) |  |  |  |  |
| 11 | `FOREGINCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 12 | `FCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 14 | `PCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 15 | `SHIPMENTDETAILS` | CHAR(50) |  |  |  |  |
| 16 | `INTERESTCHARGED` | CHAR(1) |  |  |  |  |
| 17 | `STATUS` | CHAR(10) |  |  |  |  |
| 18 | `BANKREFNO` | CHAR(30) |  |  |  |  |
| 19 | `BANKADVICEDATE` | DATE |  |  |  |  |
| 20 | `TENORPERIOD` | INTEGER | NOT NULL |  |  |  |
| 21 | `LOANSANCTIONEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 22 | `PCGLACCOUNTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `PCGLACCOUNTCODE` | CHAR(20) |  |  |  |  |
| 24 | `DUEDATE` | DATE |  |  |  |  |
| 25 | `BANKCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 26 | `BANKCHARGESGLACCOUNTCODE` | CHAR(20) |  |  |  |  |
| 27 | `ACTUALCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 28 | `PROFITCENTERPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 29 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 30 | `ANTUGENGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `ANTUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 32 | `ANTCODE` | CHAR(10) |  |  |  |  |
| 33 | `UNUTILIZEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 34 | `FCUNUTILIZEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 35 | `POSTINGDATE` | DATE |  |  |  |  |
| 36 | `CGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 37 | `CGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 38 | `CGSTGLCODE` | CHAR(20) |  |  |  |  |
| 39 | `SGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 40 | `SGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 41 | `SGSTGLCODE` | CHAR(20) |  |  |  |  |
| 42 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 43 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 44 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 45 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 46 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 47 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 48 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 49 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 50 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 51 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 52 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 53 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 54 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 55 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 56 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 57 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 58 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 59 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 60 | `BCHARGESGLACCOUNTCOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINPACKINGCREDIT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.LETTERNO,
       t.BANKCOMPANYCODE,
       t.BANKCODE,
       t.PACKINGDATE,
       t.ADJFORTHISBILL,
       t.LOANREQUISITIONAMOUNT,
       t.LOANINTERESTRATE,
       t.SUBVENSION,
       t.NETINTERESTRATE,
       t.FOREGINCURRENCYCODE
FROM   DB2ADMIN.LOGFINPACKINGCREDIT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
