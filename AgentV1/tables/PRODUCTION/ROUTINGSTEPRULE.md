# DB2ADMIN.ROUTINGSTEPRULE

- **Module**: `PRODUCTION` (high confidence — table name starts with 'ROUTING')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `ROUTINGSTEPROUTINGCOMPANYCODE`, `ROUTINGSTEPROUTINGNUMBERID`, `ROUTINGSTEPSEQUENCE`, `ROUTINGSTEPSUBSEQUENCE`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 193184

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ROUTINGSTEPROUTINGCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ROUTINGSTEPROUTINGNUMBERID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ROUTINGSTEPSEQUENCE` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ROUTINGSTEPSUBSEQUENCE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SEQUENCE` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `RULECODE` | CHAR(10) |  | FK | foreign_key |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 7 | `RULEUSABILITY` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ROUTINGSTEP_RULES` | `ROUTINGSTEPROUTINGCOMPANYCODE`, `ROUTINGSTEPROUTINGNUMBERID`, `ROUTINGSTEPSEQUENCE`, `ROUTINGSTEPSUBSEQUENCE` | [`ROUTINGSTEP`](../PRODUCTION/ROUTINGSTEP.md) | `ROUTINGCOMPANYCODE`, `ROUTINGNUMBERID`, `SEQUENCE`, `SUBSEQUENCE` | RESTRICT | `ROUTINGSTEPRULE.ROUTINGSTEPROUTINGCOMPANYCODE = ROUTINGSTEP.ROUTINGCOMPANYCODE AND ROUTINGSTEPRULE.ROUTINGSTEPROUTINGNUMBERID = ROUTINGSTEP.ROUTINGNUMBERID AND ROUTINGSTEPRULE.ROUTINGSTEPSEQUENCE = ROUTINGSTEP.SEQUENCE AND ROUTINGSTEPRULE.ROUTINGSTEPSUBSEQUENCE = ROUTINGSTEP.SUBSEQUENCE` |
| `RULES_RULE` | `ROUTINGSTEPROUTINGCOMPANYCODE`, `RULECODE` | [`RULES`](../CORE_MASTER/RULES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ROUTINGSTEPRULE.ROUTINGSTEPROUTINGCOMPANYCODE = RULES.COMPANYCODE AND ROUTINGSTEPRULE.RULECODE = RULES.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ROUTINGSTEPRULEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ROUTINGSTEPROUTINGCOMPANYCODE,
       t.ROUTINGSTEPROUTINGNUMBERID,
       t.ROUTINGSTEPSEQUENCE,
       t.ROUTINGSTEPSUBSEQUENCE,
       t.SEQUENCE,
       t.RULECODE,
       t.ABSUNIQUEID,
       t.RULEUSABILITY
FROM   DB2ADMIN.ROUTINGSTEPRULE t
FETCH FIRST 100 ROWS ONLY;
```
