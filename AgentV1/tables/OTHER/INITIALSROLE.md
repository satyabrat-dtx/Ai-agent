# DB2ADMIN.INITIALSROLE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `INITIALSCOMPANYCODE`, `INITIALSCODE`, `ROLESTANDARDGROUPTYPECODE`, `ROLECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 21409

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INITIALSCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `INITIALSCODE` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ROLESTANDARDGROUPTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ROLECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `ROLESTDGROUPTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `INITIALSROLE.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `INITIALS_ROLE` | `INITIALSCOMPANYCODE`, `INITIALSCODE` | [`INITIALS`](../CORE_MASTER/INITIALS.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INITIALSROLE.INITIALSCOMPANYCODE = INITIALS.COMPANYCODE AND INITIALSROLE.INITIALSCODE = INITIALS.CODE` |
| `STANDARDGROUP_ROLE` | `ROLESTDGROUPTYPECOMPANYCODE`, `ROLESTANDARDGROUPTYPECODE`, `ROLECODE` | [`STANDARDGROUP`](../CORE_MASTER/STANDARDGROUP.md) | `STANDARDGROUPTYPECOMPANYCODE`, `STANDARDGROUPTYPECODE`, `CODE` | RESTRICT | `INITIALSROLE.ROLESTDGROUPTYPECOMPANYCODE = STANDARDGROUP.STANDARDGROUPTYPECOMPANYCODE AND INITIALSROLE.ROLESTANDARDGROUPTYPECODE = STANDARDGROUP.STANDARDGROUPTYPECODE AND INITIALSROLE.ROLECODE = STANDARDGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INITIALSROLEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.INITIALSCOMPANYCODE,
       t.INITIALSCODE,
       t.ROLESTANDARDGROUPTYPECODE,
       t.ROLECODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.OWNINGCOMPANYCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.INITIALSROLE t
FETCH FIRST 100 ROWS ONLY;
```
