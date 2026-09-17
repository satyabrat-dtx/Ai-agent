# DB2ADMIN.AGENTSGROUPDETAIL

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `AGENTSGROUPCOMPANYCODE`, `AGENTSGROUPCODE`, `AGENTCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 27276

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `AGENTSGROUPCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `AGENTSGROUPCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `AGENTCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 4 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 5 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 6 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `AGENTSGROUP_AGENTSGROUPDETAIL` | `AGENTSGROUPCOMPANYCODE`, `AGENTSGROUPCODE` | [`AGENTSGROUP`](../SALES/AGENTSGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `AGENTSGROUPDETAIL.AGENTSGROUPCOMPANYCODE = AGENTSGROUP.COMPANYCODE AND AGENTSGROUPDETAIL.AGENTSGROUPCODE = AGENTSGROUP.CODE` |
| `AGENT_AGENT` | `AGENTSGROUPCOMPANYCODE`, `AGENTCODE` | [`AGENT`](../CORE_MASTER/AGENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `AGENTSGROUPDETAIL.AGENTSGROUPCOMPANYCODE = AGENT.COMPANYCODE AND AGENTSGROUPDETAIL.AGENTCODE = AGENT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `AGENTSGROUPDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.AGENTSGROUPCOMPANYCODE,
       t.AGENTSGROUPCODE,
       t.AGENTCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.AGENTSGROUPDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
