# DB2ADMIN.PATTERNDETAIL

- **Module**: `PRODUCTION` (low confidence — table name starts with 'PATTERN')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `PATLVLPATHEADERCOMPANYCODE`, `PATLVLPATHEADERWARPWEFTTYPE`, `PATLVLPATHEADERPATTERNCODE`, `PATTERNLEVELWARPWEFTLEVEL`, `ROWNUMBER`, `COL`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 10193

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PATLVLPATHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PATLVLPATHEADERWARPWEFTTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PATLVLPATHEADERPATTERNCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PATTERNLEVELWARPWEFTLEVEL` | DECIMAL(2,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ROWNUMBER` | CHAR(5) | NOT NULL | PK | primary_key |  |
| 5 | `COL` | CHAR(5) | NOT NULL | PK | primary_key |  |
| 6 | `NOOFENDS` | DECIMAL(5,0) |  |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PATTERNLEVEL_PATTERNDETAIL` | `PATLVLPATHEADERCOMPANYCODE`, `PATLVLPATHEADERWARPWEFTTYPE`, `PATLVLPATHEADERPATTERNCODE`, `PATTERNLEVELWARPWEFTLEVEL` | [`PATTERNLEVEL`](../PRODUCTION/PATTERNLEVEL.md) | `PATTERNHEADERCOMPANYCODE`, `PATTERNHEADERWARPWEFTTYPE`, `PATTERNHEADERPATTERNCODE`, `WARPWEFTLEVEL` | RESTRICT | `PATTERNDETAIL.PATLVLPATHEADERCOMPANYCODE = PATTERNLEVEL.PATTERNHEADERCOMPANYCODE AND PATTERNDETAIL.PATLVLPATHEADERWARPWEFTTYPE = PATTERNLEVEL.PATTERNHEADERWARPWEFTTYPE AND PATTERNDETAIL.PATLVLPATHEADERPATTERNCODE = PATTERNLEVEL.PATTERNHEADERPATTERNCODE AND PATTERNDETAIL.PATTERNLEVELWARPWEFTLEVEL = PATTERNLEVEL.WARPWEFTLEVEL` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PATTERNDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PATLVLPATHEADERCOMPANYCODE,
       t.PATLVLPATHEADERWARPWEFTTYPE,
       t.PATLVLPATHEADERPATTERNCODE,
       t.PATTERNLEVELWARPWEFTLEVEL,
       t.ROWNUMBER,
       t.COL,
       t.NOOFENDS,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PATTERNDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
