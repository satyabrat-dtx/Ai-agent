# DB2ADMIN.KRAFORMADEVNEEDS

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `KRAHEADERCOMPANYCODE`, `KRAHEADEREMPLOYEEIDCODE`, `KRAHEADERAPPCALCODEAPPCALCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 157667

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `KRAHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `KRAHEADEREMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `KRAHEADERAPPCALCODEAPPCALCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `STRENGTHS` | CHAR(50) |  |  |  |  |
| 4 | `AREASFORIMPRV` | CHAR(50) |  |  |  |  |
| 5 | `TRNNEEDS` | CHAR(50) |  |  |  |  |
| 6 | `GROWTHAREAS` | CHAR(50) |  |  |  |  |
| 7 | `PERDEVPLAN` | CHAR(50) |  |  |  |  |
| 8 | `CAREERGROWTH` | CHAR(50) |  |  |  |  |
| 9 | `REMARKS` | CHAR(50) |  |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `KRAHEADER_LINE2` | `KRAHEADERCOMPANYCODE`, `KRAHEADEREMPLOYEEIDCODE`, `KRAHEADERAPPCALCODEAPPCALCODE` | [`KRAHEADER`](../HR/KRAHEADER.md) | `COMPANYCODE`, `EMPLOYEEIDCODE`, `APPCALCODEAPPCALCODE` | RESTRICT | `KRAFORMADEVNEEDS.KRAHEADERCOMPANYCODE = KRAHEADER.COMPANYCODE AND KRAFORMADEVNEEDS.KRAHEADEREMPLOYEEIDCODE = KRAHEADER.EMPLOYEEIDCODE AND KRAFORMADEVNEEDS.KRAHEADERAPPCALCODEAPPCALCODE = KRAHEADER.APPCALCODEAPPCALCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `KRAFORMADEVNEEDSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.KRAHEADERCOMPANYCODE,
       t.KRAHEADEREMPLOYEEIDCODE,
       t.KRAHEADERAPPCALCODEAPPCALCODE,
       t.STRENGTHS,
       t.AREASFORIMPRV,
       t.TRNNEEDS,
       t.GROWTHAREAS,
       t.PERDEVPLAN,
       t.CAREERGROWTH,
       t.REMARKS,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.KRAFORMADEVNEEDS t
FETCH FIRST 100 ROWS ONLY;
```
