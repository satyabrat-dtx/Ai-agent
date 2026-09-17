# DB2ADMIN.ABSUSERDIVISION

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `ABSUSERCOMPANYABSUSERDEFUSERID`, `ABSUSERCOMPANYCOMPANYCODE`, `DIVISIONCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 32384

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUSERCOMPANYABSUSERDEFUSERID` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ABSUSERCOMPANYCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 3 | `MAINDIVISION` | SMALLINT | NOT NULL |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSUSERCOMPANY_ALLOWEDDIVISIONS` | `ABSUSERCOMPANYABSUSERDEFUSERID`, `ABSUSERCOMPANYCOMPANYCODE` | [`ABSUSERCOMPANY`](../PLATFORM/ABSUSERCOMPANY.md) | `ABSUSERDEFUSERID`, `COMPANYCODE` | RESTRICT | `ABSUSERDIVISION.ABSUSERCOMPANYABSUSERDEFUSERID = ABSUSERCOMPANY.ABSUSERDEFUSERID AND ABSUSERDIVISION.ABSUSERCOMPANYCOMPANYCODE = ABSUSERCOMPANY.COMPANYCODE` |
| `DIVISION_DIVISION` | `ABSUSERCOMPANYCOMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ABSUSERDIVISION.ABSUSERCOMPANYCOMPANYCODE = DIVISION.COMPANYCODE AND ABSUSERDIVISION.DIVISIONCODE = DIVISION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSUSERDIVISIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSUSERCOMPANYABSUSERDEFUSERID,
       t.ABSUSERCOMPANYCOMPANYCODE,
       t.DIVISIONCODE,
       t.MAINDIVISION,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSUSERDIVISION t
FETCH FIRST 100 ROWS ONLY;
```
