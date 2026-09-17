# DB2ADMIN.SCDC_PLAN_TAB_MASTER

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `PVM_IDENTIFIER`, `PVM_WKST_CODE`, `PVM_TABCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188698

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PVM_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PVM_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `PVM_TABCODE` | SMALLINT | NOT NULL | PK | primary_key |  |
| 3 | `PVM_TYPEUSED` | CHAR(1) |  |  |  |  |
| 4 | `PVM_TABDESC` | VARCHAR(40) |  |  |  |  |
| 5 | `PVM_ZOOM` | SMALLINT |  |  |  |  |
| 6 | `PVM_CURRTSCALE` | SMALLINT |  |  |  |  |
| 7 | `PVM_CURRDTTIME` | TIMESTAMP |  |  |  |  |
| 8 | `PVM_SHOWCOLORJOBMODE` | CHAR(1) |  |  |  |  |
| 9 | `PVM_PROPERTY` | VARCHAR(5) |  |  |  |  |
| 10 | `PVM_MCMMAXPRDNUM` | SMALLINT |  |  |  |  |
| 11 | `PVM_MCMMAXPRD1` | SMALLINT |  |  |  |  |
| 12 | `PVM_MCMMAXPRD2` | SMALLINT |  |  |  |  |
| 13 | `PVM_MCMCATVIEWWCHOURSPERC` | SMALLINT |  |  |  |  |
| 14 | `PVM_MCMPROPVIEWWCHOURSPERC` | SMALLINT |  |  |  |  |
| 15 | `PVM_HZOOM` | SMALLINT |  |  |  |  |
| 16 | `PVM_SZOOM` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PVM_IDENTIFIER,
       t.PVM_WKST_CODE,
       t.PVM_TABCODE,
       t.PVM_TYPEUSED,
       t.PVM_TABDESC,
       t.PVM_ZOOM,
       t.PVM_CURRTSCALE,
       t.PVM_CURRDTTIME,
       t.PVM_SHOWCOLORJOBMODE,
       t.PVM_PROPERTY,
       t.PVM_MCMMAXPRDNUM,
       t.PVM_MCMMAXPRD1
FROM   DB2ADMIN.SCDC_PLAN_TAB_MASTER t
FETCH FIRST 100 ROWS ONLY;
```
