# DB2ADMIN.APPAGENTS

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `COMPANYCODE`, `AGENTCODE`
- **FK degree**: referenced by 2 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 110712

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `AGENTCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `APPAGENTS_APPAGENTORDERSDEF` | [`APPAGENTORDERSDEF`](../SALES/APPAGENTORDERSDEF.md) | `APPAGENTSCOMPANYCODE`, `APPAGENTSAGENTCODE` | `APPAGENTORDERSDEF.APPAGENTSCOMPANYCODE = APPAGENTS.COMPANYCODE AND APPAGENTORDERSDEF.APPAGENTSAGENTCODE = APPAGENTS.AGENTCODE` |
| `APPAGENTS_APPAGENTSAVAILABILITYDEF` | [`APPAGENTSAVAILABILITYDEF`](../SALES/APPAGENTSAVAILABILITYDEF.md) | `APPAGENTSCOMPANYCODE`, `APPAGENTSAGENTCODE` | `APPAGENTSAVAILABILITYDEF.APPAGENTSCOMPANYCODE = APPAGENTS.COMPANYCODE AND APPAGENTSAVAILABILITYDEF.APPAGENTSAGENTCODE = APPAGENTS.AGENTCODE` |

## Indexes

- `APPAGENTSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.AGENTCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.APPAGENTS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
