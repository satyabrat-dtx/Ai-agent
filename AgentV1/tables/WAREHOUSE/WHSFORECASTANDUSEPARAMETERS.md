# DB2ADMIN.WHSFORECASTANDUSEPARAMETERS

- **Module**: `WAREHOUSE` (low confidence — FK neighbourhood: 1 of 1 related tables are WAREHOUSE)
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `WAREHOUSEGROUPCOMPANYCODE`, `WAREHOUSEGROUPCODE`, `ITEMFRCANDUSESTDGROUPTYPECODE`, `ITEMFORECASTANDUSECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 8848

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WAREHOUSEGROUPCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `WAREHOUSEGROUPCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITEMFRCANDUSESTDGROUPTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ITEMFORECASTANDUSECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `ALPHAQUANTITY` | DECIMAL(4,3) |  |  |  |  |
| 8 | `ALPHAAMOUNT` | DECIMAL(4,3) |  |  |  |  |
| 9 | `TRENDCORRECTION` | SMALLINT | NOT NULL |  |  |  |
| 10 | `BETAQUANTITY` | DECIMAL(4,3) |  |  |  |  |
| 11 | `BETAAMOUNT` | DECIMAL(4,3) |  |  |  |  |
| 12 | `THRESHOLDQUANTITY` | DECIMAL(5,2) |  |  |  |  |
| 13 | `THRESHOLDAMOUNT` | DECIMAL(5,2) |  |  |  |  |
| 14 | `GAMMAQUANTITY` | DECIMAL(4,3) |  |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `ITEMFRCANDUSESTDGRPTYPECMYCOD` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 22 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `WHSFORECASTANDUSEPARAMETERS.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `STANDARDGROUP_ITEMFORECASTANDUSE` | `ITEMFRCANDUSESTDGRPTYPECMYCOD`, `ITEMFRCANDUSESTDGROUPTYPECODE`, `ITEMFORECASTANDUSECODE` | [`STANDARDGROUP`](../CORE_MASTER/STANDARDGROUP.md) | `STANDARDGROUPTYPECOMPANYCODE`, `STANDARDGROUPTYPECODE`, `CODE` | RESTRICT | `WHSFORECASTANDUSEPARAMETERS.ITEMFRCANDUSESTDGRPTYPECMYCOD = STANDARDGROUP.STANDARDGROUPTYPECOMPANYCODE AND WHSFORECASTANDUSEPARAMETERS.ITEMFRCANDUSESTDGROUPTYPECODE = STANDARDGROUP.STANDARDGROUPTYPECODE AND WHSFORECASTANDUSEPARAMETERS.ITEMFORECASTANDUSECODE = STANDARDGROUP.CODE` |
| `WAREHOUSEFORECASTANDUSEGROUP_WAREHOUSEGROUP` | `WAREHOUSEGROUPCOMPANYCODE`, `WAREHOUSEGROUPCODE` | [`WAREHOUSEFORECASTANDUSEGROUP`](../WAREHOUSE/WAREHOUSEFORECASTANDUSEGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WHSFORECASTANDUSEPARAMETERS.WAREHOUSEGROUPCOMPANYCODE = WAREHOUSEFORECASTANDUSEGROUP.COMPANYCODE AND WHSFORECASTANDUSEPARAMETERS.WAREHOUSEGROUPCODE = WAREHOUSEFORECASTANDUSEGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WHSFRCANDUSEPARAMETERSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.WAREHOUSEGROUPCOMPANYCODE,
       t.WAREHOUSEGROUPCODE,
       t.ITEMFRCANDUSESTDGROUPTYPECODE,
       t.ITEMFORECASTANDUSECODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ALPHAQUANTITY,
       t.ALPHAAMOUNT,
       t.TRENDCORRECTION,
       t.BETAQUANTITY,
       t.BETAAMOUNT
FROM   DB2ADMIN.WHSFORECASTANDUSEPARAMETERS t
FETCH FIRST 100 ROWS ONLY;
```
