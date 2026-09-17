# DB2ADMIN.MANUFACTURER

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 1 of 1 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 5 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 5242

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `IMAGEPATH` | CHAR(30) |  |  |  |  |
| 6 | `IMAGENAME` | CHAR(50) |  |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `MANUFACTURER.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `MANUFACTURER.OWNINGCOMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 5

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `MANUFACTURER_MANUFACTURER` | [`NONINVENTORY`](../INTRASTAT/NONINVENTORY.md) | `MANUFACTURERCOMPANYCODE`, `MANUFACTURERCODE` | `NONINVENTORY.MANUFACTURERCOMPANYCODE = MANUFACTURER.COMPANYCODE AND NONINVENTORY.MANUFACTURERCODE = MANUFACTURER.CODE` |
| `MANUFACTURER_MANUFACTURER` | [`TOOL`](../CORE_MASTER/TOOL.md) | `MANUFACTURERCOMPANYCODE`, `MANUFACTURERCODE` | `TOOL.MANUFACTURERCOMPANYCODE = MANUFACTURER.COMPANYCODE AND TOOL.MANUFACTURERCODE = MANUFACTURER.CODE` |
| `MANUFACTURER_MANUFACTURER` | [`RESOURCES`](../PRODUCTION/RESOURCES.md) | `MANUFACTURERCOMPANYCODE`, `MANUFACTURERCODE` | `RESOURCES.MANUFACTURERCOMPANYCODE = MANUFACTURER.COMPANYCODE AND RESOURCES.MANUFACTURERCODE = MANUFACTURER.CODE` |
| `MANUFACTURER_MANUFACTURER` | [`PRODUCT`](../ITEM_MASTER/PRODUCT.md) | `MANUFACTURERCOMPANYCODE`, `MANUFACTURERCODE` | `PRODUCT.MANUFACTURERCOMPANYCODE = MANUFACTURER.COMPANYCODE AND PRODUCT.MANUFACTURERCODE = MANUFACTURER.CODE` |
| `MANUFACTURER_MANUFACTURER` | [`CONTAINER`](../CORE_MASTER/CONTAINER.md) | `MANUFACTURERCOMPANYCODE`, `MANUFACTURERCODE` | `CONTAINER.MANUFACTURERCOMPANYCODE = MANUFACTURER.COMPANYCODE AND CONTAINER.MANUFACTURERCODE = MANUFACTURER.CODE` |

## Indexes

- `MANUFACTURERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.IMAGEPATH,
       t.IMAGENAME,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.OWNINGCOMPANYCODE
FROM   DB2ADMIN.MANUFACTURER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
