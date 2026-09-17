# DB2ADMIN.LOTTRACCUSTOMSTTEMPLATEEXCL

- **Module**: `INVENTORY` (low confidence — FK neighbourhood: 1 of 1 related tables are INVENTORY)
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `COMPANYCODE`, `STTEMPLATEEXCLCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 113181

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `STTEMPLATEEXCLCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `STTEMPLATEEXCLCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LOTTRACCUSTOMSTTEMPLATEEXCL.COMPANYCODE = COMPANY.CODE` |
| `STOCKTRANSACTIONTEMPLATE_STTEMPLATEEXCL` | `STTEMPLATEEXCLCOMPANYCODE`, `STTEMPLATEEXCLCODE` | [`STOCKTRANSACTIONTEMPLATE`](../INVENTORY/STOCKTRANSACTIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LOTTRACCUSTOMSTTEMPLATEEXCL.STTEMPLATEEXCLCOMPANYCODE = STOCKTRANSACTIONTEMPLATE.COMPANYCODE AND LOTTRACCUSTOMSTTEMPLATEEXCL.STTEMPLATEEXCLCODE = STOCKTRANSACTIONTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LOTTRACCUSTOMSTTMPEXCLUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.STTEMPLATEEXCLCOMPANYCODE,
       t.STTEMPLATEEXCLCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.LOTTRACCUSTOMSTTEMPLATEEXCL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
