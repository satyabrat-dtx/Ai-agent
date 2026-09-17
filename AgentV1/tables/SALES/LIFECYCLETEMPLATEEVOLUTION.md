# DB2ADMIN.LIFECYCLETEMPLATEEVOLUTION

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `LIFECYCLETMPLIFECYCLECMYCODE`, `LIFECYCLETMPLIFECYCLEORDTYPE`, `LIFECYCLETEMPLATELIFECYCLECODE`, `LIFECYCLETEMPLATETEMPLATECODE`, `NEXTTEMPLATECODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 20601

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LIFECYCLETMPLIFECYCLECMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `LIFECYCLETMPLIFECYCLEORDTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LIFECYCLETEMPLATELIFECYCLECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LIFECYCLETEMPLATETEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `NEXTTEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `GROUPCURRENTDOCUMENTSONNEXT` | SMALLINT | NOT NULL |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `LIFECYCLETEMPLATE_EVOLUTION` | `LIFECYCLETMPLIFECYCLECMYCODE`, `LIFECYCLETMPLIFECYCLEORDTYPE`, `LIFECYCLETEMPLATELIFECYCLECODE`, `LIFECYCLETEMPLATETEMPLATECODE` | [`LIFECYCLETEMPLATE`](../SALES/LIFECYCLETEMPLATE.md) | `LIFECYCLECOMPANYCODE`, `LIFECYCLEORDERTYPE`, `LIFECYCLECODE`, `TEMPLATECODE` | RESTRICT | `LIFECYCLETEMPLATEEVOLUTION.LIFECYCLETMPLIFECYCLECMYCODE = LIFECYCLETEMPLATE.LIFECYCLECOMPANYCODE AND LIFECYCLETEMPLATEEVOLUTION.LIFECYCLETMPLIFECYCLEORDTYPE = LIFECYCLETEMPLATE.LIFECYCLEORDERTYPE AND LIFECYCLETEMPLATEEVOLUTION.LIFECYCLETEMPLATELIFECYCLECODE = LIFECYCLETEMPLATE.LIFECYCLECODE AND LIFECYCLETEMPLATEEVOLUTION.LIFECYCLETEMPLATETEMPLATECODE = LIFECYCLETEMPLATE.TEMPLATECODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LIFECYCLETEMPLATEEVOLUTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.LIFECYCLETMPLIFECYCLECMYCODE,
       t.LIFECYCLETMPLIFECYCLEORDTYPE,
       t.LIFECYCLETEMPLATELIFECYCLECODE,
       t.LIFECYCLETEMPLATETEMPLATECODE,
       t.NEXTTEMPLATECODE,
       t.GROUPCURRENTDOCUMENTSONNEXT,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.LIFECYCLETEMPLATEEVOLUTION t
FETCH FIRST 100 ROWS ONLY;
```
