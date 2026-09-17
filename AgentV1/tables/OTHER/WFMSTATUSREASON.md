# DB2ADMIN.WFMSTATUSREASON

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `CODE`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 108310

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(50) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `DESCRIPTION` | VARCHAR(100) | NOT NULL |  | description |  |
| 2 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `WFMSTATUSREASON_REASON` | [`WFMLINKEDENTITY`](../OTHER/WFMLINKEDENTITY.md) | `REASONCODE` | `WFMLINKEDENTITY.REASONCODE = WFMSTATUSREASON.CODE` |

## Indexes

- `WFMSTATUSREASONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.DESCRIPTION,
       t.ABSUNIQUEID
FROM   DB2ADMIN.WFMSTATUSREASON t
FETCH FIRST 100 ROWS ONLY;
```
