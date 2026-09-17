# DB2ADMIN.LOGEXPENSEINVOICE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 56
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 132694

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `STEP` | CHAR(1) |  |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 4 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 5 | `CODE` | CHAR(25) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `INVOICEDATE` | DATE | NOT NULL |  |  |  |
| 7 | `INVOICEPARKINGDATE` | DATE | NOT NULL |  |  |  |
| 8 | `INVOICECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 9 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 10 | `TERMSOFPAYMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `TERMSOFPAYMENTCODE` | CHAR(3) |  |  |  |  |
| 12 | `FOBDELIVERYTERMSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 13 | `FOBDELIVERYTERMSCODE` | CHAR(3) |  |  |  |  |
| 14 | `INVOICEAMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 15 | `PAYDUEDATE` | DATE |  |  |  |  |
| 16 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 17 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 18 | `RG23ISCODE` | CHAR(15) |  |  |  |  |
| 19 | `RG23IISCODE` | CHAR(15) |  |  |  |  |
| 20 | `PAYMENTMADE` | INTEGER | NOT NULL |  |  |  |
| 21 | `OPTDSTDSTEUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 22 | `OPTDSTDSTYPECODE` | CHAR(10) |  |  |  |  |
| 23 | `OPTDSTDSCODE` | CHAR(6) |  |  |  |  |
| 24 | `OPTDSTDSITAXCODE` | CHAR(3) |  |  |  |  |
| 25 | `TDSPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 26 | `TDSAPPLICABLEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 27 | `TDSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 28 | `TDSGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `TDSGLCODE` | CHAR(20) |  |  |  |  |
| 30 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 31 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 32 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 33 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 34 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 35 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 36 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 37 | `FLAG` | CHAR(15) |  |  |  |  |
| 38 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 39 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 40 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 41 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 42 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 43 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 44 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 45 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 46 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 47 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 48 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 49 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 50 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 51 | `OTHFINDOCCODE` | CHAR(15) |  |  |  |  |
| 52 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 53 | `OPTDSEXEMPTIONFROMDATE` | DATE |  |  |  |  |
| 54 | `TDSEXEMPTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 55 | `NOTDSAPPLICABLE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGEXPENSEINVOICE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.STEP,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.CODE,
       t.INVOICEDATE,
       t.INVOICEPARKINGDATE,
       t.INVOICECURRENCYCODE,
       t.EXCHANGERATE,
       t.TERMSOFPAYMENTCOMPANYCODE,
       t.TERMSOFPAYMENTCODE
FROM   DB2ADMIN.LOGEXPENSEINVOICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
