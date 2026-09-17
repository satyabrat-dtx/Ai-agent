# DB2ADMIN.KRAFORMAPD

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `KRAHEADERCOMPANYCODE`, `KRAHEADEREMPLOYEEIDCODE`, `KRAHEADERAPPCALCODEAPPCALCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 157715

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `KRAHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `KRAHEADEREMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `KRAHEADERAPPCALCODEAPPCALCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `BUSINESSPLAN` | CHAR(20) |  |  |  |  |
| 4 | `KRASJOBOBJECT` | CHAR(50) |  |  |  |  |
| 5 | `RATESELF` | INTEGER | NOT NULL |  |  |  |
| 6 | `RATEREVIEWER` | INTEGER | NOT NULL |  |  |  |
| 7 | `RATEAPPROVER` | INTEGER | NOT NULL |  |  |  |
| 8 | `REMARKS` | CHAR(20) |  |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `KRAHEADER_LINE` | `KRAHEADERCOMPANYCODE`, `KRAHEADEREMPLOYEEIDCODE`, `KRAHEADERAPPCALCODEAPPCALCODE` | [`KRAHEADER`](../HR/KRAHEADER.md) | `COMPANYCODE`, `EMPLOYEEIDCODE`, `APPCALCODEAPPCALCODE` | RESTRICT | `KRAFORMAPD.KRAHEADERCOMPANYCODE = KRAHEADER.COMPANYCODE AND KRAFORMAPD.KRAHEADEREMPLOYEEIDCODE = KRAHEADER.EMPLOYEEIDCODE AND KRAFORMAPD.KRAHEADERAPPCALCODEAPPCALCODE = KRAHEADER.APPCALCODEAPPCALCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `KRAFORMAPDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.KRAHEADERCOMPANYCODE,
       t.KRAHEADEREMPLOYEEIDCODE,
       t.KRAHEADERAPPCALCODEAPPCALCODE,
       t.BUSINESSPLAN,
       t.KRASJOBOBJECT,
       t.RATESELF,
       t.RATEREVIEWER,
       t.RATEAPPROVER,
       t.REMARKS,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.KRAFORMAPD t
FETCH FIRST 100 ROWS ONLY;
```
