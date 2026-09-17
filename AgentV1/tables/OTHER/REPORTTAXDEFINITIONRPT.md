# DB2ADMIN.REPORTTAXDEFINITIONRPT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `REPORTTAXCOMPANYCODE`, `REPORTTAXDIVISIONCODE`, `REPORTTAXCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 123452

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `REPORTTAXCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `REPORTTAXDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `REPORTTAXCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `REPORTSABSUIXMLPATH` | CHAR(50) |  |  |  |  |
| 4 | `REPORTSABSUIXMLNAME` | VARCHAR(54) |  |  |  |  |
| 5 | `REPORTSCONTEXT` | CHAR(2) |  |  |  |  |
| 6 | `REPORTSREPORTCODE` | CHAR(50) |  |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `REPORTTAX_LINE1` | `REPORTTAXCOMPANYCODE`, `REPORTTAXDIVISIONCODE`, `REPORTTAXCODE` | [`REPORTTAX`](../OTHER/REPORTTAX.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `REPORTTAXDEFINITIONRPT.REPORTTAXCOMPANYCODE = REPORTTAX.COMPANYCODE AND REPORTTAXDEFINITIONRPT.REPORTTAXDIVISIONCODE = REPORTTAX.DIVISIONCODE AND REPORTTAXDEFINITIONRPT.REPORTTAXCODE = REPORTTAX.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `REPORTTAXDEFINITIONRPTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.REPORTTAXCOMPANYCODE,
       t.REPORTTAXDIVISIONCODE,
       t.REPORTTAXCODE,
       t.REPORTSABSUIXMLPATH,
       t.REPORTSABSUIXMLNAME,
       t.REPORTSCONTEXT,
       t.REPORTSREPORTCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.REPORTTAXDEFINITIONRPT t
FETCH FIRST 100 ROWS ONLY;
```
