# DB2ADMIN.ADDITIONALDATAAUTH

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `COMPANYCODE`, `ADENTITYNAME`, `ADNAME`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 31310

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ADENTITYNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 2 | `ADNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `ADGROUPCODE` | CHAR(15) |  | FK | foreign_key |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADDITIONALDATAAUTHGROUP_ADGROUP` | `COMPANYCODE`, `ADGROUPCODE` | [`ADDITIONALDATAAUTHGROUP`](../OTHER/ADDITIONALDATAAUTHGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ADDITIONALDATAAUTH.COMPANYCODE = ADDITIONALDATAAUTHGROUP.COMPANYCODE AND ADDITIONALDATAAUTH.ADGROUPCODE = ADDITIONALDATAAUTHGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ADDITIONALDATAAUTHUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ADENTITYNAME,
       t.ADNAME,
       t.ADGROUPCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ADDITIONALDATAAUTH t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
