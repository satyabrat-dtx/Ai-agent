# DB2ADMIN.IESATTRIBUTERATING

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 29
- **Primary key**: `INTERVIEWEVALSHEETCOMPANYCODE`, `INTERVIEWEVALSHEETCODE`, `INTERVIEWEVALSHEETAPPLNOCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 169868

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INTERVIEWEVALSHEETCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `INTERVIEWEVALSHEETCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `INTERVIEWEVALSHEETAPPLNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `FAMILYBCKGROUND` | INTEGER | NOT NULL |  |  |  |
| 4 | `PHYSICALOUTLOOK` | INTEGER | NOT NULL |  |  |  |
| 5 | `JOBKNOW` | INTEGER | NOT NULL |  |  |  |
| 6 | `FUNCTIONALKNOW` | INTEGER | NOT NULL |  |  |  |
| 7 | `COMMSKILL` | INTEGER | NOT NULL |  |  |  |
| 8 | `HOUSEKEEPING` | INTEGER | NOT NULL |  |  |  |
| 9 | `ADAPTIBILITY` | INTEGER | NOT NULL |  |  |  |
| 10 | `ENGLANGUAGE` | INTEGER | NOT NULL |  |  |  |
| 11 | `AMBITION` | INTEGER | NOT NULL |  |  |  |
| 12 | `INITIATIVE` | INTEGER | NOT NULL |  |  |  |
| 13 | `TEAMSKILLS` | INTEGER | NOT NULL |  |  |  |
| 14 | `ATTITUDE` | INTEGER | NOT NULL |  |  |  |
| 15 | `MULTISKILLABILITIES` | INTEGER | NOT NULL |  |  |  |
| 16 | `CONFIDENCE` | INTEGER | NOT NULL |  |  |  |
| 17 | `BOLDNESS` | INTEGER | NOT NULL |  |  |  |
| 18 | `PROBLEMSOLVING` | INTEGER | NOT NULL |  |  |  |
| 19 | `HONESTY` | INTEGER | NOT NULL |  |  |  |
| 20 | `RESPONSIBLE` | INTEGER | NOT NULL |  |  |  |
| 21 | `HARDWORKING` | INTEGER | NOT NULL |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 27 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 28 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `INTERVIEWEVALSHEET_EVALSHEETATT` | `INTERVIEWEVALSHEETCOMPANYCODE`, `INTERVIEWEVALSHEETCODE`, `INTERVIEWEVALSHEETAPPLNOCODE` | [`INTERVIEWEVALSHEET`](../HR/INTERVIEWEVALSHEET.md) | `COMPANYCODE`, `CODE`, `APPLNOCODE` | RESTRICT | `IESATTRIBUTERATING.INTERVIEWEVALSHEETCOMPANYCODE = INTERVIEWEVALSHEET.COMPANYCODE AND IESATTRIBUTERATING.INTERVIEWEVALSHEETCODE = INTERVIEWEVALSHEET.CODE AND IESATTRIBUTERATING.INTERVIEWEVALSHEETAPPLNOCODE = INTERVIEWEVALSHEET.APPLNOCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `IESATTRIBUTERATINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.INTERVIEWEVALSHEETCOMPANYCODE,
       t.INTERVIEWEVALSHEETCODE,
       t.INTERVIEWEVALSHEETAPPLNOCODE,
       t.FAMILYBCKGROUND,
       t.PHYSICALOUTLOOK,
       t.JOBKNOW,
       t.FUNCTIONALKNOW,
       t.COMMSKILL,
       t.HOUSEKEEPING,
       t.ADAPTIBILITY,
       t.ENGLANGUAGE,
       t.AMBITION
FROM   DB2ADMIN.IESATTRIBUTERATING t
FETCH FIRST 100 ROWS ONLY;
```
