# DB2ADMIN.SHIPMENTARTICLE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 4 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 124853

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(5) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `COUNCILCODE` | CHAR(10) |  | FK | foreign_key |  |
| 6 | `COUNTRY` | CHAR(3) |  |  |  |  |
| 7 | `CATEGORY` | CHAR(15) |  |  |  |  |
| 8 | `CONVERSIONVALUE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `CONVERSIONUMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 10 | `SHIPMENTUMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `RATELISTNO` | CHAR(25) |  |  |  |  |
| 12 | `RITCNO` | CHAR(25) |  |  |  |  |
| 13 | `PUBLICNOTICESSNO` | CHAR(25) |  |  |  |  |
| 14 | `APPENDIXCONDITIONNO` | CHAR(25) |  |  |  |  |
| 15 | `IMPORTDUTY` | DECIMAL(9,5) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 23 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SHIPMENTARTICLE.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SHIPMENTARTICLE.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `COUNCIL_COUNCIL` | `COUNCILCODE` | [`COUNCIL`](../OTHER/COUNCIL.md) | `CODE` | RESTRICT | `SHIPMENTARTICLE.COUNCILCODE = COUNCIL.CODE` |
| `UNITOFMEASURE_CONVERSIONUM` | `CONVERSIONUMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `SHIPMENTARTICLE.CONVERSIONUMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_SHIPMENTUM` | `SHIPMENTUMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `SHIPMENTARTICLE.SHIPMENTUMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 4

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SHIPMENTARTICLE_SHIPMENTARTICLE` | [`PRODUCTIE`](../ITEM_MASTER/PRODUCTIE.md) | `SHIPMENTARTICLECOMPANYCODE`, `SHIPMENTARTICLECODE` | `PRODUCTIE.SHIPMENTARTICLECOMPANYCODE = SHIPMENTARTICLE.COMPANYCODE AND PRODUCTIE.SHIPMENTARTICLECODE = SHIPMENTARTICLE.CODE` |
| `SHIPMENTARTICLE_SHIPMENTARTICLEDETAIL` | [`SHIPMENTARTICLEDETAIL`](../OTHER/SHIPMENTARTICLEDETAIL.md) | `SHIPMENTARTICLECOMPANYCODE`, `SHIPMENTARTICLECODE` | `SHIPMENTARTICLEDETAIL.SHIPMENTARTICLECOMPANYCODE = SHIPMENTARTICLE.COMPANYCODE AND SHIPMENTARTICLEDETAIL.SHIPMENTARTICLECODE = SHIPMENTARTICLE.CODE` |
| `SHIPMENTARTICLE_SHIPMENTARTICLE` | [`EPCGAPPLICATIONEXPORTPRODUCT`](../PURCHASING/EPCGAPPLICATIONEXPORTPRODUCT.md) | `SHIPMENTARTICLECOMPANYCODE`, `SHIPMENTARTICLECODE` | `EPCGAPPLICATIONEXPORTPRODUCT.SHIPMENTARTICLECOMPANYCODE = SHIPMENTARTICLE.COMPANYCODE AND EPCGAPPLICATIONEXPORTPRODUCT.SHIPMENTARTICLECODE = SHIPMENTARTICLE.CODE` |
| `SHIPMENTARTICLE_SHIPMENTARTICLE` | [`SALESORDERLINEIE`](../SALES/SALESORDERLINEIE.md) | `SHIPMENTARTICLECOMPANYCODE`, `SHIPMENTARTICLECODE` | `SALESORDERLINEIE.SHIPMENTARTICLECOMPANYCODE = SHIPMENTARTICLE.COMPANYCODE AND SALESORDERLINEIE.SHIPMENTARTICLECODE = SHIPMENTARTICLE.CODE` |

## Indexes

- `SHIPMENTARTICLEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.COUNCILCODE,
       t.COUNTRY,
       t.CATEGORY,
       t.CONVERSIONVALUE,
       t.CONVERSIONUMCODE,
       t.SHIPMENTUMCODE,
       t.RATELISTNO
FROM   DB2ADMIN.SHIPMENTARTICLE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
