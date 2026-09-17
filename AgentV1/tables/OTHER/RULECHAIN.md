# DB2ADMIN.RULECHAIN

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `COMPANYCODE`, `RULE01CODE`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 42013

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `RULE01CODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `RULE02CODE` | CHAR(10) |  | FK | foreign_key |  |
| 3 | `RULE03CODE` | CHAR(10) |  | FK | foreign_key |  |
| 4 | `RULE04CODE` | CHAR(10) |  | FK | foreign_key |  |
| 5 | `RULE05CODE` | CHAR(10) |  | FK | foreign_key |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RULECHAIN.COMPANYCODE = COMPANY.CODE` |
| `RULES_RULE01` | `COMPANYCODE`, `RULE01CODE` | [`RULES`](../CORE_MASTER/RULES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RULECHAIN.COMPANYCODE = RULES.COMPANYCODE AND RULECHAIN.RULE01CODE = RULES.CODE` |
| `RULES_RULE02` | `COMPANYCODE`, `RULE02CODE` | [`RULES`](../CORE_MASTER/RULES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RULECHAIN.COMPANYCODE = RULES.COMPANYCODE AND RULECHAIN.RULE02CODE = RULES.CODE` |
| `RULES_RULE03` | `COMPANYCODE`, `RULE03CODE` | [`RULES`](../CORE_MASTER/RULES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RULECHAIN.COMPANYCODE = RULES.COMPANYCODE AND RULECHAIN.RULE03CODE = RULES.CODE` |
| `RULES_RULE04` | `COMPANYCODE`, `RULE04CODE` | [`RULES`](../CORE_MASTER/RULES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RULECHAIN.COMPANYCODE = RULES.COMPANYCODE AND RULECHAIN.RULE04CODE = RULES.CODE` |
| `RULES_RULE05` | `COMPANYCODE`, `RULE05CODE` | [`RULES`](../CORE_MASTER/RULES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RULECHAIN.COMPANYCODE = RULES.COMPANYCODE AND RULECHAIN.RULE05CODE = RULES.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RULECHAINUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.RULE01CODE,
       t.RULE02CODE,
       t.RULE03CODE,
       t.RULE04CODE,
       t.RULE05CODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.RULECHAIN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
