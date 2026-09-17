# DB2ADMIN.APPSALESORDERTEMPLATE

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `COMPANYCODE`, `SALESORDERTEMPLATECODE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 114353

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SALESORDERTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ISDEFAULT` | SMALLINT | NOT NULL |  |  |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `SALESORDERTEMPLATE_SALESORDERTEMPLATE` | `COMPANYCODE`, `SALESORDERTEMPLATECODE` | [`SALESORDERTEMPLATE`](../SALES/SALESORDERTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `APPSALESORDERTEMPLATE.COMPANYCODE = SALESORDERTEMPLATE.COMPANYCODE AND APPSALESORDERTEMPLATE.SALESORDERTEMPLATECODE = SALESORDERTEMPLATE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `APPSALESORDERTEMPLATE_TEMPLATE` | [`APPSALESORDER`](../SALES/APPSALESORDER.md) | `COMPANYCODE`, `TEMPLATESALESORDERTEMPLATECODE` | `APPSALESORDER.COMPANYCODE = APPSALESORDERTEMPLATE.COMPANYCODE AND APPSALESORDER.TEMPLATESALESORDERTEMPLATECODE = APPSALESORDERTEMPLATE.SALESORDERTEMPLATECODE` |

## Indexes

- `APPSALESORDERTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SALESORDERTEMPLATECODE,
       t.ISDEFAULT,
       t.ABSUNIQUEID
FROM   DB2ADMIN.APPSALESORDERTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
