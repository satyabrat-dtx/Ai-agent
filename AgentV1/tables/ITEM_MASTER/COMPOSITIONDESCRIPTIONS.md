# DB2ADMIN.COMPOSITIONDESCRIPTIONS

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 1 of 1 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `COMPOSITIONCOMPANYCODE`, `COMPOSITIONCODE`, `TYPE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 47658

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPOSITIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `COMPOSITIONCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 3 | `DESCRIPTION` | VARCHAR(200) |  |  | description |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPOSITION_CMPDESC` | `COMPOSITIONCOMPANYCODE`, `COMPOSITIONCODE` | [`COMPOSITION`](../ITEM_MASTER/COMPOSITION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `COMPOSITIONDESCRIPTIONS.COMPOSITIONCOMPANYCODE = COMPOSITION.COMPANYCODE AND COMPOSITIONDESCRIPTIONS.COMPOSITIONCODE = COMPOSITION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COMPOSITIONDESCRIPTIONSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPOSITIONCOMPANYCODE,
       t.COMPOSITIONCODE,
       t.TYPE,
       t.DESCRIPTION,
       t.ABSUNIQUEID
FROM   DB2ADMIN.COMPOSITIONDESCRIPTIONS t
FETCH FIRST 100 ROWS ONLY;
```
