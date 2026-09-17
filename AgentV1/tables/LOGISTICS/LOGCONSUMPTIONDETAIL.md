# DB2ADMIN.LOGCONSUMPTIONDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 50
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 220983

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CONSUMPTIONHEADERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `CONSUMPTIONHEADERDIVISIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `CONSUMPTIONHEADERITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `CONSUMPTIONHDRBUSINESSAREACOD` | CHAR(50) | NOT NULL |  |  |  |
| 4 | `CONSUMPTIONHEADERSTARTDATE` | DATE | NOT NULL |  |  |  |
| 5 | `CONSUMPTIONHEADERENDDATE` | DATE | NOT NULL |  |  |  |
| 6 | `CONSUMPTIONHDRLGLWHSCODE` | CHAR(8) | NOT NULL |  |  |  |
| 7 | `COSTCENTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 8 | `COSTCENTERCODE` | CHAR(20) | NOT NULL |  |  |  |
| 9 | `DEBITGLCODE` | CHAR(20) | NOT NULL |  |  |  |
| 10 | `CREDITGLCODE` | CHAR(20) | NOT NULL |  |  |  |
| 11 | `CLOSINGBASECOST` | DECIMAL(18,5) |  |  |  |  |
| 12 | `BASECOSTUNITCODE` | CHAR(3) | NOT NULL |  |  |  |
| 13 | `PROJECTCODE` | CHAR(20) | NOT NULL |  |  |  |
| 14 | `COMPONENTLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 15 | `QUANTITY` | DECIMAL(18,5) |  |  |  |  |
| 16 | `FIRSTUSGRPUSGENGRPTECMYCODE` | CHAR(3) |  |  |  |  |
| 17 | `FIRSTUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 18 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 19 | `SNDUSGRPUSGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `SNDUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 21 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 22 | `THIRDUSGRPUSGENGRPTECMYCODE` | CHAR(3) |  |  |  |  |
| 23 | `THIRDUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 24 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 25 | `FRUSGRPUSGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `FRUSGRPUSGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 27 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 28 | `FIFTHUSGRPUSGENGRPTECMYCODE` | CHAR(3) |  |  |  |  |
| 29 | `FIFTHUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 30 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 31 | `SIXTHUSGRPUSGENGRPTECMYCODE` | CHAR(3) |  |  |  |  |
| 32 | `SIXTHUSGRPUSGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 33 | `SIXTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 34 | `SEUSGRPUSGENGRPTECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 35 | `SEUSGRPUSGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 36 | `SEVENTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 37 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 38 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 39 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 40 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 41 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 42 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 43 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 44 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 45 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 46 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 47 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 48 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 49 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGCONSUMPTIONDETAIL.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.CONSUMPTIONHEADERCOMPANYCODE,
       t.CONSUMPTIONHEADERDIVISIONCODE,
       t.CONSUMPTIONHEADERITEMTYPECODE,
       t.CONSUMPTIONHDRBUSINESSAREACOD,
       t.CONSUMPTIONHEADERSTARTDATE,
       t.CONSUMPTIONHEADERENDDATE,
       t.CONSUMPTIONHDRLGLWHSCODE,
       t.COSTCENTERCOMPANYCODE,
       t.COSTCENTERCODE,
       t.DEBITGLCODE,
       t.CREDITGLCODE,
       t.CLOSINGBASECOST
FROM   DB2ADMIN.LOGCONSUMPTIONDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
