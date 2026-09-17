# DB2ADMIN.PRODUCTGROUPFAMILY

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'PRODUCT')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 5 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 15901

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `FAMILYNATURE` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `REPARTITIONQUANTITYARTICLE` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `INITIALSCODE` | CHAR(50) |  | FK | foreign_key |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `INITIALSCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRODUCTGROUPFAMILY.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRODUCTGROUPFAMILY.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `INITIALS_INITIALS` | `INITIALSCOMPANYCODE`, `INITIALSCODE` | [`INITIALS`](../CORE_MASTER/INITIALS.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTGROUPFAMILY.INITIALSCOMPANYCODE = INITIALS.COMPANYCODE AND PRODUCTGROUPFAMILY.INITIALSCODE = INITIALS.CODE` |

## Referenced by (child → this table) — 5

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PRODUCTGROUPFAMILY_FAMILYGRP` | [`TOOL`](../CORE_MASTER/TOOL.md) | `FAMILYGRPCOMPANYCODE`, `FAMILYGRPCODE` | `TOOL.FAMILYGRPCOMPANYCODE = PRODUCTGROUPFAMILY.COMPANYCODE AND TOOL.FAMILYGRPCODE = PRODUCTGROUPFAMILY.CODE` |
| `PRODUCTGROUPFAMILY_FAMILYGRP` | [`PRODUCT`](../ITEM_MASTER/PRODUCT.md) | `FAMILYGRPCOMPANYCODE`, `FAMILYGRPCODE` | `PRODUCT.FAMILYGRPCOMPANYCODE = PRODUCTGROUPFAMILY.COMPANYCODE AND PRODUCT.FAMILYGRPCODE = PRODUCTGROUPFAMILY.CODE` |
| `PRODUCTGROUPFAMILY_FAMILYGRP` | [`CONTAINER`](../CORE_MASTER/CONTAINER.md) | `FAMILYGRPCOMPANYCODE`, `FAMILYGRPCODE` | `CONTAINER.FAMILYGRPCOMPANYCODE = PRODUCTGROUPFAMILY.COMPANYCODE AND CONTAINER.FAMILYGRPCODE = PRODUCTGROUPFAMILY.CODE` |
| `PRODUCTGROUPFAMILY_FAMILYGRP` | [`MSESPECIFICATIONTEMPLATE`](../SPECIFICATIONS/MSESPECIFICATIONTEMPLATE.md) | `FAMILYGRPCOMPANYCODE`, `FAMILYGRPCODE` | `MSESPECIFICATIONTEMPLATE.FAMILYGRPCOMPANYCODE = PRODUCTGROUPFAMILY.COMPANYCODE AND MSESPECIFICATIONTEMPLATE.FAMILYGRPCODE = PRODUCTGROUPFAMILY.CODE` |
| `PRODUCTGROUPFAMILY_FAMILYGRP` | [`MSESPECMASTERSELFIELDVALUE`](../SPECIFICATIONS/MSESPECMASTERSELFIELDVALUE.md) | `FAMILYGRPCOMPANYCODE`, `FAMILYGRPCODE` | `MSESPECMASTERSELFIELDVALUE.FAMILYGRPCOMPANYCODE = PRODUCTGROUPFAMILY.COMPANYCODE AND MSESPECMASTERSELFIELDVALUE.FAMILYGRPCODE = PRODUCTGROUPFAMILY.CODE` |

## Indexes

- `PRODUCTGROUPFAMILYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.FAMILYNATURE,
       t.REPARTITIONQUANTITYARTICLE,
       t.INITIALSCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.PRODUCTGROUPFAMILY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
