# DB2ADMIN.LIFECYCLETEMPLATESTEP

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `LIFECYCLETMPLIFECYCLECMYCODE`, `LIFECYCLETMPLIFECYCLEORDTYPE`, `LIFECYCLETEMPLATELIFECYCLECODE`, `LIFECYCLETEMPLATETEMPLATECODE`, `CODEDOCUMENTTYPETYPE`, `CODECODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 2786

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LIFECYCLETMPLIFECYCLECMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `LIFECYCLETMPLIFECYCLEORDTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LIFECYCLETEMPLATELIFECYCLECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LIFECYCLETEMPLATETEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CODEDOCUMENTTYPETYPE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `CODECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 7 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 8 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 9 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 10 | `MANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `LIFECYCLETEMPLATE_STEP` | `LIFECYCLETMPLIFECYCLECMYCODE`, `LIFECYCLETMPLIFECYCLEORDTYPE`, `LIFECYCLETEMPLATELIFECYCLECODE`, `LIFECYCLETEMPLATETEMPLATECODE` | [`LIFECYCLETEMPLATE`](../SALES/LIFECYCLETEMPLATE.md) | `LIFECYCLECOMPANYCODE`, `LIFECYCLEORDERTYPE`, `LIFECYCLECODE`, `TEMPLATECODE` | RESTRICT | `LIFECYCLETEMPLATESTEP.LIFECYCLETMPLIFECYCLECMYCODE = LIFECYCLETEMPLATE.LIFECYCLECOMPANYCODE AND LIFECYCLETEMPLATESTEP.LIFECYCLETMPLIFECYCLEORDTYPE = LIFECYCLETEMPLATE.LIFECYCLEORDERTYPE AND LIFECYCLETEMPLATESTEP.LIFECYCLETEMPLATELIFECYCLECODE = LIFECYCLETEMPLATE.LIFECYCLECODE AND LIFECYCLETEMPLATESTEP.LIFECYCLETEMPLATETEMPLATECODE = LIFECYCLETEMPLATE.TEMPLATECODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LIFECYCLETMPSTP1` (LIFECYCLETEMPLATETEMPLATECODE, LIFECYCLETEMPLATELIFECYCLECODE, LIFECYCLETMPLIFECYCLEORDTYPE, LIFECYCLETMPLIFECYCLECMYCODE, SEQUENCE, LASTUPDATEUSER, LASTUPDATEDATETIME, CREATIONUSER, CREATIONDATETIME, MANDATORY, SEARCHDESCRIPTION, SHORTDESCRIPTION, LONGDESCRIPTION, CODECODE, CODEDOCUMENTTYPETYPE)
- `LIFECYCLETEMPLATESTEPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.LIFECYCLETMPLIFECYCLECMYCODE,
       t.LIFECYCLETMPLIFECYCLEORDTYPE,
       t.LIFECYCLETEMPLATELIFECYCLECODE,
       t.LIFECYCLETEMPLATETEMPLATECODE,
       t.CODEDOCUMENTTYPETYPE,
       t.CODECODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.SEQUENCE,
       t.MANDATORY,
       t.CREATIONDATETIME
FROM   DB2ADMIN.LIFECYCLETEMPLATESTEP t
FETCH FIRST 100 ROWS ONLY;
```
