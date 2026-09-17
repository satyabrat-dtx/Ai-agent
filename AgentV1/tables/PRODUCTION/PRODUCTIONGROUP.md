# DB2ADMIN.PRODUCTIONGROUP

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 21022

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRODUCTIONGROUP.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRODUCTIONGROUP.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIONGROUP.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND PRODUCTIONGROUP.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PRODUCTIONGROUP_PRODUCTIONGROUP` | [`PRODUCT`](../ITEM_MASTER/PRODUCT.md) | `PRODUCTIONGROUPCOMPANYCODE`, `ITEMTYPECODE`, `PRODUCTIONGROUPCODE` | `PRODUCT.PRODUCTIONGROUPCOMPANYCODE = PRODUCTIONGROUP.COMPANYCODE AND PRODUCT.ITEMTYPECODE = PRODUCTIONGROUP.ITEMTYPECODE AND PRODUCT.PRODUCTIONGROUPCODE = PRODUCTIONGROUP.CODE` |
| `PRODUCTIONGROUP_PRODUCTIONGROUP` | [`ITEMTYPECUSTOMIZEDOPTIONS`](../CORE_MASTER/ITEMTYPECUSTOMIZEDOPTIONS.md) | `PRODUCTIONGROUPCOMPANYCODE`, `ITEMTYPECODE`, `PRODUCTIONGROUPCODE` | `ITEMTYPECUSTOMIZEDOPTIONS.PRODUCTIONGROUPCOMPANYCODE = PRODUCTIONGROUP.COMPANYCODE AND ITEMTYPECUSTOMIZEDOPTIONS.ITEMTYPECODE = PRODUCTIONGROUP.ITEMTYPECODE AND ITEMTYPECUSTOMIZEDOPTIONS.PRODUCTIONGROUPCODE = PRODUCTIONGROUP.CODE` |
| `PRODUCTIONGROUP_PRODUCTIONGROUP` | [`PRODUCTIONDEMAND`](../PRODUCTION/PRODUCTIONDEMAND.md) | `PRODUCTIONGROUPCOMPANYCODE`, `ITEMTYPEAFICODE`, `PRODUCTIONGROUPCODE` | `PRODUCTIONDEMAND.PRODUCTIONGROUPCOMPANYCODE = PRODUCTIONGROUP.COMPANYCODE AND PRODUCTIONDEMAND.ITEMTYPEAFICODE = PRODUCTIONGROUP.ITEMTYPECODE AND PRODUCTIONDEMAND.PRODUCTIONGROUPCODE = PRODUCTIONGROUP.CODE` |

## Indexes

- `PRODUCTIONGROUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.ITEMTYPECOMPANYCODE
FROM   DB2ADMIN.PRODUCTIONGROUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
