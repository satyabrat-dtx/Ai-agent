# DB2ADMIN.COSTRUNNINGMANAGERHISTORY

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `COSTRUNNINGMANAGERCOMPANYCODE`, `TABLEINDEX`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 191677

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COSTRUNNINGMANAGERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TABLEINDEX` | DECIMAL(8,0) | NOT NULL | PK | primary_key |  |
| 2 | `CYCLESTARTDATETIME` | TIMESTAMP |  |  |  |  |
| 3 | `STARTCYCLEREASON` | CHAR(1) |  |  |  |  |
| 4 | `CYCLEENDDATETIME` | TIMESTAMP |  |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COSTRUNNINGMANAGER_CRMHISTORY` | `COSTRUNNINGMANAGERCOMPANYCODE` | [`COSTRUNNINGMANAGER`](../COSTING/COSTRUNNINGMANAGER.md) | `COMPANYCODE` | RESTRICT | `COSTRUNNINGMANAGERHISTORY.COSTRUNNINGMANAGERCOMPANYCODE = COSTRUNNINGMANAGER.COMPANYCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COSTRUNNINGMANAGERHISTORYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COSTRUNNINGMANAGERCOMPANYCODE,
       t.TABLEINDEX,
       t.CYCLESTARTDATETIME,
       t.STARTCYCLEREASON,
       t.CYCLEENDDATETIME,
       t.ABSUNIQUEID
FROM   DB2ADMIN.COSTRUNNINGMANAGERHISTORY t
FETCH FIRST 100 ROWS ONLY;
```
