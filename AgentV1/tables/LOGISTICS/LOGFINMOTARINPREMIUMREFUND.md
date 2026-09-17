# DB2ADMIN.LOGFINMOTARINPREMIUMREFUND

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 36
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 226486

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `VEHICLETYPE` | INTEGER | NOT NULL |  |  |  |
| 2 | `VEHICLENUMBER` | CHAR(10) | NOT NULL |  |  |  |
| 3 | `DATEOFPREMIUMCALCULATION` | DATE | NOT NULL |  |  |  |
| 4 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 5 | `BUSINESSUNITGROUPCODE` | CHAR(10) |  |  |  |  |
| 6 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 7 | `PROFITCENTERPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 8 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 9 | `FISCALYEARCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 10 | `FISCALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 11 | `EXCESSPREMIUMAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 12 | `INSURANCEEXPGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 13 | `INSURANCEEXPGLCODE` | CHAR(20) |  |  |  |  |
| 14 | `BANKGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 15 | `BANKGLCODE` | CHAR(20) |  |  |  |  |
| 16 | `POSTINGDATE` | DATE | NOT NULL |  |  |  |
| 17 | `REMARKS` | CHAR(100) |  |  |  |  |
| 18 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 19 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 20 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 21 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 22 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 23 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 24 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 25 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 26 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 27 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 28 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 30 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 31 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 32 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 33 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 34 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 35 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINMOTARINPREMIUMREFUND.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.VEHICLETYPE,
       t.VEHICLENUMBER,
       t.DATEOFPREMIUMCALCULATION,
       t.LINENO,
       t.BUSINESSUNITGROUPCODE,
       t.BUSINESSUNITCODE,
       t.PROFITCENTERPROFITCENTERCODE,
       t.COSTCENTERCOSTCENTERCODE,
       t.FISCALYEARCOMPANYCODE,
       t.FISCALYEARCODE,
       t.EXCESSPREMIUMAMOUNT
FROM   DB2ADMIN.LOGFINMOTARINPREMIUMREFUND t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
