# DB2ADMIN.STOCKTAKEUSETEMPLATE

- **Module**: `INVENTORY` (high confidence — table name starts with 'STOCK')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 22779

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `ONHANDUPDATE` | CHAR(2) | NOT NULL |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `STOCKTAKEUSETEMPLATE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `STOCKTAKEUSETEMPLATE_TEMPLATE` | [`STOCKTAKEUSETEMPLATELINE`](../INVENTORY/STOCKTAKEUSETEMPLATELINE.md) | `STOCKTAKEUSETMPCOMPANYCODE`, `STOCKTAKEUSETEMPLATECODE` | `STOCKTAKEUSETEMPLATELINE.STOCKTAKEUSETMPCOMPANYCODE = STOCKTAKEUSETEMPLATE.COMPANYCODE AND STOCKTAKEUSETEMPLATELINE.STOCKTAKEUSETEMPLATECODE = STOCKTAKEUSETEMPLATE.CODE` |

## Indexes

- `STOCKTAKEUSETEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ONHANDUPDATE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.STOCKTAKEUSETEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
