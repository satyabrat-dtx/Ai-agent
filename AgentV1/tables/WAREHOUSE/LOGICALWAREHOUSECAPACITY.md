# DB2ADMIN.LOGICALWAREHOUSECAPACITY

- **Module**: `WAREHOUSE` (high confidence — table name starts with 'LOGICALWAREHOUSE')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `COMPANYCODE`, `LOGICALWAREHOUSECODE`, `DOCUMENTTEMPLATECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 42290

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DOCUMENTTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `QUANTITYPERHOUR` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 4 | `UOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `LOGICALWAREHOUSE_LOGICALWAREHOUSE` | `LOGICALWAREHOUSECOMPANYCODE`, `LOGICALWAREHOUSECODE` | [`LOGICALWAREHOUSE`](../WAREHOUSE/LOGICALWAREHOUSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LOGICALWAREHOUSECAPACITY.LOGICALWAREHOUSECOMPANYCODE = LOGICALWAREHOUSE.COMPANYCODE AND LOGICALWAREHOUSECAPACITY.LOGICALWAREHOUSECODE = LOGICALWAREHOUSE.CODE` |
| `SALESORDERTEMPLATE_DOCUMENTTEMPLATE` | `COMPANYCODE`, `DOCUMENTTEMPLATECODE` | [`SALESORDERTEMPLATE`](../SALES/SALESORDERTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LOGICALWAREHOUSECAPACITY.COMPANYCODE = SALESORDERTEMPLATE.COMPANYCODE AND LOGICALWAREHOUSECAPACITY.DOCUMENTTEMPLATECODE = SALESORDERTEMPLATE.CODE` |
| `UNITOFMEASURE_UOM` | `UOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `LOGICALWAREHOUSECAPACITY.UOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LOGICALWAREHOUSECAPACITYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.LOGICALWAREHOUSECODE,
       t.DOCUMENTTEMPLATECODE,
       t.QUANTITYPERHOUR,
       t.UOMCODE,
       t.LOGICALWAREHOUSECOMPANYCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.LOGICALWAREHOUSECAPACITY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
