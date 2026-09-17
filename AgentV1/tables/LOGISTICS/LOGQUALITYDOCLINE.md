# DB2ADMIN.LOGQUALITYDOCLINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 68
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 212881

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `QUALITYDOCUMENTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `QUALITYDOCUMENTHEADERCODE` | CHAR(20) | NOT NULL |  |  |  |
| 2 | `QUALITYDOCHEADERSUBGROUPCODE` | CHAR(5) | NOT NULL |  |  |  |
| 3 | `QUALITYDOCUMENTHEADERNUMBERID` | INTEGER | NOT NULL |  |  |  |
| 4 | `QUALITYDOCUMENTITEMTYPEAFICODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `QUALITYDOCUMENTSUBCODE01` | CHAR(20) | NOT NULL |  |  |  |
| 6 | `QUALITYDOCUMENTSUBCODE02` | CHAR(10) | NOT NULL |  |  |  |
| 7 | `QUALITYDOCUMENTSUBCODE03` | CHAR(10) | NOT NULL |  |  |  |
| 8 | `QUALITYDOCUMENTSUBCODE04` | CHAR(10) | NOT NULL |  |  |  |
| 9 | `QUALITYDOCUMENTSUBCODE05` | CHAR(10) | NOT NULL |  |  |  |
| 10 | `QUALITYDOCUMENTSUBCODE06` | CHAR(10) | NOT NULL |  |  |  |
| 11 | `QUALITYDOCUMENTSUBCODE07` | CHAR(10) | NOT NULL |  |  |  |
| 12 | `QUALITYDOCUMENTSUBCODE08` | CHAR(10) | NOT NULL |  |  |  |
| 13 | `QUALITYDOCUMENTSUBCODE09` | CHAR(10) | NOT NULL |  |  |  |
| 14 | `QUALITYDOCUMENTSUBCODE10` | CHAR(10) | NOT NULL |  |  |  |
| 15 | `QUALITYDOCUMENTLOTCODE` | CHAR(35) | NOT NULL |  |  |  |
| 16 | `QUALITYDOCITEMELMSUBCODEKEY` | CHAR(20) | NOT NULL |  |  |  |
| 17 | `QUALITYDOCUMENTITEMELEMENTCODE` | CHAR(15) | NOT NULL |  |  |  |
| 18 | `QUALITYDOCDEMANDCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 19 | `QUALITYDOCUMENTDEMANDCODE` | CHAR(15) | NOT NULL |  |  |  |
| 20 | `QUALITYDOCPRODUCTIONORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 21 | `QUALITYDOCORDPARTNERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 22 | `QUALITYDOCORDPRNCSMSUPCODE` | CHAR(8) | NOT NULL |  |  |  |
| 23 | `QUALITYDOCUMENTHEADERLINE` | DECIMAL(15,0) | NOT NULL |  |  |  |
| 24 | `LINE` | INTEGER | NOT NULL |  |  |  |
| 25 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 26 | `TESTLINESTATUS` | INTEGER | NOT NULL |  |  |  |
| 27 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 28 | `CHARACTERISTICCODE` | CHAR(10) |  |  |  |  |
| 29 | `GROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 30 | `GROUPCODE` | CHAR(3) |  |  |  |  |
| 31 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 32 | `INTERNALSPECIFICATIONCODE` | CHAR(10) |  |  |  |  |
| 33 | `ISOSPECIFICATIONCODE` | CHAR(10) |  |  |  |  |
| 34 | `MANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 35 | `SUBCODEMIN` | CHAR(50) |  |  |  |  |
| 36 | `SUBCODEMAX` | CHAR(50) |  |  |  |  |
| 37 | `SUBCODEMEDIOMIN` | CHAR(50) |  |  |  |  |
| 38 | `SUBCODEMEDIOMAX` | CHAR(50) |  |  |  |  |
| 39 | `SUBCODESTANDARD` | CHAR(50) |  |  |  |  |
| 40 | `VALUEBOOLEAN` | SMALLINT | NOT NULL |  |  |  |
| 41 | `VALUESTRING` | CHAR(50) |  |  |  |  |
| 42 | `VALUEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 43 | `VALUEQUANTITY2` | DECIMAL(15,5) |  |  |  |  |
| 44 | `VALUEQUANTITY3` | DECIMAL(15,5) |  |  |  |  |
| 45 | `STATUS` | CHAR(2) |  |  |  |  |
| 46 | `VALUEGROUPCODE` | CHAR(20) |  |  |  |  |
| 47 | `REPETITIONNUMBER` | INTEGER | NOT NULL |  |  |  |
| 48 | `ANNOTATION` | VARCHAR(250) |  |  |  |  |
| 49 | `ADDITIONALLINE` | SMALLINT | NOT NULL |  |  |  |
| 50 | `QUALITYREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 51 | `QUALITYREASONCODE` | CHAR(3) |  |  |  |  |
| 52 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 53 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 54 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 55 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 56 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 57 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 58 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 59 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 60 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 61 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 62 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 63 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 64 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 65 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 66 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 67 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGQUALITYDOCLINE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.QUALITYDOCUMENTCOMPANYCODE,
       t.QUALITYDOCUMENTHEADERCODE,
       t.QUALITYDOCHEADERSUBGROUPCODE,
       t.QUALITYDOCUMENTHEADERNUMBERID,
       t.QUALITYDOCUMENTITEMTYPEAFICODE,
       t.QUALITYDOCUMENTSUBCODE01,
       t.QUALITYDOCUMENTSUBCODE02,
       t.QUALITYDOCUMENTSUBCODE03,
       t.QUALITYDOCUMENTSUBCODE04,
       t.QUALITYDOCUMENTSUBCODE05,
       t.QUALITYDOCUMENTSUBCODE06,
       t.QUALITYDOCUMENTSUBCODE07
FROM   DB2ADMIN.LOGQUALITYDOCLINE t
FETCH FIRST 100 ROWS ONLY;
```
