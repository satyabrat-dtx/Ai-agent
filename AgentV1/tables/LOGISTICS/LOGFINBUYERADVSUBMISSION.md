# DB2ADMIN.LOGFINBUYERADVSUBMISSION

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 39
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 202047

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ACODE` | CHAR(5) | NOT NULL |  |  |  |
| 2 | `CODE` | CHAR(10) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `SCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 4 | `SCODE` | CHAR(15) |  |  |  |  |
| 5 | `DOCNO` | CHAR(30) |  |  |  |  |
| 6 | `DOCDATE` | DATE |  |  |  |  |
| 7 | `BUYERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 8 | `BUYERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 9 | `CURRENCYSCODE` | CHAR(4) |  |  |  |  |
| 10 | `FIRCTYPE` | INTEGER | NOT NULL |  |  |  |
| 11 | `FIRCNO` | CHAR(20) |  |  |  |  |
| 12 | `FIRCDATE` | DATE |  |  |  |  |
| 13 | `FIRCAMT` | DECIMAL(18,5) |  |  |  |  |
| 14 | `INVMODE` | INTEGER | NOT NULL |  |  |  |
| 15 | `TOTALFGNVALUE` | DECIMAL(18,5) |  |  |  |  |
| 16 | `TOTALCCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 17 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 25 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 26 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 27 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 28 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 29 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 30 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 31 | `EXCHANGEFLUCTUATIONGLCMYCODE` | CHAR(3) |  |  |  |  |
| 32 | `EXCHANGEFLUCTUATIONGLCODE` | CHAR(20) |  |  |  |  |
| 33 | `POSTINGDATE` | DATE |  |  |  |  |
| 34 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 35 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 36 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 37 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 38 | `FINDOCCODE` | CHAR(15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINBUYERADVSUBMISSION.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ACODE,
       t.CODE,
       t.SCOUNTERCODE,
       t.SCODE,
       t.DOCNO,
       t.DOCDATE,
       t.BUYERCUSTOMERSUPPLIERTYPE,
       t.BUYERCUSTOMERSUPPLIERCODE,
       t.CURRENCYSCODE,
       t.FIRCTYPE,
       t.FIRCNO
FROM   DB2ADMIN.LOGFINBUYERADVSUBMISSION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
