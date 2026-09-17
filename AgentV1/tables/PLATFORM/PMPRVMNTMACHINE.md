# DB2ADMIN.PMPRVMNTMACHINE

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `PMPRVMNTCOMPANYCODE`, `PMPRVMNTCOUNTERCODE`, `PMPRVMNTCODE`, `PMBOMCOUNTERCODE`, `PMBOMCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 84269

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PMPRVMNTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PMPRVMNTCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PMPRVMNTCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PMBOMCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PMBOMCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 7 | `EFFECTIVESTARTDATE` | DATE |  |  |  |  |
| 8 | `EFFECTIVEENDDATE` | DATE |  |  |  |  |
| 9 | `NUMBEROFSCHEDULES` | INTEGER | NOT NULL |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 15 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DIVISION_DIVISION` | `PMPRVMNTCOMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMPRVMNTMACHINE.PMPRVMNTCOMPANYCODE = DIVISION.COMPANYCODE AND PMPRVMNTMACHINE.DIVISIONCODE = DIVISION.CODE` |
| `PMBOM_PMBOM` | `PMPRVMNTCOMPANYCODE`, `PMBOMCOUNTERCODE`, `PMBOMCODE` | [`PMBOM`](../CORE_MASTER/PMBOM.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMPRVMNTMACHINE.PMPRVMNTCOMPANYCODE = PMBOM.COMPANYCODE AND PMPRVMNTMACHINE.PMBOMCOUNTERCODE = PMBOM.COUNTERCODE AND PMPRVMNTMACHINE.PMBOMCODE = PMBOM.CODE` |
| `PMPRVMNT_PMPRVMNTMACHINE` | `PMPRVMNTCOMPANYCODE`, `PMPRVMNTCOUNTERCODE`, `PMPRVMNTCODE` | [`PMPRVMNT`](../PLATFORM/PMPRVMNT.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `PMPRVMNTMACHINE.PMPRVMNTCOMPANYCODE = PMPRVMNT.COMPANYCODE AND PMPRVMNTMACHINE.PMPRVMNTCOUNTERCODE = PMPRVMNT.COUNTERCODE AND PMPRVMNTMACHINE.PMPRVMNTCODE = PMPRVMNT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PMPRVMNTMACHINEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PMPRVMNTCOMPANYCODE,
       t.PMPRVMNTCOUNTERCODE,
       t.PMPRVMNTCODE,
       t.PMBOMCOUNTERCODE,
       t.PMBOMCODE,
       t.STATUS,
       t.ABSUNIQUEID,
       t.EFFECTIVESTARTDATE,
       t.EFFECTIVEENDDATE,
       t.NUMBEROFSCHEDULES,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.PMPRVMNTMACHINE t
FETCH FIRST 100 ROWS ONLY;
```
