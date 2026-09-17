# DB2ADMIN.LOGFINIMPORTFCPAYMENT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 62
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 203458

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(5) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 3 | `YEARCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `YEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 5 | `BANKGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `BANKGLCODE` | CHAR(20) |  |  |  |  |
| 7 | `STATUS` | CHAR(3) |  |  |  |  |
| 8 | `VENDORCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 9 | `VENDORCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 10 | `BANKREFNO` | CHAR(20) |  |  |  |  |
| 11 | `BANKREFDATE` | DATE |  |  |  |  |
| 12 | `VALUEDATE` | DATE |  |  |  |  |
| 13 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 14 | `FRGNCURRENCYAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 15 | `LCPURDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 16 | `NARRATION` | CHAR(50) |  |  |  |  |
| 17 | `REMARKS` | VARCHAR(200) |  |  |  |  |
| 18 | `DDTTNO` | CHAR(20) |  |  |  |  |
| 19 | `POSTINGDATE` | DATE |  |  |  |  |
| 20 | `COSTCENTERFINBVSPPCENTERCODE` | CHAR(10) |  |  |  |  |
| 21 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 22 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 23 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 24 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 25 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 26 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 27 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 28 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 29 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 30 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 31 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 32 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 33 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 34 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 35 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 36 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 37 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 38 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 39 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 40 | `MARGINGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 41 | `MARGINGLCODE` | CHAR(20) |  |  |  |  |
| 42 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 43 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 44 | `BANKCHARGESCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 45 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 46 | `LCPURLCNO` | CHAR(35) |  |  |  |  |
| 47 | `LCPURLCDATE` | DATE |  |  |  |  |
| 48 | `AVAILABLELCMARGINAMT` | DECIMAL(18,5) |  |  |  |  |
| 49 | `LCMARGINUTILIZEAMT` | DECIMAL(18,5) |  |  |  |  |
| 50 | `AMENDMARGINUTILIZEAMT` | DECIMAL(18,5) |  |  |  |  |
| 51 | `LOANAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 52 | `ADVANCEPURORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 53 | `ADVANCEPURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 54 | `ADVANCELINENO` | INTEGER | NOT NULL |  |  |  |
| 55 | `ADVANCEAMT` | DECIMAL(18,5) |  |  |  |  |
| 56 | `INVOICENO` | CHAR(25) |  |  |  |  |
| 57 | `INVOICEDATE` | DATE |  |  |  |  |
| 58 | `BILLOFENTRYNO` | CHAR(25) |  |  |  |  |
| 59 | `BILLOFENTRYDATE` | DATE |  |  |  |  |
| 60 | `UDNO` | CHAR(25) |  |  |  |  |
| 61 | `UDVALUE` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGFINIMPORTFC**.`ABSUNIQUEID` (medium confidence — name = 'LOGFINIMPORTFC' + recurring fragment 'PAYMENT' (seen in 12 tables))
  - JOIN predicate: `LOGFINIMPORTFCPAYMENT.FATHERID = LOGFINIMPORTFC.ABSUNIQUEID`

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.BUSINESSUNITCODE,
       t.YEARCOMPANYCODE,
       t.YEARCODE,
       t.BANKGLCOMPANYCODE,
       t.BANKGLCODE,
       t.STATUS,
       t.VENDORCUSTOMERSUPPLIERTYPE,
       t.VENDORCUSTOMERSUPPLIERCODE,
       t.BANKREFNO,
       t.BANKREFDATE
FROM   DB2ADMIN.LOGFINIMPORTFCPAYMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
