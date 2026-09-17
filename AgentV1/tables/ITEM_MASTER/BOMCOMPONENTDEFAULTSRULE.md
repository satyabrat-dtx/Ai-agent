# DB2ADMIN.BOMCOMPONENTDEFAULTSRULE

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'BOM')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `BCDCOMPANYCODE`, `BCDFATHERITEMTYPECODE`, `BCDCOMPITEMTYPECODE`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 193103

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BCDCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `BCDFATHERITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `BCDCOMPITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SEQUENCE` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `RULECODE` | CHAR(10) |  | FK | foreign_key |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 6 | `RULEUSABILITY` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BOMCOMPONENTDEFAULTS_RULES` | `BCDCOMPANYCODE`, `BCDFATHERITEMTYPECODE`, `BCDCOMPITEMTYPECODE` | [`BOMCOMPONENTDEFAULTS`](../ITEM_MASTER/BOMCOMPONENTDEFAULTS.md) | `COMPANYCODE`, `FATHERITEMTYPECODE`, `COMPITEMTYPECODE` | RESTRICT | `BOMCOMPONENTDEFAULTSRULE.BCDCOMPANYCODE = BOMCOMPONENTDEFAULTS.COMPANYCODE AND BOMCOMPONENTDEFAULTSRULE.BCDFATHERITEMTYPECODE = BOMCOMPONENTDEFAULTS.FATHERITEMTYPECODE AND BOMCOMPONENTDEFAULTSRULE.BCDCOMPITEMTYPECODE = BOMCOMPONENTDEFAULTS.COMPITEMTYPECODE` |
| `RULES_RULE` | `BCDCOMPANYCODE`, `RULECODE` | [`RULES`](../CORE_MASTER/RULES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BOMCOMPONENTDEFAULTSRULE.BCDCOMPANYCODE = RULES.COMPANYCODE AND BOMCOMPONENTDEFAULTSRULE.RULECODE = RULES.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BOMCOMPONENTDEFAULTSRULEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.BCDCOMPANYCODE,
       t.BCDFATHERITEMTYPECODE,
       t.BCDCOMPITEMTYPECODE,
       t.SEQUENCE,
       t.RULECODE,
       t.ABSUNIQUEID,
       t.RULEUSABILITY
FROM   DB2ADMIN.BOMCOMPONENTDEFAULTSRULE t
FETCH FIRST 100 ROWS ONLY;
```
