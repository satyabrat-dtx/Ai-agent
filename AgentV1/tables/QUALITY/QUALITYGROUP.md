# DB2ADMIN.QUALITYGROUP

- **Module**: `QUALITY` (high confidence — table name starts with 'QUALITY')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 3495

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `LOTEXPIRATIONDAYS` | INTEGER | NOT NULL |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `QUALITYGROUP.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `QUALITYGROUP.OWNINGCOMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `QUALITYGROUP_QUALITYGROUP` | [`PRODUCT`](../ITEM_MASTER/PRODUCT.md) | `QUALITYGROUPCOMPANYCODE`, `QUALITYGROUPCODE` | `PRODUCT.QUALITYGROUPCOMPANYCODE = QUALITYGROUP.COMPANYCODE AND PRODUCT.QUALITYGROUPCODE = QUALITYGROUP.CODE` |
| `QUALITYGROUP_QUALITYGROUP` | [`ITEMTYPECUSTOMIZEDOPTIONS`](../CORE_MASTER/ITEMTYPECUSTOMIZEDOPTIONS.md) | `QUALITYGROUPCOMPANYCODE`, `QUALITYGROUPCODE` | `ITEMTYPECUSTOMIZEDOPTIONS.QUALITYGROUPCOMPANYCODE = QUALITYGROUP.COMPANYCODE AND ITEMTYPECUSTOMIZEDOPTIONS.QUALITYGROUPCODE = QUALITYGROUP.CODE` |
| `QUALITYGROUP_QUALITYGROUP` | [`NETFATHERCHILDITEMTYPEIE`](../LOCALIZATION/NETFATHERCHILDITEMTYPEIE.md) | `QUALITYGROUPCOMPANYCODE`, `QUALITYGROUPCODE` | `NETFATHERCHILDITEMTYPEIE.QUALITYGROUPCOMPANYCODE = QUALITYGROUP.COMPANYCODE AND NETFATHERCHILDITEMTYPEIE.QUALITYGROUPCODE = QUALITYGROUP.CODE` |

## Indexes

- `QUALITYGROUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.LOTEXPIRATIONDAYS,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.OWNINGCOMPANYCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.QUALITYGROUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
