# DB2ADMIN.LOGFINPREMIUMCALCULATION

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 69
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 228284

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEETYPE` | CHAR(5) | NOT NULL |  |  |  |
| 2 | `RISKTYPE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `ENTRYDATE` | DATE | NOT NULL |  |  |  |
| 4 | `BUGROUPCODE` | CHAR(10) |  |  |  |  |
| 5 | `INSURANCETYPE` | CHAR(10) |  |  |  |  |
| 6 | `DUEDATE` | DATE |  |  |  |  |
| 7 | `FINANCIALYEARCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 9 | `WORKERTYPE` | CHAR(5) |  |  |  |  |
| 10 | `PREMIUMPOLICY` | DECIMAL(18,5) |  |  |  |  |
| 11 | `INCOMPANYCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 12 | `INCOMPANYCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 13 | `PREPAIDEXPENSE` | DECIMAL(18,5) |  |  |  |  |
| 14 | `SUMASSUREDIII` | DECIMAL(18,5) |  |  |  |  |
| 15 | `SUMASSUREDIV` | DECIMAL(18,5) |  |  |  |  |
| 16 | `TABLE2RATE` | DECIMAL(18,5) |  |  |  |  |
| 17 | `TOTALOFTABLE2` | DECIMAL(18,5) |  |  |  |  |
| 18 | `DSCUGENGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 19 | `DSCUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 20 | `DISCOUNTCODE` | CHAR(10) |  |  |  |  |
| 21 | `TOTALOFTABLE2AFTERDISCOUNT` | DECIMAL(18,5) |  |  |  |  |
| 22 | `TABLE3RATE` | DECIMAL(18,5) |  |  |  |  |
| 23 | `TOTALOFTABLE3` | DECIMAL(18,5) |  |  |  |  |
| 24 | `TABLE4RATE` | DECIMAL(18,5) |  |  |  |  |
| 25 | `TOTALOFTABLE4` | DECIMAL(18,5) |  |  |  |  |
| 26 | `TOTALOFTABLE234` | DECIMAL(18,5) |  |  |  |  |
| 27 | `DISCOUNT50` | DECIMAL(18,5) |  |  |  |  |
| 28 | `ADDITIONALDISCOUNT` | DECIMAL(18,5) |  |  |  |  |
| 29 | `ADDITIONALDISCOUNTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 30 | `TOTALDISCOUNT` | DECIMAL(18,5) |  |  |  |  |
| 31 | `ADDITIONALPREMIUM` | DECIMAL(18,5) |  |  |  |  |
| 32 | `TOTALPREMIUM` | DECIMAL(18,5) |  |  |  |  |
| 33 | `GSTRATE` | DECIMAL(18,5) |  |  |  |  |
| 34 | `GSTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 35 | `CGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 36 | `SGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 37 | `TOTALPREMIUMAFTERTAX` | DECIMAL(18,5) |  |  |  |  |
| 38 | `PROFITCENTERPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 39 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 40 | `INSURENCEACCGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 41 | `INSURENCEACCGLCODE` | CHAR(20) |  |  |  |  |
| 42 | `CGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 43 | `CGSTGLCODE` | CHAR(20) |  |  |  |  |
| 44 | `SGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 45 | `SGSTGLCODE` | CHAR(20) |  |  |  |  |
| 46 | `POSTINGDATE` | DATE | NOT NULL |  |  |  |
| 47 | `POSTINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 48 | `REMARKS` | VARCHAR(255) |  |  |  |  |
| 49 | `FLAG` | CHAR(15) |  |  |  |  |
| 50 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 51 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 52 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 53 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 54 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 55 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 56 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 57 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 58 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 59 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 60 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 61 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 62 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 63 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 64 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 65 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 66 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 67 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 68 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINPREMIUMCALCULATION.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGFINPREMIUMCALCULATIONCLAIM`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEETYPE,
       t.RISKTYPE,
       t.ENTRYDATE,
       t.BUGROUPCODE,
       t.INSURANCETYPE,
       t.DUEDATE,
       t.FINANCIALYEARCOMPANYCODE,
       t.FINANCIALYEARCODE,
       t.WORKERTYPE,
       t.PREMIUMPOLICY,
       t.INCOMPANYCUSTOMERSUPPLIERTYPE
FROM   DB2ADMIN.LOGFINPREMIUMCALCULATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
