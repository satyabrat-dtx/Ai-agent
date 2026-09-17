# DB2ADMIN.LOGFINFORWARDCONTRACT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 87
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 203142

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DUEDATETO` | DATE |  |  |  |  |
| 2 | `FCNO` | CHAR(10) | NOT NULL |  |  |  |
| 3 | `BANKCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `BANKCODE` | CHAR(20) |  |  |  |  |
| 5 | `FCLETTERDATE` | DATE |  |  |  |  |
| 6 | `BANKREFERENCENO` | CHAR(30) |  |  |  |  |
| 7 | `SPOTRATE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `PREMIUM` | DECIMAL(18,5) |  |  |  |  |
| 9 | `MARGIN` | DECIMAL(18,5) |  |  |  |  |
| 10 | `FCRATE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 11 | `CANCELLATIONRATE` | DECIMAL(18,5) |  |  |  |  |
| 12 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 13 | `STATUS` | CHAR(1) |  |  |  |  |
| 14 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 15 | `FCVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 16 | `FCUTILISED` | DECIMAL(18,5) |  |  |  |  |
| 17 | `FCUNUTILISED` | DECIMAL(18,5) |  |  |  |  |
| 18 | `CANCELLEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 19 | `FCCANCELLEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 20 | `UNUTILISED` | DECIMAL(18,5) |  |  |  |  |
| 21 | `UTILISED` | DECIMAL(18,5) |  |  |  |  |
| 22 | `PURPOSE` | CHAR(3) |  |  |  |  |
| 23 | `DUEDATEFROM` | DATE |  |  |  |  |
| 24 | `REMARKS` | CHAR(50) |  |  |  |  |
| 25 | `ADVICEDATE` | DATE |  |  |  |  |
| 26 | `BANKCHARGESGLACCOUNTCODE` | CHAR(20) |  |  |  |  |
| 27 | `BANKCHARGESACTUAL` | DECIMAL(18,5) |  |  |  |  |
| 28 | `BANKCHARGESMANUAL` | DECIMAL(18,5) |  |  |  |  |
| 29 | `NARRATION` | CHAR(50) |  |  |  |  |
| 30 | `TENOR` | CHAR(1) |  |  |  |  |
| 31 | `COSTCENTERFINBVSPPCENTERCODE` | CHAR(10) |  |  |  |  |
| 32 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 33 | `CGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 34 | `CGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 35 | `CGSTGLCODE` | CHAR(20) |  |  |  |  |
| 36 | `SGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 37 | `SGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 38 | `SGSTGLCODE` | CHAR(20) |  |  |  |  |
| 39 | `POSTINGDATE` | DATE |  |  |  |  |
| 40 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 41 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 42 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 43 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 44 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 45 | `CANCELLATIONDATE` | DATE |  |  |  |  |
| 46 | `CANCELLPOSTINGDATE` | DATE |  |  |  |  |
| 47 | `GLACCOUNTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 48 | `GLACCOUNTCODE` | CHAR(20) |  |  |  |  |
| 49 | `LOSSORGAIN` | DECIMAL(18,5) |  |  |  |  |
| 50 | `EXPORTIMPORTINTERESTCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 51 | `EXPORTIMPORTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 52 | `EXPORTIMPORTGLCODE` | CHAR(20) |  |  |  |  |
| 53 | `BANKCHARGESGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 54 | `BANKCHARGESGLCODE` | CHAR(20) |  |  |  |  |
| 55 | `CANCELBANKCHARGESACTUAL` | DECIMAL(18,5) |  |  |  |  |
| 56 | `CANCELBANKCHARGESMANUAL` | DECIMAL(18,5) |  |  |  |  |
| 57 | `CANCELLATIONREASON1` | CHAR(50) |  |  |  |  |
| 58 | `CANCELLATIONREASON2` | CHAR(50) |  |  |  |  |
| 59 | `CANCELCCFINBVSPPCENTERCODE` | CHAR(10) |  |  |  |  |
| 60 | `CANCELCCCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 61 | `CANCELCGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 62 | `CANCELCGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 63 | `CANCELCGSTGLCODE` | CHAR(20) |  |  |  |  |
| 64 | `CANCELSGSTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 65 | `CANCELSGSTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 66 | `CANCELSGSTGLCODE` | CHAR(20) |  |  |  |  |
| 67 | `CANFINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 68 | `CANFINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 69 | `CANFINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 70 | `CANFINDOCSTATGRPCODE` | CHAR(6) |  |  |  |  |
| 71 | `CANFINDOCCODE` | CHAR(15) |  |  |  |  |
| 72 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 73 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 74 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 75 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 76 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 77 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 78 | `STEP` | CHAR(1) |  |  |  |  |
| 79 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 80 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 81 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 82 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 83 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 84 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 85 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 86 | `BCHARGESGLACCOUNTCOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINFORWARDCONTRACT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DUEDATETO,
       t.FCNO,
       t.BANKCOMPANYCODE,
       t.BANKCODE,
       t.FCLETTERDATE,
       t.BANKREFERENCENO,
       t.SPOTRATE,
       t.PREMIUM,
       t.MARGIN,
       t.FCRATE,
       t.CANCELLATIONRATE
FROM   DB2ADMIN.LOGFINFORWARDCONTRACT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
