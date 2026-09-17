# DB2ADMIN.IESATTRIBUTESUMMARY

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `INTERVIEWEVALSHEETCOMPANYCODE`, `INTERVIEWEVALSHEETCODE`, `INTERVIEWEVALSHEETAPPLNOCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 169928

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INTERVIEWEVALSHEETCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `INTERVIEWEVALSHEETCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `INTERVIEWEVALSHEETAPPLNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PERSONALITY` | INTEGER | NOT NULL |  |  |  |
| 4 | `ABILITY` | INTEGER | NOT NULL |  |  |  |
| 5 | `IESCHARACTER` | INTEGER | NOT NULL |  |  |  |
| 6 | `LEADERSHIP` | INTEGER | NOT NULL |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `INTERVIEWEVALSHEET_EVALSHEETRAT` | `INTERVIEWEVALSHEETCOMPANYCODE`, `INTERVIEWEVALSHEETCODE`, `INTERVIEWEVALSHEETAPPLNOCODE` | [`INTERVIEWEVALSHEET`](../HR/INTERVIEWEVALSHEET.md) | `COMPANYCODE`, `CODE`, `APPLNOCODE` | RESTRICT | `IESATTRIBUTESUMMARY.INTERVIEWEVALSHEETCOMPANYCODE = INTERVIEWEVALSHEET.COMPANYCODE AND IESATTRIBUTESUMMARY.INTERVIEWEVALSHEETCODE = INTERVIEWEVALSHEET.CODE AND IESATTRIBUTESUMMARY.INTERVIEWEVALSHEETAPPLNOCODE = INTERVIEWEVALSHEET.APPLNOCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `IESATTRIBUTESUMMARYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.INTERVIEWEVALSHEETCOMPANYCODE,
       t.INTERVIEWEVALSHEETCODE,
       t.INTERVIEWEVALSHEETAPPLNOCODE,
       t.PERSONALITY,
       t.ABILITY,
       t.IESCHARACTER,
       t.LEADERSHIP,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.IESATTRIBUTESUMMARY t
FETCH FIRST 100 ROWS ONLY;
```
