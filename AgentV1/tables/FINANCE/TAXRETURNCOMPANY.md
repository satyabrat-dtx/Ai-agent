# DB2ADMIN.TAXRETURNCOMPANY

- **Module**: `FINANCE` (low confidence — FK neighbourhood: 1 of 1 related tables are FINANCE)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `TAXRETURNCODE`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 103278

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TAXRETURNCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `TEXT` | CHAR(50) |  |  |  |  |
| 3 | `TESTDATE` | DATE |  |  |  |  |
| 4 | `TAXCODECODE` | CHAR(5) |  | FK | foreign_key |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `TAXRETURN_TAXRETURNCOMPANY` | `TAXRETURNCODE` | [`TAXRETURN`](../FINANCE/TAXRETURN.md) | `CODE` | RESTRICT | `TAXRETURNCOMPANY.TAXRETURNCODE = TAXRETURN.CODE` |
| `VAT_TAXCODE` | `COMPANYCODE`, `TAXCODECODE` | [`VAT`](../FINANCE/VAT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TAXRETURNCOMPANY.COMPANYCODE = VAT.COMPANYCODE AND TAXRETURNCOMPANY.TAXCODECODE = VAT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TAXRETURNCOMPANYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TAXRETURNCODE,
       t.COMPANYCODE,
       t.TEXT,
       t.TESTDATE,
       t.TAXCODECODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.TAXRETURNCOMPANY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
