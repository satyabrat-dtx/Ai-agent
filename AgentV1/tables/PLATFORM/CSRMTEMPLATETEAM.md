# DB2ADMIN.CSRMTEMPLATETEAM

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `CSRMTEMPLATECOMPANYCODE`, `CSRMTEMPLATECODE`, `TEAMCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 118807

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CSRMTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CSRMTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TEAMCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 4 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 5 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 6 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 7 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 8 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CSRMTEAM_TEAM` | `CSRMTEMPLATECOMPANYCODE`, `TEAMCODE` | [`CSRMTEAM`](../PLATFORM/CSRMTEAM.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRMTEMPLATETEAM.CSRMTEMPLATECOMPANYCODE = CSRMTEAM.COMPANYCODE AND CSRMTEMPLATETEAM.TEAMCODE = CSRMTEAM.CODE` |
| `CSRMTEMPLATE_TEAM` | `CSRMTEMPLATECOMPANYCODE`, `CSRMTEMPLATECODE` | [`CSRMTEMPLATE`](../PLATFORM/CSRMTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CSRMTEMPLATETEAM.CSRMTEMPLATECOMPANYCODE = CSRMTEMPLATE.COMPANYCODE AND CSRMTEMPLATETEAM.CSRMTEMPLATECODE = CSRMTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CSRMTEMPLATETEAMUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CSRMTEMPLATECOMPANYCODE,
       t.CSRMTEMPLATECODE,
       t.TEAMCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.CSRMTEMPLATETEAM t
FETCH FIRST 100 ROWS ONLY;
```
