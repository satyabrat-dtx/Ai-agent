# DB2ADMIN.ITEMLIFOGROUP

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'ITEM')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 5 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 18143

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `UNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `EXCLUDESLIFOCALCULATION` | SMALLINT | NOT NULL |  |  |  |
| 7 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ITEMLIFOGROUP.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ITEMLIFOGROUP.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `UNITOFMEASURE_UNITOFMEASURE` | `UNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `ITEMLIFOGROUP.UNITOFMEASURECODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 5

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ITEMLIFOGROUP_LIFOGRP` | [`TOOL`](../CORE_MASTER/TOOL.md) | `LIFOGRPCOMPANYCODE`, `LIFOGRPCODE` | `TOOL.LIFOGRPCOMPANYCODE = ITEMLIFOGROUP.COMPANYCODE AND TOOL.LIFOGRPCODE = ITEMLIFOGROUP.CODE` |
| `ITEMLIFOGROUP_LIFOGRP` | [`PRODUCT`](../ITEM_MASTER/PRODUCT.md) | `LIFOGRPCOMPANYCODE`, `LIFOGRPCODE` | `PRODUCT.LIFOGRPCOMPANYCODE = ITEMLIFOGROUP.COMPANYCODE AND PRODUCT.LIFOGRPCODE = ITEMLIFOGROUP.CODE` |
| `ITEMLIFOGROUP_LIFOGRP` | [`CONTAINER`](../CORE_MASTER/CONTAINER.md) | `LIFOGRPCOMPANYCODE`, `LIFOGRPCODE` | `CONTAINER.LIFOGRPCOMPANYCODE = ITEMLIFOGROUP.COMPANYCODE AND CONTAINER.LIFOGRPCODE = ITEMLIFOGROUP.CODE` |
| `ITEMLIFOGROUP_LIFOGRP` | [`MSESPECIFICATIONTEMPLATE`](../SPECIFICATIONS/MSESPECIFICATIONTEMPLATE.md) | `LIFOGRPCOMPANYCODE`, `LIFOGRPCODE` | `MSESPECIFICATIONTEMPLATE.LIFOGRPCOMPANYCODE = ITEMLIFOGROUP.COMPANYCODE AND MSESPECIFICATIONTEMPLATE.LIFOGRPCODE = ITEMLIFOGROUP.CODE` |
| `ITEMLIFOGROUP_LIFOGRP` | [`MSESPECMASTERSELFIELDVALUE`](../SPECIFICATIONS/MSESPECMASTERSELFIELDVALUE.md) | `LIFOGRPCOMPANYCODE`, `LIFOGRPCODE` | `MSESPECMASTERSELFIELDVALUE.LIFOGRPCOMPANYCODE = ITEMLIFOGROUP.COMPANYCODE AND MSESPECMASTERSELFIELDVALUE.LIFOGRPCODE = ITEMLIFOGROUP.CODE` |

## Indexes

- `ITEMLIFOGROUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.UNITOFMEASURECODE,
       t.EXCLUDESLIFOCALCULATION,
       t.OWNINGCOMPANYCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.ITEMLIFOGROUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
