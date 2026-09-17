# DB2ADMIN.RECIPEGROUP

- **Module**: `INTERNAL_ORDERS` (low confidence — FK neighbourhood: 1 of 1 related tables are INTERNAL_ORDERS)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 6 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 15484

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `LINETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 6 | `COMPONENTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `BASEVALUE` | DECIMAL(5,2) |  |  |  |  |
| 8 | `ROUNDINGBASE` | DECIMAL(5,2) |  |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RECIPEGROUP.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 6

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `RECIPEGROUP_GROUP1` | [`RECIPECHECKGROUP`](../INTERNAL_ORDERS/RECIPECHECKGROUP.md) | `COMPANYCODE`, `GROUP1CODE` | `RECIPECHECKGROUP.COMPANYCODE = RECIPEGROUP.COMPANYCODE AND RECIPECHECKGROUP.GROUP1CODE = RECIPEGROUP.CODE` |
| `RECIPEGROUP_GROUP2` | [`RECIPECHECKGROUP`](../INTERNAL_ORDERS/RECIPECHECKGROUP.md) | `COMPANYCODE`, `GROUP2CODE` | `RECIPECHECKGROUP.COMPANYCODE = RECIPEGROUP.COMPANYCODE AND RECIPECHECKGROUP.GROUP2CODE = RECIPEGROUP.CODE` |
| `RECIPEGROUP_GROUP3` | [`RECIPECHECKGROUP`](../INTERNAL_ORDERS/RECIPECHECKGROUP.md) | `COMPANYCODE`, `GROUP3CODE` | `RECIPECHECKGROUP.COMPANYCODE = RECIPEGROUP.COMPANYCODE AND RECIPECHECKGROUP.GROUP3CODE = RECIPEGROUP.CODE` |
| `RECIPEGROUP_GROUP4` | [`RECIPECHECKGROUP`](../INTERNAL_ORDERS/RECIPECHECKGROUP.md) | `COMPANYCODE`, `GROUP4CODE` | `RECIPECHECKGROUP.COMPANYCODE = RECIPEGROUP.COMPANYCODE AND RECIPECHECKGROUP.GROUP4CODE = RECIPEGROUP.CODE` |
| `RECIPEGROUP_GROUP5` | [`RECIPECHECKGROUP`](../INTERNAL_ORDERS/RECIPECHECKGROUP.md) | `COMPANYCODE`, `GROUP5CODE` | `RECIPECHECKGROUP.COMPANYCODE = RECIPEGROUP.COMPANYCODE AND RECIPECHECKGROUP.GROUP5CODE = RECIPEGROUP.CODE` |
| `RECIPEGROUP_GROUPTYPE` | [`RECIPECOMPONENT`](../INTERNAL_ORDERS/RECIPECOMPONENT.md) | `RECIPECOMPANYCODE`, `GROUPTYPECODE` | `RECIPECOMPONENT.RECIPECOMPANYCODE = RECIPEGROUP.COMPANYCODE AND RECIPECOMPONENT.GROUPTYPECODE = RECIPEGROUP.CODE` |

## Indexes

- `RECIPEGROUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.LINETYPE,
       t.COMPONENTITEMTYPECODE,
       t.BASEVALUE,
       t.ROUNDINGBASE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.RECIPEGROUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
