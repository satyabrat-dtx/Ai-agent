# DB2ADMIN.LOGPRODUCTIONORDERSTEP

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`
- **Columns**: 86
- **Primary key**: `PRODUCTIONORDERCOMPANYCODE`, `PRODUCTIONORDERCOUNTERCODE`, `PRODUCTIONORDERCODE`, `SPLITCODE`, `STEPNUMBER`, `LOGTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 10928

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PRODUCTIONORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `PRODUCTIONORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `PRODUCTIONORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `SPLITCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `STEPNUMBER` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 5 | `ORDERLINE` | DECIMAL(5,0) |  |  |  |  |
| 6 | `STDRTGSTEPROUTINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 7 | `STDROUTINGSTEPROUTINGNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 8 | `STDROUTINGSTEPSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 9 | `STDROUTINGSTEPALTERNATIVE` | CHAR(3) |  |  |  |  |
| 10 | `STDROUTINGSTEPSUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 11 | `STEPTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `PLANNEDWORKCENTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 13 | `WORKCENTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 14 | `PLANNEDOPERATIONCODE` | CHAR(8) | NOT NULL |  |  |  |
| 15 | `OPERATIONCODE` | CHAR(8) | NOT NULL |  |  |  |
| 16 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(3) |  |  |  |  |
| 17 | `WAREHOUSEWIPCODE` | CHAR(8) |  |  |  |  |
| 18 | `LOCWIPISSUEWHSZONEPHYWHSCODE` | CHAR(8) |  |  |  |  |
| 19 | `LOCWIPISSUEWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 20 | `LOCATIONWIPISSUECODE` | CHAR(10) |  |  |  |  |
| 21 | `LOCWIPENTRYWHSZONEPHYWHSCODE` | CHAR(8) |  |  |  |  |
| 22 | `LOCWIPENTRYWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 23 | `LOCATIONWIPENTRYCODE` | CHAR(10) |  |  |  |  |
| 24 | `MAXNUMBEROFRESOURCESALLOWED` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 25 | `CALENDARCODE` | CHAR(3) |  |  |  |  |
| 26 | `INITIALPLANNEDDATETIME` | TIMESTAMP |  |  |  |  |
| 27 | `FINALPLANNEDDATETIME` | TIMESTAMP |  |  |  |  |
| 28 | `INITIALSCHEDULEDDATETIME` | TIMESTAMP |  |  |  |  |
| 29 | `FINALSCHEDULEDDATETIME` | TIMESTAMP |  |  |  |  |
| 30 | `LONGDESCRIPTION` | CHAR(50) | NOT NULL |  | description | Long human-readable label. |
| 31 | `SHORTDESCRIPTION` | CHAR(20) |  |  | description | Short human-readable label. |
| 32 | `SEARCHDESCRIPTION` | CHAR(30) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 33 | `PRODUCTIONSETUPCODE` | CHAR(8) |  |  |  |  |
| 34 | `STANDARDSTEPQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 35 | `STEPEFFICIENCY` | DECIMAL(5,2) |  |  |  |  |
| 36 | `STEPEFFICIENCYAPPLY` | CHAR(1) |  |  |  |  |
| 37 | `REPETITIONNUMBER` | DECIMAL(17,6) | NOT NULL |  |  |  |
| 38 | `BATHVOLUMEUOMCODE` | CHAR(3) |  |  |  |  |
| 39 | `BATHVOLUME` | DECIMAL(17,6) |  |  |  |  |
| 40 | `CURRENTSTEPPROGRESS` | CHAR(1) |  |  |  |  |
| 41 | `PREVIOUSSTEPPROGRESS` | CHAR(1) |  |  |  |  |
| 42 | `PROGRESSINGAUTOMATICISSUE` | CHAR(1) |  |  |  |  |
| 43 | `PROGRESSINGAUTOMATICENTRY` | CHAR(1) |  |  |  |  |
| 44 | `LOSSINCREASETYPE1CODE` | CHAR(3) |  |  |  |  |
| 45 | `LOSSINCREASE1` | DECIMAL(15,5) |  |  |  |  |
| 46 | `LOSSINCREASEREFUOM1CODE` | CHAR(3) |  |  |  |  |
| 47 | `LOSSINCREASETYPE2CODE` | CHAR(3) |  |  |  |  |
| 48 | `LOSSINCREASE2` | DECIMAL(15,5) |  |  |  |  |
| 49 | `LOSSINCREASEREFUOM2CODE` | CHAR(3) |  |  |  |  |
| 50 | `LOSSINCREASETYPE3CODE` | CHAR(3) |  |  |  |  |
| 51 | `LOSSINCREASE3` | DECIMAL(15,5) |  |  |  |  |
| 52 | `LOSSINCREASEREFUOM3CODE` | CHAR(3) |  |  |  |  |
| 53 | `TIMETYPE1CODE` | CHAR(3) |  |  |  |  |
| 54 | `TIME1` | DECIMAL(10,5) |  |  |  |  |
| 55 | `TIMEUNIT1` | CHAR(2) |  |  |  |  |
| 56 | `TIMEREFUOM1CODE` | CHAR(3) |  |  |  |  |
| 57 | `TIMEREFQTY1` | DECIMAL(15,5) |  |  |  |  |
| 58 | `TIMETYPE2CODE` | CHAR(3) |  |  |  |  |
| 59 | `TIME2` | DECIMAL(10,5) |  |  |  |  |
| 60 | `TIMEUNIT2` | CHAR(2) |  |  |  |  |
| 61 | `TIMEREFUOM2CODE` | CHAR(3) |  |  |  |  |
| 62 | `TIMEREFQTY2` | DECIMAL(15,5) |  |  |  |  |
| 63 | `TIMETYPE3CODE` | CHAR(3) |  |  |  |  |
| 64 | `TIME3` | DECIMAL(10,5) |  |  |  |  |
| 65 | `TIMEUNIT3` | CHAR(2) |  |  |  |  |
| 66 | `TIMEREFUOM3CODE` | CHAR(3) |  |  |  |  |
| 67 | `TIMEREFQTY3` | DECIMAL(15,5) |  |  |  |  |
| 68 | `TIMETYPE4CODE` | CHAR(3) |  |  |  |  |
| 69 | `TIME4` | DECIMAL(10,5) |  |  |  |  |
| 70 | `TIMEUNIT4` | CHAR(2) |  |  |  |  |
| 71 | `TIMEREFUOM4CODE` | CHAR(3) |  |  |  |  |
| 72 | `TIMEREFQTY4` | DECIMAL(15,5) |  |  |  |  |
| 73 | `TIMETYPE5CODE` | CHAR(3) |  |  |  |  |
| 74 | `TIME5` | DECIMAL(10,5) |  |  |  |  |
| 75 | `TIMEUNIT5` | CHAR(2) |  |  |  |  |
| 76 | `TIMEREFUOM5CODE` | CHAR(3) |  |  |  |  |
| 77 | `TIMEREFQTY5` | DECIMAL(15,5) |  |  |  |  |
| 78 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 79 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 80 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 81 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 82 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 83 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 84 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 85 | `LOGUSER` | CHAR(25) |  |  | audit | User responsible for the audited change (change-log table). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PRODUCTIONORDERCOMPANYCODE,
       t.PRODUCTIONORDERCOUNTERCODE,
       t.PRODUCTIONORDERCODE,
       t.SPLITCODE,
       t.STEPNUMBER,
       t.ORDERLINE,
       t.STDRTGSTEPROUTINGCOMPANYCODE,
       t.STDROUTINGSTEPROUTINGNUMBERID,
       t.STDROUTINGSTEPSEQUENCE,
       t.STDROUTINGSTEPALTERNATIVE,
       t.STDROUTINGSTEPSUBSEQUENCE,
       t.STEPTYPE
FROM   DB2ADMIN.LOGPRODUCTIONORDERSTEP t
FETCH FIRST 100 ROWS ONLY;
```
