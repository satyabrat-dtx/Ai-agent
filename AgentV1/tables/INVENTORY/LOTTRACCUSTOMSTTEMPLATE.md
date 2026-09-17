# DB2ADMIN.LOTTRACCUSTOMSTTEMPLATE

- **Module**: `INVENTORY` (low confidence — FK neighbourhood: 1 of 1 related tables are INVENTORY)
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `COMPANYCODE`, `STTEMPLATECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 112731

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `STTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `STTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LOTTRACCUSTOMSTTEMPLATE.COMPANYCODE = COMPANY.CODE` |
| `STOCKTRANSACTIONTEMPLATE_STTEMPLATE` | `STTEMPLATECOMPANYCODE`, `STTEMPLATECODE` | [`STOCKTRANSACTIONTEMPLATE`](../INVENTORY/STOCKTRANSACTIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LOTTRACCUSTOMSTTEMPLATE.STTEMPLATECOMPANYCODE = STOCKTRANSACTIONTEMPLATE.COMPANYCODE AND LOTTRACCUSTOMSTTEMPLATE.STTEMPLATECODE = STOCKTRANSACTIONTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LOTTRACCUSTOMSTTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.STTEMPLATECOMPANYCODE,
       t.STTEMPLATECODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.LOTTRACCUSTOMSTTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
