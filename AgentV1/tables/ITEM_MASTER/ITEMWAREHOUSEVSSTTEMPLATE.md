# DB2ADMIN.ITEMWAREHOUSEVSSTTEMPLATE

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'ITEM')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `ANALYSISTYPECODE`, `ITEMTYPECODE`, `WAREHOUSECODE`, `STOCKTRANSACTIONTEMPLATECODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 125330

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ANALYSISTYPECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `WAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 5 | `WAREHOUSECODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `STOCKTRNTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 7 | `STOCKTRANSACTIONTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ANALYSISTYPE_ANALYSISTYPE` | `COMPANYCODE`, `ANALYSISTYPECODE` | [`ANALYSISTYPE`](../ITEM_MASTER/ANALYSISTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMWAREHOUSEVSSTTEMPLATE.COMPANYCODE = ANALYSISTYPE.COMPANYCODE AND ITEMWAREHOUSEVSSTTEMPLATE.ANALYSISTYPECODE = ANALYSISTYPE.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ITEMWAREHOUSEVSSTTEMPLATE.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMWAREHOUSEVSSTTEMPLATE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND ITEMWAREHOUSEVSSTTEMPLATE.ITEMTYPECODE = ITEMTYPE.CODE` |
| `LOGICALWAREHOUSE_WAREHOUSE` | `WAREHOUSECOMPANYCODE`, `WAREHOUSECODE` | [`LOGICALWAREHOUSE`](../WAREHOUSE/LOGICALWAREHOUSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMWAREHOUSEVSSTTEMPLATE.WAREHOUSECOMPANYCODE = LOGICALWAREHOUSE.COMPANYCODE AND ITEMWAREHOUSEVSSTTEMPLATE.WAREHOUSECODE = LOGICALWAREHOUSE.CODE` |
| `STOCKTRANSACTIONTEMPLATE_STOCKTRANSACTIONTEMPLATE` | `STOCKTRNTEMPLATECOMPANYCODE`, `STOCKTRANSACTIONTEMPLATECODE` | [`STOCKTRANSACTIONTEMPLATE`](../INVENTORY/STOCKTRANSACTIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMWAREHOUSEVSSTTEMPLATE.STOCKTRNTEMPLATECOMPANYCODE = STOCKTRANSACTIONTEMPLATE.COMPANYCODE AND ITEMWAREHOUSEVSSTTEMPLATE.STOCKTRANSACTIONTEMPLATECODE = STOCKTRANSACTIONTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ITEMWAREHOUSEVSSTTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ANALYSISTYPECODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.WAREHOUSECOMPANYCODE,
       t.WAREHOUSECODE,
       t.STOCKTRNTEMPLATECOMPANYCODE,
       t.STOCKTRANSACTIONTEMPLATECODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.ITEMWAREHOUSEVSSTTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
