# DB2ADMIN.USACOSTCENTERGROUP

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `COMPANYCODE`, `GROUPCODE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 107661

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `GROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `DESCRIPTION` | CHAR(30) |  |  | description |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `USACOSTCENTERGROUP.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `USACOSTCENTERGROUP_COSTCENTER` | [`USACOSTCENTERGROUPDETAIL`](../LOCALIZATION/USACOSTCENTERGROUPDETAIL.md) | `USACOSTCENTERGROUPCOMPANYCODE`, `USACOSTCENTERGROUPGROUPCODE` | `USACOSTCENTERGROUPDETAIL.USACOSTCENTERGROUPCOMPANYCODE = USACOSTCENTERGROUP.COMPANYCODE AND USACOSTCENTERGROUPDETAIL.USACOSTCENTERGROUPGROUPCODE = USACOSTCENTERGROUP.GROUPCODE` |

## Indexes

- `USACOSTCENTERGROUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.GROUPCODE,
       t.DESCRIPTION,
       t.ABSUNIQUEID
FROM   DB2ADMIN.USACOSTCENTERGROUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
