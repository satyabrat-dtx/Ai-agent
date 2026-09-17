# DB2ADMIN.SORLOTBREAKUPNOOFBEAM

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `NOOFSET`, `BEAMPERSET`, `COUNTTYPE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 205313

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `NOOFSET` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 1 | `BEAMPERSET` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 2 | `COUNTTYPE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 3 | `BEAMPERCREEL` | VARCHAR(500) | NOT NULL |  |  |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SORLOTBREAKUPNOOFBEAMUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.NOOFSET,
       t.BEAMPERSET,
       t.COUNTTYPE,
       t.BEAMPERCREEL,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.SORLOTBREAKUPNOOFBEAM t
FETCH FIRST 100 ROWS ONLY;
```
