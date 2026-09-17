# DB2ADMIN.SCORECARDDETAIL

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `SCORECARDHEADERCOMPANYCODE`, `SCORECARDHEADEREMPLOYEEIDCODE`, `SCORECARDHEADERSCRDATE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 160757

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SCORECARDHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SCORECARDHEADEREMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SCORECARDHEADERSCRDATE` | DATE | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `JOBKNOWLEDGE` | INTEGER | NOT NULL |  |  |  |
| 4 | `SPEED` | INTEGER | NOT NULL |  |  |  |
| 5 | `QUALITYOFWORK` | INTEGER | NOT NULL |  |  |  |
| 6 | `ATTITUDE` | INTEGER | NOT NULL |  |  |  |
| 7 | `PUNCTUALITY` | INTEGER | NOT NULL |  |  |  |
| 8 | `TEAMWORKER` | INTEGER | NOT NULL |  |  |  |
| 9 | `DEPENDABILITY` | INTEGER | NOT NULL |  |  |  |
| 10 | `ABILITY` | INTEGER | NOT NULL |  |  |  |
| 11 | `TOOLS` | INTEGER | NOT NULL |  |  |  |
| 12 | `REACTIONS` | INTEGER | NOT NULL |  |  |  |
| 13 | `DISCIPLINE` | INTEGER | NOT NULL |  |  |  |
| 14 | `DAMAGES` | INTEGER | NOT NULL |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `SCORECARDHEADER_LINE` | `SCORECARDHEADERCOMPANYCODE`, `SCORECARDHEADEREMPLOYEEIDCODE`, `SCORECARDHEADERSCRDATE` | [`SCORECARDHEADER`](../HR/SCORECARDHEADER.md) | `COMPANYCODE`, `EMPLOYEEIDCODE`, `SCRDATE` | RESTRICT | `SCORECARDDETAIL.SCORECARDHEADERCOMPANYCODE = SCORECARDHEADER.COMPANYCODE AND SCORECARDDETAIL.SCORECARDHEADEREMPLOYEEIDCODE = SCORECARDHEADER.EMPLOYEEIDCODE AND SCORECARDDETAIL.SCORECARDHEADERSCRDATE = SCORECARDHEADER.SCRDATE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SCORECARDDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SCORECARDHEADERCOMPANYCODE,
       t.SCORECARDHEADEREMPLOYEEIDCODE,
       t.SCORECARDHEADERSCRDATE,
       t.JOBKNOWLEDGE,
       t.SPEED,
       t.QUALITYOFWORK,
       t.ATTITUDE,
       t.PUNCTUALITY,
       t.TEAMWORKER,
       t.DEPENDABILITY,
       t.ABILITY,
       t.TOOLS
FROM   DB2ADMIN.SCORECARDDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
