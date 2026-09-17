# DB2ADMIN.LIFECYCLECOMPLETE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `CURRENTORDERTYPE`, `CURRENTTYPE`, `NEXTORDERTYPE`, `NEXTTYPE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 4589

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CURRENTORDERTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CURRENTTYPE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `NEXTORDERTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `NEXTTYPE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DOCUMENTTYPE_CURRENT` | `CURRENTORDERTYPE`, `CURRENTTYPE` | [`DOCUMENTTYPE`](../CORE_MASTER/DOCUMENTTYPE.md) | `ORDERTYPE`, `TYPE` | RESTRICT | `LIFECYCLECOMPLETE.CURRENTORDERTYPE = DOCUMENTTYPE.ORDERTYPE AND LIFECYCLECOMPLETE.CURRENTTYPE = DOCUMENTTYPE.TYPE` |
| `DOCUMENTTYPE_NEXT` | `NEXTORDERTYPE`, `NEXTTYPE` | [`DOCUMENTTYPE`](../CORE_MASTER/DOCUMENTTYPE.md) | `ORDERTYPE`, `TYPE` | RESTRICT | `LIFECYCLECOMPLETE.NEXTORDERTYPE = DOCUMENTTYPE.ORDERTYPE AND LIFECYCLECOMPLETE.NEXTTYPE = DOCUMENTTYPE.TYPE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LIFECYCLECOMPLETEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CURRENTORDERTYPE,
       t.CURRENTTYPE,
       t.NEXTORDERTYPE,
       t.NEXTTYPE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.LIFECYCLECOMPLETE t
FETCH FIRST 100 ROWS ONLY;
```
