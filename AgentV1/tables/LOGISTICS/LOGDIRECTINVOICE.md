# DB2ADMIN.LOGDIRECTINVOICE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 99
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 217340

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `BOOKINGFOR` | CHAR(1) | NOT NULL |  |  |  |
| 3 | `DOCUMENT` | CHAR(1) | NOT NULL |  |  |  |
| 4 | `TEMPLATECODE` | CHAR(8) |  |  |  |  |
| 5 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `COUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 7 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 8 | `DOCUMENTDATE` | DATE | NOT NULL |  |  |  |
| 9 | `DOTPARKINGDATE` | DATE | NOT NULL |  |  |  |
| 10 | `OPTDSTDSTEUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 11 | `OPTDSTDSTYPECODE` | CHAR(10) |  |  |  |  |
| 12 | `OPTDSTDSCODE` | CHAR(6) |  |  |  |  |
| 13 | `OPTDSTDSITAXCODE` | CHAR(3) |  |  |  |  |
| 14 | `OPTDSEXEMPTIONFROMDATE` | DATE |  |  |  |  |
| 15 | `TDSPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 16 | `TDSAPPLICABLEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 17 | `TDSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 18 | `TDSEXEMPTEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 19 | `TDSGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `TDSGLCODE` | CHAR(20) |  |  |  |  |
| 21 | `INVOICECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 22 | `INVOICENO` | CHAR(25) |  |  |  |  |
| 23 | `INVOICEDATE` | DATE |  |  |  |  |
| 24 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 25 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 26 | `PAYMENTTERMCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 27 | `PAYMENTTERMCODE` | CHAR(3) |  |  |  |  |
| 28 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 30 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 31 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 32 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 33 | `FACTORYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 34 | `FACTORYCODE` | CHAR(8) |  |  |  |  |
| 35 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 36 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 37 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 38 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 39 | `ROUNDOFFVALUE` | DECIMAL(18,5) |  |  |  |  |
| 40 | `NETTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 41 | `ROUNDOFFITAXCODE` | CHAR(3) |  |  |  |  |
| 42 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 43 | `POSTINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 44 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 45 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 46 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 47 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 48 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 49 | `REFERENCETEXT1` | CHAR(20) |  |  |  |  |
| 50 | `REFERENCETEXT2` | CHAR(20) |  |  |  |  |
| 51 | `REFERENCETEXT3` | CHAR(20) |  |  |  |  |
| 52 | `REFERENCETEXT4` | CHAR(20) |  |  |  |  |
| 53 | `REFERENCETEXT5` | CHAR(20) |  |  |  |  |
| 54 | `FIRSTGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 55 | `FIRSTUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 56 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 57 | `SECONDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 58 | `SNDUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 59 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 60 | `THIRDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 61 | `THIRDUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 62 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 63 | `FOURTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 64 | `FRUSGRPUSGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 65 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 66 | `FIFTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 67 | `FIFTHUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 68 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 69 | `SIXTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 70 | `SIXTHUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 71 | `SIXTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 72 | `SEVENTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 73 | `SEUSGRPUSGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 74 | `SEVENTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 75 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 76 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 77 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 78 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 79 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 80 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 81 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 82 | `OTHFINDOCCODE` | CHAR(15) |  |  |  |  |
| 83 | `TYPEFOREINVOICE` | CHAR(1) |  |  |  |  |
| 84 | `FLAG` | CHAR(15) |  |  |  |  |
| 85 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 86 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 87 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 88 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 89 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 90 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 91 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 92 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 93 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 94 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 95 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 96 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 97 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 98 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGDIRECTINVOICE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGDIRECTINVOICEDETAIL`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.BOOKINGFOR,
       t.DOCUMENT,
       t.TEMPLATECODE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.DOCUMENTDATE,
       t.DOTPARKINGDATE,
       t.OPTDSTDSTEUSGENGROUPTYPECODE,
       t.OPTDSTDSTYPECODE
FROM   DB2ADMIN.LOGDIRECTINVOICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
