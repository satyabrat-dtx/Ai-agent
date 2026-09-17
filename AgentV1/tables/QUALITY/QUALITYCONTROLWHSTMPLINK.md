# DB2ADMIN.QUALITYCONTROLWHSTMPLINK

- **Module**: `QUALITY` (high confidence — table name starts with 'QUALITY')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `WAREHOUSECODE`, `TEMPLATECODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 23834

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `WAREHOUSECODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `DSTWAREHOUSECODE` | CHAR(8) |  | FK | foreign_key |  |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `WAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 13 | `TEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 14 | `DSTWAREHOUSECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 15 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `QUALITYCONTROLWHSTMPLINK.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `QUALITYCONTROLWHSTMPLINK.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `LOGICALWAREHOUSE_DSTWAREHOUSE` | `DSTWAREHOUSECOMPANYCODE`, `DSTWAREHOUSECODE` | [`LOGICALWAREHOUSE`](../WAREHOUSE/LOGICALWAREHOUSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QUALITYCONTROLWHSTMPLINK.DSTWAREHOUSECOMPANYCODE = LOGICALWAREHOUSE.COMPANYCODE AND QUALITYCONTROLWHSTMPLINK.DSTWAREHOUSECODE = LOGICALWAREHOUSE.CODE` |
| `LOGICALWAREHOUSE_WAREHOUSE` | `WAREHOUSECOMPANYCODE`, `WAREHOUSECODE` | [`LOGICALWAREHOUSE`](../WAREHOUSE/LOGICALWAREHOUSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QUALITYCONTROLWHSTMPLINK.WAREHOUSECOMPANYCODE = LOGICALWAREHOUSE.COMPANYCODE AND QUALITYCONTROLWHSTMPLINK.WAREHOUSECODE = LOGICALWAREHOUSE.CODE` |
| `STOCKTRANSACTIONTEMPLATE_TEMPLATE` | `TEMPLATECOMPANYCODE`, `TEMPLATECODE` | [`STOCKTRANSACTIONTEMPLATE`](../INVENTORY/STOCKTRANSACTIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QUALITYCONTROLWHSTMPLINK.TEMPLATECOMPANYCODE = STOCKTRANSACTIONTEMPLATE.COMPANYCODE AND QUALITYCONTROLWHSTMPLINK.TEMPLATECODE = STOCKTRANSACTIONTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `QUALITYCONTROLWHSTMPLINKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.WAREHOUSECODE,
       t.TEMPLATECODE,
       t.DSTWAREHOUSECODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.QUALITYCONTROLWHSTMPLINK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
