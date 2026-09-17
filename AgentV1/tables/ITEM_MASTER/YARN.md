# DB2ADMIN.YARN

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 1 of 1 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `CODE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 26927

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(4) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `DESCRIPTION` | VARCHAR(80) | NOT NULL |  | description |  |
| 2 | `MULTIPLYFACTOR` | DECIMAL(15,5) |  |  |  |  |
| 3 | `DIVISIONFACTOR` | DECIMAL(15,5) |  |  |  |  |
| 4 | `DIRECTINDIRECT` | CHAR(1) | NOT NULL |  |  |  |
| 5 | `FACTORLENGTHUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `FACTORWEIGHTUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `UNITOFMEASURE_FACTORLENGTHUOM` | `FACTORLENGTHUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `YARN.FACTORLENGTHUOMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_FACTORWEIGHTUOM` | `FACTORWEIGHTUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `YARN.FACTORWEIGHTUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `YARN_YARNCOUNTSYSTEM` | [`PRODUCTSPECIALIZEDYARN`](../ITEM_MASTER/PRODUCTSPECIALIZEDYARN.md) | `YARNCOUNTSYSTEMCODE` | `PRODUCTSPECIALIZEDYARN.YARNCOUNTSYSTEMCODE = YARN.CODE` |

## Indexes

- `YARNUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.DESCRIPTION,
       t.MULTIPLYFACTOR,
       t.DIVISIONFACTOR,
       t.DIRECTINDIRECT,
       t.FACTORLENGTHUOMCODE,
       t.FACTORWEIGHTUOMCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.YARN t
FETCH FIRST 100 ROWS ONLY;
```
