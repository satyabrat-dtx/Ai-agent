# DB2ADMIN.FINCSFI8REPORTS

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `FINCSFI8COMPANYCODE`, `FINCSFI8DIVISIONCODE`, `FINCSFI8URSRID`, `URSRREPREPID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 103903

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINCSFI8COMPANYCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINCSFI8DIVISIONCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FINCSFI8URSRID` | CHAR(12) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `URSRREPREPID` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINCSFI8_URSRREP` | `FINCSFI8COMPANYCODE`, `FINCSFI8DIVISIONCODE`, `FINCSFI8URSRID` | [`FINCSFI8`](../FINANCE/FINCSFI8.md) | `COMPANYCODE`, `DIVISIONCODE`, `URSRID` | RESTRICT | `FINCSFI8REPORTS.FINCSFI8COMPANYCODE = FINCSFI8.COMPANYCODE AND FINCSFI8REPORTS.FINCSFI8DIVISIONCODE = FINCSFI8.DIVISIONCODE AND FINCSFI8REPORTS.FINCSFI8URSRID = FINCSFI8.URSRID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINCSFI8REPORTSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINCSFI8COMPANYCODE,
       t.FINCSFI8DIVISIONCODE,
       t.FINCSFI8URSRID,
       t.URSRREPREPID,
       t.ABSUNIQUEID
FROM   DB2ADMIN.FINCSFI8REPORTS t
FETCH FIRST 100 ROWS ONLY;
```
