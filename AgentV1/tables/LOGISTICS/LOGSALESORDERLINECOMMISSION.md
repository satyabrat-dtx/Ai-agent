# DB2ADMIN.LOGSALESORDERLINECOMMISSION

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 34
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 55666

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALORDLINESALORDERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `SALORDLINESALORDERCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `SALESORDERLINESALESORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `SALESORDERLINEORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `SALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 5 | `SALORDLINECOMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 6 | `AGENTCODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `NUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 8 | `SEQUENCE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 9 | `COMMISSIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `COMMISSIONVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 11 | `COMMISSIONCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 12 | `COMMISSIONSIGN` | CHAR(2) | NOT NULL |  |  |  |
| 13 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 14 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 15 | `COMMISSIONCREATIONTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 16 | `DEFSALCMSDEFINITIONNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 17 | `DEFINITIONNUMBERLINEID` | DECIMAL(3,0) |  |  |  |  |
| 18 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 19 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 20 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 26 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 27 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 28 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 30 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 31 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 32 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 33 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGSALESORDERLINE**.`ABSUNIQUEID` (medium confidence — name = 'LOGSALESORDERLINE' + recurring fragment 'COMMISSION' (seen in 11 tables))
  - JOIN predicate: `LOGSALESORDERLINECOMMISSION.FATHERID = LOGSALESORDERLINE.ABSUNIQUEID`

## Starter query

```sql
SELECT t.SALORDLINESALORDERCOMPANYCODE,
       t.SALORDLINESALORDERCOUNTERCODE,
       t.SALESORDERLINESALESORDERCODE,
       t.SALESORDERLINEORDERLINE,
       t.SALESORDERLINEORDERSUBLINE,
       t.SALORDLINECOMPONENTORDERLINE,
       t.AGENTCODE,
       t.NUMBERID,
       t.SEQUENCE,
       t.COMMISSIONTYPE,
       t.COMMISSIONVALUE,
       t.COMMISSIONCURRENCYCODE
FROM   DB2ADMIN.LOGSALESORDERLINECOMMISSION t
FETCH FIRST 100 ROWS ONLY;
```
