# DB2ADMIN.LOGFINMOTORPREMIUMCHARTDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 54
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 222797

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINMOTORPREMIUMCHARTCMYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINMOTORPREMIUMCHARTVEHICLETE` | INTEGER | NOT NULL |  |  |  |
| 2 | `FINMOTORPREMIUMCHARTFROMDATE` | DATE | NOT NULL |  |  |  |
| 3 | `AGEOFVEHICLE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 4 | `TWSLAB1` | DECIMAL(18,5) |  |  |  |  |
| 5 | `TWSLAB2` | DECIMAL(18,5) |  |  |  |  |
| 6 | `TWSLAB3` | DECIMAL(18,5) |  |  |  |  |
| 7 | `TWSLAB4` | DECIMAL(18,5) |  |  |  |  |
| 8 | `TW1TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 9 | `TW2TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 10 | `TW3TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 11 | `TW4TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 12 | `TW1TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 13 | `TW2TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 14 | `TW3TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 15 | `TW4TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 16 | `PCSLAB1` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 17 | `PCSLAB2` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 18 | `PCSLAB3` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 19 | `PC1TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 20 | `PC2TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 21 | `PC3TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 22 | `PC1TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 23 | `PC2TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 24 | `PC3TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 25 | `PVSLAB1` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 26 | `PVSLAB1AP` | DECIMAL(18,5) |  |  |  |  |
| 27 | `PV1TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 28 | `PV1TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 29 | `PVSLAB2` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 30 | `PVSLAB2AP` | DECIMAL(18,5) |  |  |  |  |
| 31 | `PV2TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 32 | `PV2TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 33 | `PVSLAB3` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 34 | `PVSLAB3AP` | DECIMAL(18,5) |  |  |  |  |
| 35 | `PV3TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 36 | `PV3TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 37 | `PVSLAB4` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 38 | `PVSLAB4AP` | DECIMAL(18,5) |  |  |  |  |
| 39 | `PV4TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 40 | `PV4TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 41 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 42 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 43 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 44 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 45 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 46 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 47 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 48 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 49 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 50 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 51 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 52 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 53 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGFINMOTORPREMIUMCHART**.`ABSUNIQUEID` (high confidence — name = 'LOGFINMOTORPREMIUMCHART' + known child suffix 'DETAIL')
  - JOIN predicate: `LOGFINMOTORPREMIUMCHARTDETAIL.FATHERID = LOGFINMOTORPREMIUMCHART.ABSUNIQUEID`

## Starter query

```sql
SELECT t.FINMOTORPREMIUMCHARTCMYCODE,
       t.FINMOTORPREMIUMCHARTVEHICLETE,
       t.FINMOTORPREMIUMCHARTFROMDATE,
       t.AGEOFVEHICLE,
       t.TWSLAB1,
       t.TWSLAB2,
       t.TWSLAB3,
       t.TWSLAB4,
       t.TW1TPPREMIUMPERSONS,
       t.TW2TPPREMIUMPERSONS,
       t.TW3TPPREMIUMPERSONS,
       t.TW4TPPREMIUMPERSONS
FROM   DB2ADMIN.LOGFINMOTORPREMIUMCHARTDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
