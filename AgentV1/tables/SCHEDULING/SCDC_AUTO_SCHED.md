# DB2ADMIN.SCDC_AUTO_SCHED

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 88
- **Primary key**: `ASC_IDENTIFIER`, `ASC_WKST_CODE`, `ASC_CFGNAME`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188395

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ASC_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `ASC_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `ASC_CFGNAME` | VARCHAR(14) | NOT NULL | PK | primary_key |  |
| 3 | `ASC_CFGDESC` | VARCHAR(50) |  |  |  |  |
| 4 | `ASC_MINJOBRESCOMP` | SMALLINT |  |  |  |  |
| 5 | `ASC_MINJOBJOBCOMP` | SMALLINT |  |  |  |  |
| 6 | `ASC_MAXJOBJOBCOMP` | SMALLINT |  |  |  |  |
| 7 | `ASC_MINJOBCAPRESCOMP` | SMALLINT |  |  |  |  |
| 8 | `ASC_AFTERHIGHLIMIT` | SMALLINT |  |  |  |  |
| 9 | `ASC_TOLLAFTERHIGHLIMIT` | SMALLINT |  |  |  |  |
| 10 | `ASC_TOLLAFTERHIGHLIMITHOURS` | SMALLINT |  |  |  |  |
| 11 | `ASC_TOLLAFTERHIGHLIMITMINUTES` | SMALLINT |  |  |  |  |
| 12 | `ASC_BEFORELOWLIMIT` | SMALLINT |  |  |  |  |
| 13 | `ASC_TOLLBEFORELOWLIMIT` | SMALLINT |  |  |  |  |
| 14 | `ASC_TOLLBEFORELOWLIMITHOURS` | SMALLINT |  |  |  |  |
| 15 | `ASC_TOLLBEFORELOWLIMITMINUTES` | SMALLINT |  |  |  |  |
| 16 | `ASC_PREFTGTDATE` | SMALLINT |  |  |  |  |
| 17 | `ASC_PRVORNXTLINKEDJOBTGTDATE` | CHAR(1) |  |  |  |  |
| 18 | `ASC_MOVEOBJSALLOWED` | SMALLINT |  |  |  |  |
| 19 | `ASC_MOVEFINALOBJSALWD` | SMALLINT |  |  |  |  |
| 20 | `ASC_MOVEINITIALOBJSALWD` | SMALLINT |  |  |  |  |
| 21 | `ASC_MOVELEVEL1OBJSALWD` | SMALLINT |  |  |  |  |
| 22 | `ASC_MOVELEVEL2OBJSALWD` | SMALLINT |  |  |  |  |
| 23 | `ASC_MOVELEVEL3OBJSALWD` | SMALLINT |  |  |  |  |
| 24 | `ASC_MOVELEVEL4OBJSALWD` | SMALLINT |  |  |  |  |
| 25 | `ASC_MOVELEVEL5OBJSALWD` | SMALLINT |  |  |  |  |
| 26 | `ASC_MINSTARTDATEOFFSET` | SMALLINT |  |  |  |  |
| 27 | `ASC_PRIORERRLOOP` | CHAR(1) |  |  |  |  |
| 28 | `ASC_TEMPFINAL` | SMALLINT |  |  |  |  |
| 29 | `ASC_SLEEP` | SMALLINT |  |  |  |  |
| 30 | `ASC_RANKREP` | CHAR(1) |  |  |  |  |
| 31 | `ASC_GROUPALLOWONEJOB` | CHAR(1) |  |  |  |  |
| 32 | `ASC_MATWOMATERIALS` | SMALLINT |  |  |  |  |
| 33 | `ASC_ONESTEPATTIME` | SMALLINT |  |  |  |  |
| 34 | `ASC_MATLINKREQ` | SMALLINT |  |  |  |  |
| 35 | `ASC_MATWOADDRES` | SMALLINT |  |  |  |  |
| 36 | `ASC_COMPACTENTITIES` | SMALLINT |  |  |  |  |
| 37 | `ASC_NEXTDAYS` | SMALLINT |  |  |  |  |
| 38 | `ASC_GRAPHONMOVE` | CHAR(1) |  |  |  |  |
| 39 | `ASC_BEFEARLDATETOL` | DECIMAL(11,2) |  |  |  |  |
| 40 | `ASC_WITHEARLDATETOL` | DECIMAL(11,2) |  |  |  |  |
| 41 | `ASC_AFTERLATDATETOL` | DECIMAL(11,2) |  |  |  |  |
| 42 | `ASC_WITHLATDATETOL` | DECIMAL(11,2) |  |  |  |  |
| 43 | `ASC_PENJOBTOJOB` | DECIMAL(11,2) |  |  |  |  |
| 44 | `ASC_PENSETUPMIN` | DECIMAL(11,2) |  |  |  |  |
| 45 | `ASC_PENJOBTORES` | DECIMAL(11,2) |  |  |  |  |
| 46 | `ASC_PENJOBTOCAPRES` | DECIMAL(11,2) |  |  |  |  |
| 47 | `ASC_PENJOBNOTCAPRES` | DECIMAL(11,2) |  |  |  |  |
| 48 | `ASC_DATESCOREWEIGHT` | SMALLINT |  |  |  |  |
| 49 | `ASC_COMPSCOREWEIGHT` | SMALLINT |  |  |  |  |
| 50 | `ASC_AUTOSPLITBYSTDBTCHSIZE` | SMALLINT |  |  |  |  |
| 51 | `ASC_LASTSPLITCANGOUNDERMINMAC` | SMALLINT |  |  |  |  |
| 52 | `ASC_CRETERIAOFRESFORBACHZISE` | SMALLINT |  |  |  |  |
| 53 | `ASC_LOADEDRESOURCE` | CHAR(1) |  |  |  |  |
| 54 | `ASC_SORTBEFORESCHEDULE` | CHAR(1) |  |  |  |  |
| 55 | `ASC_BINSORTFIELDID1` | SMALLINT |  |  |  |  |
| 56 | `ASC_BINSORTFIELDID2` | SMALLINT |  |  |  |  |
| 57 | `ASC_BINSORTFIELDID3` | SMALLINT |  |  |  |  |
| 58 | `ASC_BINSORTFIELDID4` | SMALLINT |  |  |  |  |
| 59 | `ASC_BINSORTFIELDID5` | SMALLINT |  |  |  |  |
| 60 | `ASC_LOADEDONSAMERESCAT` | CHAR(1) |  |  |  |  |
| 61 | `ASC_STOPONFIRSTNOTSCHEDJOB` | CHAR(1) |  |  |  |  |
| 62 | `ASC_LIMITGAPBTWNSUBSTEPS` | CHAR(1) |  |  |  |  |
| 63 | `ASC_TOLDAYSGAPBTWSUBSTEPS` | SMALLINT |  |  |  |  |
| 64 | `ASC_TOLHOURSGAPBTWNSUBSTEPS` | SMALLINT |  |  |  |  |
| 65 | `ASC_TOLMINGAPBTWNSUBSTEPS` | SMALLINT |  |  |  |  |
| 66 | `ASC_CFGNEXTNAME` | VARCHAR(14) |  |  |  |  |
| 67 | `ASC_SORT_RES` | CHAR(1) |  |  |  |  |
| 68 | `ASC_RES_TOSCHED` | CHAR(1) |  |  |  |  |
| 69 | `ASC_ALLOWSCHEDBEFORENONECNFLVL` | CHAR(1) |  |  |  |  |
| 70 | `ASC_SCHEDTOPOSIBLESTARTPENALTY` | DECIMAL(11,2) |  |  |  |  |
| 71 | `ASC_CFG_GROUP` | VARCHAR(10) |  |  |  |  |
| 72 | `ASC_RUNNING_MODE` | CHAR(1) |  |  |  |  |
| 73 | `ASC_START_SCHED_FROM` | CHAR(1) |  |  |  |  |
| 74 | `ASC_SPECIFIC_DATETIME` | TIMESTAMP |  |  |  |  |
| 75 | `ASC_NUM_DAYS_FROM_CURRENT` | SMALLINT |  |  |  |  |
| 76 | `ASC_HOURSTOLERANCEOFGAPBTWJOBS` | SMALLINT |  |  |  |  |
| 77 | `ASC_RESCHEDERLIERJOBSWHENTOLRC` | CHAR(1) |  |  |  |  |
| 78 | `ASC_PENALTYSCOREBEFORETOLERANC` | DECIMAL(11,2) |  |  |  |  |
| 79 | `ASC_PENALTYSCOREAFTERTOLERANCE` | DECIMAL(11,2) |  |  |  |  |
| 80 | `ASC_IGNORERIGHTOVERLAPPING` | SMALLINT |  |  |  |  |
| 81 | `ASC_IGNORELEFTOVERLAPPING` | SMALLINT |  |  |  |  |
| 82 | `ASC_SAMEWCPLANTTOSERVINGGROUP` | CHAR(1) |  |  |  |  |
| 83 | `ASC_CALENDARFORDATESPENALTY` | VARCHAR(3) |  |  |  |  |
| 84 | `ASC_LATESTDATELIMIT` | SMALLINT |  |  |  |  |
| 85 | `ASC_DATELIMITTYPE` | SMALLINT |  |  |  |  |
| 86 | `ASC_NUMOFDAYSFROMSTARTPOINT` | SMALLINT |  |  |  |  |
| 87 | `ASC_DATEFROMSTARTPOINTALLOW` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ASC_IDENTIFIER,
       t.ASC_WKST_CODE,
       t.ASC_CFGNAME,
       t.ASC_CFGDESC,
       t.ASC_MINJOBRESCOMP,
       t.ASC_MINJOBJOBCOMP,
       t.ASC_MAXJOBJOBCOMP,
       t.ASC_MINJOBCAPRESCOMP,
       t.ASC_AFTERHIGHLIMIT,
       t.ASC_TOLLAFTERHIGHLIMIT,
       t.ASC_TOLLAFTERHIGHLIMITHOURS,
       t.ASC_TOLLAFTERHIGHLIMITMINUTES
FROM   DB2ADMIN.SCDC_AUTO_SCHED t
FETCH FIRST 100 ROWS ONLY;
```
