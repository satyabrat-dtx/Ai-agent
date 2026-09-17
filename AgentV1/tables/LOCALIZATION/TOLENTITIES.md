# DB2ADMIN.TOLENTITIES

- **Module**: `LOCALIZATION` (low confidence — FK neighbourhood: 1 of 1 related tables are LOCALIZATION)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `TERMSOFLOGCOMPANYCODE`, `TERMSOFLOGORDERTYPE`, `TERMSOFLOGCODE`, `TOLENTITYNAME`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 12982

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TERMSOFLOGCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TERMSOFLOGORDERTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TERMSOFLOGCODE` | CHAR(2) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `TOLENTITYNAME` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `IGNOREME` | CHAR(1) |  |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADENTITY_TOLENTITY` | `TOLENTITYNAME` | [`ADENTITY`](../LOCALIZATION/ADENTITY.md) | `NAME` | RESTRICT | `TOLENTITIES.TOLENTITYNAME = ADENTITY.NAME` |
| `TERMSOFLOG_LOGENTITIES` | `TERMSOFLOGCOMPANYCODE`, `TERMSOFLOGORDERTYPE`, `TERMSOFLOGCODE` | [`TERMSOFLOG`](../CORE_MASTER/TERMSOFLOG.md) | `COMPANYCODE`, `ORDERTYPE`, `CODE` | RESTRICT | `TOLENTITIES.TERMSOFLOGCOMPANYCODE = TERMSOFLOG.COMPANYCODE AND TOLENTITIES.TERMSOFLOGORDERTYPE = TERMSOFLOG.ORDERTYPE AND TOLENTITIES.TERMSOFLOGCODE = TERMSOFLOG.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TOLENTITIES_LOGATTRIBUTES` | [`TOLATTRIBUTES`](../LOCALIZATION/TOLATTRIBUTES.md) | `TOLENTITIESTERMSOFLOGCMYCODE`, `TOLENTITIESTERMSOFLOGORDERTYPE`, `TOLENTITIESTERMSOFLOGCODE`, `TOLENTITIESTOLENTITYNAME` | `TOLATTRIBUTES.TOLENTITIESTERMSOFLOGCMYCODE = TOLENTITIES.TERMSOFLOGCOMPANYCODE AND TOLATTRIBUTES.TOLENTITIESTERMSOFLOGORDERTYPE = TOLENTITIES.TERMSOFLOGORDERTYPE AND TOLATTRIBUTES.TOLENTITIESTERMSOFLOGCODE = TOLENTITIES.TERMSOFLOGCODE AND TOLATTRIBUTES.TOLENTITIESTOLENTITYNAME = TOLENTITIES.TOLENTITYNAME` |

## Indexes

- `TOLENTITIESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TERMSOFLOGCOMPANYCODE,
       t.TERMSOFLOGORDERTYPE,
       t.TERMSOFLOGCODE,
       t.TOLENTITYNAME,
       t.IGNOREME,
       t.ABSUNIQUEID
FROM   DB2ADMIN.TOLENTITIES t
FETCH FIRST 100 ROWS ONLY;
```
