# DB2ADMIN.LOGPURCHASEINVOICE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 83
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 222252

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `STEP` | CHAR(1) |  |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `DFINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 4 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 5 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 6 | `DFINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 7 | `CODE` | CHAR(25) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 8 | `DFINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 9 | `INVOICEDATE` | DATE | NOT NULL |  |  |  |
| 10 | `INVOICEPARKINGDATE` | DATE | NOT NULL |  |  |  |
| 11 | `DFINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 12 | `INVOICECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 13 | `DFINDOCCODE` | CHAR(15) |  |  |  |  |
| 14 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 15 | `PURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 16 | `EXTOPCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 17 | `EXTOPCODE` | CHAR(15) |  |  |  |  |
| 18 | `EXTOPORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 19 | `TERMSOFPAYMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `TERMSOFPAYMENTCODE` | CHAR(3) |  |  |  |  |
| 21 | `FOBDELIVERYTERMSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 22 | `FOBDELIVERYTERMSCODE` | CHAR(3) |  |  |  |  |
| 23 | `PAYDUEDATE` | DATE |  |  |  |  |
| 24 | `BASICVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 25 | `INVOICEAMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 26 | `GROSSVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 27 | `TAXVALUE` | DECIMAL(18,5) |  |  |  |  |
| 28 | `BILLPASSEDAMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 29 | `ACTUALBILLPASSEDAMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 30 | `DEDUCTIONAMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 31 | `LCLCNO` | CHAR(35) |  |  |  |  |
| 32 | `LCLCDATE` | DATE |  |  |  |  |
| 33 | `LCPURLCNO` | CHAR(35) |  |  |  |  |
| 34 | `LCPURLCDATE` | DATE |  |  |  |  |
| 35 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 36 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 37 | `RG23ISCODE` | CHAR(15) |  |  |  |  |
| 38 | `RG23IISCODE` | CHAR(15) |  |  |  |  |
| 39 | `PAYMENTMADE` | INTEGER | NOT NULL |  |  |  |
| 40 | `USEDCOUNTER` | INTEGER | NOT NULL |  |  |  |
| 41 | `POSTINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 42 | `CFORMNO` | CHAR(20) |  |  |  |  |
| 43 | `OPTDSTDSTEUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 44 | `OPTDSTDSTYPECODE` | CHAR(10) |  |  |  |  |
| 45 | `OPTDSTDSCODE` | CHAR(6) |  |  |  |  |
| 46 | `OPTDSTDSITAXCODE` | CHAR(3) |  |  |  |  |
| 47 | `OPTDSEXEMPTIONFROMDATE` | DATE |  |  |  |  |
| 48 | `TDSPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 49 | `TDSAPPLICABLEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 50 | `TDSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 51 | `TDSEXEMPTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 52 | `TDSGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 53 | `TDSGLCODE` | CHAR(20) |  |  |  |  |
| 54 | `FLAG` | CHAR(15) |  |  |  |  |
| 55 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 56 | `DEBITNOTEFLAG` | CHAR(15) |  |  |  |  |
| 57 | `DEBITNOTEMESSAGE` | LONG VARCHAR |  |  |  |  |
| 58 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 59 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 60 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 61 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 62 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 63 | `OTHFINDOCCODE` | CHAR(15) |  |  |  |  |
| 64 | `OTHFINDOCCODE2` | CHAR(15) |  |  |  |  |
| 65 | `ADVTOTALAMT` | DECIMAL(15,5) |  |  |  |  |
| 66 | `ADVTOTALTDSAPPAMT` | DECIMAL(15,5) |  |  |  |  |
| 67 | `ADVTOTALTDSDETECTEDAMT` | DECIMAL(15,5) |  |  |  |  |
| 68 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 69 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 70 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 71 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 72 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 73 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 74 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 75 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 76 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 77 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 78 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 79 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 80 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 81 | `NOTDSAPPLICABLE` | SMALLINT | NOT NULL |  |  |  |
| 82 | `EXCEMPTIONAMOUNT` | DECIMAL(15,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGPURCHASEINVOICE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.STEP,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.DFINDOCBUSINESSUNITCODE,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.DFINDOCFINANCIALYEARCODE,
       t.CODE,
       t.DFINDOCTEMPLATECODE,
       t.INVOICEDATE,
       t.INVOICEPARKINGDATE,
       t.DFINDOCSTATISTICALGROUPCODE
FROM   DB2ADMIN.LOGPURCHASEINVOICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
