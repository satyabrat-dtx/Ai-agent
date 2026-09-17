# DB2ADMIN.LOGFINPOLICYMASTER

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 63
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 223539

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL |  |  |  |
| 2 | `POLICYTEUGENGRPTECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `POLICYTEUGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `POLICYTYPECODE` | CHAR(10) | NOT NULL |  |  |  |
| 5 | `INCOMPANYCUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `INCOMPANYCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 7 | `POLICYNO` | CHAR(20) | NOT NULL |  |  |  |
| 8 | `POLICYDATE` | DATE | NOT NULL |  |  |  |
| 9 | `FINANCIALYEARCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 10 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 11 | `SUMASSURED` | DECIMAL(18,5) |  |  |  |  |
| 12 | `PREMIUMAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 13 | `PREMIUMDATE` | DATE |  |  |  |  |
| 14 | `LETTER` | CHAR(2) |  |  |  |  |
| 15 | `CHEQUENO` | CHAR(10) |  |  |  |  |
| 16 | `BANKNAME` | CHAR(20) |  |  |  |  |
| 17 | `SERVICETAX` | DECIMAL(18,5) |  |  |  |  |
| 18 | `CGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 19 | `CGSTGLCODE` | CHAR(20) |  |  |  |  |
| 20 | `SGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 21 | `SGSTGLCODE` | CHAR(20) |  |  |  |  |
| 22 | `CGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 23 | `SGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 24 | `DUEDATE` | DATE |  |  |  |  |
| 25 | `PREPAIDEXPENSE` | DECIMAL(18,5) |  |  |  |  |
| 26 | `PREMIUMPOLICY` | DECIMAL(18,5) |  |  |  |  |
| 27 | `DECLARATIONDATE` | DATE |  |  |  |  |
| 28 | `POLICYBY` | CHAR(1) |  |  |  |  |
| 29 | `REMARKS` | CHAR(50) |  |  |  |  |
| 30 | `WHAREHSOUEGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `WHAREHSOUEGROUPCODE` | CHAR(3) |  |  |  |  |
| 32 | `VERIFIED` | SMALLINT | NOT NULL |  |  |  |
| 33 | `PAYMENTDATE` | DATE | NOT NULL |  |  |  |
| 34 | `PROFITCENTERPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 35 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 36 | `INSURANCEEXPGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 37 | `INSURANCEEXPGLCODE` | CHAR(20) |  |  |  |  |
| 38 | `BANKGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 39 | `BANKGLCODE` | CHAR(20) |  |  |  |  |
| 40 | `DOCNUMBERBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 41 | `DOCNUMBERFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 42 | `DOCNUMBERDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 43 | `DOCNUMBERSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 44 | `DOCNUMBERCODE` | CHAR(15) |  |  |  |  |
| 45 | `POSTINGDATE` | DATE | NOT NULL |  |  |  |
| 46 | `NARRATION` | CHAR(100) |  |  |  |  |
| 47 | `POSTINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 48 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 49 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 50 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 51 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 52 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 53 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 54 | `FLAG` | CHAR(15) |  |  |  |  |
| 55 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 56 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 57 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 58 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 59 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 60 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 61 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 62 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINPOLICYMASTER.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.POLICYTEUGENGRPTECOMPANYCODE,
       t.POLICYTEUGENERICGROUPTYPECODE,
       t.POLICYTYPECODE,
       t.INCOMPANYCUSTOMERSUPPLIERTYPE,
       t.INCOMPANYCUSTOMERSUPPLIERCODE,
       t.POLICYNO,
       t.POLICYDATE,
       t.FINANCIALYEARCOMPANYCODE,
       t.FINANCIALYEARCODE,
       t.SUMASSURED
FROM   DB2ADMIN.LOGFINPOLICYMASTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
