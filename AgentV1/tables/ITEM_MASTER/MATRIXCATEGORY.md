# DB2ADMIN.MATRIXCATEGORY

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 1 of 1 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 237912

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `COMPONENTMATRIXMANAGEMENT` | INTEGER | NOT NULL |  |  |  |
| 6 | `FILTERON` | SMALLINT | NOT NULL |  |  |  |
| 7 | `CHOICETYPE` | INTEGER | NOT NULL |  |  |  |
| 8 | `MATRIXROWNR` | INTEGER | NOT NULL |  |  |  |
| 9 | `MATRIXCOLUMNNR` | INTEGER | NOT NULL |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `MATRIXCATEGORY_MATRIXTYPE` | [`BOMCMPDEFAULTSDIRECTIVETMP`](../ITEM_MASTER/BOMCMPDEFAULTSDIRECTIVETMP.md) | `BCDCOMPANYCODE`, `MATRIXTYPECODE` | `BOMCMPDEFAULTSDIRECTIVETMP.BCDCOMPANYCODE = MATRIXCATEGORY.COMPANYCODE AND BOMCMPDEFAULTSDIRECTIVETMP.MATRIXTYPECODE = MATRIXCATEGORY.CODE` |

## Indexes

- `MATRIXCATEGORYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.COMPONENTMATRIXMANAGEMENT,
       t.FILTERON,
       t.CHOICETYPE,
       t.MATRIXROWNR,
       t.MATRIXCOLUMNNR,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.MATRIXCATEGORY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
