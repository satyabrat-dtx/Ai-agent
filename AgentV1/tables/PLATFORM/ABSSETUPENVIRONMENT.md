# DB2ADMIN.ABSSETUPENVIRONMENT

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `DATASETGROUP`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 72094

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SESSIONNAME` | CHAR(100) | NOT NULL |  |  |  |
| 1 | `SEQUENCE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 2 | `ENTITYNAME` | CHAR(100) | NOT NULL |  |  |  |
| 3 | `FIELDSTOEXCLUDEONCREATE` | VARCHAR(500) |  |  |  |  |
| 4 | `IMPORTOPERATION` | CHAR(1) | NOT NULL |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 6 | `DATASETGROUP` | CHAR(30) | NOT NULL | PK | primary_key |  |
| 7 | `ALTERNATIVEPKS` | VARCHAR(500) |  |  |  |  |
| 8 | `EXPORTFILTER` | VARCHAR(500) |  |  |  |  |
| 9 | `FIELDSTOEXCLUDE` | VARCHAR(500) |  |  |  |  |
| 10 | `DEPENDENTS` | VARCHAR(3000) |  |  |  |  |
| 11 | `MERGEDEPENDENTS` | SMALLINT | NOT NULL |  |  |  |
| 12 | `CHILDREN` | CLOB(1000000) |  |  |  |  |
| 13 | `FALSECHILDREN` | CLOB(1000000) |  |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSSETUPENVIRONMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SESSIONNAME,
       t.SEQUENCE,
       t.ENTITYNAME,
       t.FIELDSTOEXCLUDEONCREATE,
       t.IMPORTOPERATION,
       t.ABSUNIQUEID,
       t.DATASETGROUP,
       t.ALTERNATIVEPKS,
       t.EXPORTFILTER,
       t.FIELDSTOEXCLUDE,
       t.DEPENDENTS,
       t.MERGEDEPENDENTS
FROM   DB2ADMIN.ABSSETUPENVIRONMENT t
FETCH FIRST 100 ROWS ONLY;
```
