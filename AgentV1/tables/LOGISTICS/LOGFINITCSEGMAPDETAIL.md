# DB2ADMIN.LOGFINITCSEGMAPDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 51
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 225725

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINITCSEGMAPCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINITCSEGMAPNUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 2 | `DETAILNUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 3 | `DESTINATIONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 5 | `HEADERTEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `HEADERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 7 | `CUSTOMERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 8 | `CUSTOMERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 9 | `VENDORCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 10 | `VENDORCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 11 | `GLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 12 | `GLCODE` | CHAR(20) |  |  |  |  |
| 13 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 14 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 15 | `FIRSTUSERGROUPTYPE` | CHAR(3) |  |  |  |  |
| 16 | `FIRSTUGRPUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 17 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 18 | `SECONDUSERGROUPTYPE` | CHAR(3) |  |  |  |  |
| 19 | `SNDUGRPUGENGRPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 21 | `THIRDUSERGROUPTYPE` | CHAR(3) |  |  |  |  |
| 22 | `THIRDUGRPUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 24 | `FOURTHUSERGROUPTYPE` | CHAR(3) |  |  |  |  |
| 25 | `FRUGRPUGENGRPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 27 | `FIFTHUSERGROUPTYPE` | CHAR(3) |  |  |  |  |
| 28 | `FIFTHUGRPUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 29 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 30 | `SIXTHUSERGROUPTYPE` | CHAR(3) |  |  |  |  |
| 31 | `SIXTHUGRPUGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 32 | `SIXTHUSERGROUPCODE` | CHAR(10) |  |  |  |  |
| 33 | `SEVENTHUSERGROUPTYPE` | CHAR(3) |  |  |  |  |
| 34 | `SEUGRPUGENGRPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 35 | `SEVENTHUSERGROUPCODE` | CHAR(10) |  |  |  |  |
| 36 | `EMAILADDRESS` | CHAR(60) |  |  |  |  |
| 37 | `LETTERTEMPLATECODE` | CHAR(30) |  |  |  |  |
| 38 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 39 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 40 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 41 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 42 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 43 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 44 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 45 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 46 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 47 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 48 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 49 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 50 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGFINITCSEGMAP**.`ABSUNIQUEID` (high confidence — name = 'LOGFINITCSEGMAP' + known child suffix 'DETAIL')
  - JOIN predicate: `LOGFINITCSEGMAPDETAIL.FATHERID = LOGFINITCSEGMAP.ABSUNIQUEID`

## Starter query

```sql
SELECT t.FINITCSEGMAPCOMPANYCODE,
       t.FINITCSEGMAPNUMBERID,
       t.DETAILNUMBERID,
       t.DESTINATIONCOMPANYCODE,
       t.BUSINESSUNITCODE,
       t.HEADERTEMPLATECOMPANYCODE,
       t.HEADERTEMPLATECODE,
       t.CUSTOMERCUSTOMERSUPPLIERTYPE,
       t.CUSTOMERCUSTOMERSUPPLIERCODE,
       t.VENDORCUSTOMERSUPPLIERTYPE,
       t.VENDORCUSTOMERSUPPLIERCODE,
       t.GLCOMPANYCODE
FROM   DB2ADMIN.LOGFINITCSEGMAPDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
