# DB2ADMIN.SIZESTYPE

- **Module**: `PDM` (low confidence — FK neighbourhood: 1 of 1 related tables are PDM)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 14043

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SIZESTYPE.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SIZESTYPE.OWNINGCOMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SIZESTYPE_SIZES` | [`SIZES`](../PDM/SIZES.md) | `SIZESTYPECOMPANYCODE`, `SIZESTYPECODE` | `SIZES.SIZESTYPECOMPANYCODE = SIZESTYPE.COMPANYCODE AND SIZES.SIZESTYPECODE = SIZESTYPE.CODE` |
| `SIZESTYPE_GENERICSIZETYPE` | [`PDMCUSTOMIZEDOPTIONS`](../PDM/PDMCUSTOMIZEDOPTIONS.md) | `GENERICSIZETYPECOMPANYCODE`, `GENERICSIZETYPECODE` | `PDMCUSTOMIZEDOPTIONS.GENERICSIZETYPECOMPANYCODE = SIZESTYPE.COMPANYCODE AND PDMCUSTOMIZEDOPTIONS.GENERICSIZETYPECODE = SIZESTYPE.CODE` |
| `SIZESTYPE_SIZESTYPE` | [`SIZESDISTRIBUTION`](../ITEM_MASTER/SIZESDISTRIBUTION.md) | `SIZESTYPECOMPANYCODE`, `SIZESTYPECODE` | `SIZESDISTRIBUTION.SIZESTYPECOMPANYCODE = SIZESTYPE.COMPANYCODE AND SIZESDISTRIBUTION.SIZESTYPECODE = SIZESTYPE.CODE` |

## Indexes

- `SIZESTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.OWNINGCOMPANYCODE,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.SIZESTYPE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
