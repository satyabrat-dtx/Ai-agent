# DB2ADMIN.CSRMPARTICIPANT

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `CSRMCOMPANYCODE`, `CSRMCOUNTERCODE`, `CSRMCODE`, `USERUSERID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 118534

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CSRMCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CSRMCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CSRMCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `USERUSERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CSRM_CSRMPARTICIPANT` | `CSRMCOMPANYCODE`, `CSRMCOUNTERCODE`, `CSRMCODE` | [`CSRM`](../PLATFORM/CSRM.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `CSRMPARTICIPANT.CSRMCOMPANYCODE = CSRM.COMPANYCODE AND CSRMPARTICIPANT.CSRMCOUNTERCODE = CSRM.COUNTERCODE AND CSRMPARTICIPANT.CSRMCODE = CSRM.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CSRMPARTICIPANTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CSRMCOMPANYCODE,
       t.CSRMCOUNTERCODE,
       t.CSRMCODE,
       t.USERUSERID,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.CSRMPARTICIPANT t
FETCH FIRST 100 ROWS ONLY;
```
