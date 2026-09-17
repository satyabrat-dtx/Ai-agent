# DB2ADMIN.CSRMTEAMMEMBERS

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `CSRMTEAMCOMPANYCODE`, `CSRMTEAMCODE`, `USERUSERID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 118716

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CSRMTEAMCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CSRMTEAMCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `USERUSERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 4 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 5 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 6 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 7 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 8 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CSRMTEAM_TEAMMEMBER` | `CSRMTEAMCOMPANYCODE`, `CSRMTEAMCODE` | [`CSRMTEAM`](../PLATFORM/CSRMTEAM.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRMTEAMMEMBERS.CSRMTEAMCOMPANYCODE = CSRMTEAM.COMPANYCODE AND CSRMTEAMMEMBERS.CSRMTEAMCODE = CSRMTEAM.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CSRMTEAMMEMBERSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CSRMTEAMCOMPANYCODE,
       t.CSRMTEAMCODE,
       t.USERUSERID,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.CSRMTEAMMEMBERS t
FETCH FIRST 100 ROWS ONLY;
```
