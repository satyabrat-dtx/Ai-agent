# DB2ADMIN.MILAUTHUSERPRICELIST

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `COMPANYCODE`, `USERUSERID`, `STATISTICALGROUPCODE`, `COLLECTIONGROUPCODE`, `PRICELISTORDERTYPE`, `PRICELISTCODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 33426

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `USERUSERID` | CHAR(25) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `STATISTICALGROUPCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `COLLECTIONGROUPCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PRICELISTORDERTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `PRICELISTCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 10 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 11 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSUSERDEF_USER` | `USERUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `MILAUTHUSERPRICELIST.USERUSERID = ABSUSERDEF.USERID` |
| `COLLECTIONGROUP_COLLECTIONGROUP` | `COLLECTIONGROUPCOMPANYCODE`, `COLLECTIONGROUPCODE` | [`COLLECTIONGROUP`](../CORE_MASTER/COLLECTIONGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MILAUTHUSERPRICELIST.COLLECTIONGROUPCOMPANYCODE = COLLECTIONGROUP.COMPANYCODE AND MILAUTHUSERPRICELIST.COLLECTIONGROUPCODE = COLLECTIONGROUP.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `MILAUTHUSERPRICELIST.COMPANYCODE = COMPANY.CODE` |
| `PRICELIST_PRICELIST` | `COMPANYCODE`, `PRICELISTORDERTYPE`, `PRICELISTCODE` | [`PRICELIST`](../SALES/PRICELIST.md) | `COMPANYCODE`, `ORDERTYPE`, `CODE` | RESTRICT | `MILAUTHUSERPRICELIST.COMPANYCODE = PRICELIST.COMPANYCODE AND MILAUTHUSERPRICELIST.PRICELISTORDERTYPE = PRICELIST.ORDERTYPE AND MILAUTHUSERPRICELIST.PRICELISTCODE = PRICELIST.CODE` |
| `STATISTICALGROUP_STATISTICALGROUP` | `STATISTICALGROUPCOMPANYCODE`, `STATISTICALGROUPCODE` | [`STATISTICALGROUP`](../CORE_MASTER/STATISTICALGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MILAUTHUSERPRICELIST.STATISTICALGROUPCOMPANYCODE = STATISTICALGROUP.COMPANYCODE AND MILAUTHUSERPRICELIST.STATISTICALGROUPCODE = STATISTICALGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MILAUTHUSERPRICELISTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.USERUSERID,
       t.STATISTICALGROUPCODE,
       t.COLLECTIONGROUPCODE,
       t.PRICELISTORDERTYPE,
       t.PRICELISTCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.STATISTICALGROUPCOMPANYCODE,
       t.COLLECTIONGROUPCOMPANYCODE
FROM   DB2ADMIN.MILAUTHUSERPRICELIST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
