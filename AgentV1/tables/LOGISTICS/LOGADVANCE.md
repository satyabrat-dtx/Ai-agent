# DB2ADMIN.LOGADVANCE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 50
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 220047

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `PURCHASEORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `ADUSGENGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `ADUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `ADCODE` | CHAR(10) |  |  |  |  |
| 6 | `DUEDATE` | DATE |  |  |  |  |
| 7 | `POADVANCEDATE` | DATE | NOT NULL |  |  |  |
| 8 | `INVOICEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 9 | `PAYMENTADVPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 10 | `PAYMENTADVAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `CASHDISCOUNTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 12 | `NETAMTAFTERDEDUCTION` | DECIMAL(18,5) |  |  |  |  |
| 13 | `UPDATEAMTFLAG` | INTEGER | NOT NULL |  |  |  |
| 14 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 15 | `PAYMENTBY` | INTEGER | NOT NULL |  |  |  |
| 16 | `PERCENTAGE` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 17 | `CALCULATEDVALUER` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 18 | `PAYEMENTMADE` | INTEGER | NOT NULL |  |  |  |
| 19 | `POLINE` | CHAR(15) |  |  |  |  |
| 20 | `LCPURDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 21 | `LCPURLCNO` | CHAR(35) |  |  |  |  |
| 22 | `LCPURLCDATE` | DATE |  |  |  |  |
| 23 | `REMARKS` | CHAR(140) |  |  |  |  |
| 24 | `REMARK1` | VARCHAR(200) |  |  |  |  |
| 25 | `REMARK2` | DECIMAL(10,0) |  |  |  |  |
| 26 | `STATUS` | CHAR(1) |  |  |  |  |
| 27 | `WFMORDERSTATUS` | INTEGER | NOT NULL |  |  |  |
| 28 | `UNDERPROPOSAL` | SMALLINT | NOT NULL |  |  |  |
| 29 | `FLAG` | CHAR(15) |  |  |  |  |
| 30 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 31 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 32 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 33 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 34 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 35 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 36 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 37 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 38 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 39 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 40 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 41 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 42 | `OTHFINDOCCODE` | CHAR(15) |  |  |  |  |
| 43 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 44 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 45 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 46 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 47 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 48 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 49 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGADVANCE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGADVANCEDETAIL`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.ADUSGENGROUPTYPECOMPANYCODE,
       t.ADUSERGENERICGROUPTYPECODE,
       t.ADCODE,
       t.DUEDATE,
       t.POADVANCEDATE,
       t.INVOICEAMOUNT,
       t.PAYMENTADVPERCENTAGE,
       t.PAYMENTADVAMOUNT,
       t.CASHDISCOUNTAMOUNT
FROM   DB2ADMIN.LOGADVANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
