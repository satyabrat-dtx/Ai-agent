# DB2ADMIN.PATTERNREPETITION

- **Module**: `PRODUCTION` (low confidence — table name starts with 'PATTERN')
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `PATLVLPATHEADERCOMPANYCODE`, `PATLVLPATHEADERWARPWEFTTYPE`, `PATLVLPATHEADERPATTERNCODE`, `PATTERNLEVELWARPWEFTLEVEL`, `REPETITIONLEVEL`, `FROMCOL`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 23352

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PATLVLPATHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PATLVLPATHEADERWARPWEFTTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PATLVLPATHEADERPATTERNCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PATTERNLEVELWARPWEFTLEVEL` | DECIMAL(2,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `REPETITIONLEVEL` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 5 | `FROMCOL` | CHAR(5) | NOT NULL | PK | primary_key |  |
| 6 | `TOCOL` | CHAR(5) |  |  |  |  |
| 7 | `FIELDVALUE` | CHAR(5) |  |  |  |  |
| 8 | `NOOFREPS` | DECIMAL(5,0) |  |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PATTERNLEVEL_PATTERNREPETITION` | `PATLVLPATHEADERCOMPANYCODE`, `PATLVLPATHEADERWARPWEFTTYPE`, `PATLVLPATHEADERPATTERNCODE`, `PATTERNLEVELWARPWEFTLEVEL` | [`PATTERNLEVEL`](../PRODUCTION/PATTERNLEVEL.md) | `PATTERNHEADERCOMPANYCODE`, `PATTERNHEADERWARPWEFTTYPE`, `PATTERNHEADERPATTERNCODE`, `WARPWEFTLEVEL` | RESTRICT | `PATTERNREPETITION.PATLVLPATHEADERCOMPANYCODE = PATTERNLEVEL.PATTERNHEADERCOMPANYCODE AND PATTERNREPETITION.PATLVLPATHEADERWARPWEFTTYPE = PATTERNLEVEL.PATTERNHEADERWARPWEFTTYPE AND PATTERNREPETITION.PATLVLPATHEADERPATTERNCODE = PATTERNLEVEL.PATTERNHEADERPATTERNCODE AND PATTERNREPETITION.PATTERNLEVELWARPWEFTLEVEL = PATTERNLEVEL.WARPWEFTLEVEL` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PATTERNREPETITIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PATLVLPATHEADERCOMPANYCODE,
       t.PATLVLPATHEADERWARPWEFTTYPE,
       t.PATLVLPATHEADERPATTERNCODE,
       t.PATTERNLEVELWARPWEFTLEVEL,
       t.REPETITIONLEVEL,
       t.FROMCOL,
       t.TOCOL,
       t.FIELDVALUE,
       t.NOOFREPS,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.PATTERNREPETITION t
FETCH FIRST 100 ROWS ONLY;
```
