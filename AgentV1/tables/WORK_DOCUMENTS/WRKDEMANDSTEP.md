# DB2ADMIN.WRKDEMANDSTEP

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 158
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 212436

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INITIALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 1 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 2 | `PRODUCTIONDEMANDCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 3 | `FINALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 4 | `PRODEMANDCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `PRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 6 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 7 | `PRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 8 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 9 | `EXISTENTSTEP` | SMALLINT | NOT NULL |  |  |  |
| 10 | `INITIALBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 11 | `FINALBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 12 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 15 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 16 | `INITIALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 17 | `FINALUSERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 18 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 19 | `INITIALBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 20 | `FINALBASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 22 | `INITIALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 23 | `FINALUSERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 25 | `STDROUTINGSTEPNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 26 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 27 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 28 | `DYELOTHANDLED` | SMALLINT | NOT NULL |  |  |  |
| 29 | `WORKCENTERANDOPERATTRIBUTESCOD` | CHAR(20) |  |  |  |  |
| 30 | `PARTIALSTEP` | SMALLINT | NOT NULL |  |  |  |
| 31 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 32 | `STEPTYPE` | CHAR(2) |  |  |  |  |
| 33 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 34 | `MAXNUMBEROFRESOURCESALLOWED` | DECIMAL(3,0) |  |  |  |  |
| 35 | `WAREHOUSEWIPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 36 | `WAREHOUSEWIPCODE` | CHAR(8) |  |  |  |  |
| 37 | `LOCWIPISSUEWHSZONEPHYWHSCMYCOD` | CHAR(3) |  |  |  |  |
| 38 | `LOCWIPISSUEWHSZONEPHYWHSCODE` | CHAR(8) |  |  |  |  |
| 39 | `LOCWIPISSUEWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 40 | `LOCATIONWIPISSUECODE` | CHAR(10) |  |  |  |  |
| 41 | `LOCWIPENTRYWHSZONEPHYWHSCMYCOD` | CHAR(3) |  |  |  |  |
| 42 | `LOCWIPENTRYWHSZONEPHYWHSCODE` | CHAR(8) |  |  |  |  |
| 43 | `LOCWIPENTRYWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 44 | `LOCATIONWIPENTRYCODE` | CHAR(10) |  |  |  |  |
| 45 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 46 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 47 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 48 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 49 | `STEPNUMBERLINK` | DECIMAL(5,0) |  |  |  |  |
| 50 | `CALENDARCODE` | CHAR(3) |  |  |  |  |
| 51 | `INITIALPLANNEDDATETIME` | TIMESTAMP |  |  |  |  |
| 52 | `FINALPLANNEDDATETIME` | TIMESTAMP |  |  |  |  |
| 53 | `INITIALPLANSCHEDDATETIME` | TIMESTAMP |  |  |  |  |
| 54 | `FINALPLANSCHEDDATETIME` | TIMESTAMP |  |  |  |  |
| 55 | `INITIALSCHEDULEDDATETIME` | TIMESTAMP |  |  |  |  |
| 56 | `SCHEDULEDSTEP` | SMALLINT | NOT NULL |  |  |  |
| 57 | `FINALSCHEDULEDDATETIME` | TIMESTAMP |  |  |  |  |
| 58 | `STANDARDSTEPQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 59 | `STANDARDSTEPQUANTITYUOMCODE` | CHAR(3) |  |  |  |  |
| 60 | `STEPEFFICIENCYAPPLY` | CHAR(1) |  |  |  |  |
| 61 | `STEPEFFICIENCY` | DECIMAL(5,2) |  |  |  |  |
| 62 | `NROFMACHINE` | INTEGER | NOT NULL |  |  |  |
| 63 | `REPETITIONNUMBER` | DECIMAL(17,6) |  |  |  |  |
| 64 | `BATHVOLUME` | DECIMAL(17,6) |  |  |  |  |
| 65 | `BATHVOLUMEUOMCODE` | CHAR(3) |  |  |  |  |
| 66 | `OPSTEPGROUPCODE` | CHAR(8) |  |  |  |  |
| 67 | `GENERATEAUTOMATICQATEST` | SMALLINT | NOT NULL |  |  |  |
| 68 | `OVERLAPPINGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 69 | `OVERLAPPINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 70 | `OVERLAPPINGUOMCATEGORY` | CHAR(1) |  |  |  |  |
| 71 | `LOSSINCREASETYPE1CODE` | CHAR(3) |  |  |  |  |
| 72 | `LOSSINCREASE1` | DECIMAL(15,5) |  |  |  |  |
| 73 | `LOSSINCREASEREFUOM1CODE` | CHAR(3) |  |  |  |  |
| 74 | `LOSSINCREASETYPE2CODE` | CHAR(3) |  |  |  |  |
| 75 | `LOSSINCREASE2` | DECIMAL(15,5) |  |  |  |  |
| 76 | `LOSSINCREASEREFUOM2CODE` | CHAR(3) |  |  |  |  |
| 77 | `LOSSINCREASETYPE3CODE` | CHAR(3) |  |  |  |  |
| 78 | `LOSSINCREASE3` | DECIMAL(15,5) |  |  |  |  |
| 79 | `LOSSINCREASEREFUOM3CODE` | CHAR(3) |  |  |  |  |
| 80 | `LOSSINCREASETYPE4CODE` | CHAR(3) |  |  |  |  |
| 81 | `LOSSINCREASE4` | DECIMAL(15,5) |  |  |  |  |
| 82 | `LOSSINCREASEREFUOM4CODE` | CHAR(3) |  |  |  |  |
| 83 | `LOSSINCREASETYPE5CODE` | CHAR(3) |  |  |  |  |
| 84 | `LOSSINCREASE5` | DECIMAL(15,5) |  |  |  |  |
| 85 | `LOSSINCREASEREFUOM5CODE` | CHAR(3) |  |  |  |  |
| 86 | `LOSSINCREASETYPE6CODE` | CHAR(3) |  |  |  |  |
| 87 | `LOSSINCREASE6` | DECIMAL(15,5) |  |  |  |  |
| 88 | `LOSSINCREASEREFUOM6CODE` | CHAR(3) |  |  |  |  |
| 89 | `LOSSINCREASETYPE7CODE` | CHAR(3) |  |  |  |  |
| 90 | `LOSSINCREASE7` | DECIMAL(15,5) |  |  |  |  |
| 91 | `LOSSINCREASEREFUOM7CODE` | CHAR(3) |  |  |  |  |
| 92 | `LOSSINCREASETYPE8CODE` | CHAR(3) |  |  |  |  |
| 93 | `LOSSINCREASE8` | DECIMAL(15,5) |  |  |  |  |
| 94 | `LOSSINCREASEREFUOM8CODE` | CHAR(3) |  |  |  |  |
| 95 | `LOSSINCREASETYPEPOLICY` | CHAR(3) |  |  |  |  |
| 96 | `PARALLELPDNUMBER` | INTEGER | NOT NULL |  |  |  |
| 97 | `PLANNINGLEADTIME` | DECIMAL(15,5) |  |  |  |  |
| 98 | `TIMETYPE1CODE` | CHAR(3) |  |  |  |  |
| 99 | `TIME1` | DECIMAL(10,5) |  |  |  |  |
| 100 | `TIMEUNIT1` | CHAR(2) |  |  |  |  |
| 101 | `TIMEREFQTY1` | DECIMAL(15,5) |  |  |  |  |
| 102 | `TIMEREFUOM1CODE` | CHAR(3) |  |  |  |  |
| 103 | `TIMETYPE2CODE` | CHAR(3) |  |  |  |  |
| 104 | `TIME2` | DECIMAL(10,5) |  |  |  |  |
| 105 | `TIMEUNIT2` | CHAR(2) |  |  |  |  |
| 106 | `TIMEREFQTY2` | DECIMAL(15,5) |  |  |  |  |
| 107 | `TIMEREFUOM2CODE` | CHAR(3) |  |  |  |  |
| 108 | `TIMETYPE3CODE` | CHAR(3) |  |  |  |  |
| 109 | `TIME3` | DECIMAL(10,5) |  |  |  |  |
| 110 | `TIMEUNIT3` | CHAR(2) |  |  |  |  |
| 111 | `TIMEREFQTY3` | DECIMAL(15,5) |  |  |  |  |
| 112 | `TIMEREFUOM3CODE` | CHAR(3) |  |  |  |  |
| 113 | `TIMETYPE4CODE` | CHAR(3) |  |  |  |  |
| 114 | `TIME4` | DECIMAL(10,5) |  |  |  |  |
| 115 | `TIMEUNIT4` | CHAR(2) |  |  |  |  |
| 116 | `TIMEREFQTY4` | DECIMAL(15,5) |  |  |  |  |
| 117 | `TIMEREFUOM4CODE` | CHAR(3) |  |  |  |  |
| 118 | `TIMETYPE5CODE` | CHAR(3) |  |  |  |  |
| 119 | `TIME5` | DECIMAL(10,5) |  |  |  |  |
| 120 | `TIMEUNIT5` | CHAR(2) |  |  |  |  |
| 121 | `TIMEREFQTY5` | DECIMAL(15,5) |  |  |  |  |
| 122 | `TIMEREFUOM5CODE` | CHAR(3) |  |  |  |  |
| 123 | `CALCULATEDTIME1` | DECIMAL(10,5) |  |  |  |  |
| 124 | `CALCULATEDTIME2` | DECIMAL(10,5) |  |  |  |  |
| 125 | `CALCULATEDTIME3` | DECIMAL(10,5) |  |  |  |  |
| 126 | `CALCULATEDTIME4` | DECIMAL(10,5) |  |  |  |  |
| 127 | `MINBEGINQUEUE` | DATE |  |  |  |  |
| 128 | `MINBEGINQUEUETIME` | TIME |  |  |  |  |
| 129 | `MINBEGINPRESETUP` | DATE |  |  |  |  |
| 130 | `MINBEGINPRESETUPTIME` | TIME |  |  |  |  |
| 131 | `MINBEGINOPERATION` | DATE |  |  |  |  |
| 132 | `MINBEGINOPERATIONTIME` | TIME |  |  |  |  |
| 133 | `MINBEGINPOSTSETUP` | DATE |  |  |  |  |
| 134 | `MINBEGINPOSTSETUPTIME` | TIME |  |  |  |  |
| 135 | `MINENDSTEP` | DATE |  |  |  |  |
| 136 | `MINENDSTEPTIME` | TIME |  |  |  |  |
| 137 | `STDBEGINQUEUE` | DATE |  |  |  |  |
| 138 | `STDBEGINQUEUETIME` | TIME |  |  |  |  |
| 139 | `STDBEGINPRESETUP` | DATE |  |  |  |  |
| 140 | `STDBEGINPRESETUPTIME` | TIME |  |  |  |  |
| 141 | `STDBEGINOPERATION` | DATE |  |  |  |  |
| 142 | `STDBEGINOPERATIONTIME` | TIME |  |  |  |  |
| 143 | `STDBEGINPOSTSETUP` | DATE |  |  |  |  |
| 144 | `STDBEGINPOSTSETUPTIME` | TIME |  |  |  |  |
| 145 | `STDENDSTEP` | DATE |  |  |  |  |
| 146 | `STDENDSTEPTIME` | TIME |  |  |  |  |
| 147 | `MAXBEGINQUEUE` | DATE |  |  |  |  |
| 148 | `MAXBEGINQUEUETIME` | TIME |  |  |  |  |
| 149 | `MAXBEGINPRESETUP` | DATE |  |  |  |  |
| 150 | `MAXBEGINPRESETUPTIME` | TIME |  |  |  |  |
| 151 | `MAXBEGINOPERATION` | DATE |  |  |  |  |
| 152 | `MAXBEGINOPERATIONTIME` | TIME |  |  |  |  |
| 153 | `MAXBEGINPOSTSETUP` | DATE |  |  |  |  |
| 154 | `MAXBEGINPOSTSETUPTIME` | TIME |  |  |  |  |
| 155 | `MAXENDSTEP` | DATE |  |  |  |  |
| 156 | `MAXENDSTEPTIME` | TIME |  |  |  |  |
| 157 | `GROUPSTEPNUMBER` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.INITIALUSERPRIMARYQUANTITY,
       t.CHOOSE,
       t.PRODUCTIONDEMANDCOMPANYCODE,
       t.FINALUSERPRIMARYQUANTITY,
       t.PRODEMANDCOUNTERCOMPANYCODE,
       t.PRODUCTIONDEMANDCOUNTERCODE,
       t.USERPRIMARYUOMCODE,
       t.PRODUCTIONDEMANDCODE,
       t.STEPNUMBER,
       t.EXISTENTSTEP,
       t.INITIALBASEPRIMARYQUANTITY,
       t.FINALBASEPRIMARYQUANTITY
FROM   DB2ADMIN.WRKDEMANDSTEP t
FETCH FIRST 100 ROWS ONLY;
```
