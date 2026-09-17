# DB2ADMIN.SHIFT

- **Module**: `HR` (low confidence — FK neighbourhood: 4 of 4 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 10 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 156107

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `SHIFTGROUP` | INTEGER | NOT NULL |  |  |  |
| 6 | `STARTTIME` | TIME | NOT NULL |  |  |  |
| 7 | `ATTDSTARTTIME` | TIME |  |  |  |  |
| 8 | `ATTDENDTIME` | TIME |  |  |  |  |
| 9 | `ENDTIME` | TIME | NOT NULL |  |  |  |
| 10 | `TOTALHOURS` | DECIMAL(5,2) |  |  |  |  |
| 11 | `RECESSSTARTTIME` | TIME | NOT NULL |  |  |  |
| 12 | `RECESSENDTIME` | TIME | NOT NULL |  |  |  |
| 13 | `TOTALMINUTES` | DECIMAL(5,2) |  |  |  |  |
| 14 | `RECESSINCLUDE` | INTEGER | NOT NULL |  |  |  |
| 15 | `EARLYIN` | TIME |  |  |  |  |
| 16 | `LATEOUT` | TIME |  |  |  |  |
| 17 | `EARLYBEFORETIME` | TIME |  |  |  |  |
| 18 | `LATEAFTERTIME` | TIME |  |  |  |  |
| 19 | `BUSLATEALLOWSTARTTIME` | INTEGER | NOT NULL |  |  |  |
| 20 | `BUSLATEALLOWENDTIME` | INTEGER | NOT NULL |  |  |  |
| 21 | `MINHRSFORHALFDAY` | DECIMAL(5,2) |  |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 27 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 28 | `STEP` | CHAR(1) |  |  |  |  |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SHIFT.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 10

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SHIFT_SHIFT` | [`DESGVSCOSTCENTER`](../COSTING/DESGVSCOSTCENTER.md) | `COMPANYCODE`, `SHIFTCODE` | `DESGVSCOSTCENTER.COMPANYCODE = SHIFT.COMPANYCODE AND DESGVSCOSTCENTER.SHIFTCODE = SHIFT.CODE` |
| `SHIFT_SHIFT` | [`SHIFTROTATIONDETAIL`](../HR/SHIFTROTATIONDETAIL.md) | `SHIFTROTATIONCOMPANYCODE`, `SHIFTCODE` | `SHIFTROTATIONDETAIL.SHIFTROTATIONCOMPANYCODE = SHIFT.COMPANYCODE AND SHIFTROTATIONDETAIL.SHIFTCODE = SHIFT.CODE` |
| `SHIFT_SHIFT` | [`PRODVSPAYROLLSHIFT`](../HR/PRODVSPAYROLLSHIFT.md) | `COMPANYCODE`, `SHIFTCODE` | `PRODVSPAYROLLSHIFT.COMPANYCODE = SHIFT.COMPANYCODE AND PRODVSPAYROLLSHIFT.SHIFTCODE = SHIFT.CODE` |
| `SHIFT_SHIFT` | [`ACCINTIMATION`](../HR/ACCINTIMATION.md) | `COMPANYCODE`, `SHIFTCODE` | `ACCINTIMATION.COMPANYCODE = SHIFT.COMPANYCODE AND ACCINTIMATION.SHIFTCODE = SHIFT.CODE` |
| `SHIFT_SHIFT` | [`ATTENDANCECORRECTION`](../HR/ATTENDANCECORRECTION.md) | `COMPANYCODE`, `SHIFTCODE` | `ATTENDANCECORRECTION.COMPANYCODE = SHIFT.COMPANYCODE AND ATTENDANCECORRECTION.SHIFTCODE = SHIFT.CODE` |
| `SHIFT_SHIFT` | [`ATTENDANCEDETAIL`](../HR/ATTENDANCEDETAIL.md) | `COMPANYCODE`, `SHIFTCODE` | `ATTENDANCEDETAIL.COMPANYCODE = SHIFT.COMPANYCODE AND ATTENDANCEDETAIL.SHIFTCODE = SHIFT.CODE` |
| `SHIFT_SHIFT` | [`ATTENDANCEDETAILTEMP`](../HR/ATTENDANCEDETAILTEMP.md) | `COMPANYCODE`, `SHIFTCODE` | `ATTENDANCEDETAILTEMP.COMPANYCODE = SHIFT.COMPANYCODE AND ATTENDANCEDETAILTEMP.SHIFTCODE = SHIFT.CODE` |
| `SHIFT_SHIFT` | [`ATTENDANCEDETAILTEMPPEREMP`](../HR/ATTENDANCEDETAILTEMPPEREMP.md) | `COMPANYCODE`, `SHIFTCODE` | `ATTENDANCEDETAILTEMPPEREMP.COMPANYCODE = SHIFT.COMPANYCODE AND ATTENDANCEDETAILTEMPPEREMP.SHIFTCODE = SHIFT.CODE` |
| `SHIFT_SHIFT` | [`GATEPASS`](../HR/GATEPASS.md) | `COMPANYCODE`, `SHIFTCODE` | `GATEPASS.COMPANYCODE = SHIFT.COMPANYCODE AND GATEPASS.SHIFTCODE = SHIFT.CODE` |
| `SHIFT_SHIFT` | [`OTATTENDANCEDETAIL`](../HR/OTATTENDANCEDETAIL.md) | `COMPANYCODE`, `SHIFTCODE` | `OTATTENDANCEDETAIL.COMPANYCODE = SHIFT.COMPANYCODE AND OTATTENDANCEDETAIL.SHIFTCODE = SHIFT.CODE` |

## Indexes

- `SHIFTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.SHIFTGROUP,
       t.STARTTIME,
       t.ATTDSTARTTIME,
       t.ATTDENDTIME,
       t.ENDTIME,
       t.TOTALHOURS,
       t.RECESSSTARTTIME
FROM   DB2ADMIN.SHIFT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
