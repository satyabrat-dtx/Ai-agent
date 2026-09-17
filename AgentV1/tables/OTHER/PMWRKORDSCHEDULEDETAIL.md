# DB2ADMIN.PMWRKORDSCHEDULEDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `COMPANYCODE`, `PMWORKORDERCOUNTERCODE`, `PMWORKORDERCODE`, `SCHEDULEID`, `LINEID`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 108899

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PMWORKORDERCOUNTERCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `PMWORKORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PMWORKORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `SCHEDULEID` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `LINEID` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `SCHEDULEDATE` | DATE |  |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PMWRKORDSCHEDULEDETAIL.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_PMWORKORDERCOUNTER` | `PMWORKORDERCOUNTERCOMPANYCODE`, `PMWORKORDERCOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMWRKORDSCHEDULEDETAIL.PMWORKORDERCOUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND PMWRKORDSCHEDULEDETAIL.PMWORKORDERCOUNTERCODE = COUNTER.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PMWRKORDSCHEDULEDETAIL_LINEID` | [`PMSCHEDULING`](../OTHER/PMSCHEDULING.md) | `COMPANYCODE`, `LINEIDPMWORKORDERCOUNTERCODE`, `LINEIDPMWORKORDERCODE`, `LINEIDSCHEDULEID`, `LINEIDLINEID` | `PMSCHEDULING.COMPANYCODE = PMWRKORDSCHEDULEDETAIL.COMPANYCODE AND PMSCHEDULING.LINEIDPMWORKORDERCOUNTERCODE = PMWRKORDSCHEDULEDETAIL.PMWORKORDERCOUNTERCODE AND PMSCHEDULING.LINEIDPMWORKORDERCODE = PMWRKORDSCHEDULEDETAIL.PMWORKORDERCODE AND PMSCHEDULING.LINEIDSCHEDULEID = PMWRKORDSCHEDULEDETAIL.SCHEDULEID AND PMSCHEDULING.LINEIDLINEID = PMWRKORDSCHEDULEDETAIL.LINEID` |

## Indexes

- `PMWRKORDSCHEDULEDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PMWORKORDERCOUNTERCOMPANYCODE,
       t.PMWORKORDERCOUNTERCODE,
       t.PMWORKORDERCODE,
       t.SCHEDULEID,
       t.LINEID,
       t.SCHEDULEDATE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PMWRKORDSCHEDULEDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
