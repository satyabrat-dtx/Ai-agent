# DB2ADMIN.LOGFINMOTORVEHICLEPREMIEUMCL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 40
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 227359

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `VEHICLETYPE` | INTEGER | NOT NULL |  |  |  |
| 2 | `VEHICLENUMBER` | CHAR(10) | NOT NULL |  |  |  |
| 3 | `DATEOFPREMIUMCALCULATION` | DATE | NOT NULL |  |  |  |
| 4 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 5 | `BUGROUPCODE` | CHAR(10) |  |  |  |  |
| 6 | `CLAIMAPPLIED` | DECIMAL(18,5) |  |  |  |  |
| 7 | `CLAIMRECEIVED` | DECIMAL(18,5) |  |  |  |  |
| 8 | `NCBPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 9 | `RECEIVEDDATE` | DATE |  |  |  |  |
| 10 | `REMARKS` | VARCHAR(500) |  |  |  |  |
| 11 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 12 | `PROFITCENTERPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 13 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 14 | `CLAIMAPPLIEDGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 15 | `CLAIMAPPLIEDGLCODE` | CHAR(20) |  |  |  |  |
| 16 | `CLAIMRECIEVEDGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 17 | `CLAIMRECIEVEDGLCODE` | CHAR(20) |  |  |  |  |
| 18 | `POSTINGDATE` | DATE | NOT NULL |  |  |  |
| 19 | `POSTINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 20 | `FLAG` | CHAR(15) |  |  |  |  |
| 21 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 27 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 28 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 29 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 30 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 31 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 32 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 33 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 34 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 35 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 36 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 37 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 38 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 39 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINMOTORVEHICLEPREMIEUMCL.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.VEHICLETYPE,
       t.VEHICLENUMBER,
       t.DATEOFPREMIUMCALCULATION,
       t.LINENO,
       t.BUGROUPCODE,
       t.CLAIMAPPLIED,
       t.CLAIMRECEIVED,
       t.NCBPERCENTAGE,
       t.RECEIVEDDATE,
       t.REMARKS,
       t.BUSINESSUNITCODE
FROM   DB2ADMIN.LOGFINMOTORVEHICLEPREMIEUMCL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
