# DB2ADMIN.TNAACTIVITYLINKEDTOOBJECT

- **Module**: `TNA` (low confidence — table name starts with 'TNA')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `TNAACTIVITYUNIQUEID`, `TNAACTIVITYTNAHDRCOMPANYCODE`, `TNAACTIVITYTNAHEADERCODE`, `UNIQUEID`, `TNAHEADERCODE`, `TNAHEADERCOMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 195256

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TNAACTIVITYUNIQUEID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TNAACTIVITYTNAHDRCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TNAACTIVITYTNAHEADERCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 4 | `TNAHEADERCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 5 | `TNAHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `TNAACTIVITY_LINKTOOBJECT` | `TNAACTIVITYUNIQUEID`, `TNAACTIVITYTNAHDRCOMPANYCODE`, `TNAACTIVITYTNAHEADERCODE` | [`TNAACTIVITY`](../TNA/TNAACTIVITY.md) | `UNIQUEID`, `TNAHEADERCOMPANYCODE`, `TNAHEADERCODE` | RESTRICT | `TNAACTIVITYLINKEDTOOBJECT.TNAACTIVITYUNIQUEID = TNAACTIVITY.UNIQUEID AND TNAACTIVITYLINKEDTOOBJECT.TNAACTIVITYTNAHDRCOMPANYCODE = TNAACTIVITY.TNAHEADERCOMPANYCODE AND TNAACTIVITYLINKEDTOOBJECT.TNAACTIVITYTNAHEADERCODE = TNAACTIVITY.TNAHEADERCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TNAACTIVITYLINKEDTOOBJECTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TNAACTIVITYUNIQUEID,
       t.TNAACTIVITYTNAHDRCOMPANYCODE,
       t.TNAACTIVITYTNAHEADERCODE,
       t.UNIQUEID,
       t.TNAHEADERCODE,
       t.TNAHEADERCOMPANYCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.TNAACTIVITYLINKEDTOOBJECT t
FETCH FIRST 100 ROWS ONLY;
```
