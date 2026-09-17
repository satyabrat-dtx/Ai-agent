# DB2ADMIN.BOMCOMPONENTCOSTGROUPS

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'BOM')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `BOMCMPBILLOFMATCOMPANYCODE`, `BOMCMPBILLOFMATERIALNUMBERID`, `BOMCOMPONENTSEQUENCE`, `BOMCOMPONENTSUBSEQUENCE`, `COSTSCOSTGROUPCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 198776

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BOMCMPBILLOFMATCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `BOMCMPBILLOFMATERIALNUMBERID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `BOMCOMPONENTSEQUENCE` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `BOMCOMPONENTSUBSEQUENCE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `COSTSCOSTGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `COSTPER` | DECIMAL(18,5) |  |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BOMCOMPONENT_COSTGROUPS` | `BOMCMPBILLOFMATCOMPANYCODE`, `BOMCMPBILLOFMATERIALNUMBERID`, `BOMCOMPONENTSEQUENCE`, `BOMCOMPONENTSUBSEQUENCE` | [`BOMCOMPONENT`](../ITEM_MASTER/BOMCOMPONENT.md) | `BILLOFMATERIALCOMPANYCODE`, `BILLOFMATERIALNUMBERID`, `SEQUENCE`, `SUBSEQUENCE` | RESTRICT | `BOMCOMPONENTCOSTGROUPS.BOMCMPBILLOFMATCOMPANYCODE = BOMCOMPONENT.BILLOFMATERIALCOMPANYCODE AND BOMCOMPONENTCOSTGROUPS.BOMCMPBILLOFMATERIALNUMBERID = BOMCOMPONENT.BILLOFMATERIALNUMBERID AND BOMCOMPONENTCOSTGROUPS.BOMCOMPONENTSEQUENCE = BOMCOMPONENT.SEQUENCE AND BOMCOMPONENTCOSTGROUPS.BOMCOMPONENTSUBSEQUENCE = BOMCOMPONENT.SUBSEQUENCE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BOMCOMPONENTCOSTGROUPSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.BOMCMPBILLOFMATCOMPANYCODE,
       t.BOMCMPBILLOFMATERIALNUMBERID,
       t.BOMCOMPONENTSEQUENCE,
       t.BOMCOMPONENTSUBSEQUENCE,
       t.COSTSCOSTGROUPCODE,
       t.COSTPER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.BOMCOMPONENTCOSTGROUPS t
FETCH FIRST 100 ROWS ONLY;
```
