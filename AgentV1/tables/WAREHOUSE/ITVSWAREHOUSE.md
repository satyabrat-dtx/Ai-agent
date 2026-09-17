# DB2ADMIN.ITVSWAREHOUSE

- **Module**: `WAREHOUSE` (low confidence — FK neighbourhood: 1 of 1 related tables are WAREHOUSE)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`, `LOGICALWAREHOUSECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 147007

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `PARTIALSHIPMENTALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ITVSWAREHOUSE.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITVSWAREHOUSE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND ITVSWAREHOUSE.ITEMTYPECODE = ITEMTYPE.CODE` |
| `LOGICALWAREHOUSE_LOGICALWAREHOUSE` | `LOGICALWAREHOUSECOMPANYCODE`, `LOGICALWAREHOUSECODE` | [`LOGICALWAREHOUSE`](../WAREHOUSE/LOGICALWAREHOUSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITVSWAREHOUSE.LOGICALWAREHOUSECOMPANYCODE = LOGICALWAREHOUSE.COMPANYCODE AND ITVSWAREHOUSE.LOGICALWAREHOUSECODE = LOGICALWAREHOUSE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ITVSWAREHOUSEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.LOGICALWAREHOUSECOMPANYCODE,
       t.LOGICALWAREHOUSECODE,
       t.PARTIALSHIPMENTALLOWED,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ITVSWAREHOUSE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
