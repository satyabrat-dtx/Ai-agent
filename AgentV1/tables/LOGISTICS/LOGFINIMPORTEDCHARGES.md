# DB2ADMIN.LOGFINIMPORTEDCHARGES

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 37
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 203289

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `FORWARDCONTRACTCODE` | CHAR(5) |  |  |  |  |
| 3 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 4 | `BANKGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `BANKGLCODE` | CHAR(20) |  |  |  |  |
| 6 | `BANKREFERENCENO` | CHAR(20) |  |  |  |  |
| 7 | `ADVICEDATE` | DATE |  |  |  |  |
| 8 | `RATE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 9 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 10 | `DUEDATEFROM` | DATE |  |  |  |  |
| 11 | `DUEDATETO` | DATE |  |  |  |  |
| 12 | `POSTINGDATE` | DATE |  |  |  |  |
| 13 | `EXPORTIMPORTGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 14 | `EXPORTIMPORTGLCODE` | CHAR(20) |  |  |  |  |
| 15 | `PROFITCENTERPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 16 | `COSTCENTERCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 17 | `BANKCHARGESGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 18 | `BANKCHARGESGLCODE` | CHAR(20) |  |  |  |  |
| 19 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 20 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 21 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 22 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 23 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 24 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 25 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 26 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 27 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 28 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 29 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 30 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 31 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 32 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 33 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 34 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 35 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 36 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINIMPORTEDCHARGES.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.FORWARDCONTRACTCODE,
       t.BUSINESSUNITCODE,
       t.BANKGLCOMPANYCODE,
       t.BANKGLCODE,
       t.BANKREFERENCENO,
       t.ADVICEDATE,
       t.RATE,
       t.VALUE,
       t.DUEDATEFROM,
       t.DUEDATETO
FROM   DB2ADMIN.LOGFINIMPORTEDCHARGES t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
