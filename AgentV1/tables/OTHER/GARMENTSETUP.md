# DB2ADMIN.GARMENTSETUP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 41
- **Primary key**: `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 105389

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `MARKERHANDLE` | SMALLINT | NOT NULL |  |  |  |
| 3 | `LAYDOWNHANDLE` | SMALLINT | NOT NULL |  |  |  |
| 4 | `CUTTINGHANDLE` | SMALLINT | NOT NULL |  |  |  |
| 5 | `MARKERSPECDATATYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `MARKERDATAMAND` | SMALLINT | NOT NULL |  |  |  |
| 7 | `FABRICITS` | CHAR(90) |  |  |  |  |
| 8 | `RECRESBYLAWDOWN` | SMALLINT | NOT NULL |  |  |  |
| 9 | `ALLOCBYWIDTH` | SMALLINT | NOT NULL |  |  |  |
| 10 | `WIDTHFORFILTERTYPE` | INTEGER | NOT NULL |  |  |  |
| 11 | `USEMEASUREMENTFIRST` | SMALLINT | NOT NULL |  |  |  |
| 12 | `MARKEROVERRIDEQTY` | SMALLINT | NOT NULL |  |  |  |
| 13 | `MAXLAYLENGTH` | DECIMAL(8,3) |  |  |  |  |
| 14 | `MAXNOLAYERS` | INTEGER | NOT NULL |  |  |  |
| 15 | `WIDTHRANGEFROM` | DECIMAL(5,2) |  |  |  |  |
| 16 | `WIDTHRANGETO` | DECIMAL(5,2) |  |  |  |  |
| 17 | `GSMRANGEFROM` | DECIMAL(5,2) |  |  |  |  |
| 18 | `GSMRANGETO` | DECIMAL(5,2) |  |  |  |  |
| 19 | `SHRINKAGE` | DECIMAL(5,2) |  |  |  |  |
| 20 | `LAYDOWNDOCCOUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 21 | `LAYDOWNDOCCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 22 | `LAYDOWNPROGCOUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 23 | `LAYDOWNPROGCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 24 | `LAYDOWNDISTPROGPLYCODE` | CHAR(20) |  |  |  |  |
| 25 | `LAYDOWNDISTISSUEQTYPLYCODE` | CHAR(20) |  |  |  |  |
| 26 | `BUNDLEHANDLE` | SMALLINT | NOT NULL |  |  |  |
| 27 | `CHILDBUNDLEHANDLE` | SMALLINT | NOT NULL |  |  |  |
| 28 | `CUTTINGDOCCOUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 29 | `CUTTINGDOCCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 30 | `CUTTINGPROGCOUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 31 | `CUTTINGPROGCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 32 | `CUTTINGDISTPROGPLYCODE` | CHAR(20) |  |  |  |  |
| 33 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 34 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 35 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 36 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 37 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 38 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 39 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 40 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `GARMENTSETUP.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `COUNTER_CUTTINGDOCCOUNTER` | `CUTTINGDOCCOUNTERCOMPANYCODE`, `CUTTINGDOCCOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `GARMENTSETUP.CUTTINGDOCCOUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND GARMENTSETUP.CUTTINGDOCCOUNTERCODE = COUNTER.CODE` |
| `COUNTER_CUTTINGPROGCOUNTER` | `CUTTINGPROGCOUNTERCOMPANYCODE`, `CUTTINGPROGCOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `GARMENTSETUP.CUTTINGPROGCOUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND GARMENTSETUP.CUTTINGPROGCOUNTERCODE = COUNTER.CODE` |
| `COUNTER_LAYDOWNDOCCOUNTER` | `LAYDOWNDOCCOUNTERCOMPANYCODE`, `LAYDOWNDOCCOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `GARMENTSETUP.LAYDOWNDOCCOUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND GARMENTSETUP.LAYDOWNDOCCOUNTERCODE = COUNTER.CODE` |
| `COUNTER_LAYDOWNPROGCOUNTER` | `LAYDOWNPROGCOUNTERCOMPANYCODE`, `LAYDOWNPROGCOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `GARMENTSETUP.LAYDOWNPROGCOUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND GARMENTSETUP.LAYDOWNPROGCOUNTERCODE = COUNTER.CODE` |
| `ITEMTYPE_GARMENT` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `GARMENTSETUP.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND GARMENTSETUP.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `GARMENTSETUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.MARKERHANDLE,
       t.LAYDOWNHANDLE,
       t.CUTTINGHANDLE,
       t.MARKERSPECDATATYPE,
       t.MARKERDATAMAND,
       t.FABRICITS,
       t.RECRESBYLAWDOWN,
       t.ALLOCBYWIDTH,
       t.WIDTHFORFILTERTYPE,
       t.USEMEASUREMENTFIRST
FROM   DB2ADMIN.GARMENTSETUP t
FETCH FIRST 100 ROWS ONLY;
```
