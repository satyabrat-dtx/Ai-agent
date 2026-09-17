# DB2ADMIN.RECIPECHECKGROUP

- **Module**: `INTERNAL_ORDERS` (low confidence — FK neighbourhood: 1 of 1 related tables are INTERNAL_ORDERS)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 14554

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `GROUP1CODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `GROUP2CODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `GROUP3CODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `GROUP4CODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `GROUP5CODE` | CHAR(3) |  | FK | foreign_key |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RECIPECHECKGROUP.COMPANYCODE = COMPANY.CODE` |
| `RECIPEGROUP_GROUP1` | `COMPANYCODE`, `GROUP1CODE` | [`RECIPEGROUP`](../INTERNAL_ORDERS/RECIPEGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPECHECKGROUP.COMPANYCODE = RECIPEGROUP.COMPANYCODE AND RECIPECHECKGROUP.GROUP1CODE = RECIPEGROUP.CODE` |
| `RECIPEGROUP_GROUP2` | `COMPANYCODE`, `GROUP2CODE` | [`RECIPEGROUP`](../INTERNAL_ORDERS/RECIPEGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPECHECKGROUP.COMPANYCODE = RECIPEGROUP.COMPANYCODE AND RECIPECHECKGROUP.GROUP2CODE = RECIPEGROUP.CODE` |
| `RECIPEGROUP_GROUP3` | `COMPANYCODE`, `GROUP3CODE` | [`RECIPEGROUP`](../INTERNAL_ORDERS/RECIPEGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPECHECKGROUP.COMPANYCODE = RECIPEGROUP.COMPANYCODE AND RECIPECHECKGROUP.GROUP3CODE = RECIPEGROUP.CODE` |
| `RECIPEGROUP_GROUP4` | `COMPANYCODE`, `GROUP4CODE` | [`RECIPEGROUP`](../INTERNAL_ORDERS/RECIPEGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPECHECKGROUP.COMPANYCODE = RECIPEGROUP.COMPANYCODE AND RECIPECHECKGROUP.GROUP4CODE = RECIPEGROUP.CODE` |
| `RECIPEGROUP_GROUP5` | `COMPANYCODE`, `GROUP5CODE` | [`RECIPEGROUP`](../INTERNAL_ORDERS/RECIPEGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RECIPECHECKGROUP.COMPANYCODE = RECIPEGROUP.COMPANYCODE AND RECIPECHECKGROUP.GROUP5CODE = RECIPEGROUP.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `RECIPECHECKGROUP_CHECKGROUP` | [`RECIPETEMPLATE`](../OTHER/RECIPETEMPLATE.md) | `COMPANYCODE`, `CHECKGROUPCODE` | `RECIPETEMPLATE.COMPANYCODE = RECIPECHECKGROUP.COMPANYCODE AND RECIPETEMPLATE.CHECKGROUPCODE = RECIPECHECKGROUP.CODE` |

## Indexes

- `RECIPECHECKGROUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.GROUP1CODE,
       t.GROUP2CODE,
       t.GROUP3CODE,
       t.GROUP4CODE,
       t.GROUP5CODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.RECIPECHECKGROUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
