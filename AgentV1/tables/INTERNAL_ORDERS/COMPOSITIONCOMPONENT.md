# DB2ADMIN.COMPOSITIONCOMPONENT

- **Module**: `INTERNAL_ORDERS` (low confidence — FK neighbourhood: 1 of 1 related tables are INTERNAL_ORDERS)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 27899

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `COMPOSITIONCOMPONENT.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `COMPOSITIONCOMPONENT.OWNINGCOMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `COMPOSITIONCOMPONENT_COMPOSITIONCOMPONENT` | [`RECIPECOMPONENT`](../INTERNAL_ORDERS/RECIPECOMPONENT.md) | `COMPOSITIONCMPCOMPANYCODE`, `COMPOSITIONCOMPONENTCODE` | `RECIPECOMPONENT.COMPOSITIONCMPCOMPANYCODE = COMPOSITIONCOMPONENT.COMPANYCODE AND RECIPECOMPONENT.COMPOSITIONCOMPONENTCODE = COMPOSITIONCOMPONENT.CODE` |
| `COMPOSITIONCOMPONENT_COMPOSITIONDETAIL` | [`SIONDETAIL`](../INTERNAL_ORDERS/SIONDETAIL.md) | `COMPOSITIONDETAILCOMPANYCODE`, `COMPOSITIONDETAILCODE` | `SIONDETAIL.COMPOSITIONDETAILCOMPANYCODE = COMPOSITIONCOMPONENT.COMPANYCODE AND SIONDETAIL.COMPOSITIONDETAILCODE = COMPOSITIONCOMPONENT.CODE` |
| `COMPOSITIONCOMPONENT_COMPOSITIONDETAIL` | [`ADVSIONDETAIL`](../OTHER/ADVSIONDETAIL.md) | `COMPOSITIONDETAILCOMPANYCODE`, `COMPOSITIONDETAILCODE` | `ADVSIONDETAIL.COMPOSITIONDETAILCOMPANYCODE = COMPOSITIONCOMPONENT.COMPANYCODE AND ADVSIONDETAIL.COMPOSITIONDETAILCODE = COMPOSITIONCOMPONENT.CODE` |

## Indexes

- `COMPOSITIONCOMPONENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.OWNINGCOMPANYCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.COMPOSITIONCOMPONENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
