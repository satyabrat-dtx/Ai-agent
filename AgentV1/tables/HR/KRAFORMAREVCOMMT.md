# DB2ADMIN.KRAFORMAREVCOMMT

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `KRAHEADERCOMPANYCODE`, `KRAHEADEREMPLOYEEIDCODE`, `KRAHEADERAPPCALCODEAPPCALCODE`, `EMPLOYEEIDCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 157809

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `KRAHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `KRAHEADEREMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `KRAHEADERAPPCALCODEAPPCALCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `RATINGOFAPP` | INTEGER | NOT NULL |  |  |  |
| 5 | `COMMENTS` | CHAR(50) |  |  |  |  |
| 6 | `RECOMMANDATIONS` | CHAR(50) |  |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EMPLOYEE_EMPLOYEEID` | `KRAHEADERCOMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `KRAFORMAREVCOMMT.KRAHEADERCOMPANYCODE = EMPLOYEE.COMPANYCODE AND KRAFORMAREVCOMMT.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `KRAHEADER_LINE4` | `KRAHEADERCOMPANYCODE`, `KRAHEADEREMPLOYEEIDCODE`, `KRAHEADERAPPCALCODEAPPCALCODE` | [`KRAHEADER`](../HR/KRAHEADER.md) | `COMPANYCODE`, `EMPLOYEEIDCODE`, `APPCALCODEAPPCALCODE` | RESTRICT | `KRAFORMAREVCOMMT.KRAHEADERCOMPANYCODE = KRAHEADER.COMPANYCODE AND KRAFORMAREVCOMMT.KRAHEADEREMPLOYEEIDCODE = KRAHEADER.EMPLOYEEIDCODE AND KRAFORMAREVCOMMT.KRAHEADERAPPCALCODEAPPCALCODE = KRAHEADER.APPCALCODEAPPCALCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `KRAFORMAREVCOMMTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.KRAHEADERCOMPANYCODE,
       t.KRAHEADEREMPLOYEEIDCODE,
       t.KRAHEADERAPPCALCODEAPPCALCODE,
       t.EMPLOYEEIDCODE,
       t.RATINGOFAPP,
       t.COMMENTS,
       t.RECOMMANDATIONS,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.KRAFORMAREVCOMMT t
FETCH FIRST 100 ROWS ONLY;
```
