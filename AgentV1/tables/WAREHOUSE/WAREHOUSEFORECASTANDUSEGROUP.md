# DB2ADMIN.WAREHOUSEFORECASTANDUSEGROUP

- **Module**: `WAREHOUSE` (high confidence — table name starts with 'WAREHOUSE')
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 8469

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `PERIODIZEDCALENDARTYPECODE` | CHAR(10) |  | FK | foreign_key |  |
| 6 | `ALPHAQUANTITY` | DECIMAL(4,3) |  |  |  |  |
| 7 | `ALPHAAMOUNT` | DECIMAL(4,3) |  |  |  |  |
| 8 | `TRENDCORRECTION` | SMALLINT | NOT NULL |  |  |  |
| 9 | `BETAQUANTITY` | DECIMAL(4,3) |  |  |  |  |
| 10 | `BETAAMOUNT` | DECIMAL(4,3) |  |  |  |  |
| 11 | `THRESHOLDQUANTITY` | DECIMAL(5,2) |  |  |  |  |
| 12 | `THRESHOLDAMOUNT` | DECIMAL(5,2) |  |  |  |  |
| 13 | `GAMMAQUANTITY` | DECIMAL(4,3) |  |  |  |  |
| 14 | `THRESHOLDACLASS` | DECIMAL(5,2) |  |  |  |  |
| 15 | `THRESHOLDBCLASS` | DECIMAL(5,2) |  |  |  |  |
| 16 | `THRESHOLDCCLASS` | DECIMAL(5,2) |  |  |  |  |
| 17 | `THRESHOLDDCLASS` | DECIMAL(5,2) |  |  |  |  |
| 18 | `THRESHOLDECLASS` | DECIMAL(5,2) |  |  |  |  |
| 19 | `THRESHOLDFCLASS` | DECIMAL(5,2) |  |  |  |  |
| 20 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 21 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 22 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 23 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 24 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 25 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 26 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 27 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `WAREHOUSEFORECASTANDUSEGROUP.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `WAREHOUSEFORECASTANDUSEGROUP.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `PERIODIZEDCALENDARTYPE_PERIODIZEDCALENDARTYPE` | `PERIODIZEDCALENDARTYPECODE` | [`PERIODIZEDCALENDARTYPE`](../CORE_MASTER/PERIODIZEDCALENDARTYPE.md) | `CODE` | RESTRICT | `WAREHOUSEFORECASTANDUSEGROUP.PERIODIZEDCALENDARTYPECODE = PERIODIZEDCALENDARTYPE.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `WAREHOUSEFORECASTANDUSEGROUP_WAREHOUSEGROUP` | [`WHSFORECASTANDUSEPARAMETERS`](../WAREHOUSE/WHSFORECASTANDUSEPARAMETERS.md) | `WAREHOUSEGROUPCOMPANYCODE`, `WAREHOUSEGROUPCODE` | `WHSFORECASTANDUSEPARAMETERS.WAREHOUSEGROUPCOMPANYCODE = WAREHOUSEFORECASTANDUSEGROUP.COMPANYCODE AND WHSFORECASTANDUSEPARAMETERS.WAREHOUSEGROUPCODE = WAREHOUSEFORECASTANDUSEGROUP.CODE` |
| `WAREHOUSEFORECASTANDUSEGROUP_FORECASTANDUSEGROUP` | [`LOGICALWAREHOUSE`](../WAREHOUSE/LOGICALWAREHOUSE.md) | `FORECASTANDUSEGROUPCOMPANYCODE`, `FORECASTANDUSEGROUPCODE` | `LOGICALWAREHOUSE.FORECASTANDUSEGROUPCOMPANYCODE = WAREHOUSEFORECASTANDUSEGROUP.COMPANYCODE AND LOGICALWAREHOUSE.FORECASTANDUSEGROUPCODE = WAREHOUSEFORECASTANDUSEGROUP.CODE` |

## Indexes

- `WHSFORECASTANDUSEGROUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.PERIODIZEDCALENDARTYPECODE,
       t.ALPHAQUANTITY,
       t.ALPHAAMOUNT,
       t.TRENDCORRECTION,
       t.BETAQUANTITY,
       t.BETAAMOUNT,
       t.THRESHOLDQUANTITY
FROM   DB2ADMIN.WAREHOUSEFORECASTANDUSEGROUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
