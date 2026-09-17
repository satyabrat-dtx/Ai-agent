# DB2ADMIN.NUMBEROFMACHINESQUANTITIES

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 1 of 1 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`, `CODE`, `UPTOQUANITY`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 211722

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `UPTOQUANITY` | DECIMAL(15,5) | NOT NULL | PK | primary_key |  |
| 4 | `NUMBEROFMACHINES` | DECIMAL(3,0) |  |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 6 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `NUMBEROFMACHINESQUANTITIES.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `NUMBEROFMACHINESSET_NUMBEROFMACHINESQUANTITIES` | `COMPANYCODE`, `ITEMTYPECODE`, `CODE` | [`NUMBEROFMACHINESSET`](../ITEM_MASTER/NUMBEROFMACHINESSET.md) | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE`, `CODE` | RESTRICT | `NUMBEROFMACHINESQUANTITIES.COMPANYCODE = NUMBEROFMACHINESSET.ITEMTYPECOMPANYCODE AND NUMBEROFMACHINESQUANTITIES.ITEMTYPECODE = NUMBEROFMACHINESSET.ITEMTYPECODE AND NUMBEROFMACHINESQUANTITIES.CODE = NUMBEROFMACHINESSET.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `NUMBEROFMACHINESQUANTITIESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.CODE,
       t.UPTOQUANITY,
       t.NUMBEROFMACHINES,
       t.ABSUNIQUEID,
       t.OWNINGCOMPANYCODE
FROM   DB2ADMIN.NUMBEROFMACHINESQUANTITIES t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
