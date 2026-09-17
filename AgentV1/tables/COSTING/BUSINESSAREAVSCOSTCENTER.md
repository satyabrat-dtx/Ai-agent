# DB2ADMIN.BUSINESSAREAVSCOSTCENTER

- **Module**: `COSTING` (low confidence — FK neighbourhood: 1 of 1 related tables are COSTING)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `COMPANYCODE`, `BUSINESSAREACODE`, `EVENTCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 121378

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSAREACODE` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 2 | `EVENTCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `COSTCENTERCODE` | CHAR(20) |  | FK | foreign_key |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BUSINESSAREAVSCOSTCENTER.COMPANYCODE = COMPANY.CODE` |
| `COSTCENTER_COSTCENTER` | `COSTCENTERCOMPANYCODE`, `COSTCENTERCODE` | [`COSTCENTER`](../COSTING/COSTCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BUSINESSAREAVSCOSTCENTER.COSTCENTERCOMPANYCODE = COSTCENTER.COMPANYCODE AND BUSINESSAREAVSCOSTCENTER.COSTCENTERCODE = COSTCENTER.CODE` |
| `EVENTMASTER_EVENT` | `EVENTCODE` | [`EVENTMASTER`](../CORE_MASTER/EVENTMASTER.md) | `CODE` | RESTRICT | `BUSINESSAREAVSCOSTCENTER.EVENTCODE = EVENTMASTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BUSINESSAREAVSCOSTCENTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSAREACODE,
       t.EVENTCODE,
       t.COSTCENTERCOMPANYCODE,
       t.COSTCENTERCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.BUSINESSAREAVSCOSTCENTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
