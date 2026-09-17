# DB2ADMIN.COMPOSITIONDETAIL

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 1 of 1 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPOSITIONCOMPANYCODE`, `COMPOSITIONCODE`, `SUBCOMPOSITION`, `TOUSE`, `SEQUENCE`, `COMPONENTCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 43844

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPOSITIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `COMPOSITIONCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SUBCOMPOSITION` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 3 | `TOUSE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 4 | `SEQUENCE` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `COMPONENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 6 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 7 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 8 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 9 | `COMPONENTPERCENTAGE` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 10 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 16 | `COMPONENTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `COMPOSITIONDETAIL.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `COMPOSITION_DETAIL` | `COMPOSITIONCOMPANYCODE`, `COMPOSITIONCODE` | [`COMPOSITION`](../ITEM_MASTER/COMPOSITION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `COMPOSITIONDETAIL.COMPOSITIONCOMPANYCODE = COMPOSITION.COMPANYCODE AND COMPOSITIONDETAIL.COMPOSITIONCODE = COMPOSITION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COMPOSITIONDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPOSITIONCOMPANYCODE,
       t.COMPOSITIONCODE,
       t.SUBCOMPOSITION,
       t.TOUSE,
       t.SEQUENCE,
       t.COMPONENTCODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.COMPONENTPERCENTAGE,
       t.OWNINGCOMPANYCODE,
       t.CREATIONDATETIME
FROM   DB2ADMIN.COMPOSITIONDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
