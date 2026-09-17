# DB2ADMIN.CSRMTE

- **Module**: `LOCALIZATION` (low confidence — FK neighbourhood: 1 of 1 related tables are LOCALIZATION)
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `CSRMTERMSOFLOGCOMPANYCODE`, `CSRMTERMSOFLOGCODE`, `CSRMTOLENTITYNAME`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 118637

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CSRMTERMSOFLOGCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CSRMTERMSOFLOGCODE` | CHAR(2) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CSRMTOLENTITYNAME` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `IGNOREME` | CHAR(1) |  |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADENTITY_CSRMTOLENTITY` | `CSRMTOLENTITYNAME` | [`ADENTITY`](../LOCALIZATION/ADENTITY.md) | `NAME` | RESTRICT | `CSRMTE.CSRMTOLENTITYNAME = ADENTITY.NAME` |
| `CSRMTERMSOFLOG_LOGENTITIES` | `CSRMTERMSOFLOGCOMPANYCODE`, `CSRMTERMSOFLOGCODE` | [`CSRMTERMSOFLOG`](../PLATFORM/CSRMTERMSOFLOG.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRMTE.CSRMTERMSOFLOGCOMPANYCODE = CSRMTERMSOFLOG.COMPANYCODE AND CSRMTE.CSRMTERMSOFLOGCODE = CSRMTERMSOFLOG.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `CSRMTE_LOGATTRIBUTES` | [`CSRMTOLATTRIBUTES`](../LOCALIZATION/CSRMTOLATTRIBUTES.md) | `CSRMTECSRMTERMSOFLOGCMYCODE`, `CSRMTECSRMTERMSOFLOGCODE`, `CSRMTECSRMTOLENTITYNAME` | `CSRMTOLATTRIBUTES.CSRMTECSRMTERMSOFLOGCMYCODE = CSRMTE.CSRMTERMSOFLOGCOMPANYCODE AND CSRMTOLATTRIBUTES.CSRMTECSRMTERMSOFLOGCODE = CSRMTE.CSRMTERMSOFLOGCODE AND CSRMTOLATTRIBUTES.CSRMTECSRMTOLENTITYNAME = CSRMTE.CSRMTOLENTITYNAME` |

## Indexes

- `CSRMTEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CSRMTERMSOFLOGCOMPANYCODE,
       t.CSRMTERMSOFLOGCODE,
       t.CSRMTOLENTITYNAME,
       t.IGNOREME,
       t.ABSUNIQUEID
FROM   DB2ADMIN.CSRMTE t
FETCH FIRST 100 ROWS ONLY;
```
