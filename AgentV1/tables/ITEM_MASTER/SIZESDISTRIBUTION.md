# DB2ADMIN.SIZESDISTRIBUTION

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 1 of 1 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 97054

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(30) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `SIZESTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 3 | `SIZESTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SIZESDISTRIBUTION.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SIZESDISTRIBUTION.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `SIZESTYPE_SIZESTYPE` | `SIZESTYPECOMPANYCODE`, `SIZESTYPECODE` | [`SIZESTYPE`](../PDM/SIZESTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SIZESDISTRIBUTION.SIZESTYPECOMPANYCODE = SIZESTYPE.COMPANYCODE AND SIZESDISTRIBUTION.SIZESTYPECODE = SIZESTYPE.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SIZESDISTRIBUTION_SIZEDISTRIBUTION` | [`PRODUCTSPECIALIZEDSIZE`](../ITEM_MASTER/PRODUCTSPECIALIZEDSIZE.md) | `SIZEDISTRIBUTIONCOMPANYCODE`, `SIZEDISTRIBUTIONCODE` | `PRODUCTSPECIALIZEDSIZE.SIZEDISTRIBUTIONCOMPANYCODE = SIZESDISTRIBUTION.COMPANYCODE AND PRODUCTSPECIALIZEDSIZE.SIZEDISTRIBUTIONCODE = SIZESDISTRIBUTION.CODE` |
| `SIZESDISTRIBUTION_SIZEDISTRIBUTIONMATRIXROW` | [`PRODUCTSPECIALIZEDSIZE`](../ITEM_MASTER/PRODUCTSPECIALIZEDSIZE.md) | `SIZEDISTRIBUTIONMRCOMPANYCODE`, `SIZEDISTRIBUTIONMATRIXROWCODE` | `PRODUCTSPECIALIZEDSIZE.SIZEDISTRIBUTIONMRCOMPANYCODE = SIZESDISTRIBUTION.COMPANYCODE AND PRODUCTSPECIALIZEDSIZE.SIZEDISTRIBUTIONMATRIXROWCODE = SIZESDISTRIBUTION.CODE` |
| `SIZESDISTRIBUTION_DETAILS` | [`SIZESDISTRIBUTIONDETAIL`](../ITEM_MASTER/SIZESDISTRIBUTIONDETAIL.md) | `SIZEDISTRSIZETYPECOMPANYCODE`, `SIZESDISTRIBUTIONCODE` | `SIZESDISTRIBUTIONDETAIL.SIZEDISTRSIZETYPECOMPANYCODE = SIZESDISTRIBUTION.COMPANYCODE AND SIZESDISTRIBUTIONDETAIL.SIZESDISTRIBUTIONCODE = SIZESDISTRIBUTION.CODE` |

## Implicit links (NOT declared in the DDL — inferred)

- child `SIZESDISTRIBUTIONDETAILBEAN`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Indexes

- `SIZESDISTRIBUTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.SIZESTYPECOMPANYCODE,
       t.SIZESTYPECODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.OWNINGCOMPANYCODE,
       t.ABSUNIQUEID,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.SIZESDISTRIBUTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
