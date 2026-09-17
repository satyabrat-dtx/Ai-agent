# DB2ADMIN.SCDC_APP_GLOBALS

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 47
- **Primary key**: `AG_IDENTIFIER`, `AG_WKST_CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188280

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `AG_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `AG_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `AG_ENVDESCR` | VARCHAR(30) |  |  |  |  |
| 3 | `AG_CUSTOMER` | VARCHAR(35) |  |  |  |  |
| 4 | `AG_MQMVERSION` | VARCHAR(30) |  |  |  |  |
| 5 | `AG_MONTHBEFORE` | INTEGER |  |  |  |  |
| 6 | `AG_STDATEFORPLAN` | TIMESTAMP |  |  |  |  |
| 7 | `AG_LANGUAGE` | VARCHAR(14) |  |  |  |  |
| 8 | `AG_CURRTSCALE` | SMALLINT |  |  |  |  |
| 9 | `AG_CURRDTTIME` | TIMESTAMP |  |  |  |  |
| 10 | `AG_SHOWCAL` | SMALLINT |  |  |  |  |
| 11 | `AG_CURRRSCSORT` | SMALLINT |  |  |  |  |
| 12 | `AG_SHOWZOOM` | SMALLINT |  |  |  |  |
| 13 | `AG_RSCORDERTYPE` | VARCHAR(14) |  |  |  |  |
| 14 | `AG_RSCORDERITEM` | VARCHAR(14) |  |  |  |  |
| 15 | `AG_WDWPLANLEFT` | SMALLINT |  |  |  |  |
| 16 | `AG_WDWPLANTOP` | SMALLINT |  |  |  |  |
| 17 | `AG_WDWPLANWIDTH` | SMALLINT |  |  |  |  |
| 18 | `AG_WDWPLANHEIGHT` | SMALLINT |  |  |  |  |
| 19 | `AG_WDWPLANSTATE` | SMALLINT |  |  |  |  |
| 20 | `AG_WDWBINDOCK` | SMALLINT |  |  |  |  |
| 21 | `AG_WDWBINLEFT` | SMALLINT |  |  |  |  |
| 22 | `AG_WDWBINTOP` | SMALLINT |  |  |  |  |
| 23 | `AG_WDWBINWIDTH` | SMALLINT |  |  |  |  |
| 24 | `AG_WDWBINHEIGHT` | SMALLINT |  |  |  |  |
| 25 | `AG_WDWBINSTATE` | SMALLINT |  |  |  |  |
| 26 | `AG_WDWBINSPLITTER` | SMALLINT |  |  |  |  |
| 27 | `AG_TOOLBARDOCK` | SMALLINT |  |  |  |  |
| 28 | `AG_TOOLBARLEFT` | SMALLINT |  |  |  |  |
| 29 | `AG_TOOLBARTOP` | SMALLINT |  |  |  |  |
| 30 | `AG_TOOLBARWIDTH` | SMALLINT |  |  |  |  |
| 31 | `AG_TOOLBARHEIGHT` | SMALLINT |  |  |  |  |
| 32 | `AG_TOOLBARSTATE` | SMALLINT |  |  |  |  |
| 33 | `AG_CHECKSTEPSEQ` | SMALLINT |  |  |  |  |
| 34 | `AG_CENTERSTARTONMOVE` | SMALLINT |  |  |  |  |
| 35 | `AG_WARNONMOVEFINAL` | SMALLINT |  |  |  |  |
| 36 | `AG_DEFSCHEDTYPE` | SMALLINT |  |  |  |  |
| 37 | `AG_MOVEOPTION` | SMALLINT |  |  |  |  |
| 38 | `AG_ACTAUTOSCHEDCODE` | VARCHAR(14) |  |  |  |  |
| 39 | `AG_CONFLEVELS` | SMALLINT |  |  |  |  |
| 40 | `AG_SHOWCOLORJOBMODE` | CHAR(1) |  |  |  |  |
| 41 | `AG_PROPERTY` | VARCHAR(5) |  |  |  |  |
| 42 | `AG_UNSCHEDULECLOSEDJOBSONSTART` | CHAR(1) |  |  |  |  |
| 43 | `AG_SLOTDISPLAY` | SMALLINT |  |  |  |  |
| 44 | `AG_CUSTOMSLOTDISPLAY` | SMALLINT |  |  |  |  |
| 45 | `AG_CUSTOMPROPDISPLAY` | VARCHAR(5) |  |  |  |  |
| 46 | `AG_CUSTOMPROPSYMBOL` | VARCHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.AG_IDENTIFIER,
       t.AG_WKST_CODE,
       t.AG_ENVDESCR,
       t.AG_CUSTOMER,
       t.AG_MQMVERSION,
       t.AG_MONTHBEFORE,
       t.AG_STDATEFORPLAN,
       t.AG_LANGUAGE,
       t.AG_CURRTSCALE,
       t.AG_CURRDTTIME,
       t.AG_SHOWCAL,
       t.AG_CURRRSCSORT
FROM   DB2ADMIN.SCDC_APP_GLOBALS t
FETCH FIRST 100 ROWS ONLY;
```
