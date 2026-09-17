# DB2ADMIN.ITDBILLS

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `INVESTMENTDECENTRYCOMPANYCODE`, `INVESTMENTDECEFINANCIALYEARCOD`, `INVESTMENTDECEEMPLOYEEIDCODE`, `INVESTMENTDECENTRYGROUPCODE`, `INVESTMENTDECEGROUPITEMCODE`, `SERIALNO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 166641

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INVESTMENTDECENTRYCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `INVESTMENTDECEFINANCIALYEARCOD` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `INVESTMENTDECEEMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `INVESTMENTDECENTRYGROUPCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `INVESTMENTDECEGROUPITEMCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `SERIALNO` | BIGINT | NOT NULL | PK | primary_key |  |
| 6 | `REFERENCENO` | CHAR(15) |  |  |  |  |
| 7 | `AMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 8 | `AUTHORIZEDFLAG` | INTEGER | NOT NULL |  |  |  |
| 9 | `SUMMARY` | CHAR(50) |  |  |  |  |
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
| `INVESTMENTDECENTRY_DETAIL` | `INVESTMENTDECENTRYCOMPANYCODE`, `INVESTMENTDECEFINANCIALYEARCOD`, `INVESTMENTDECEEMPLOYEEIDCODE`, `INVESTMENTDECENTRYGROUPCODE`, `INVESTMENTDECEGROUPITEMCODE` | [`INVESTMENTDECENTRY`](../HR/INVESTMENTDECENTRY.md) | `COMPANYCODE`, `FINANCIALYEARCODE`, `EMPLOYEEIDCODE`, `GROUPCODE`, `GROUPITEMCODE` | RESTRICT | `ITDBILLS.INVESTMENTDECENTRYCOMPANYCODE = INVESTMENTDECENTRY.COMPANYCODE AND ITDBILLS.INVESTMENTDECEFINANCIALYEARCOD = INVESTMENTDECENTRY.FINANCIALYEARCODE AND ITDBILLS.INVESTMENTDECEEMPLOYEEIDCODE = INVESTMENTDECENTRY.EMPLOYEEIDCODE AND ITDBILLS.INVESTMENTDECENTRYGROUPCODE = INVESTMENTDECENTRY.GROUPCODE AND ITDBILLS.INVESTMENTDECEGROUPITEMCODE = INVESTMENTDECENTRY.GROUPITEMCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ITDBILLSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.INVESTMENTDECENTRYCOMPANYCODE,
       t.INVESTMENTDECEFINANCIALYEARCOD,
       t.INVESTMENTDECEEMPLOYEEIDCODE,
       t.INVESTMENTDECENTRYGROUPCODE,
       t.INVESTMENTDECEGROUPITEMCODE,
       t.SERIALNO,
       t.REFERENCENO,
       t.AMOUNT,
       t.AUTHORIZEDFLAG,
       t.SUMMARY,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.ITDBILLS t
FETCH FIRST 100 ROWS ONLY;
```
