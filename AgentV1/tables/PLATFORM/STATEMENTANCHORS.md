# DB2ADMIN.STATEMENTANCHORS

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `SAVEDSTATEMENTCOMPANYCODE`, `SAVEDSTATEMENTCODE`, `ANCHOR`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 112443

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SAVEDSTATEMENTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SAVEDSTATEMENTCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ANCHOR` | VARCHAR(250) | NOT NULL | PK | primary_key |  |
| 3 | `VALUE` | VARCHAR(250) |  |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `SAVEDSTATEMENT_ANCHORS` | `SAVEDSTATEMENTCOMPANYCODE`, `SAVEDSTATEMENTCODE` | [`SAVEDSTATEMENT`](../PLATFORM/SAVEDSTATEMENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `STATEMENTANCHORS.SAVEDSTATEMENTCOMPANYCODE = SAVEDSTATEMENT.COMPANYCODE AND STATEMENTANCHORS.SAVEDSTATEMENTCODE = SAVEDSTATEMENT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `STATEMENTANCHORSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SAVEDSTATEMENTCOMPANYCODE,
       t.SAVEDSTATEMENTCODE,
       t.ANCHOR,
       t.VALUE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.STATEMENTANCHORS t
FETCH FIRST 100 ROWS ONLY;
```
