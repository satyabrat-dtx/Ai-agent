# DB2ADMIN.WORKCENTERDAILYCAPACITY

- **Module**: `PRODUCTION` (high confidence — table name starts with 'WORKCENTER')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `COMPANYCODE`, `WORKCENTERCODE`, `CALENDARDATE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 212134

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `WORKCENTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CALENDARDATE` | DATE | NOT NULL | PK | primary_key |  |
| 3 | `WORKINGHOURS` | DECIMAL(10,5) |  |  |  |  |
| 4 | `BUSYHOURS` | DECIMAL(10,5) |  |  |  |  |
| 5 | `STOPPEDHOURS` | DECIMAL(10,5) |  |  |  |  |
| 6 | `ADDITIONALHOURS` | DECIMAL(10,5) |  |  |  |  |
| 7 | `EXCLUDEDHOURSCHECKOVERCAPACITY` | DECIMAL(10,5) |  |  |  |  |
| 8 | `NOTES` | VARCHAR(200) |  |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `WORKCENTERDAILYCAPACITY.COMPANYCODE = COMPANY.CODE` |
| `WORKCENTER_WORKCENTER` | `COMPANYCODE`, `WORKCENTERCODE` | [`WORKCENTER`](../PRODUCTION/WORKCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WORKCENTERDAILYCAPACITY.COMPANYCODE = WORKCENTER.COMPANYCODE AND WORKCENTERDAILYCAPACITY.WORKCENTERCODE = WORKCENTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WORKCENTERDAILYCAPACITYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.WORKCENTERCODE,
       t.CALENDARDATE,
       t.WORKINGHOURS,
       t.BUSYHOURS,
       t.STOPPEDHOURS,
       t.ADDITIONALHOURS,
       t.EXCLUDEDHOURSCHECKOVERCAPACITY,
       t.NOTES,
       t.ABSUNIQUEID
FROM   DB2ADMIN.WORKCENTERDAILYCAPACITY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
