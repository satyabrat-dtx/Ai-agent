# DB2ADMIN.NETTOLENTITIES

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'NET')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `NETTOLOGCOMPANYCODE`, `NETTOLOGCODE`, `TOLENTITYNAME`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 122858

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `NETTOLOGCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `NETTOLOGCODE` | CHAR(2) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TOLENTITYNAME` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `IGNOREME` | CHAR(1) |  |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADENTITY_TOLENTITY` | `TOLENTITYNAME` | [`ADENTITY`](../LOCALIZATION/ADENTITY.md) | `NAME` | RESTRICT | `NETTOLENTITIES.TOLENTITYNAME = ADENTITY.NAME` |
| `NETTOLOG_LOGENTITIES` | `NETTOLOGCOMPANYCODE`, `NETTOLOGCODE` | [`NETTOLOG`](../LOCALIZATION/NETTOLOG.md) | `COMPANYCODE`, `CODE` | RESTRICT | `NETTOLENTITIES.NETTOLOGCOMPANYCODE = NETTOLOG.COMPANYCODE AND NETTOLENTITIES.NETTOLOGCODE = NETTOLOG.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `NETTOLENTITIES_LOGATTRIBUTES` | [`NETTOLATTRIBUTES`](../LOCALIZATION/NETTOLATTRIBUTES.md) | `NETTOLENTITIESNETTOLOGCMYCODE`, `NETTOLENTITIESNETTOLOGCODE`, `NETTOLENTITIESTOLENTITYNAME` | `NETTOLATTRIBUTES.NETTOLENTITIESNETTOLOGCMYCODE = NETTOLENTITIES.NETTOLOGCOMPANYCODE AND NETTOLATTRIBUTES.NETTOLENTITIESNETTOLOGCODE = NETTOLENTITIES.NETTOLOGCODE AND NETTOLATTRIBUTES.NETTOLENTITIESTOLENTITYNAME = NETTOLENTITIES.TOLENTITYNAME` |

## Indexes

- `NETTOLENTITIESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.NETTOLOGCOMPANYCODE,
       t.NETTOLOGCODE,
       t.TOLENTITYNAME,
       t.IGNOREME,
       t.ABSUNIQUEID
FROM   DB2ADMIN.NETTOLENTITIES t
FETCH FIRST 100 ROWS ONLY;
```
