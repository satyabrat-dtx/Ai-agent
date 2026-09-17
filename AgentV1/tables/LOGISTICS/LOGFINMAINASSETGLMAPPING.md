# DB2ADMIN.LOGFINMAINASSETGLMAPPING

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 42
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 228119

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL |  |  |  |
| 2 | `MAINASSETASSETUGENGRPTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `MAINASSETASSETCODE` | CHAR(10) | NOT NULL |  |  |  |
| 4 | `MAINASSETCODE` | CHAR(15) | NOT NULL |  |  |  |
| 5 | `ASSETCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `ASSETCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 7 | `CAPITALGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `CAPITALGLCODE` | CHAR(20) |  |  |  |  |
| 9 | `ACCUMDEPRGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 10 | `ACCUMDEPRGLCODE` | CHAR(20) |  |  |  |  |
| 11 | `CURRYEARDEPGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 12 | `CURRYEARDEPGLCODE` | CHAR(20) |  |  |  |  |
| 13 | `DEPRATECOMCOMPANYITACT` | CHAR(1) |  |  |  |  |
| 14 | `DEPRATECOMDEPRRATECODE` | CHAR(5) |  |  |  |  |
| 15 | `DEPRATECOMRATE` | DECIMAL(5,2) |  |  |  |  |
| 16 | `DEPRATECOMNOOFMONTH` | DECIMAL(20,0) |  |  |  |  |
| 17 | `DEPRATECOMADDITIONDEPRESIONJOB` | DECIMAL(5,2) |  |  |  |  |
| 18 | `DEPRATECOMDEPRMETHOD` | CHAR(1) |  |  |  |  |
| 19 | `DEPRATECOMEFFECTIVEDATEFROM` | DATE |  |  |  |  |
| 20 | `DEPRATEITCOMPANYITACT` | CHAR(1) |  |  |  |  |
| 21 | `DEPRATEITDEPRRATECODE` | CHAR(5) |  |  |  |  |
| 22 | `DEPRATEITRATE` | DECIMAL(5,2) |  |  |  |  |
| 23 | `DEPRATEITNOOFMONTH` | DECIMAL(20,0) |  |  |  |  |
| 24 | `DEPRATEITADDITIONDEPRESIONJOB` | DECIMAL(5,2) |  |  |  |  |
| 25 | `DEPRATEITDEPRMETHOD` | CHAR(1) |  |  |  |  |
| 26 | `DEPRATEITEFFECTIVEDATEFROM` | DATE |  |  |  |  |
| 27 | `MAINASSETGLFROMDATE` | DATE | NOT NULL |  |  |  |
| 28 | `MAINASSETGLTODATE` | DATE |  |  |  |  |
| 29 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 30 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 31 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 32 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 33 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 34 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 35 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 36 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 37 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 38 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 39 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 40 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 41 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGFINMAINASSET**.`ABSUNIQUEID` (medium confidence — name = 'LOGFINMAINASSET' + recurring fragment 'GLMAPPING' (seen in 7 tables))
  - JOIN predicate: `LOGFINMAINASSETGLMAPPING.FATHERID = LOGFINMAINASSET.ABSUNIQUEID`

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.MAINASSETASSETUGENGRPTYPECODE,
       t.MAINASSETASSETCODE,
       t.MAINASSETCODE,
       t.ASSETCOUNTERCOMPANYCODE,
       t.ASSETCOUNTERCODE,
       t.CAPITALGLCOMPANYCODE,
       t.CAPITALGLCODE,
       t.ACCUMDEPRGLCOMPANYCODE,
       t.ACCUMDEPRGLCODE,
       t.CURRYEARDEPGLCOMPANYCODE
FROM   DB2ADMIN.LOGFINMAINASSETGLMAPPING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
