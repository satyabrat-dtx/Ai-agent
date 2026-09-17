# DB2ADMIN.SCORECARDHEADER

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `EMPLOYEEIDCODE`, `SCRDATE`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 160810

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SCRDATE` | DATE | NOT NULL | PK | primary_key |  |
| 3 | `PERIODOFREVIEW` | CHAR(20) |  |  |  |  |
| 4 | `TOTALSCORE` | INTEGER | NOT NULL |  |  |  |
| 5 | `REVIEWDONEBYCODE` | CHAR(9) |  | FK | foreign_key |  |
| 6 | `APPROVEDBYCODE` | CHAR(9) |  | FK | foreign_key |  |
| 7 | `APPDATE` | DATE |  |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EMPLOYEE_APPROVEDBY` | `COMPANYCODE`, `APPROVEDBYCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SCORECARDHEADER.COMPANYCODE = EMPLOYEE.COMPANYCODE AND SCORECARDHEADER.APPROVEDBYCODE = EMPLOYEE.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SCORECARDHEADER.COMPANYCODE = EMPLOYEE.COMPANYCODE AND SCORECARDHEADER.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `EMPLOYEE_REVIEWDONEBY` | `COMPANYCODE`, `REVIEWDONEBYCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SCORECARDHEADER.COMPANYCODE = EMPLOYEE.COMPANYCODE AND SCORECARDHEADER.REVIEWDONEBYCODE = EMPLOYEE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SCORECARDHEADER_LINE` | [`SCORECARDDETAIL`](../HR/SCORECARDDETAIL.md) | `SCORECARDHEADERCOMPANYCODE`, `SCORECARDHEADEREMPLOYEEIDCODE`, `SCORECARDHEADERSCRDATE` | `SCORECARDDETAIL.SCORECARDHEADERCOMPANYCODE = SCORECARDHEADER.COMPANYCODE AND SCORECARDDETAIL.SCORECARDHEADEREMPLOYEEIDCODE = SCORECARDHEADER.EMPLOYEEIDCODE AND SCORECARDDETAIL.SCORECARDHEADERSCRDATE = SCORECARDHEADER.SCRDATE` |

## Indexes

- `SCORECARDHEADERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.SCRDATE,
       t.PERIODOFREVIEW,
       t.TOTALSCORE,
       t.REVIEWDONEBYCODE,
       t.APPROVEDBYCODE,
       t.APPDATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.SCORECARDHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
