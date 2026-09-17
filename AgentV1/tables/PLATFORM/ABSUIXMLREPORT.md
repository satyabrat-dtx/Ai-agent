# DB2ADMIN.ABSUIXMLREPORT

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `ABSUIXMLPATH`, `ABSUIXMLNAME`, `CONTEXT`, `REPORTCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 12114

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `ABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `CONTEXT` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 3 | `REPORTCODE` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `TOKEN` | CHAR(50) |  |  |  |  |
| 5 | `SEQUENCE` | DECIMAL(5,0) | NOT NULL |  |  |  |
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
| `ABSREPORTDEF_REPORT` | `REPORTCODE` | [`ABSREPORTDEF`](../PLATFORM/ABSREPORTDEF.md) | `CODE` | RESTRICT | `ABSUIXMLREPORT.REPORTCODE = ABSREPORTDEF.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSUIXMLREPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSUIXMLPATH,
       t.ABSUIXMLNAME,
       t.CONTEXT,
       t.REPORTCODE,
       t.TOKEN,
       t.SEQUENCE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.ABSUIXMLREPORT t
FETCH FIRST 100 ROWS ONLY;
```
