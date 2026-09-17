# DB2ADMIN.LINKEDSTOCKTEMPLATE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 215127

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `STOCKTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `NEGATIVESTOCKTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LINKEDSTOCKTEMPLATE.COMPANYCODE = COMPANY.CODE` |
| `STOCKTYPE_NEGATIVESTOCKTYPE` | `NEGATIVESTOCKTYPECODE` | [`STOCKTYPE`](../INVENTORY/STOCKTYPE.md) | `CODE` | RESTRICT | `LINKEDSTOCKTEMPLATE.NEGATIVESTOCKTYPECODE = STOCKTYPE.CODE` |
| `STOCKTYPE_STOCKTYPE` | `STOCKTYPECODE` | [`STOCKTYPE`](../INVENTORY/STOCKTYPE.md) | `CODE` | RESTRICT | `LINKEDSTOCKTEMPLATE.STOCKTYPECODE = STOCKTYPE.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `LINKEDSTOCKTEMPLATE_LINKEDSTOCKTEMPLATE` | [`PURCHASEORDERTEMPLATE`](../PURCHASING/PURCHASEORDERTEMPLATE.md) | `COMPANYCODE`, `LINKEDSTOCKTEMPLATECODE` | `PURCHASEORDERTEMPLATE.COMPANYCODE = LINKEDSTOCKTEMPLATE.COMPANYCODE AND PURCHASEORDERTEMPLATE.LINKEDSTOCKTEMPLATECODE = LINKEDSTOCKTEMPLATE.CODE` |
| `LINKEDSTOCKTEMPLATE_LINKEDSTOCKTEMPLATE` | [`PRODUCTIONDEMANDTEMPLATE`](../PRODUCTION/PRODUCTIONDEMANDTEMPLATE.md) | `COMPANYCODE`, `LINKEDSTOCKTEMPLATECODE` | `PRODUCTIONDEMANDTEMPLATE.COMPANYCODE = LINKEDSTOCKTEMPLATE.COMPANYCODE AND PRODUCTIONDEMANDTEMPLATE.LINKEDSTOCKTEMPLATECODE = LINKEDSTOCKTEMPLATE.CODE` |

## Indexes

- `LINKEDSTOCKTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.STOCKTYPECODE,
       t.NEGATIVESTOCKTYPECODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.LINKEDSTOCKTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
